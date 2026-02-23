#!/usr/bin/env python3
"""Generate sync + async resource classes from the Jira Cloud OpenAPI spec.

Reads the OpenAPI JSON, groups operations by tag, and emits:
  - ``jirapi/resources/<tag>.py`` with ``<Tag>(SyncAPIResource)``
    and ``Async<Tag>(AsyncAPIResource)`` classes.
  - Updates ``jirapi/client.py`` with ``@cached_property`` wiring.

Usage::

    uv run python scripts/generate_resources.py
"""

from __future__ import annotations

from collections import defaultdict
import json
from pathlib import Path
import re
import subprocess
import textwrap
from typing import Any


REPO_ROOT = Path(__file__).resolve().parent.parent
OPENAPI_SPEC = REPO_ROOT / "docs" / "jira-cloud-api-openapi.json"
RESOURCES_DIR = REPO_ROOT / "jirapi" / "resources"
CLIENT_FILE = REPO_ROOT / "jirapi" / "client.py"

# ──────────────────────────────────────────────────────────────────────
# Helpers
# ──────────────────────────────────────────────────────────────────────


def _camel_to_snake(name: str) -> str:
    # Some operationIds have dots (e.g., "resource.method") — take last segment
    if "." in name:
        name = name.rsplit(".", 1)[-1]
    s1 = re.sub(r"([A-Z]+)([A-Z][a-z])", r"\1_\2", name)
    result = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", s1).lower()
    # Ensure valid Python identifier
    result = re.sub(r"[^a-z0-9_]", "_", result)
    result = re.sub(r"_+", "_", result).strip("_")
    return result


def _tag_to_module(tag: str) -> str:
    return tag.lower().replace(" ", "_").replace("-", "_").replace("(", "").replace(")", "")


PYTHON_KEYWORDS = frozenset(
    {
        "False",
        "None",
        "True",
        "and",
        "as",
        "assert",
        "async",
        "await",
        "break",
        "class",
        "continue",
        "def",
        "del",
        "elif",
        "else",
        "except",
        "finally",
        "for",
        "from",
        "global",
        "if",
        "import",
        "in",
        "is",
        "lambda",
        "nonlocal",
        "not",
        "or",
        "pass",
        "raise",
        "return",
        "try",
        "while",
        "with",
        "yield",
        "type",
    }
)

PYTHON_BUILTINS = frozenset(
    {
        "filter",
        "format",
        "id",
        "input",
        "list",
        "map",
        "max",
        "min",
        "next",
        "object",
        "open",
        "print",
        "range",
        "set",
        "super",
        "type",
        "vars",
        "zip",
    }
)

RESERVED = PYTHON_KEYWORDS | PYTHON_BUILTINS


def _safe_param_name(name: str) -> str:
    """Ensure a parameter name isn't a Python keyword or builtin."""
    snake = _camel_to_snake(name)
    if snake in RESERVED:
        return snake + "_"
    return snake


def _tag_to_class(tag: str) -> str:
    return "".join(word.capitalize() for word in _tag_to_module(tag).split("_"))


def _ref_to_model(ref: str | None) -> str | None:
    if not ref:
        return None
    return ref.rsplit("/", 1)[-1]


def _resolve_schema_ref(schema: dict[str, Any]) -> str | None:
    if "$ref" in schema:
        return _ref_to_model(schema["$ref"])
    if "items" in schema and "$ref" in schema.get("items", {}):
        return _ref_to_model(schema["items"]["$ref"])
    return None


def _openapi_type_to_python(param: dict[str, Any]) -> str:
    schema = param.get("schema", {})
    t = schema.get("type", "str")
    mapping = {
        "string": "str",
        "integer": "int",
        "boolean": "bool",
        "number": "float",
        "array": "list[str]",
    }
    py = mapping.get(t, "str")
    if not param.get("required", False):
        return f"{py} | None"
    return py


