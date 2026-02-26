#!/usr/bin/env python3
"""Generate Pydantic v2 models from the Jira Cloud OpenAPI specification.

Wraps ``datamodel-code-generator`` with the project's preferred flags, runs a
post-processing pass to fix Python-builtin field-name collisions, splits the
monolithic output into domain-themed submodules under ``jirapi/models/``, then
formats with ``ruff``.

The split places each model into a submodule matching its Jira API domain
(e.g. ``issues``, ``projects``, ``workflows``).  Models used by multiple
domains—and all enums—go to ``_shared``.  A re-exporting ``__init__.py``
preserves the ``from jirapi.models import X`` public API.

Usage::

    uv run python scripts/generate_models.py
"""

from __future__ import annotations

from collections import defaultdict
import json
from pathlib import Path
import re
import subprocess
import sys
from typing import Any


REPO_ROOT = Path(__file__).resolve().parent.parent
OPENAPI_SPEC = REPO_ROOT / "docs" / "jira-cloud-api-openapi.json"
MODELS_DIR = REPO_ROOT / "jirapi" / "models"
STAGING_FILE = MODELS_DIR / "_staging.py"

sys.path.insert(0, str(Path(__file__).resolve().parent))
from generate_resources import TAG_CONSOLIDATION  # noqa: E402


_JSONNODE_REPLACEMENT = '''\
class JsonNode(BaseModel):
    """Represents an arbitrary JSON value (Jackson JsonNode).

    The upstream schema defines fields (``float``, ``int``, ``type``, …) that
    shadow Python builtins and break annotation resolution.  This replacement
    uses ``extra="allow"`` to accept any JSON structure.
    """

    model_config = ConfigDict(
        extra="allow",
    )
'''

# Names that appear in class bodies but are NOT model references
_STDLIB_BASES = frozenset({"BaseModel", "StrEnum", "Enum"})

# Pydantic / typing / stdlib names to detect for import generation
_TYPING_NAMES = ("Annotated", "Any", "Literal")
_PYDANTIC_NAMES = (
    "AnyUrl",
    "AwareDatetime",
    "Base64Str",
    "BaseModel",
    "ConfigDict",
    "Field",
    "RootModel",
)

# ──────────────────────────────────────────────────────────────────────
# Post-processing helpers (existing)
# ──────────────────────────────────────────────────────────────────────


def _camel_to_snake(name: str) -> str:
    """Convert a camelCase string to snake_case."""
    s1 = re.sub(r"([A-Z]+)([A-Z][a-z])", r"\1_\2", name)
    return re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", s1).lower()


def _fix_builtin_shadows(content: str) -> str:
    """Replace problematic generated classes whose fields shadow Python builtins."""
    return _replace_class(content, "JsonNode", _JSONNODE_REPLACEMENT)


def _strip_discriminators(content: str) -> str:
    """Remove ``discriminator=...`` from Field() calls and standalone usages."""
    q = r"""['"]"""
    val = r"""[^'"]*"""
    disc = rf"discriminator={q}{val}{q}"

    content = re.sub(rf"Field\({disc}\)", "Field()", content)
    content = re.sub(rf",\s*{disc}", "", content)
    content = re.sub(rf"{disc},\s*", "", content)
    content = re.sub(rf"\s*{disc},?", "", content)
    content = re.sub(r",\s*Field\(\)", "", content)

    prev = None
    while prev != content:
        prev = content
        content = re.sub(r",(\s*)\]", r"\1]", content)

    content = re.sub(r"Annotated\[([^,\[\]]+)\]", r"\1", content)
    return content


def _replace_class(content: str, class_name: str, replacement: str) -> str:
    """Replace a top-level class definition with *replacement* text."""
    pattern = re.compile(
        rf"^class {class_name}\(.*?\):.*?(?=\nclass |\n[A-Z]|\Z)",
        re.MULTILINE | re.DOTALL,
    )
    return pattern.sub(replacement.rstrip(), content, count=1)


