"""Tests for resource methods that return primitive types (str, int, dict).

These cover the code paths added when fixing 12 endpoints that previously
returned None due to unhandled OpenAPI schema patterns.
"""

from __future__ import annotations

import httpx
import pytest
import respx

from jirapi import AsyncJira, Jira


BASE_URL = "https://test.atlassian.net"


class TestStringReturn:
    """Endpoints that return -> str."""

    @respx.mock(base_url=BASE_URL)
    def test_get_preference_sync(self, respx_mock: respx.MockRouter) -> None:
        respx_mock.get("/rest/api/3/mypreferences").mock(
            return_value=httpx.Response(200, json="en_US")
        )
        client = Jira(url=BASE_URL, email="a@b.com", api_token="tok")
        result = client.myself.get_preference(key="user.locale")
        assert result == "en_US"
        assert isinstance(result, str)
        client.close()

    @pytest.mark.asyncio()
    @respx.mock(base_url=BASE_URL)
    async def test_get_preference_async(self, respx_mock: respx.MockRouter) -> None:
        respx_mock.get("/rest/api/3/mypreferences").mock(
            return_value=httpx.Response(200, json="en_US")
        )
        async with AsyncJira(url=BASE_URL, email="a@b.com", api_token="tok") as client:
            result = await client.myself.get_preference(key="user.locale")
            assert result == "en_US"


class TestIntReturn:
    """Endpoints that return -> int."""

    @respx.mock(base_url=BASE_URL)
    def test_create_plan_sync(self, respx_mock: respx.MockRouter) -> None:
        respx_mock.post("/rest/api/3/plans/plan").mock(return_value=httpx.Response(201, json=42))
        from jirapi.models import CreatePlanRequest

        body = CreatePlanRequest.model_construct(name="Test Plan")
        client = Jira(url=BASE_URL, email="a@b.com", api_token="tok")
        result = client.plans.create_plan(body=body)
        assert result == 42
        assert isinstance(result, int)
        client.close()

    @pytest.mark.asyncio()
    @respx.mock(base_url=BASE_URL)
    async def test_create_plan_async(self, respx_mock: respx.MockRouter) -> None:
        respx_mock.post("/rest/api/3/plans/plan").mock(return_value=httpx.Response(201, json=99))
        from jirapi.models import CreatePlanRequest

        body = CreatePlanRequest.model_construct(name="Test Plan")
        async with AsyncJira(url=BASE_URL, email="a@b.com", api_token="tok") as client:
            result = await client.plans.create_plan(body=body)
            assert result == 99


class TestDictReturn:
    """Endpoints that return -> dict[str, Any]."""

    @respx.mock(base_url=BASE_URL)
    def test_get_project_roles_sync(self, respx_mock: respx.MockRouter) -> None:
        roles_payload = {
            "Administrators": "https://test.atlassian.net/rest/api/3/project/PROJ/role/10002",
            "Developers": "https://test.atlassian.net/rest/api/3/project/PROJ/role/10001",
        }
        respx_mock.get("/rest/api/3/project/PROJ/role").mock(
            return_value=httpx.Response(200, json=roles_payload)
        )
        client = Jira(url=BASE_URL, email="a@b.com", api_token="tok")
        result = client.project_roles.get_project_roles("PROJ")
        assert isinstance(result, dict)
        assert "Administrators" in result
        assert "Developers" in result
        client.close()

    @pytest.mark.asyncio()
    @respx.mock(base_url=BASE_URL)
    async def test_get_project_roles_async(self, respx_mock: respx.MockRouter) -> None:
        roles_payload = {
            "Administrators": "https://test.atlassian.net/rest/api/3/project/PROJ/role/10002",
        }
        respx_mock.get("/rest/api/3/project/PROJ/role").mock(
            return_value=httpx.Response(200, json=roles_payload)
        )
        async with AsyncJira(url=BASE_URL, email="a@b.com", api_token="tok") as client:
            result = await client.project_roles.get_project_roles("PROJ")
            assert isinstance(result, dict)
            assert "Administrators" in result
