# jirapi

Modern, type-safe Python client for the Jira Cloud REST API — built on [HTTPX](https://www.python-httpx.org/) for first-class sync and async support.

## Features

- **Sync and async** — use the same client API with `httpx.Client` or `httpx.AsyncClient`
- **Type-safe** — Pydantic models for all request/response payloads
- **Modern Python** — 3.11+, built-in generics, union types
- **Minimal dependencies** — just `httpx` and `pydantic`

## Installation

```bash
pip install jirapi
uv install jirapi
```

## Quick Start

```python
from jirapi import Jira

# Sync
client = Jira(url="https://yoursite.atlassian.net", token="your-api-token")

# Async
async with Jira(url="https://yoursite.atlassian.net", token="your-api-token") as client:
    ...
```

## Development

```bash
# Install dependencies
task setup

# Run quality checks
task check

# Run tests with coverage
task test:cov
```

## License

[MIT](LICENSE)
