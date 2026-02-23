"""Custom exception hierarchy for jirapi.

Maps Jira Cloud REST API error responses and HTTP status codes to typed,
catchable Python exceptions.
"""

from __future__ import annotations

from typing import Any


__all__ = [
    "JiraError",
    "AuthenticationError",
    "ForbiddenError",
    "NotFoundError",
    "ConflictError",
    "RateLimitError",
    "ServerError",
    "ValidationError",
]


class JiraError(Exception):
    """Base exception for all Jira API errors.

    Attributes:
        status_code: HTTP status code from the response, if available.
        errors: Field-level error mapping from Jira's ``ErrorCollection``.
        error_messages: List of top-level error messages from the response.
        response_body: Raw response body for debugging.
    """

    def __init__(  # noqa: D107
        self,
        message: str,
        *,
        status_code: int | None = None,
        errors: dict[str, str] | None = None,
        error_messages: list[str] | None = None,
        response_body: Any = None,
    ) -> None:
        super().__init__(message)
        self.status_code = status_code
        self.errors = errors or {}
        self.error_messages = error_messages or []
        self.response_body = response_body


class ValidationError(JiraError):
    """Raised on 400 Bad Request — invalid input or failed validation."""


class AuthenticationError(JiraError):
    """Raised on 401 Unauthorized — missing or invalid credentials."""


class ForbiddenError(JiraError):
    """Raised on 403 Forbidden — valid credentials but insufficient permissions."""


class NotFoundError(JiraError):
    """Raised on 404 Not Found — the requested resource does not exist."""


class ConflictError(JiraError):
    """Raised on 409 Conflict — resource state conflict (e.g. duplicate key)."""


class RateLimitError(JiraError):
    """Raised on 429 Too Many Requests.

    Attributes:
        retry_after: Seconds to wait before retrying, parsed from the
            ``Retry-After`` header when available.
    """

    def __init__(  # noqa: D107
        self,
        message: str,
        *,
        retry_after: float | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(message, **kwargs)
        self.retry_after = retry_after


class ServerError(JiraError):
    """Raised on 5xx responses — an error on the Jira server side."""


_STATUS_CODE_TO_EXCEPTION: dict[int, type[JiraError]] = {
    400: ValidationError,
    401: AuthenticationError,
    403: ForbiddenError,
    404: NotFoundError,
    409: ConflictError,
    429: RateLimitError,
}


def exception_for_status(status_code: int) -> type[JiraError]:
    """Return the appropriate exception class for an HTTP status code."""
    if status_code in _STATUS_CODE_TO_EXCEPTION:
        return _STATUS_CODE_TO_EXCEPTION[status_code]
    if 500 <= status_code < 600:
        return ServerError
    return JiraError
