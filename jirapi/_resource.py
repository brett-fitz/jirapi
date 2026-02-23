"""Base resource classes for the composition pattern.

Every generated resource (e.g. ``Issues``, ``Projects``) inherits from
``SyncAPIResource`` or ``AsyncAPIResource``.  The resource holds a
back-reference to the parent client and delegates all HTTP calls through it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING


__all__: list[str] = []

if TYPE_CHECKING:
    from jirapi._base_client import AsyncAPIClient, SyncAPIClient


class SyncAPIResource:
    """Base class for synchronous resource groups."""

    _client: SyncAPIClient

    def __init__(self, client: SyncAPIClient) -> None:
        self._client = client


class AsyncAPIResource:
    """Base class for asynchronous resource groups."""

    _client: AsyncAPIClient

    def __init__(self, client: AsyncAPIClient) -> None:
        self._client = client