def _strip_bean_suffix(content: str) -> str:
    """Remove the ``Bean`` suffix from generated model class names.

    Jira's OpenAPI spec inherits Java naming conventions where many schemas end
    in ``Bean`` (e.g. ``IssueBean``, ``CommentBean``).  This function strips
    that suffix to produce idiomatic Python names.

    When the stripped name already exists as a separate class (e.g. ``UserBean``
    vs ``User``), the Bean variant is considered redundant — its class
    definition is deleted and all references are remapped to the existing class.

    Compound helper types derived from a Bean class (e.g. ``UserBeanAvatarUrls``
    from ``UserBean``) are also renamed (``UserAvatarUrls``).
    """
    all_classes = set(re.findall(r"^class (\w+)\(", content, re.MULTILINE))
    bean_classes = sorted(n for n in all_classes if n.endswith("Bean"))

    if not bean_classes:
        return content

    rename_map: dict[str, str] = {}
    conflicts: set[str] = set()

    for name in bean_classes:
        stripped = name[:-4]
        if stripped in all_classes:
            conflicts.add(name)
        rename_map[name] = stripped

    # Also rename compound helper types derived from a Bean class
    # (e.g. UserBeanAvatarUrls -> UserAvatarUrls)
    for bean_name in list(rename_map):
        for cls in all_classes:
            if cls.startswith(bean_name) and cls != bean_name:
                suffix = cls[len(bean_name) :]
                rename_map[cls] = rename_map[bean_name] + suffix

    # Delete redundant Bean class definitions for conflicts
    for name in conflicts:
        content = _replace_class(content, name, "")
        content = re.sub(r"\n{3,}", "\n\n\n", content)

    # Apply renames longest-first to avoid partial matches
    for old in sorted(rename_map, key=len, reverse=True):
        new = rename_map[old]
        content = re.sub(rf"\b{old}\b", new, content)

    renamed = len(rename_map) - len(conflicts)
    print(f"  Stripped Bean suffix: {renamed} renamed, {len(conflicts)} merged with existing class")
    return content


# ──────────────────────────────────────────────────────────────────────
# Phase 2: Parse generated content
# ──────────────────────────────────────────────────────────────────────


def _parse_classes(content: str) -> list[tuple[str, str]]:
    """Extract class definitions from generated code.

    Returns list of ``(class_name, full_text)`` tuples in definition order.
    """
    class_pat = re.compile(r"^class (\w+)\(", re.MULTILINE)
    matches = list(class_pat.finditer(content))

    classes: list[tuple[str, str]] = []
    for i, match in enumerate(matches):
        name = match.group(1)
        start = match.start()
        if i + 1 < len(matches):
            end = matches[i + 1].start()
        else:
            tail = content[start:]
            m = re.search(r"^\w+\.model_rebuild\(\)", tail, re.MULTILINE)
            if not m:
                m = re.search(r"^__all__", tail, re.MULTILINE)
            end = (start + m.start()) if m else len(content)

        text = content[start:end].rstrip()
        classes.append((name, text))

    return classes


def _extract_rebuild_names(content: str) -> list[str]:
    """Return class names that have ``model_rebuild()`` calls."""
    return re.findall(r"^(\w+)\.model_rebuild\(\)", content, re.MULTILINE)


# ──────────────────────────────────────────────────────────────────────
# Phase 3: Build domain mapping from OpenAPI spec
# ──────────────────────────────────────────────────────────────────────


def _collect_refs(obj: Any) -> set[str]:
    """Recursively collect all ``$ref`` schema names from an OpenAPI fragment."""
    refs: set[str] = set()
    if isinstance(obj, dict):
        if "$ref" in obj:
            refs.add(obj["$ref"].rsplit("/", 1)[-1])
        for v in obj.values():
            refs.update(_collect_refs(v))
    elif isinstance(obj, list):
        for item in obj:
            refs.update(_collect_refs(item))
    return refs


def _build_schema_to_groups(spec: dict[str, Any]) -> dict[str, set[str]]:
    """Map each OpenAPI schema name to the set of domain groups that use it.

    Walks every operation in the spec, maps its tag to a group via
    ``TAG_CONSOLIDATION``, collects direct ``$ref`` names from request bodies
    and responses, then propagates group membership through the schema
    dependency graph so transitive dependencies are captured.
    """
    group_direct: dict[str, set[str]] = defaultdict(set)

    for _path, methods in spec.get("paths", {}).items():
        for http_method, op in methods.items():
            if http_method not in ("get", "post", "put", "delete", "patch"):
                continue
            tag = op.get("tags", ["untagged"])[0]
            if tag not in TAG_CONSOLIDATION:
                continue
            group = TAG_CONSOLIDATION[tag][0]

            refs: set[str] = set()
            refs.update(_collect_refs(op.get("requestBody", {})))
            refs.update(_collect_refs(op.get("responses", {})))
            group_direct[group].update(refs)

    # Schema dependency graph: schema → schemas it references
    all_schemas = spec.get("components", {}).get("schemas", {})
    schema_deps: dict[str, set[str]] = {}
    for name, definition in all_schemas.items():
        schema_deps[name] = _collect_refs(definition)

    # Compute transitive reachability per group
    def _reachable(start: str, visited: set[str] | None = None) -> set[str]:
        if visited is None:
            visited = set()
        if start in visited:
            return visited
        visited.add(start)
        for dep in schema_deps.get(start, set()):
            _reachable(dep, visited)
        return visited

    schema_groups: dict[str, set[str]] = defaultdict(set)
    for group, direct in group_direct.items():
        reachable: set[str] = set()
        for s in direct:
            reachable.update(_reachable(s))
        for s in reachable:
            schema_groups[s].add(group)

    return dict(schema_groups)


