"""Tests for jirapi.exceptions."""

from __future__ import annotations

import pytest

from jirapi.exceptions import (
    AuthenticationError,
    ConflictError,
    ForbiddenError,
    JiraError,
    NotFoundError,
    RateLimitError,
    ServerError,
    ValidationError,
    exception_for_status,
)


class TestExceptionHierarchy:
    """All custom exceptions inherit from JiraError."""

    def test_jira_error_is_exception(self) -> None:
        assert issubclass(JiraError, Exception)

    @pytest.mark.parametrize(
        "exc_cls",
        [
            AuthenticationError,
            ForbiddenError,
            NotFoundError,
            ConflictError,
            RateLimitError,
            ServerError,
            ValidationError,
        ],
    )
    def test_subclass_of_jira_error(self, exc_cls: type[JiraError]) -> None:
        assert issubclass(exc_cls, JiraError)


class TestJiraErrorAttributes:
    """JiraError stores useful context from the API response."""

    def test_default_attributes(self) -> None:
        err = JiraError("boom")
        assert str(err) == "boom"
        assert err.status_code is None
        assert err.errors == {}
        assert err.error_messages == []
        assert err.response_body is None

    def test_custom_attributes(self) -> None:
        err = JiraError(
            "bad",
            status_code=400,
            errors={"summary": "required"},
            error_messages=["Something went wrong"],
            response_body={"errorMessages": ["Something went wrong"]},
        )
        assert err.status_code == 400
        assert err.errors == {"summary": "required"}
        assert err.error_messages == ["Something went wrong"]
        assert err.response_body is not None


class TestRateLimitError:
    """RateLimitError carries retry_after."""

    def test_retry_after(self) -> None:
        err = RateLimitError("slow down", retry_after=30.0, status_code=429)
        assert err.retry_after == 30.0
        assert err.status_code == 429

    def test_retry_after_none(self) -> None:
        err = RateLimitError("slow down")
        assert err.retry_after is None


class TestExceptionForStatus:
    """exception_for_status maps HTTP codes to exception classes."""

    @pytest.mark.parametrize(
        ("code", "expected"),
        [
            (400, ValidationError),
            (401, AuthenticationError),
            (403, ForbiddenError),
            (404, NotFoundError),
            (409, ConflictError),
            (429, RateLimitError),
            (500, ServerError),
            (502, ServerError),
            (503, ServerError),
            (418, JiraError),
        ],
    )
    def test_mapping(self, code: int, expected: type[JiraError]) -> None:
        assert exception_for_status(code) is expected