def _get_success_response(op: dict[str, Any]) -> tuple[str | None, str]:
    """Return (model_name, status_code) for the first 2xx response with a schema."""
    for code in ("200", "201", "202", "204"):
        resp = op.get("responses", {}).get(code)
        if not resp:
            continue
        if code == "204":
            return None, code
        content = resp.get("content", {})
        json_ct = content.get("application/json", {})
        schema = json_ct.get("schema", {})
        model = _resolve_schema_ref(schema)
        if model:
            return model, code
        if schema.get("type") == "array":
            item_model = _resolve_schema_ref(schema)
            if item_model:
                return item_model, code
        return None, code
    return None, "200"


def _get_request_body(op: dict[str, Any]) -> str | None:
    body = op.get("requestBody", {})
    content = body.get("content", {})
    json_ct = content.get("application/json", {})
    schema = json_ct.get("schema", {})
    return _resolve_schema_ref(schema)


# ──────────────────────────────────────────────────────────────────────
# Parsing
# ──────────────────────────────────────────────────────────────────────


def parse_operations(spec: dict[str, Any]) -> dict[str, list[dict[str, Any]]]:
    """Group non-deprecated operations by their primary tag."""
    by_tag: dict[str, list[dict[str, Any]]] = defaultdict(list)

    for path, methods in spec.get("paths", {}).items():
        for http_method, op in methods.items():
            if http_method not in ("get", "post", "put", "delete", "patch"):
                continue
            if op.get("deprecated"):
                continue

            tags = op.get("tags", ["untagged"])
            tag = tags[0]
            operation_id = op.get("operationId", "")
            summary = op.get("summary", "")

            path_params = []
            query_params = []
            for p in op.get("parameters", []):
                if p.get("in") == "path":
                    path_params.append(
                        {
                            "name": _safe_param_name(p["name"]),
                            "original": p["name"],
                            "type": "str",
                            "required": True,
                        }
                    )
                elif p.get("in") == "query":
                    query_params.append(
                        {
                            "name": _safe_param_name(p["name"]),
                            "original": p["name"],
                            "type": _openapi_type_to_python(p),
                            "required": p.get("required", False),
                        }
                    )

            request_model = _get_request_body(op)
            response_model, status_code = _get_success_response(op)

            by_tag[tag].append(
                {
                    "operation_id": operation_id,
                    "method_name": _camel_to_snake(operation_id),
                    "http_method": http_method.upper(),
                    "path": path,
                    "summary": summary,
                    "path_params": path_params,
                    "query_params": query_params,
                    "request_model": request_model,
                    "response_model": response_model,
                    "status_code": status_code,
                }
            )

    return dict(by_tag)


# ──────────────────────────────────────────────────────────────────────
# Code generation
# ──────────────────────────────────────────────────────────────────────


def _build_method_sig(op: dict[str, Any], *, is_async: bool, renames: dict[str, str]) -> str:
    """Build the method signature line(s)."""
    parts = ["self"]

    for p in op["path_params"]:
        parts.append(f"{p['name']}: str")

    if op["request_model"]:
        model = renames.get(op["request_model"], op["request_model"])
        parts.append(f"body: {model}")

    kw_only_added = False
    for p in op["query_params"]:
        if not kw_only_added:
            parts.append("*")
            kw_only_added = True
        if p["required"]:
            parts.append(f"{p['name']}: {p['type']}")
        else:
            parts.append(f"{p['name']}: {p['type']} = None")

    args = ", ".join(parts)
    ret_model = op["response_model"]
    ret = renames.get(ret_model, ret_model) if ret_model else "None"
    prefix = "async def" if is_async else "def"
    return f"    {prefix} {op['method_name']}({args}) -> {ret}:"


