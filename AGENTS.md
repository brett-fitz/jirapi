# AGENTS.md

This file provides guidance to AI coding agents when working with code in this repository.

## Project Overview

`jirapi` is a modern, type-safe Python client for the Jira Cloud REST API, built on [HTTPX](https://www.python-httpx.org/) for first-class sync and async support.

**Technology Stack:**
- Python 3.11+ with UV for dependency management
- [Taskfile](https://taskfile.dev/) (go-task) for task running (`Taskfile.yml`)
- Ruff for linting and formatting
- pytest for testing with pytest-cov for coverage
- HTTPX for HTTP transport (sync + async)
- Pydantic for data models and validation

## Common Development Commands

### Setup and Installation
```bash
task setup                  # uv sync --all-groups
uv run python -c "import jirapi; print('OK')"
```

### Testing
```bash
task test                   # uv run pytest tests/unit
task test:cov               # uv run pytest --cov=jirapi tests/unit
uv run pytest tests/unit/test_specific.py  # single file
task test:integration       # requires live Jira API access
```

### Code Quality
```bash
task format                 # uv run ruff format .
task lint                   # uv run ruff check .
task lint:fix               # uv run ruff check . --fix
task typecheck              # uv run ty check jirapi
task check                  # lint + format check + typecheck + tests
task lock:check             # verify lockfile is up-to-date
```

### Code Generation
```bash
task generate:models        # generate Pydantic models from OpenAPI spec
task generate:resources     # generate resource classes from OpenAPI spec
task generate               # run all generators (models + resources)
```

### Building
```bash
task build                  # uv build
```

## Architecture and Code Organization

```
jirapi/                          # Python package (the library)
├── __init__.py                  # Public API exports
├── client.py                    # Jira (sync) + AsyncJira — entry points (~39 @cached_property)
├── _base_client.py              # Shared HTTP logic, auth, error checking
├── _resource.py                 # SyncAPIResource / AsyncAPIResource base classes
├── _types.py                    # Type aliases (JSON, Params, T)
├── exceptions.py                # Custom exception hierarchy
├── pagination.py                # Offset / PageBean / cursor iterators
├── models/                      # 1086 auto-generated Pydantic v2 models (domain split)
│   ├── __init__.py              # Re-exports all models for backward compat
│   ├── _shared.py               # Enums + cross-domain models (~241 classes)
│   ├── issues.py                # Issue-domain models (~170 classes)
│   ├── projects.py              # Project-domain models (~98 classes)
│   ├── workflows.py             # Workflow-domain models (~129 classes)
│   └── ...                      # 37 domain submodules total
├── issues/                      # Resource group with sub-resources
│   ├── __init__.py              # Exports Issues, AsyncIssues
│   ├── _resource.py             # Core methods + @cached_property sub-resource wiring
│   ├── comments.py              # Sub-resource: IssueComments, AsyncIssueComments
│   ├── attachments.py           # Sub-resource: IssueAttachments
│   ├── worklogs.py              # Sub-resource: IssueWorklogs
│   └── ...                      # votes, watchers, links, properties, etc.
├── projects/                    # Resource group with sub-resources
│   ├── _resource.py             # Core: CRUD, search + merged small tags
│   ├── versions.py              # Sub-resource: ProjectVersions
│   └── ...                      # components, roles, categories, etc.
├── labels/                      # Standalone resource group (small, 1 method)
│   ├── __init__.py
│   └── _resource.py
└── ...                          # 39 resource groups total, 37 sub-resources
└── py.typed                     # PEP 561 marker

scripts/                         # Code generation scripts
├── generate_models.py           # OpenAPI → Pydantic models
└── generate_resources.py        # OpenAPI → resource packages + client wiring

tests/                           # Test suites
├── unit/                        # Unit tests (pytest default)
│   └── conftest.py              # Shared fixtures
└── integration/                 # Integration tests (live API)

docs/                            # Documentation
```

### Models Organization

Models are split into domain-themed submodules under `jirapi/models/` for navigability.  The public API (`from jirapi.models import X`) is unchanged — `__init__.py` re-exports everything.

- **`_shared.py`**: All enums, RootModel wrappers, and models used by 2+ domain groups
- **Domain modules** (e.g. `issues.py`, `projects.py`): Models used exclusively by that domain's API operations
- **Assignment logic**: The model generator uses the OpenAPI spec + `TAG_CONSOLIDATION` to transitively map each schema to the domain groups that reference it.  Single-group → domain module, multi-group → `_shared`
- **Cross-module resolution**: `__init__.py` injects all type names into submodule namespaces so Pydantic can resolve cross-module type annotations at validation time

### Resource Organization

Resources are consolidated from the 97 OpenAPI tags into ~39 logical groups:

- **Major domains** (issues, projects, fields, screens, workflows, users) have sub-resources accessed via `@cached_property` (e.g. `jira.issues.comments`, `jira.projects.roles`)
- **Merged groups** (permissions, issue_types, priorities, etc.) combine related tags into a single flat resource
- **Standalone groups** (labels, webhooks, server_info, etc.) stay self-contained

The code generator (`scripts/generate_resources.py`) contains:
- `TAG_CONSOLIDATION` dict mapping each OpenAPI tag → `(group, sub_resource | None)`
- `METHOD_NAME_OVERRIDES` dict for explicit method name mappings
- Auto-strip algorithm that removes redundant resource-context tokens from method names
- Conflict detection that falls back to original names when auto-stripping produces duplicates

## Code Style and Standards

### Python Style

**Imports:**
- Use absolute imports over relative imports
- Order imports alphabetically (isort via ruff)

**Type Hints:**
- Use type hints for all function parameters and returns
- Prefer built-in generics (`list[str]`, `dict[str, int]`) over `typing` equivalents
- Use union syntax (`str | None`) instead of `Optional[str]`
- Do not import deprecated typing names (`Dict`, `List`, `Set`, `Tuple`, `Optional`)

**Naming Conventions:**
- snake_case for functions and variables
- PascalCase for classes
- UPPER_CASE for constants
- Maximum line length: 100 characters

**Docstrings:**
- Use Google-style docstrings (configured in ruff)
- Document all public APIs
- Focus on why, not what
- Every module must have a module-level docstring

**Other Rules:**
- `__init__.py` files must define `__all__` to declare the public API
- Always specify exception types — never use bare `except:` or `except Exception:` without good reason
- Prefer `async def` for all I/O-bound operations
- Constants over magic numbers
- Single responsibility per function

### Testing Requirements

- Write tests before fixing bugs
- Test edge cases and error scenarios
- Use pytest for all testing
- Use proper mocking with pytest-mock and respx (for HTTPX)
- Use fixtures for test setup
- Mark integration tests with `@pytest.mark.integration`
- **MUST run `task format && task lint` before completion**

### Security

- Never commit credentials or sensitive information
- Never hardcode API tokens — accept them as parameters
- Sanitize all user inputs

### Version Control

- Feature branches: `feature/<description>`
- Bugfix branches: `fix/<description>`
- Small, focused commits with clear messages
- Follow semantic versioning (MAJOR.MINOR.PATCH)
- **MUST run `task format && task lint` before considering work complete**

### Changelog

- **MUST update `CHANGELOG.md`** when making user-facing changes
- Add a new version section (e.g. `## [0.2.0] - YYYY-MM-DD`) or append to the latest unreleased section at the top
- Use the appropriate subsection: `Added`, `Changed`, `Fixed`, `Removed`
- Follow [Keep a Changelog](https://keepachangelog.com/) format
- Do not modify entries for already-released versions

### Development Workflow

1. Create feature branch
2. Make changes following coding standards
3. Run quality checks: `task format && task lint`
4. Run tests: `task test:cov`
5. Verify lockfile: `task lock:check`
6. Update `CHANGELOG.md`
7. Submit PR using the PR template
