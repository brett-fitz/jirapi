# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/), and this project adheres to [Semantic Versioning](https://semver.org/).

## [0.3.0] - 2026-02-26

### Added

- **ty type checking**: Added Astral's `ty` type checker as a dev dependency. Run locally with `task typecheck`; a dedicated `typecheck` CI job runs in parallel with `lint` on every PR. Two rules that produce known false positives on auto-generated code (`unresolved-reference`, `invalid-type-form`) are downgraded to warnings in `[tool.ty.rules]` until the underlying generator patterns are addressed.

### Fixed

- **StatusCategory bug**: `WorkflowStatusCategories.list()` and `.get()` called `.model_validate()` on `StatusCategory` (a `StrEnum`), which would crash at runtime with `AttributeError`. Fixed to use the correct `StatusCategory3` `BaseModel`, and `list()` now properly parses the array response.
- **Resource generator enum guard**: `generate_resources.py` now detects enum response models and emits a warning instead of generating `.model_validate()` calls that would fail at runtime.

## [0.2.0] - 2026-02-25

### Changed (BREAKING)

- **Resource consolidation**: Consolidated 97 OpenAPI-tag-based resource files into 39 logical resource groups. Major domains (issues, projects, fields, screens, workflows, users) now use sub-resources for better organization (e.g. `jira.issues.comments`, `jira.projects.versions`)
- **Method name simplification**: Shortened verbose method names using auto-stripping and manual overrides. Examples: `jira.issue_search.search_and_reconsile_issues_using_jql()` → `jira.issues.search()`, `jira.issues.get_issue()` → `jira.issues.get()`, `jira.projects.search_projects()` → `jira.projects.search()`
- **Directory restructuring**: Moved from flat `jirapi/resources/*.py` to per-group packages `jirapi/<group>/` (e.g. `jirapi/issues/`, `jirapi/projects/`). Each group has `_resource.py` (core methods) and optional sub-resource modules
- **Import paths**: All resource imports changed from `jirapi.resources.<tag>` to `jirapi.<group>` (e.g. `from jirapi.issues import Issues`)
- Client properties reduced from 97 to 39 for better discoverability

### Added

- **Stripped Bean suffixes**: Removed the Java-inherited `Bean` suffix from 95 model class names (e.g. `IssueBean` → `Issue`, `CommentBean` → `Comment`, `ProjectBean` → `Project`). 3 redundant Bean variants (`UserBean`, `IconBean`, `FieldAssociationSchemeLinksBean`) were merged into their existing non-Bean counterparts
- **Models domain split**: Split the monolithic `models/__init__.py` (21K lines) into 37 domain-themed submodules plus `_shared.py`. Models are now navigable by domain (e.g. `from jirapi.models.issues import Issue`) while `from jirapi.models import Issue` remains fully supported
- Sub-resource pattern: major resource groups expose sub-resources as `@cached_property` (e.g. `jira.issues.comments`, `jira.issues.worklogs`, `jira.projects.roles`)
- 14 new model organization tests covering backward-compatible imports, domain submodule imports, cross-module Pydantic annotation resolution, and `__all__` completeness
- 7 new sub-resource wiring tests verifying type correctness and caching behavior
- Method name conflict detection in the code generator with automatic fallback to original names
- Taskfile commands for code generation: `task generate`, `task generate:models`, `task generate:resources`

## [0.1.0] - 2026-02-22

### Added

- Sync (`Jira`) and async (`AsyncJira`) client classes with HTTPX transport
- Foundation layer: `_BaseClient`, `SyncAPIClient`, `AsyncAPIClient` with shared auth, URL building, and error handling
- Composition pattern: 60+ resource groups exposed as `@cached_property` attributes (e.g. `jira.issues`, `jira.projects`)
- Custom exception hierarchy: `JiraError`, `AuthenticationError`, `ForbiddenError`, `NotFoundError`, `ConflictError`, `RateLimitError`, `ServerError`, `ValidationError`
- 967 auto-generated Pydantic v2 models from the Jira Cloud OpenAPI schema
- 580+ auto-generated endpoint methods across sync and async resource classes
- Pagination helpers for offset-based, PageBean, and cursor-based patterns (sync + async)
- Code generation scripts: `scripts/generate_models.py` and `scripts/generate_resources.py`
- Unit test suite (50 tests) covering exceptions, base client, pagination, issues, and projects
- CI pipeline with ruff lint/format, pytest matrix (Python 3.11/3.12/3.13/3.14), coverage reporting, and PyPI publish on release
- Claude AI workflows: issue triage, issue coding, PR review comments, and automated code review
- GitHub Sponsors funding configuration
- Bug report issue template (structured YAML form)
- `__all__` declarations in `jirapi/models/__init__.py` and `jirapi/resources/__init__.py`

### Fixed

- 12 endpoint methods that incorrectly returned `None` instead of their actual response type (`str`, `int`, `dict[str, Any]`, or Pydantic model) due to unhandled OpenAPI schema patterns (primitive types, `oneOf`, `additionalProperties`, inline objects)
- Narrow exception handling in `_check_response` from bare `except Exception` to specific types
- Handle non-dict JSON bodies in error responses without crashing
- Replace magic number `30.0` timeout with `_DEFAULT_TIMEOUT` constant in client constructors
- Remove unused `resp` variable assignment in void resource methods

### Removed

- Dead `_parse_response` method from `_BaseClient` (never called)
