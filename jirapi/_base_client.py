"""Base client classes providing shared and transport-specific HTTP logic.

``_BaseClient`` holds all transport-agnostic behaviour (auth setup, URL
building, response checking, parameter filtering).  ``SyncAPIClient`` and
``AsyncAPIClient`` extend it with synchronous / asynchronous HTTP transport
via *httpx*.
"""

from __future__ import annotations

import contextlib
import logging
from typing import Any, Self

import httpx
from pydantic import BaseModel

from jirapi._types import T
from jirapi.exceptions import RateLimitError, exception_for_status


__all__: list[str] = []

logger = logging.getLogger("jirapi")

_DEFAULT_TIMEOUT: float = 30.0


class _BaseClient:
    """Transport-agnostic base shared by both sync and async clients.

    Handles authentication, common headers, response validation, and
    parameter construction.
    """

    _base_url: str
    _auth: httpx.BasicAuth
    _timeout: float

    def __init__(
        self,
        *,
        url: str,
        email: str,
        api_token: str,
        timeout: float = _DEFAULT_TIMEOUT,
        **_httpx_client_kwargs: Any,
    ) -> None:
        self._base_url = url.rstrip("/")
        self._auth = httpx.BasicAuth(username=email, password=api_token)
        self._timeout = timeout
        self._httpx_client_kwargs = _httpx_client_kwargs
        self._default_headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

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
            error_messages = body.get("errorMessages", [])
            errors = body.get("errors", {})
        except Exception:  # noqa: BLE001
            body = response.text

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

    def _parse_response(self, response: httpx.Response, model: type[T]) -> T:
        """Validate a successful JSON response into a Pydantic model."""
        self._check_response(response)
        data = response.json()
        if isinstance(model, type) and issubclass(model, BaseModel):
            return model.model_validate(data)  # type: ignore[return-value]
        return data  # type: ignore[return-value]

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
