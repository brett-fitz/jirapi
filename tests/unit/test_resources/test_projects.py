"""Tests for jirapi.projects (Projects / AsyncProjects)."""

from __future__ import annotations

import httpx
import pytest
import respx

from jirapi import AsyncJira, Jira


BASE_URL = "https://test.atlassian.net"


class TestProjectsSync:
    """Synchronous Projects resource tests."""

    @respx.mock(base_url=BASE_URL)
    def test_get_project(self, respx_mock: respx.MockRouter) -> None:
        respx_mock.get("/rest/api/3/project/PROJ").mock(
            return_value=httpx.Response(
                200,
                json={
                    "id": "10000",
                    "key": "PROJ",
                    "name": "My Project",
                    "self": "https://test.atlassian.net/rest/api/3/project/10000",
                },
            )
        )
        client = Jira(url=BASE_URL, email="a@b.com", api_token="tok")
        project = client.projects.get("PROJ")
        assert project.key == "PROJ"
        assert project.name == "My Project"
        client.close()

    @respx.mock(base_url=BASE_URL)
    def test_search_projects(self, respx_mock: respx.MockRouter) -> None:
        respx_mock.get("/rest/api/3/project/search").mock(
            return_value=httpx.Response(
                200,
                json={
                    "startAt": 0,
                    "maxResults": 50,
                    "total": 1,
                    "isLast": True,
                    "values": [
                        {
                            "id": "10000",
                            "key": "PROJ",
                            "name": "My Project",
                            "self": "https://test.atlassian.net/rest/api/3/project/10000",
                        }
                    ],
                },
            )
        )
        client = Jira(url=BASE_URL, email="a@b.com", api_token="tok")
        result = client.projects.search()
        assert result.total == 1
        client.close()


class TestProjectsAsync:
    """Asynchronous Projects resource tests."""

    @pytest.mark.asyncio()
    @respx.mock(base_url=BASE_URL)
    async def test_get_project(self, respx_mock: respx.MockRouter) -> None:
        respx_mock.get("/rest/api/3/project/PROJ").mock(
            return_value=httpx.Response(
                200,
                json={
                    "id": "10000",
                    "key": "PROJ",
                    "name": "My Project",
                    "self": "https://test.atlassian.net/rest/api/3/project/10000",
                },
            )
        )
        async with AsyncJira(url=BASE_URL, email="a@b.com", api_token="tok") as client:
            project = await client.projects.get("PROJ")
            assert project.key == "PROJ"