def _build_method_body(op: dict[str, Any], *, is_async: bool, renames: dict[str, str]) -> list[str]:
    """Build the method body lines."""
    lines: list[str] = []

    # Docstring
    if op["summary"]:
        safe_summary = op["summary"].replace('"', '\\"')
        lines.append(f'        """{safe_summary}"""')

    # Build path with f-string substitutions
    path = op["path"]
    for p in op["path_params"]:
        path = path.replace("{" + p["original"] + "}", "{" + p["name"] + "}")

    # Build params dict
    if op["query_params"]:
        param_items = []
        for p in op["query_params"]:
            param_items.append(f'"{p["original"]}": {p["name"]}')
        lines.append(f"        params = self._client._build_params(**{{{', '.join(param_items)}}})")

    # Build kwargs
    kwargs = []
    if op["query_params"]:
        kwargs.append("params=params")
    if op["request_model"]:
        kwargs.append("json=body.model_dump(by_alias=True, exclude_none=True)")

    kwargs_str = ", ".join(kwargs)
    if kwargs_str:
        kwargs_str = ", " + kwargs_str

    # Request call
    await_prefix = "await " if is_async else ""
    method = op["http_method"]
    url_expr = f'f"{path}"' if op["path_params"] else f'"{path}"'
    lines.append(
        f'        resp = {await_prefix}self._client._request("{method}", {url_expr}{kwargs_str})'
    )

    # Return
    if op["response_model"]:
        model = renames.get(op["response_model"], op["response_model"])
        lines.append(f"        return {model}.model_validate(resp.json())")
    elif op["status_code"] == "204":
        lines.append("        return None")
    else:
        lines.append("        return None")

    return lines


def generate_resource_file(tag: str, operations: list[dict[str, Any]]) -> str:
    """Generate the full Python source for a resource module."""
    class_name = _tag_to_class(tag)
    async_class_name = f"Async{class_name}"

    # Collect model imports
    models: set[str] = set()
    for op in operations:
        if op["request_model"]:
            models.add(op["request_model"])
        if op["response_model"]:
            models.add(op["response_model"])

    lines: list[str] = []
    lines.append(f'"""Resource classes for the {tag} API group."""')
    lines.append("")
    lines.append("from __future__ import annotations")
    lines.append("")

    # Avoid import conflicts: if a model name matches the resource class name
    conflicting = models & {class_name, async_class_name}
    safe_models = models - conflicting
    renames = {c: f"{c}Model" for c in conflicting}

    if safe_models:
        model_imports = ", ".join(sorted(safe_models))
        lines.append(f"from jirapi.models import {model_imports}")
    for conflict in sorted(conflicting):
        lines.append(f"from jirapi.models import {conflict} as {conflict}Model")

    lines.append("from jirapi._resource import AsyncAPIResource, SyncAPIResource")
    lines.append("")
    lines.append("")

    # Sync class
    lines.append(f"class {class_name}(SyncAPIResource):")
    lines.append(f'    """Synchronous resource for the {tag} API group."""')
    lines.append("")
    for op in operations:
        lines.append(_build_method_sig(op, is_async=False, renames=renames))
        lines.extend(_build_method_body(op, is_async=False, renames=renames))
        lines.append("")

    lines.append("")

    # Async class
    lines.append(f"class {async_class_name}(AsyncAPIResource):")
    lines.append(f'    """Asynchronous resource for the {tag} API group."""')
    lines.append("")
    for op in operations:
        lines.append(_build_method_sig(op, is_async=True, renames=renames))
        lines.extend(_build_method_body(op, is_async=True, renames=renames))
        lines.append("")

    return "\n".join(lines)


