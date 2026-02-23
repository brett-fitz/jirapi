# jirapi

Modern, type-safe Python client for the **Jira Cloud REST API** — built on [HTTPX](https://www.python-httpx.org/) for first-class sync and async support.

## Features

- **Sync and async** — identical API surface via `Jira` (sync) and `AsyncJira` (async)
- **Full API coverage** — auto-generated resource methods for 580+ Jira Cloud REST endpoints
- **Type-safe** — Pydantic v2 models for every request and response payload
- **Composition pattern** — resource groups (`issues`, `projects`, `users`, …) exposed as lazy `@cached_property` attributes
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
issue = jira.issues.get_issue("PROJ-123")
print(issue.fields.summary)

# Search projects
page = jira.projects.search_projects(query="backend", max_results=10)

# Always close when done (or use a context manager)
jira.close()
```

### Context Manager

```python
from jirapi import Jira

with Jira(url="https://yoursite.atlassian.net", email="...", api_token="...") as jira:
    issue = jira.issues.get_issue("PROJ-123")
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
        issue = await jira.issues.get_issue("PROJ-123")
        print(issue.fields.summary)

asyncio.run(main())
```

## Resource Groups

All API endpoints are organised into resource groups accessible as properties on the client:

```python
jira.issues               # Issues, changelogs, transitions
jira.projects             # Projects CRUD and search
jira.users                # User lookup and management
jira.issue_search         # JQL search
jira.dashboards           # Dashboard operations
jira.filters              # Saved filter management
jira.workflows            # Workflow definitions
jira.permissions          # Permission checks
jira.server_info          # Jira instance metadata
# … 60+ resource groups in total
```

Each method returns a strongly-typed Pydantic model:

```python
from jirapi.models import IssueUpdateDetails

# Create an issue
created = jira.issues.create_issue(
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
    jira.issues.get_issue("DOES-NOT-EXIST")
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

jirapi provides pagination helpers for all three patterns used by the Jira API:

```python
from jirapi.pagination import paginate_offset, paginate_page_bean

# Offset-based (e.g. issue search)
for issue in paginate_offset(jira._request, "GET", "/rest/api/3/search", results_key="issues"):
    print(issue["key"])

# PageBean-based (e.g. project search)
for project in paginate_page_bean(jira._request, "GET", "/rest/api/3/project/search"):
    print(project["name"])
```

## Configuration

| Parameter              | Description                                      | Default |
|------------------------|--------------------------------------------------|---------|
| `url`                  | Jira Cloud instance URL                          | —       |
| `email`                | Account email for Basic auth                     | —       |
| `api_token`            | API token from id.atlassian.com                  | —       |
| `timeout`              | Request timeout in seconds                       | `30.0`  |
| `**httpx_client_kwargs`| Extra kwargs passed to the underlying HTTPX client| —      |

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
├── __init__.py          # Public API exports
├── client.py            # Jira (sync) + AsyncJira — entry points
├── _base_client.py      # Shared HTTP logic, auth, error checking
├── _resource.py         # SyncAPIResource / AsyncAPIResource bases
├── _types.py            # Type aliases (JSON, Params, T)
├── exceptions.py        # Exception hierarchy
├── pagination.py        # Offset / PageBean / cursor iterators
├── models/              # 967 auto-generated Pydantic v2 models
│   └── __init__.py
└── resources/           # 60+ auto-generated resource modules
    ├── __init__.py
    ├── issues.py        # Issues + AsyncIssues
    ├── projects.py      # Projects + AsyncProjects
    └── ...

scripts/
├── generate_models.py     # OpenAPI → Pydantic models
└── generate_resources.py  # OpenAPI → resource classes + client wiring
```

## License

[MIT](LICENSE)
