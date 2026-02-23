"""Tests for jirapi.pagination."""

from __future__ import annotations

import httpx
import pytest
import respx

from jirapi import AsyncJira, Jira
from jirapi.pagination import (
    paginate_cursor,
    paginate_cursor_async,
    paginate_offset,
    paginate_offset_async,
    paginate_page_bean,
    paginate_page_bean_async,
)


BASE_URL = "https://test.atlassian.net"


class TestPaginateOffset:
    """Offset-based pagination (startAt / maxResults / total)."""

    @respx.mock(base_url=BASE_URL)
    def test_single_page(self, respx_mock: respx.MockRouter) -> None:
        respx_mock.get("/rest/api/3/search").mock(
            return_value=httpx.Response(
                200,
                json={
                    "startAt": 0,
                    "maxResults": 50,
                    "total": 2,
                    "issues": [{"key": "A-1"}, {"key": "A-2"}],
                },
            )
        )
        client = Jira(url=BASE_URL, email="a@b.com", api_token="tok")
        items = list(paginate_offset(client._request, "GET", "/rest/api/3/search"))
        assert len(items) == 2
        assert items[0]["key"] == "A-1"
        client.close()

    @respx.mock(base_url=BASE_URL)
    def test_multiple_pages(self, respx_mock: respx.MockRouter) -> None:
        respx_mock.get("/rest/api/3/search").mock(
            side_effect=[
                httpx.Response(
                    200,
                    json={
                        "startAt": 0,
                        "maxResults": 2,
                        "total": 3,
                        "issues": [{"key": "A-1"}, {"key": "A-2"}],
                    },
                ),
                httpx.Response(
                    200,
                    json={
                        "startAt": 2,
                        "maxResults": 2,
                        "total": 3,
                        "issues": [{"key": "A-3"}],
                    },
                ),
            ]
        )
        client = Jira(url=BASE_URL, email="a@b.com", api_token="tok")
        items = list(
            paginate_offset(
                client._request,
                "GET",
                "/rest/api/3/search",
                max_results=2,
            )
        )
        assert len(items) == 3
        client.close()


class TestPaginatePageBean:
    """PageBean pagination (values / isLast)."""

    @respx.mock(base_url=BASE_URL)
    def test_single_page_with_is_last(self, respx_mock: respx.MockRouter) -> None:
        respx_mock.get("/rest/api/3/project/search").mock(
            return_value=httpx.Response(
                200,
                json={
                    "startAt": 0,
                    "maxResults": 50,
                    "isLast": True,
                    "values": [{"key": "PROJ"}],
                },
            )
        )
        client = Jira(url=BASE_URL, email="a@b.com", api_token="tok")
        items = list(paginate_page_bean(client._request, "GET", "/rest/api/3/project/search"))
        assert len(items) == 1
        client.close()

    @respx.mock(base_url=BASE_URL)
    def test_multiple_pages(self, respx_mock: respx.MockRouter) -> None:
        respx_mock.get("/rest/api/3/project/search").mock(
            side_effect=[
                httpx.Response(
                    200,
                    json={
                        "startAt": 0,
                        "maxResults": 1,
                        "isLast": False,
                        "values": [{"key": "A"}],
                    },
                ),
                httpx.Response(
                    200,
                    json={
                        "startAt": 1,
                        "maxResults": 1,
                        "isLast": True,
                        "values": [{"key": "B"}],
                    },
                ),
            ]
        )
        client = Jira(url=BASE_URL, email="a@b.com", api_token="tok")
        items = list(
            paginate_page_bean(
                client._request,
                "GET",
                "/rest/api/3/project/search",
                max_results=1,
            )
        )
        assert [i["key"] for i in items] == ["A", "B"]
        client.close()


class TestPaginateCursor:
    """Cursor-based pagination (nextPageToken)."""

    @respx.mock(base_url=BASE_URL)
    def test_follows_next_page_token(self, respx_mock: respx.MockRouter) -> None:
        respx_mock.get("/rest/api/3/search/jql").mock(
            side_effect=[
                httpx.Response(
                    200,
                    json={
                        "issues": [{"key": "A-1"}],
                        "nextPageToken": "abc123",
                    },
                ),
                httpx.Response(
                    200,
                    json={
                        "issues": [{"key": "A-2"}],
                    },
                ),
            ]
        )
        client = Jira(url=BASE_URL, email="a@b.com", api_token="tok")
        items = list(paginate_cursor(client._request, "GET", "/rest/api/3/search/jql"))
        assert len(items) == 2
        client.close()


class TestAsyncPaginateOffset:
    """Async offset-based pagination."""

    @pytest.mark.asyncio()
    @respx.mock(base_url=BASE_URL)
    async def test_single_page(self, respx_mock: respx.MockRouter) -> None:
        respx_mock.get("/rest/api/3/search").mock(
            return_value=httpx.Response(
                200,
                json={
                    "startAt": 0,
                    "maxResults": 50,
                    "total": 1,
                    "issues": [{"key": "A-1"}],
                },
            )
        )
        client = AsyncJira(url=BASE_URL, email="a@b.com", api_token="tok")
        items = [
            item
            async for item in paginate_offset_async(client._request, "GET", "/rest/api/3/search")
        ]
        assert len(items) == 1
        await client.close()


class TestAsyncPaginatePageBean:
    """Async PageBean pagination."""

    @pytest.mark.asyncio()
    @respx.mock(base_url=BASE_URL)
    async def test_single_page(self, respx_mock: respx.MockRouter) -> None:
        respx_mock.get("/rest/api/3/project/search").mock(
            return_value=httpx.Response(
                200,
                json={
                    "startAt": 0,
                    "maxResults": 50,
                    "isLast": True,
                    "values": [{"key": "PROJ"}],
                },
            )
        )
        client = AsyncJira(url=BASE_URL, email="a@b.com", api_token="tok")
        items = [
            item
            async for item in paginate_page_bean_async(
                client._request, "GET", "/rest/api/3/project/search"
            )
        ]
        assert len(items) == 1
        await client.close()


class TestAsyncPaginateCursor:
    """Async cursor-based pagination."""

    @pytest.mark.asyncio()
    @respx.mock(base_url=BASE_URL)
    async def test_follows_token(self, respx_mock: respx.MockRouter) -> None:
        respx_mock.get("/rest/api/3/search/jql").mock(
            side_effect=[
                httpx.Response(
                    200,
                    json={
                        "issues": [{"key": "A-1"}],
                        "nextPageToken": "tok1",
                    },
                ),
                httpx.Response(
                    200,
                    json={"issues": [{"key": "A-2"}]},
                ),
            ]
        )
        client = AsyncJira(url=BASE_URL, email="a@b.com", api_token="tok")
        items = [
            item
            async for item in paginate_cursor_async(
                client._request, "GET", "/rest/api/3/search/jql"
            )
        ]
        assert len(items) == 2
        await client.close()