# ──────────────────────────────────────────────────────────────────────
# Phase 4: Assign classes to modules
# ──────────────────────────────────────────────────────────────────────


def _assign_to_modules(
    classes: list[tuple[str, str]],
    schema_groups: dict[str, set[str]],
) -> tuple[dict[str, list[tuple[str, str]]], dict[str, str]]:
    """Assign each class to a submodule name.

    Returns:
        modules: mapping of module_name → [(class_name, class_text), ...]
        assigned: mapping of class_name → module_name
    """
    assigned: dict[str, str] = {}

    # Detect cross-class inheritance (child → non-stdlib parent)
    inheritance_parents: dict[str, str] = {}
    # Detect RootModel wrappers and their wrapped type
    rootmodel_wrapped: dict[str, str | None] = {}

    for name, text in classes:
        base_match = re.match(r"^class \w+\((\w+)\):", text)
        if base_match:
            base = base_match.group(1)
            if base not in _STDLIB_BASES:
                inheritance_parents[name] = base

        rm_match = re.match(r"^class \w+\(RootModel\[(?:list\[)?(\w+)", text)
        if rm_match:
            wrapped = rm_match.group(1)
            rootmodel_wrapped[name] = (
                None if wrapped in ("int", "str", "float", "bool") else wrapped
            )

    # ── Pass 1: enums and regular models ──
    deferred: list[tuple[str, str]] = []

    for name, text in classes:
        if name in inheritance_parents or name in rootmodel_wrapped:
            deferred.append((name, text))
            continue

        if re.match(r"^class \w+\((StrEnum|Enum)\)", text):
            assigned[name] = "_shared"
            continue

        groups = schema_groups.get(name, set())
        if len(groups) == 1:
            assigned[name] = next(iter(groups))
        else:
            assigned[name] = "_shared"

    # ── Pass 2: children and RootModel wrappers follow their dependency ──
    for name, _text in deferred:
        if name in inheritance_parents:
            parent = inheritance_parents[name]
            assigned[name] = assigned.get(parent, "_shared")
        elif name in rootmodel_wrapped:
            wrapped = rootmodel_wrapped[name]
            if wrapped and wrapped in assigned:
                assigned[name] = assigned[wrapped]
            else:
                assigned[name] = "_shared"

    # Build ordered module dict preserving original class order
    modules: dict[str, list[tuple[str, str]]] = defaultdict(list)
    for name, text in classes:
        modules[assigned[name]].append((name, text))

    return dict(modules), assigned


# ──────────────────────────────────────────────────────────────────────
# Phase 5: Write submodule files
# ──────────────────────────────────────────────────────────────────────


def _detect_imports(class_texts: list[str]) -> tuple[list[str], list[str], list[str]]:
    """Detect stdlib, typing, and pydantic imports needed by a set of classes."""
    combined = "\n".join(class_texts)

    stdlib: list[str] = []
    if "date_aliased" in combined:
        stdlib.append("from datetime import date as date_aliased")
    if "UUID" in combined:
        stdlib.append("from uuid import UUID")
    enum_names = sorted(n for n in ("Enum", "StrEnum") if re.search(rf"\b{n}\b", combined))
    if enum_names:
        stdlib.append(f"from enum import {', '.join(enum_names)}")

    typing_names = sorted(n for n in _TYPING_NAMES if re.search(rf"\b{n}\b", combined))
    pydantic_names = sorted(n for n in _PYDANTIC_NAMES if re.search(rf"\b{n}\b", combined))

    return stdlib, typing_names, pydantic_names


