"""Tests for sub-resource wiring (verifies @cached_property plumbing)."""

from __future__ import annotations

import httpx
import pytest
import respx

from jirapi import AsyncJira, Jira


BASE_URL = "https://test.atlassian.net"


class TestIssueSubResourcesSync:
    """Verify issues sub-resource access and basic calls (sync)."""

    def test_sub_resource_types(self) -> None:
        client = Jira(url=BASE_URL, email="a@b.com", api_token="tok")
        from jirapi.issues.attachments import IssueAttachments
        from jirapi.issues.comments import IssueComments
        from jirapi.issues.links import IssueLinks
        from jirapi.issues.properties import IssueProperties
        from jirapi.issues.votes import IssueVotes
        from jirapi.issues.watchers import IssueWatchers
        from jirapi.issues.worklogs import IssueWorklogs

        assert isinstance(client.issues.comments, IssueComments)
        assert isinstance(client.issues.attachments, IssueAttachments)
        assert isinstance(client.issues.worklogs, IssueWorklogs)
        assert isinstance(client.issues.votes, IssueVotes)
        assert isinstance(client.issues.watchers, IssueWatchers)
        assert isinstance(client.issues.links, IssueLinks)
        assert isinstance(client.issues.properties, IssueProperties)
        client.close()

    def test_sub_resource_cached(self) -> None:
        client = Jira(url=BASE_URL, email="a@b.com", api_token="tok")
        assert client.issues.comments is client.issues.comments
        assert client.issues.worklogs is client.issues.worklogs
        client.close()

    @respx.mock(base_url=BASE_URL)
    def test_comments_list(self, respx_mock: respx.MockRouter) -> None:
        respx_mock.get("/rest/api/3/issue/KEY-1/comment").mock(
            return_value=httpx.Response(
                200,
                json={
                    "startAt": 0,
                    "maxResults": 50,
                    "total": 0,
                    "comments": [],
                },
            )
        )
        client = Jira(url=BASE_URL, email="a@b.com", api_token="tok")
        result = client.issues.comments.list("KEY-1")
        assert result.total == 0
        client.close()


class TestIssueSubResourcesAsync:
    """Verify issues sub-resource access (async)."""

    @pytest.mark.asyncio()
    async def test_sub_resource_types(self) -> None:
        from jirapi.issues.comments import AsyncIssueComments

        async with AsyncJira(url=BASE_URL, email="a@b.com", api_token="tok") as client:
            assert isinstance(client.issues.comments, AsyncIssueComments)
            assert client.issues.comments is client.issues.comments

    @pytest.mark.asyncio()
    @respx.mock(base_url=BASE_URL)
    async def test_comments_list(self, respx_mock: respx.MockRouter) -> None:
        respx_mock.get("/rest/api/3/issue/KEY-1/comment").mock(
            return_value=httpx.Response(
                200,
                json={
                    "startAt": 0,
                    "maxResults": 50,
                    "total": 0,
                    "comments": [],
                },
            )
        )
        async with AsyncJira(url=BASE_URL, email="a@b.com", api_token="tok") as client:
            result = await client.issues.comments.list("KEY-1")
            assert result.total == 0


class TestProjectSubResources:
    """Verify project sub-resource wiring."""

    def test_sub_resource_types(self) -> None:
        client = Jira(url=BASE_URL, email="a@b.com", api_token="tok")
        from jirapi.projects.components import ProjectComponents
        from jirapi.projects.roles import ProjectRoles
        from jirapi.projects.versions import ProjectVersions

        assert isinstance(client.projects.versions, ProjectVersions)
        assert isinstance(client.projects.components, ProjectComponents)
        assert isinstance(client.projects.roles, ProjectRoles)
        client.close()

    def test_sub_resource_cached(self) -> None:
        client = Jira(url=BASE_URL, email="a@b.com", api_token="tok")
        assert client.projects.roles is client.projects.roles
        assert client.projects.versions is client.projects.versions
        client.close()
