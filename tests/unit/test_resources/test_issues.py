"""Tests for jirapi.resources.issues (Issues / AsyncIssues)."""

from __future__ import annotations

import httpx
import pytest
import respx

from jirapi import AsyncJira, Jira


BASE_URL = "https://test.atlassian.net"


class TestIssuesSync:
    """Synchronous Issues resource tests."""

    @respx.mock(base_url=BASE_URL)
    def test_get_issue(self, respx_mock: respx.MockRouter) -> None:
        respx_mock.get("/rest/api/3/issue/PROJ-1").mock(
            return_value=httpx.Response(
                200,
                json={
                    "id": "10001",
                    "key": "PROJ-1",
                    "self": "https://test.atlassian.net/rest/api/3/issue/10001",
                    "fields": {},
                },
            )
        )
        client = Jira(url=BASE_URL, email="a@b.com", api_token="tok")
        issue = client.issues.get_issue("PROJ-1")
        assert issue.key == "PROJ-1"
        assert issue.id == "10001"
        client.close()

    @respx.mock(base_url=BASE_URL)
    def test_create_issue(self, respx_mock: respx.MockRouter) -> None:
        respx_mock.post("/rest/api/3/issue").mock(
            return_value=httpx.Response(
                201,
                json={
                    "id": "10002",
                    "key": "PROJ-2",
                    "self": "https://test.atlassian.net/rest/api/3/issue/10002",
                },
            )
        )
        from jirapi.models import IssueUpdateDetails

        client = Jira(url=BASE_URL, email="a@b.com", api_token="tok")
        body = IssueUpdateDetails()
        created = client.issues.create_issue(body)
        assert created.key == "PROJ-2"
        client.close()

    @respx.mock(base_url=BASE_URL)
    def test_delete_issue(self, respx_mock: respx.MockRouter) -> None:
        respx_mock.delete("/rest/api/3/issue/PROJ-3").mock(return_value=httpx.Response(204))
        client = Jira(url=BASE_URL, email="a@b.com", api_token="tok")
        result = client.issues.delete_issue("PROJ-3")
        assert result is None
        client.close()


class TestIssuesAsync:
    """Asynchronous Issues resource tests."""

    @pytest.mark.asyncio()
    @respx.mock(base_url=BASE_URL)
    async def test_get_issue(self, respx_mock: respx.MockRouter) -> None:
        respx_mock.get("/rest/api/3/issue/PROJ-1").mock(
            return_value=httpx.Response(
                200,
                json={
                    "id": "10001",
                    "key": "PROJ-1",
                    "self": "https://test.atlassian.net/rest/api/3/issue/10001",
                    "fields": {},
                },
            )
        )
        async with AsyncJira(url=BASE_URL, email="a@b.com", api_token="tok") as client:
            issue = await client.issues.get_issue("PROJ-1")
            assert issue.key == "PROJ-1"
