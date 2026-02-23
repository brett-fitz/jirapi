"""jirapi — Modern Python Jira client with sync and async support."""

from importlib.metadata import version

from jirapi.client import AsyncJira, Jira
from jirapi.exceptions import (
    AuthenticationError,
    ConflictError,
    ForbiddenError,
    JiraError,
    NotFoundError,
    RateLimitError,
    ServerError,
    ValidationError,
)


__version__ = version("jirapi")

__all__ = [
    "__version__",
    "Jira",
    "AsyncJira",
    "JiraError",
    "AuthenticationError",
    "ConflictError",
    "ForbiddenError",
    "NotFoundError",
    "RateLimitError",
    "ServerError",
    "ValidationError",
]