def generate_client_file(tags: list[str]) -> str:
    """Generate jirapi/client.py with @cached_property for each resource."""
    sync_props: list[str] = []
    async_props: list[str] = []

    for tag in sorted(tags):
        module = _tag_to_module(tag)
        class_name = _tag_to_class(tag)
        async_class_name = f"Async{class_name}"
        prop_name = module

        sync_props.append(
            f"    @cached_property\n"
            f"    def {prop_name}(self) -> {class_name}:\n"
            f"        from jirapi.resources.{module} import {class_name}\n"
            f"\n"
            f"        return {class_name}(self)\n"
        )

        async_props.append(
            f"    @cached_property\n"
            f"    def {prop_name}(self) -> {async_class_name}:\n"
            f"        from jirapi.resources.{module} import {async_class_name}\n"
            f"\n"
            f"        return {async_class_name}(self)\n"
        )

    sync_block = "\n".join(sync_props)
    async_block = "\n".join(async_props)

    # Build TYPE_CHECKING imports for type hints
    type_imports: list[str] = []
    for tag in sorted(tags):
        module = _tag_to_module(tag)
        class_name = _tag_to_class(tag)
        async_class_name = f"Async{class_name}"
        type_imports.append(
            f"    from jirapi.resources.{module} import {async_class_name}, {class_name}"
        )
    type_imports_block = "\n".join(type_imports)

    return textwrap.dedent(f'''\
"""Public Jira client classes.

``Jira`` provides synchronous access and ``AsyncJira`` provides asynchronous
access to the Jira Cloud REST API.  Resource groups are exposed as
``@cached_property`` attributes (e.g. ``jira.issues``, ``jira.projects``).
"""

from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING, Any

from jirapi._base_client import AsyncAPIClient, SyncAPIClient


if TYPE_CHECKING:
{type_imports_block}

__all__ = ["Jira", "AsyncJira"]


class Jira(SyncAPIClient):
    """Synchronous Jira Cloud REST API client.

    Usage::

        from jirapi import Jira

        jira = Jira(url="https://acme.atlassian.net", email="me@acme.com", api_token="...")
        issue = jira.issues.get_issue("PROJ-123")

    Or as a context manager::

        with Jira(url="...", email="...", api_token="...") as jira:
            issue = jira.issues.get_issue("PROJ-123")
    """

    def __init__(  # noqa: D107
        self,
        *,
        url: str,
        email: str,
        api_token: str,
        timeout: float = 30.0,
        **httpx_client_kwargs: Any,
    ) -> None:
        super().__init__(
            url=url,
            email=email,
            api_token=api_token,
            timeout=timeout,
            **httpx_client_kwargs,
        )

{sync_block}

class AsyncJira(AsyncAPIClient):
    """Asynchronous Jira Cloud REST API client.

    Usage::

        from jirapi import AsyncJira

        async with AsyncJira(
            url="https://acme.atlassian.net", email="me@acme.com", api_token="..."
        ) as jira:
            issue = await jira.issues.get_issue("PROJ-123")
    """

    def __init__(  # noqa: D107
        self,
        *,
        url: str,
        email: str,
        api_token: str,
        timeout: float = 30.0,
        **httpx_client_kwargs: Any,
    ) -> None:
        super().__init__(
            url=url,
            email=email,
            api_token=api_token,
            timeout=timeout,
            **httpx_client_kwargs,
        )

{async_block}''')


# ──────────────────────────────────────────────────────────────────────
# Main
# ──────────────────────────────────────────────────────────────────────


def main() -> None:
    """Parse the OpenAPI spec and generate resource modules + client."""
    print("Loading OpenAPI spec …")
    spec = json.loads(OPENAPI_SPEC.read_text())

    print("Parsing operations …")
    by_tag = parse_operations(spec)

    total_ops = sum(len(ops) for ops in by_tag.values())
    print(f"  {total_ops} operations across {len(by_tag)} tags")

    RESOURCES_DIR.mkdir(parents=True, exist_ok=True)

    print("Generating resource modules …")
    for tag, operations in sorted(by_tag.items()):
        module = _tag_to_module(tag)
        source = generate_resource_file(tag, operations)
        (RESOURCES_DIR / f"{module}.py").write_text(source)

    # Write resources __init__
    init_lines = ['"""Generated resource classes for the Jira Cloud REST API."""', ""]
    for tag in sorted(by_tag.keys()):
        module = _tag_to_module(tag)
        class_name = _tag_to_class(tag)
        init_lines.append(f"from jirapi.resources.{module} import Async{class_name}, {class_name}")
    init_lines.append("")
    (RESOURCES_DIR / "__init__.py").write_text("\n".join(init_lines))

    print("Generating client.py …")
    client_source = generate_client_file(list(by_tag.keys()))
    CLIENT_FILE.write_text(client_source)

    print("Running ruff format …")
    subprocess.run(
        ["uv", "run", "ruff", "format", str(RESOURCES_DIR), str(CLIENT_FILE)],
        check=False,
    )

    print("Running ruff check --fix …")
    subprocess.run(
        ["uv", "run", "ruff", "check", str(RESOURCES_DIR), str(CLIENT_FILE), "--fix"],
        check=False,
    )

    print(f"Done. Generated {len(by_tag)} resource modules with {total_ops} endpoint methods.")


if __name__ == "__main__":
    main()
