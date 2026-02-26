"""Tests for WorkflowStatusCategories and AsyncWorkflowStatusCategories."""

from __future__ import annotations

import httpx
import pytest
import respx

from jirapi import AsyncJira, Jira
from jirapi.models import StatusCategory3


BASE_URL = "https://test.atlassian.net"

SAMPLE_CATEGORY = {
    "self": "https://test.atlassian.net/rest/api/3/statuscategory/4",
    "id": 4,
    "key": "indeterminate",
    "colorName": "yellow",
    "name": "In Progress",
}

SAMPLE_CATEGORIES = [
    {
        "self": "https://test.atlassian.net/rest/api/3/statuscategory/1",
        "id": 1,
        "key": "undefined",
        "colorName": "medium-gray",
        "name": "No Category",
    },
    SAMPLE_CATEGORY,
    {
        "self": "https://test.atlassian.net/rest/api/3/statuscategory/2",
        "id": 2,
        "key": "new",
        "colorName": "blue-gray",
        "name": "To Do",
    },
]


class TestWorkflowStatusCategoriesSync:
    """Sync WorkflowStatusCategories returns StatusCategory3 models."""

    @respx.mock(base_url=BASE_URL)
    def test_list_returns_list_of_models(self, respx_mock: respx.MockRouter) -> None:
        respx_mock.get("/rest/api/3/statuscategory").mock(
            return_value=httpx.Response(200, json=SAMPLE_CATEGORIES)
        )
        client = Jira(url=BASE_URL, email="a@b.com", api_token="tok")
        result = client.workflows.status_categories.list()

        assert isinstance(result, list)
        assert len(result) == 3
        assert all(isinstance(r, StatusCategory3) for r in result)
        assert result[1].name == "In Progress"
        assert result[1].color_name == "yellow"
        client.close()

    @respx.mock(base_url=BASE_URL)
    def test_get_returns_single_model(self, respx_mock: respx.MockRouter) -> None:
        respx_mock.get("/rest/api/3/statuscategory/4").mock(
            return_value=httpx.Response(200, json=SAMPLE_CATEGORY)
        )
        client = Jira(url=BASE_URL, email="a@b.com", api_token="tok")
        result = client.workflows.status_categories.get("4")

        assert isinstance(result, StatusCategory3)
        assert result.id == 4
        assert result.key == "indeterminate"
        assert result.color_name == "yellow"
        client.close()


class TestWorkflowStatusCategoriesAsync:
    """Async WorkflowStatusCategories returns StatusCategory3 models."""

    @pytest.mark.asyncio()
    @respx.mock(base_url=BASE_URL)
    async def test_list_returns_list_of_models(self, respx_mock: respx.MockRouter) -> None:
        respx_mock.get("/rest/api/3/statuscategory").mock(
            return_value=httpx.Response(200, json=SAMPLE_CATEGORIES)
        )
        client = AsyncJira(url=BASE_URL, email="a@b.com", api_token="tok")
        result = await client.workflows.status_categories.list()

        assert isinstance(result, list)
        assert len(result) == 3
        assert all(isinstance(r, StatusCategory3) for r in result)
        assert result[0].name == "No Category"
        await client.close()

    @pytest.mark.asyncio()
    @respx.mock(base_url=BASE_URL)
    async def test_get_returns_single_model(self, respx_mock: respx.MockRouter) -> None:
        respx_mock.get("/rest/api/3/statuscategory/4").mock(
            return_value=httpx.Response(200, json=SAMPLE_CATEGORY)
        )
        client = AsyncJira(url=BASE_URL, email="a@b.com", api_token="tok")
        result = await client.workflows.status_categories.get("4")

        assert isinstance(result, StatusCategory3)
        assert result.name == "In Progress"
        assert result.id == 4
        await client.close()
