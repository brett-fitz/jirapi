# jirapi

[![CI](https://github.com/brett-fitz/jirapi/actions/workflows/ci.yml/badge.svg)](https://github.com/brett-fitz/jirapi/actions/workflows/ci.yml)
[![PyPI](https://img.shields.io/pypi/v/jirapi)](https://pypi.org/project/jirapi/)
[![Python](https://img.shields.io/pypi/pyversions/jirapi)](https://pypi.org/project/jirapi/)
[![License](https://img.shields.io/pypi/l/jirapi)](LICENSE)
[![Downloads](https://img.shields.io/pypi/dm/jirapi)](https://pypistats.org/packages/jirapi)
[![Checked with ty](https://img.shields.io/badge/type--checked-ty-blue)](https://github.com/astral-sh/ty)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

Modern, type-safe Python client for the **Jira Cloud REST API** — built on [HTTPX](https://www.python-httpx.org/) for first-class sync and async support.

## Features

- **Sync and async** — identical API surface via `Jira` (sync) and `AsyncJira` (async)
- **Full API coverage** — auto-generated resource methods for 580+ Jira Cloud REST endpoints
- **Type-safe** — Pydantic v2 models for every request and response payload
- **Intuitive resource hierarchy** — `jira.issues.comments.list()`, `jira.projects.versions.create()`, etc.
- **Pagination helpers** — built-in iterators for offset, PageBean, and cursor pagination
- **Semantic exceptions** — `AuthenticationError`, `NotFoundError`, `RateLimitError`, etc.
- **Modern Python** — 3.11+, built-in generics, union types, no legacy `typing` imports
- **Minimal dependencies** — just `httpx` and `pydantic`

## Installation

```bash
pip install jirapi
# or
uv add jirapi
```

## Quick Start

### Synchronous

```python
from jirapi import Jira

jira = Jira(
    url="https://yoursite.atlassian.net",
    email="you@example.com",
    api_token="your-api-token",
)

# Fetch a single issue
issue = jira.issues.get("PROJ-123")
print(issue.fields.summary)

# Search with JQL
results = jira.issues.search(jql="project = PROJ ORDER BY created DESC")

# Access sub-resources
comments = jira.issues.comments.list("PROJ-123")
jira.issues.watchers.add("PROJ-123")

# Search projects
page = jira.projects.search(query="backend", max_results=10)

# Always close when done (or use a context manager)
jira.close()
```

### Context Manager

```python
from jirapi import Jira

with Jira(url="https://yoursite.atlassian.net", email="...", api_token="...") as jira:
    issue = jira.issues.get("PROJ-123")
```

### Asynchronous

```python
import asyncio
from jirapi import AsyncJira

async def main():
    async with AsyncJira(
        url="https://yoursite.atlassian.net",
        email="you@example.com",
        api_token="your-api-token",
    ) as jira:
        issue = await jira.issues.get("PROJ-123")
        print(issue.fields.summary)

asyncio.run(main())
```

## Authentication

Three mutually exclusive authentication strategies are supported. Supply exactly one when constructing a client.

### Basic Auth (Jira Cloud)

The most common method for Jira Cloud — uses your Atlassian account email and an [API token](https://id.atlassian.com/manage-profile/security/api-tokens):

```python
jira = Jira(
    url="https://yoursite.atlassian.net",
    email="you@example.com",
    api_token="your-api-token",
)
```

### Bearer Token / Personal Access Token

For Jira Data Center/Server (PATs) or when you already have an OAuth 2.0 access token:

```python
jira = Jira(
    url="https://yoursite.atlassian.net",
    token="your-personal-access-token",
)
```

### Custom Auth

Pass any `httpx.Auth` instance for full control — useful for OAuth 2.0 flows, Digest auth, or other schemes:

```python
import httpx

jira = Jira(
    url="https://yoursite.atlassian.net",
    auth=httpx.BasicAuth("service-account", "secret"),
)
```

## Resource Groups

All API endpoints are organised into logical resource groups accessible as properties on the client:

```python
jira.issues               # Issues: CRUD, search, transitions, bulk ops
jira.issues.comments      # Sub-resource: issue comments
jira.issues.attachments   # Sub-resource: issue attachments
jira.issues.worklogs      # Sub-resource: issue worklogs
jira.projects             # Projects: CRUD, search, features, email, validation
jira.projects.versions    # Sub-resource: project versions
jira.projects.components  # Sub-resource: project components
jira.projects.roles       # Sub-resource: project roles & actors
jira.users                # User lookup, search, preferences
jira.workflows            # Workflow definitions and management
jira.dashboards           # Dashboard operations
jira.filters              # Saved filter management
jira.permissions          # Permission checks and schemes
jira.fields               # Field configuration and custom fields
jira.screens              # Screen configuration
jira.jql                  # JQL utilities and functions
jira.plans                # Plans and team management
# … 39 resource groups with 37 sub-resources
```

Each method returns a strongly-typed Pydantic model:

```python
from jirapi.models import IssueUpdateDetails

# Create an issue
created = jira.issues.create(
    body=IssueUpdateDetails.model_validate({
        "fields": {
            "project": {"key": "PROJ"},
            "summary": "New issue from jirapi",
            "issuetype": {"name": "Task"},
        }
    })
)
print(created.key)
```

## Error Handling

All API errors are mapped to typed exceptions:

```python
from jirapi import Jira, NotFoundError, RateLimitError, AuthenticationError
import time

jira = Jira(url="...", email="...", api_token="...")

try:
    jira.issues.get("DOES-NOT-EXIST")
except NotFoundError as e:
    print(f"Issue not found: {e}")
except RateLimitError as e:
    print(f"Rate limited — retry after {e.retry_after}s")
    time.sleep(e.retry_after or 60)
except AuthenticationError:
    print("Check your credentials")
```

| Status Code | Exception            |
|-------------|----------------------|
| 400         | `ValidationError`    |
| 401         | `AuthenticationError`|
| 403         | `ForbiddenError`     |
| 404         | `NotFoundError`      |
| 409         | `ConflictError`      |
| 429         | `RateLimitError`     |
| 5xx         | `ServerError`        |

## Pagination

Resource methods that return lists handle pagination automatically. For lower-level control, jirapi exposes helpers for all three patterns used by the Jira API — offset-based (`startAt`/`total`), PageBean (`values`/`isLast`), and cursor-based (`nextPageToken`):

```python
from jirapi.pagination import paginate_offset, paginate_page_bean, paginate_cursor
```

Each helper accepts a request callable, HTTP method, path, and optional parameters, then yields individual items across all pages. See the `jirapi.pagination` module docstring for full signatures and async variants (`paginate_offset_async`, `paginate_page_bean_async`, `paginate_cursor_async`).

## Configuration

| Parameter              | Description                                      | Default |
|------------------------|--------------------------------------------------|---------|
| `url`                  | Jira Cloud instance URL                          | —       |
| `email`                | Account email for Basic auth                     | `None`  |
| `api_token`            | API token from id.atlassian.com                  | `None`  |
| `token`                | Personal access token or OAuth 2.0 Bearer token  | `None`  |
| `auth`                 | Custom `httpx.Auth` instance                     | `None`  |
| `timeout`              | Request timeout in seconds                       | `30.0`  |
| `**httpx_client_kwargs`| Extra kwargs passed to the underlying HTTPX client| —      |

Exactly one authentication method must be provided: `email` + `api_token`, `token`, or `auth`.

## Development

```bash
# Install dependencies
task setup          # uv sync --all-groups

# Run quality checks
task check          # lint + format check + tests

# Run tests with coverage
task test:cov       # uv run pytest --cov=jirapi tests/unit

# Regenerate models from OpenAPI spec
uv run python scripts/generate_models.py

# Regenerate resource classes and client wiring
uv run python scripts/generate_resources.py
```

## Architecture

```
jirapi/
├── client.py          # Jira (sync) + AsyncJira entry points
├── _base_client.py    # Shared HTTP logic, auth, error handling
├── models/            # 1 000+ auto-generated Pydantic v2 models (domain-split)
├── <group>/           # 39 resource packages (issues/, projects/, workflows/, …)
│   ├── _resource.py   # Core methods for the group
│   └── *.py           # Optional sub-resource modules (comments, versions, …)
├── pagination.py      # Offset / PageBean / cursor iterators
└── exceptions.py      # Typed exception hierarchy

scripts/
├── generate_models.py     # OpenAPI spec → Pydantic models
└── generate_resources.py  # OpenAPI spec → resource packages + client wiring
```

## Contributing

Contributions are welcome! Please [open an issue](https://github.com/brett-fitz/jirapi/issues) first to discuss proposed changes. See the [Development](#development) section for setup instructions.

## License

[MIT](LICENSE) | [Changelog](CHANGELOG.md) | [PyPI](https://pypi.org/project/jirapi/)