def _shared_runtime_imports(
    module_classes: list[tuple[str, str]],
    shared_names: set[str],
) -> set[str]:
    """Determine which ``_shared`` names must be imported at runtime.

    Runtime imports are needed for:
    - Base classes: ``class Foo(SharedBase):``
    - Enum default values: ``field: E = E.member``
    """
    needed: set[str] = set()
    for _name, text in module_classes:
        base_match = re.match(r"^class \w+\((\w+)", text)
        if base_match and base_match.group(1) in shared_names:
            needed.add(base_match.group(1))
        for m in re.finditer(r"=\s+(\w+)\.", text):
            if m.group(1) in shared_names:
                needed.add(m.group(1))
    return needed


def _write_submodule(
    module_name: str,
    classes: list[tuple[str, str]],
    shared_names: set[str],
    output_dir: Path,
) -> None:
    """Write a domain submodule file (e.g. ``models/issues.py``)."""
    texts = [text for _, text in classes]
    stdlib, typing_names, pydantic_names = _detect_imports(texts)
    runtime_shared = _shared_runtime_imports(classes, shared_names)

    lines: list[str] = []
    label = module_name.replace("_", " ")
    lines.append(f'"""Pydantic models for the {label} domain."""')
    lines.append("")
    lines.append("from __future__ import annotations")
    lines.append("")

    for imp in stdlib:
        lines.append(imp)
    if stdlib:
        lines.append("")

    if typing_names:
        lines.append(f"from typing import {', '.join(typing_names)}")
        lines.append("")

    if pydantic_names:
        lines.append(f"from pydantic import {', '.join(pydantic_names)}")
        lines.append("")

    if runtime_shared:
        names = ", ".join(sorted(runtime_shared))
        lines.append(f"from jirapi.models._shared import {names}")
        lines.append("")

    lines.append("")
    for _name, text in classes:
        lines.append(text)
        lines.append("")
        lines.append("")

    all_names = [name for name, _ in classes]
    all_block = "__all__ = [\n" + "".join(f'    "{n}",\n' for n in all_names) + "]"
    lines.append(all_block)
    lines.append("")

    (output_dir / f"{module_name}.py").write_text("\n".join(lines))


def _write_shared_module(
    classes: list[tuple[str, str]],
    output_dir: Path,
) -> None:
    """Write ``_shared.py`` containing enums, shared models, and RootModel wrappers."""
    texts = [text for _, text in classes]
    stdlib, typing_names, pydantic_names = _detect_imports(texts)

    lines: list[str] = []
    lines.append('"""Shared Pydantic models, enums, and base types used across domains."""')
    lines.append("")
    lines.append("from __future__ import annotations")
    lines.append("")

    for imp in stdlib:
        lines.append(imp)
    if stdlib:
        lines.append("")

    if typing_names:
        lines.append(f"from typing import {', '.join(typing_names)}")
        lines.append("")

    if pydantic_names:
        lines.append(f"from pydantic import {', '.join(pydantic_names)}")
        lines.append("")

    lines.append("")
    for _name, text in classes:
        lines.append(text)
        lines.append("")
        lines.append("")

    all_names = [name for name, _ in classes]
    all_block = "__all__ = [\n" + "".join(f'    "{n}",\n' for n in all_names) + "]"
    lines.append(all_block)
    lines.append("")

    (output_dir / "_shared.py").write_text("\n".join(lines))


def _write_models_init(
    modules: dict[str, list[tuple[str, str]]],
    rebuild_names: list[str],
    output_dir: Path,
) -> None:
    """Write the re-exporting ``__init__.py``."""
    sorted_module_names = ["_shared"] + sorted(m for m in modules if m != "_shared")

    all_class_names: list[str] = []
    for mod in sorted_module_names:
        for name, _ in modules[mod]:
            all_class_names.append(name)
    all_class_names.sort()

    lines: list[str] = []
    lines.append('"""Pydantic models for the Jira Cloud REST API.')
    lines.append("")
    lines.append("Models are organized into domain-themed submodules for navigability.")
    lines.append("All names are re-exported here for backward compatibility::")
    lines.append("")
    lines.append("    from jirapi.models import Issue          # works")
    lines.append("    from jirapi.models.issues import Issue   # also works")
    lines.append('"""')
    lines.append("")
    lines.append("from __future__ import annotations")
    lines.append("")
    lines.append("import sys as _sys")
    lines.append("")

    for mod in sorted_module_names:
        lines.append(f"from jirapi.models.{mod} import *  # noqa: F403")
    lines.append("")

    # Inject full namespace into submodules so Pydantic can resolve
    # cross-module type annotations via typing.get_type_hints().
    lines.append("_all_types = {k: v for k, v in globals().items() if isinstance(v, type)}")
    lines.append("for _mod in (")
    lines.append("    m")
    lines.append("    for name, m in _sys.modules.items()")
    lines.append('    if name.startswith("jirapi.models.") and m is not None')
    lines.append("):")
    lines.append("    _mod.__dict__.update(_all_types)")
    lines.append("")

    if rebuild_names:
        for rn in rebuild_names:
            lines.append(f"{rn}.model_rebuild()  # noqa: F405")
        lines.append("")

    all_block = "\n__all__ = [\n" + "".join(f'    "{n}",\n' for n in all_class_names) + "]\n"
    lines.append(all_block)

    (output_dir / "__init__.py").write_text("\n".join(lines))


