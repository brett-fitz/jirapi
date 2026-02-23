#!/usr/bin/env python3
"""Generate Pydantic v2 models from the Jira Cloud OpenAPI specification.

Wraps ``datamodel-code-generator`` with the project's preferred flags, runs a
post-processing pass to fix Python-builtin field-name collisions, then formats
with ``ruff``.

Usage::

    uv run python scripts/generate_models.py
"""

from __future__ import annotations

from pathlib import Path
import re
import subprocess
import sys


REPO_ROOT = Path(__file__).resolve().parent.parent
OPENAPI_SPEC = REPO_ROOT / "docs" / "jira-cloud-api-openapi.json"
MODELS_DIR = REPO_ROOT / "jirapi" / "models"
OUTPUT_FILE = MODELS_DIR / "__init__.py"

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


def _camel_to_snake(name: str) -> str:
    """Convert a camelCase string to snake_case."""
    s1 = re.sub(r"([A-Z]+)([A-Z][a-z])", r"\1_\2", name)
    return re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", s1).lower()


def _fix_builtin_shadows(content: str) -> str:
    """Replace problematic generated classes whose fields shadow Python builtins.

    The Jira OpenAPI spec includes ``JsonNode`` (Jackson's generic JSON
    representation) with properties named ``float``, ``int``, ``type``, etc.
    ``from __future__ import annotations`` causes Pydantic to resolve those
    names from the class namespace instead of builtins.

    Rather than fragile field-renaming, we replace the entire ``JsonNode``
    class with a permissive ``extra="allow"`` model that correctly represents
    arbitrary JSON.
    """
    content = _replace_class(content, "JsonNode", _JSONNODE_REPLACEMENT)
    return content


def _strip_discriminators(content: str) -> str:
    """Remove ``discriminator=...`` from Field() calls and standalone usages.

    ``datamodel-code-generator`` emits discriminators using JSON alias names
    (camelCase), but Pydantic v2 with ``--snake-case-field`` renames fields to
    snake_case.  Rather than mapping every alias, we strip discriminators
    entirely — Pydantic will still validate union types by trying each member.
    """
    q = r"""['"]"""  # match single or double quote
    val = r"""[^'"]*"""  # match value inside quotes
    disc = rf"discriminator={q}{val}{q}"

    # Field(discriminator='...') -> Field()  (sole argument)
    content = re.sub(rf"Field\({disc}\)", "Field()", content)
    # discriminator='...' as trailing arg: , discriminator='...'
    content = re.sub(rf",\s*{disc}", "", content)
    # discriminator='...' as leading arg: discriminator='...',
    content = re.sub(rf"{disc},\s*", "", content)
    # standalone discriminator='...' (not inside Field)
    content = re.sub(rf"\s*{disc},?", "", content)
    # Clean up empty Field() inside Annotated
    content = re.sub(r",\s*Field\(\)", "", content)
    # After stripping Field(discriminator=...), some Annotated[X,] are left
    # with a trailing comma and only one argument.  Two-pass cleanup:
    #  1) Drop the empty trailing-comma element: Annotated[X,] -> Annotated[X]
    #  2) Unwrap single-arg Annotated: Annotated[X] -> X  (invalid in typing)
    # The pattern `,\s*\]` is safe to collapse globally (trailing commas are
    # redundant before `]` in Python).

    # Pass 1: remove trailing comma before ]  (handles multi-line)
    prev = None
    while prev != content:
        prev = content
        content = re.sub(r",(\s*)\]", r"\1]", content)

    # Pass 2: unwrap Annotated[X] that now have only one arg (no comma inside)
    content = re.sub(r"Annotated\[([^,\[\]]+)\]", r"\1", content)

    return content


def _replace_class(content: str, class_name: str, replacement: str) -> str:
    """Replace a top-level class definition with *replacement* text."""
    pattern = re.compile(
        rf"^class {class_name}\(.*?\):.*?(?=\nclass |\n[A-Z]|\Z)",
        re.MULTILINE | re.DOTALL,
    )
    return pattern.sub(replacement.rstrip(), content, count=1)


def main() -> None:
    """Run datamodel-codegen and post-process the output."""
    if not OPENAPI_SPEC.exists():
        print(f"ERROR: OpenAPI spec not found at {OPENAPI_SPEC}", file=sys.stderr)
        sys.exit(1)

    MODELS_DIR.mkdir(parents=True, exist_ok=True)

    cmd = [
        sys.executable,
        "-m",
        "datamodel_code_generator",
        "--input",
        str(OPENAPI_SPEC),
        "--output",
        str(OUTPUT_FILE),
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
    print("  Models generated successfully.")

    print("Post-processing …")
    content = OUTPUT_FILE.read_text()
    content = _fix_builtin_shadows(content)
    content = _strip_discriminators(content)
    OUTPUT_FILE.write_text(content)

    print("Running ruff format …")
    subprocess.run(
        ["uv", "run", "ruff", "format", str(MODELS_DIR)],
        check=True,
    )

    print("Running ruff check --fix …")
    subprocess.run(
        ["uv", "run", "ruff", "check", str(MODELS_DIR), "--fix"],
        check=False,
    )

    print(f"Done. Models written to {OUTPUT_FILE.relative_to(REPO_ROOT)}")


if __name__ == "__main__":
    main()
