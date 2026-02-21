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
task check                  # lint + format check + tests
task lock:check             # verify lockfile is up-to-date
```

### Building
```bash
task build                  # uv build
```

## Architecture and Code Organization

```
jirapi/                     # Python package (the library)
├── __init__.py             # Public API exports
├── client.py               # Jira (sync + async)
├── models/                 # Pydantic request/response models
├── exceptions.py           # Custom exception hierarchy
└── py.typed                # PEP 561 marker

tests/                      # Test suites
├── unit/                   # Unit tests (pytest default)
│   └── conftest.py         # Shared fixtures
└── integration/            # Integration tests (live API)

docs/                       # Documentation
```

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

### Development Workflow

1. Create feature branch
2. Make changes following coding standards
3. Run quality checks: `task format && task lint`
4. Run tests: `task test:cov`
5. Verify lockfile: `task lock:check`
6. Submit PR using the PR template