# ──────────────────────────────────────────────────────────────────────
# Main
# ──────────────────────────────────────────────────────────────────────


def main() -> None:
    """Run datamodel-codegen, post-process, split into submodules, and format."""
    if not OPENAPI_SPEC.exists():
        print(f"ERROR: OpenAPI spec not found at {OPENAPI_SPEC}", file=sys.stderr)
        sys.exit(1)

    MODELS_DIR.mkdir(parents=True, exist_ok=True)

    # ── Phase 1: Generate monolithic file ──
    cmd = [
        sys.executable,
        "-m",
        "datamodel_code_generator",
        "--input",
        str(OPENAPI_SPEC),
        "--output",
        str(STAGING_FILE),
        "--output-model-type",
        "pydantic_v2.BaseModel",
        "--target-python-version",
        "3.11",
        "--input-file-type",
        "openapi",
        "--use-union-operator",
        "--use-annotated",
        "--field-constraints",
        "--use-default-kwarg",
        "--collapse-root-models",
        "--snake-case-field",
        "--use-standard-collections",
        "--enum-field-as-literal",
        "one",
        "--set-default-enum-member",
        "--strict-nullable",
    ]

    print("Running datamodel-codegen …")
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print("STDOUT:", result.stdout, file=sys.stderr)
        print("STDERR:", result.stderr, file=sys.stderr)
        sys.exit(result.returncode)
    print("  Monolithic output generated.")

    print("Post-processing …")
    content = STAGING_FILE.read_text()
    content = _fix_builtin_shadows(content)
    content = _strip_discriminators(content)
    content = _strip_bean_suffix(content)

    # ── Phase 2: Parse classes and rebuild calls ──
    print("Parsing class definitions …")
    classes = _parse_classes(content)
    rebuild_names = _extract_rebuild_names(content)
    print(f"  {len(classes)} classes, {len(rebuild_names)} model_rebuild calls")

    # ── Phase 3: Build domain mapping ──
    print("Building domain mapping from OpenAPI spec …")
    spec = json.loads(OPENAPI_SPEC.read_text())
    schema_groups = _build_schema_to_groups(spec)

    # ── Phase 4: Assign to modules ──
    print("Assigning classes to submodules …")
    modules, assigned = _assign_to_modules(classes, schema_groups)

    shared_count = len(modules.get("_shared", []))
    domain_count = sum(len(v) for k, v in modules.items() if k != "_shared")
    domain_modules = sorted(k for k in modules if k != "_shared")
    print(
        f"  {shared_count} shared, {domain_count} domain-specific"
        f" across {len(domain_modules)} modules"
    )

    # ── Phase 5: Clean old files and write new submodules ──
    print("Writing submodule files …")

    # Remove old single-file output and any prior submodules
    for existing in MODELS_DIR.glob("*.py"):
        existing.unlink()

    shared_names = {name for name, _ in modules.get("_shared", [])}
    _write_shared_module(modules.get("_shared", []), MODELS_DIR)

    for mod_name in domain_modules:
        _write_submodule(mod_name, modules[mod_name], shared_names, MODELS_DIR)

    _write_models_init(modules, rebuild_names, MODELS_DIR)

    # Remove staging file
    STAGING_FILE.unlink(missing_ok=True)

    # ── Phase 6: Format ──
    print("Running ruff format …")
    subprocess.run(["uv", "run", "ruff", "format", str(MODELS_DIR)], check=True)

    print("Running ruff check --fix …")
    subprocess.run(
        ["uv", "run", "ruff", "check", str(MODELS_DIR), "--fix"],
        check=False,
    )

    models_rel = MODELS_DIR.relative_to(REPO_ROOT)
    print(f"\nDone. Models split into {len(domain_modules) + 1} submodules under {models_rel}/")
    print(f"  _shared.py: {shared_count} models (enums + cross-domain)")
    for mod_name in domain_modules:
        print(f"  {mod_name}.py: {len(modules[mod_name])} models")


if __name__ == "__main__":
    main()
