"""Shared test fixtures for jirapi unit tests."""

from __future__ import annotations

import pytest
import respx

from jirapi import AsyncJira, Jira


BASE_URL = "https://test.atlassian.net"


@pytest.fixture()
def mock_router() -> respx.MockRouter:
    """Provide a ``respx`` mock router for intercepting HTTPX requests."""
    with respx.mock(base_url=BASE_URL, assert_all_called=False) as router:
        yield router


@pytest.fixture()
def sync_client(mock_router: respx.MockRouter) -> Jira:
    """Create a synchronous ``Jira`` client wired to the mock router."""
    client = Jira(url=BASE_URL, email="test@acme.com", api_token="fake-token")
    return client


@pytest.fixture()
def async_client(mock_router: respx.MockRouter) -> AsyncJira:
    """Create an asynchronous ``AsyncJira`` client wired to the mock router."""
    client = AsyncJira(url=BASE_URL, email="test@acme.com", api_token="fake-token")
    return client
