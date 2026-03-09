"""Base client classes providing shared and transport-specific HTTP logic.

``_BaseClient`` holds all transport-agnostic behaviour (auth setup, URL
building, response checking, parameter filtering).  ``SyncAPIClient`` and
``AsyncAPIClient`` extend it with synchronous / asynchronous HTTP transport
via *httpx*.
"""

from __future__ import annotations

from collections.abc import Generator
import contextlib
import logging
from typing import Any, Self

import httpx

from jirapi.exceptions import RateLimitError, exception_for_status


__all__: list[str] = []

logger = logging.getLogger("jirapi")

_DEFAULT_TIMEOUT: float = 30.0


class _BearerAuth(httpx.Auth):
    """HTTPX auth handler that injects a ``Bearer`` token."""

    def __init__(self, token: str) -> None:
        self._token = token

    def auth_flow(self, request: httpx.Request) -> Generator[httpx.Request, Any, None]:
        request.headers["Authorization"] = f"Bearer {self._token}"
        yield request


class _BaseClient:
    """Transport-agnostic base shared by both sync and async clients.

    Handles authentication, common headers, response validation, and
    parameter construction.
    """

    _base_url: str
    _auth: httpx.Auth
    _timeout: float

    def __init__(
        self,
        *,
        url: str,
        email: str | None = None,
        api_token: str | None = None,
        token: str | None = None,
        auth: httpx.Auth | None = None,
        timeout: float = _DEFAULT_TIMEOUT,
        **_httpx_client_kwargs: Any,
    ) -> None:
        self._base_url = url.rstrip("/")
        self._auth = self._resolve_auth(
            email=email,
            api_token=api_token,
            token=token,
            auth=auth,
        )
        self._timeout = timeout
        self._httpx_client_kwargs = _httpx_client_kwargs
        self._default_headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

    @staticmethod
    def _resolve_auth(
        *,
        email: str | None,
        api_token: str | None,
        token: str | None,
        auth: httpx.Auth | None,
    ) -> httpx.Auth:
        """Validate auth arguments and return the appropriate ``httpx.Auth``."""
        has_basic = email is not None or api_token is not None
        has_token = token is not None
        has_auth = auth is not None

        provided = sum([has_basic, has_token, has_auth])
        if provided == 0:
            raise ValueError(
                "No authentication provided. Supply one of: (email + api_token), token, or auth."
            )
        if provided > 1:
            raise ValueError(
                "Multiple authentication methods provided. Supply exactly one of: "
                "(email + api_token), token, or auth."
            )

        if has_basic:
            if email is None or api_token is None:
                raise ValueError("Basic auth requires both 'email' and 'api_token'.")
            return httpx.BasicAuth(username=email, password=api_token)

        if has_token:
            return _BearerAuth(token)  # type: ignore[arg-type]

        return auth  # type: ignore[return-value]

    # --------------------------------------------------------------------- #
    # Response helpers
    # --------------------------------------------------------------------- #

    def _check_response(self, response: httpx.Response) -> None:
        """Raise a typed ``JiraError`` subclass on non-2xx responses."""
        if response.is_success:
            return

        status = response.status_code
        error_messages: list[str] = []
        errors: dict[str, str] = {}
        body: Any = None

        try:
            body = response.json()
        except (ValueError, UnicodeDecodeError):
            body = response.text
        else:
            if isinstance(body, dict):
                error_messages = body.get("errorMessages", [])
                errors = body.get("errors", {})

        message_parts = error_messages or [response.reason_phrase or "Unknown error"]
        message = f"[{status}] {'; '.join(message_parts)}"

        exc_cls = exception_for_status(status)

        kwargs: dict[str, Any] = {
            "status_code": status,
            "errors": errors,
            "error_messages": error_messages,
            "response_body": body,
        }

        if exc_cls is RateLimitError:
            retry_after_raw = response.headers.get("Retry-After")
            retry_after: float | None = None
            if retry_after_raw:
                with contextlib.suppress(ValueError):
                    retry_after = float(retry_after_raw)
            kwargs["retry_after"] = retry_after

        raise exc_cls(message, **kwargs)

    # --------------------------------------------------------------------- #
    # Parameter helpers
    # --------------------------------------------------------------------- #

    @staticmethod
    def _build_params(**kwargs: Any) -> dict[str, Any]:
        """Filter out ``None`` values from keyword arguments."""
        return {k: v for k, v in kwargs.items() if v is not None}


class SyncAPIClient(_BaseClient):
    """Synchronous HTTP client backed by ``httpx.Client``."""

    _client: httpx.Client

    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self._client = httpx.Client(
            base_url=self._base_url,
            auth=self._auth,
            headers=self._default_headers,
            timeout=self._timeout,
            **self._httpx_client_kwargs,
        )

    # --------------------------------------------------------------------- #
    # Core request
    # --------------------------------------------------------------------- #

    def _request(self, method: str, path: str, **kwargs: Any) -> httpx.Response:
        """Send a synchronous HTTP request and check the response."""
        resp = self._client.request(method, path, **kwargs)
        self._check_response(resp)
        return resp

    # --------------------------------------------------------------------- #
    # Context manager
    # --------------------------------------------------------------------- #

    def __enter__(self) -> Self:
        return self

    def __exit__(self, *_args: Any) -> None:
        self.close()

    def close(self) -> None:
        """Close the underlying HTTPX client and release resources."""
        self._client.close()


class AsyncAPIClient(_BaseClient):
    """Asynchronous HTTP client backed by ``httpx.AsyncClient``."""

    _client: httpx.AsyncClient

    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self._client = httpx.AsyncClient(
            base_url=self._base_url,
            auth=self._auth,
            headers=self._default_headers,
            timeout=self._timeout,
            **self._httpx_client_kwargs,
        )

    # --------------------------------------------------------------------- #
    # Core request
    # --------------------------------------------------------------------- #

    async def _request(self, method: str, path: str, **kwargs: Any) -> httpx.Response:
        """Send an asynchronous HTTP request and check the response."""
        resp = await self._client.request(method, path, **kwargs)
        self._check_response(resp)
        return resp

    # --------------------------------------------------------------------- #
    # Async context manager
    # --------------------------------------------------------------------- #

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, *_args: Any) -> None:
        await self.close()

    async def close(self) -> None:
        """Close the underlying async HTTPX client and release resources."""
        await self._client.aclose()
