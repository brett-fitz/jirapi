# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/), and this project adheres to [Semantic Versioning](https://semver.org/).

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
- CI pipeline with ruff lint/format, pytest matrix (Python 3.11/3.12/3.13), coverage reporting, and PyPI publish on release
- Claude AI workflows: issue triage, issue coding, PR review comments, and automated code review
- GitHub Sponsors funding configuration
- Bug report issue template (structured YAML form)
