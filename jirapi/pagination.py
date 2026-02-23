"""Pagination helpers for Jira Cloud REST API responses.

Jira uses three pagination patterns:

- **Offset-based**: ``startAt`` / ``maxResults`` / ``total`` fields on the
  response object (e.g. ``SearchResults``).
- **PageBean**: ``startAt`` / ``maxResults`` / ``isLast`` / ``values`` wrapper
  (e.g. ``PageBeanProject``).
- **Cursor-based**: ``nextPageToken`` field returned in newer endpoints.

Each pattern is exposed as both a synchronous iterator and an asynchronous
iterator that yield individual items.
"""

from __future__ import annotations

from collections.abc import AsyncIterator, Iterator
from typing import Any, TypeVar

import httpx


__all__: list[str] = []

ItemT = TypeVar("ItemT")


# ──────────────────────────────────────────────────────────────────────
# Offset-based pagination  (startAt / maxResults / total)
# ──────────────────────────────────────────────────────────────────────


def paginate_offset(
    request_fn: Any,
    method: str,
    path: str,
    *,
    results_key: str = "issues",
    start_at: int = 0,
    max_results: int = 50,
    params: dict[str, Any] | None = None,
    **kwargs: Any,
) -> Iterator[dict[str, Any]]:
    """Synchronous offset-based pagination.

    Yields individual items from the *results_key* list until all pages
    have been fetched.

    Args:
        request_fn: The ``_request`` method on a sync client.
        method: HTTP method (usually ``"GET"`` or ``"POST"``).
        path: API endpoint path.
        results_key: JSON key containing the items list.
        start_at: Starting offset.
        max_results: Page size.
        params: Additional query parameters.
        **kwargs: Extra keyword arguments forwarded to *request_fn*.
    """
    base_params = dict(params or {})

    while True:
        page_params = {
            **base_params,
            "startAt": start_at,
            "maxResults": max_results,
        }
        resp: httpx.Response = request_fn(method, path, params=page_params, **kwargs)
        data = resp.json()

        items = data.get(results_key, [])
        yield from items

        total = data.get("total")
        start_at += len(items)

        if not items or (total is not None and start_at >= total):
            break


async def paginate_offset_async(
    request_fn: Any,
    method: str,
    path: str,
    *,
    results_key: str = "issues",
    start_at: int = 0,
    max_results: int = 50,
    params: dict[str, Any] | None = None,
    **kwargs: Any,
) -> AsyncIterator[dict[str, Any]]:
    """Asynchronous offset-based pagination.

    Yields individual items from the *results_key* list.
    """
    base_params = dict(params or {})

    while True:
        page_params = {
            **base_params,
            "startAt": start_at,
            "maxResults": max_results,
        }
        resp: httpx.Response = await request_fn(method, path, params=page_params, **kwargs)
        data = resp.json()

        items = data.get(results_key, [])
        for item in items:
            yield item

        total = data.get("total")
        start_at += len(items)

        if not items or (total is not None and start_at >= total):
            break


# ──────────────────────────────────────────────────────────────────────
# PageBean pagination  (startAt / maxResults / isLast / values)
# ──────────────────────────────────────────────────────────────────────


def paginate_page_bean(
    request_fn: Any,
    method: str,
    path: str,
    *,
    start_at: int = 0,
    max_results: int = 50,
    params: dict[str, Any] | None = None,
    **kwargs: Any,
) -> Iterator[dict[str, Any]]:
    """Synchronous PageBean pagination.

    Yields individual items from the ``values`` list until ``isLast`` is
    ``True`` or no more items are returned.
    """
    base_params = dict(params or {})

    while True:
        page_params = {
            **base_params,
            "startAt": start_at,
            "maxResults": max_results,
        }
        resp: httpx.Response = request_fn(method, path, params=page_params, **kwargs)
        data = resp.json()

        values = data.get("values", [])
        yield from values

        if data.get("isLast", True) or not values:
            break

        start_at += len(values)


async def paginate_page_bean_async(
    request_fn: Any,
    method: str,
    path: str,
    *,
    start_at: int = 0,
    max_results: int = 50,
    params: dict[str, Any] | None = None,
    **kwargs: Any,
) -> AsyncIterator[dict[str, Any]]:
    """Asynchronous PageBean pagination.

    Yields individual items from the ``values`` list.
    """
    base_params = dict(params or {})

    while True:
        page_params = {
            **base_params,
            "startAt": start_at,
            "maxResults": max_results,
        }
        resp: httpx.Response = await request_fn(method, path, params=page_params, **kwargs)
        data = resp.json()

        values = data.get("values", [])
        for item in values:
            yield item

        if data.get("isLast", True) or not values:
            break

        start_at += len(values)


# ──────────────────────────────────────────────────────────────────────
# Cursor-based pagination  (nextPageToken)
# ──────────────────────────────────────────────────────────────────────


def paginate_cursor(
    request_fn: Any,
    method: str,
    path: str,
    *,
    results_key: str = "issues",
    params: dict[str, Any] | None = None,
    **kwargs: Any,
) -> Iterator[dict[str, Any]]:
    """Synchronous cursor-based pagination.

    Yields individual items, following ``nextPageToken`` until exhausted.
    """
    base_params = dict(params or {})
    token: str | None = None

    while True:
        page_params = {**base_params}
        if token:
            page_params["nextPageToken"] = token

        resp: httpx.Response = request_fn(method, path, params=page_params, **kwargs)
        data = resp.json()

        items = data.get(results_key, [])
        yield from items

        token = data.get("nextPageToken")
        if not token or not items:
            break


async def paginate_cursor_async(
    request_fn: Any,
    method: str,
    path: str,
    *,
    results_key: str = "issues",
    params: dict[str, Any] | None = None,
    **kwargs: Any,
) -> AsyncIterator[dict[str, Any]]:
    """Asynchronous cursor-based pagination.

    Yields individual items, following ``nextPageToken`` until exhausted.
    """
    base_params = dict(params or {})
    token: str | None = None

    while True:
        page_params = {**base_params}
        if token:
            page_params["nextPageToken"] = token

        resp: httpx.Response = await request_fn(method, path, params=page_params, **kwargs)
        data = resp.json()

        items = data.get(results_key, [])
        for item in items:
            yield item

        token = data.get("nextPageToken")
        if not token or not items:
            break
