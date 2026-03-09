"""Tests for jirapi._base_client."""

from __future__ import annotations

import httpx
import pytest
import respx

from jirapi import AsyncJira, Jira
from jirapi._base_client import _BearerAuth
from jirapi.exceptions import (
    AuthenticationError,
    ForbiddenError,
    NotFoundError,
    RateLimitError,
    ServerError,
    ValidationError,
)


BASE_URL = "https://test.atlassian.net"


# ------------------------------------------------------------------ #
# Authentication resolution
# ------------------------------------------------------------------ #


class TestAuthBasic:
    """Basic auth (email + api_token) path."""

    @respx.mock(base_url=BASE_URL)
    def test_basic_auth_sets_authorization_header(
        self,
        respx_mock: respx.MockRouter,
    ) -> None:
        respx_mock.get("/rest/api/3/test").mock(
            return_value=httpx.Response(200, json={"ok": True}),
        )
        client = Jira(url=BASE_URL, email="a@b.com", api_token="tok")
        resp = client._request("GET", "/rest/api/3/test")
        assert resp.status_code == 200
        sent_request = respx_mock.calls.last.request
        assert sent_request.headers["authorization"].startswith("Basic ")
        client.close()

    @respx.mock(base_url=BASE_URL)
    def test_basic_auth_async(self) -> None:
        client = AsyncJira(url=BASE_URL, email="a@b.com", api_token="tok")
        assert isinstance(client._auth, httpx.BasicAuth)


class TestAuthBearer:
    """Bearer / PAT (token) path."""

    def test_token_creates_bearer_auth(self) -> None:
        client = Jira(url=BASE_URL, token="my-pat-123")
        assert isinstance(client._auth, _BearerAuth)
        client.close()

    @respx.mock(base_url=BASE_URL)
    def test_bearer_sends_correct_header(self, respx_mock: respx.MockRouter) -> None:
        respx_mock.get("/rest/api/3/test").mock(
            return_value=httpx.Response(200, json={"ok": True}),
        )
        client = Jira(url=BASE_URL, token="my-pat-123")
        client._request("GET", "/rest/api/3/test")
        sent_request = respx_mock.calls.last.request
        assert sent_request.headers["authorization"] == "Bearer my-pat-123"
        client.close()

    @respx.mock(base_url=BASE_URL)
    def test_bearer_async(self) -> None:
        client = AsyncJira(url=BASE_URL, token="my-pat-123")
        assert isinstance(client._auth, _BearerAuth)


class TestAuthCustom:
    """Custom httpx.Auth pass-through."""

    def test_custom_auth_passed_through(self) -> None:
        custom = httpx.BasicAuth(username="custom", password="secret")
        client = Jira(url=BASE_URL, auth=custom)
        assert client._auth is custom
        client.close()

    def test_custom_auth_async(self) -> None:
        custom = httpx.BasicAuth(username="custom", password="secret")
        client = AsyncJira(url=BASE_URL, auth=custom)
        assert client._auth is custom


class TestAuthValidation:
    """Validation of mutually exclusive auth arguments."""

    def test_no_auth_raises(self) -> None:
        with pytest.raises(ValueError, match="No authentication provided"):
            Jira(url=BASE_URL)

    def test_email_without_api_token_raises(self) -> None:
        with pytest.raises(ValueError, match="both 'email' and 'api_token'"):
            Jira(url=BASE_URL, email="a@b.com")

    def test_api_token_without_email_raises(self) -> None:
        with pytest.raises(ValueError, match="both 'email' and 'api_token'"):
            Jira(url=BASE_URL, api_token="tok")

    def test_basic_plus_token_raises(self) -> None:
        with pytest.raises(ValueError, match="Multiple authentication"):
            Jira(url=BASE_URL, email="a@b.com", api_token="tok", token="pat")

    def test_basic_plus_custom_raises(self) -> None:
        with pytest.raises(ValueError, match="Multiple authentication"):
            Jira(
                url=BASE_URL,
                email="a@b.com",
                api_token="tok",
                auth=httpx.BasicAuth("x", "y"),
            )

    def test_token_plus_custom_raises(self) -> None:
        with pytest.raises(ValueError, match="Multiple authentication"):
            Jira(url=BASE_URL, token="pat", auth=httpx.BasicAuth("x", "y"))

    def test_all_three_raises(self) -> None:
        with pytest.raises(ValueError, match="Multiple authentication"):
            Jira(
                url=BASE_URL,
                email="a@b.com",
                api_token="tok",
                token="pat",
                auth=httpx.BasicAuth("x", "y"),
            )

    def test_async_no_auth_raises(self) -> None:
        with pytest.raises(ValueError, match="No authentication provided"):
            AsyncJira(url=BASE_URL)


class TestBuildParams:
    """_build_params filters None values."""

    def test_filters_none(self) -> None:
        result = Jira._build_params(a=1, b=None, c="hello")
        assert result == {"a": 1, "c": "hello"}

    def test_empty_when_all_none(self) -> None:
        result = Jira._build_params(x=None, y=None)
        assert result == {}

    def test_preserves_falsy(self) -> None:
        result = Jira._build_params(a=0, b="", c=False)
        assert result == {"a": 0, "b": "", "c": False}


class TestSyncClientContextManager:
    """Jira client can be used as a context manager."""

    @respx.mock(base_url=BASE_URL)
    def test_context_manager(self) -> None:
        with Jira(url=BASE_URL, email="a@b.com", api_token="tok") as client:
            assert client is not None


class TestSyncRequestErrorHandling:
    """Sync client raises typed exceptions for error responses."""

    @respx.mock(base_url=BASE_URL)
    def test_401_raises_authentication_error(self, respx_mock: respx.MockRouter) -> None:
        respx_mock.get("/rest/api/3/test").mock(
            return_value=httpx.Response(401, json={"errorMessages": ["Not authenticated"]})
        )
        client = Jira(url=BASE_URL, email="a@b.com", api_token="tok")
        with pytest.raises(AuthenticationError) as exc_info:
            client._request("GET", "/rest/api/3/test")
        assert exc_info.value.status_code == 401
        client.close()

    @respx.mock(base_url=BASE_URL)
    def test_403_raises_forbidden_error(self, respx_mock: respx.MockRouter) -> None:
        respx_mock.get("/rest/api/3/test").mock(
            return_value=httpx.Response(403, json={"errorMessages": ["Forbidden"]})
        )
        client = Jira(url=BASE_URL, email="a@b.com", api_token="tok")
        with pytest.raises(ForbiddenError):
            client._request("GET", "/rest/api/3/test")
        client.close()

    @respx.mock(base_url=BASE_URL)
    def test_404_raises_not_found_error(self, respx_mock: respx.MockRouter) -> None:
        respx_mock.get("/rest/api/3/test").mock(
            return_value=httpx.Response(404, json={"errorMessages": ["Not found"]})
        )
        client = Jira(url=BASE_URL, email="a@b.com", api_token="tok")
        with pytest.raises(NotFoundError):
            client._request("GET", "/rest/api/3/test")
        client.close()

    @respx.mock(base_url=BASE_URL)
    def test_400_raises_validation_error(self, respx_mock: respx.MockRouter) -> None:
        respx_mock.post("/rest/api/3/test").mock(
            return_value=httpx.Response(
                400,
                json={
                    "errorMessages": [],
                    "errors": {"summary": "Field is required"},
                },
            )
        )
        client = Jira(url=BASE_URL, email="a@b.com", api_token="tok")
        with pytest.raises(ValidationError) as exc_info:
            client._request("POST", "/rest/api/3/test")
        assert exc_info.value.errors == {"summary": "Field is required"}
        client.close()

    @respx.mock(base_url=BASE_URL)
    def test_429_raises_rate_limit_with_retry_after(self, respx_mock: respx.MockRouter) -> None:
        respx_mock.get("/rest/api/3/test").mock(
            return_value=httpx.Response(
                429,
                json={"errorMessages": ["Rate limited"]},
                headers={"Retry-After": "60"},
            )
        )
        client = Jira(url=BASE_URL, email="a@b.com", api_token="tok")
        with pytest.raises(RateLimitError) as exc_info:
            client._request("GET", "/rest/api/3/test")
        assert exc_info.value.retry_after == 60.0
        client.close()

    @respx.mock(base_url=BASE_URL)
    def test_500_raises_server_error(self, respx_mock: respx.MockRouter) -> None:
        respx_mock.get("/rest/api/3/test").mock(
            return_value=httpx.Response(500, text="Internal Server Error")
        )
        client = Jira(url=BASE_URL, email="a@b.com", api_token="tok")
        with pytest.raises(ServerError):
            client._request("GET", "/rest/api/3/test")
        client.close()

    @respx.mock(base_url=BASE_URL)
    def test_non_dict_json_error_response(self, respx_mock: respx.MockRouter) -> None:
        respx_mock.get("/rest/api/3/test").mock(
            return_value=httpx.Response(400, json=[{"id": 1}, {"id": 2}])
        )
        client = Jira(url=BASE_URL, email="a@b.com", api_token="tok")
        with pytest.raises(ValidationError) as exc_info:
            client._request("GET", "/rest/api/3/test")
        assert exc_info.value.status_code == 400
        assert exc_info.value.response_body == [{"id": 1}, {"id": 2}]
        client.close()

    @respx.mock(base_url=BASE_URL)
    def test_non_json_error_response(self, respx_mock: respx.MockRouter) -> None:
        respx_mock.get("/rest/api/3/test").mock(
            return_value=httpx.Response(502, text="<html>Bad Gateway</html>")
        )
        client = Jira(url=BASE_URL, email="a@b.com", api_token="tok")
        with pytest.raises(ServerError) as exc_info:
            client._request("GET", "/rest/api/3/test")
        assert exc_info.value.status_code == 502
        assert exc_info.value.response_body == "<html>Bad Gateway</html>"
        client.close()

    @respx.mock(base_url=BASE_URL)
    def test_200_does_not_raise(self, respx_mock: respx.MockRouter) -> None:
        respx_mock.get("/rest/api/3/test").mock(return_value=httpx.Response(200, json={"ok": True}))
        client = Jira(url=BASE_URL, email="a@b.com", api_token="tok")
        resp = client._request("GET", "/rest/api/3/test")
        assert resp.status_code == 200
        client.close()


class TestAsyncClientContextManager:
    """AsyncJira client can be used as an async context manager."""

    @pytest.mark.asyncio()
    @respx.mock(base_url=BASE_URL)
    async def test_async_context_manager(self) -> None:
        async with AsyncJira(url=BASE_URL, email="a@b.com", api_token="tok") as client:
            assert client is not None

    @pytest.mark.asyncio()
    @respx.mock(base_url=BASE_URL)
    async def test_async_401(self, respx_mock: respx.MockRouter) -> None:
        respx_mock.get("/rest/api/3/test").mock(
            return_value=httpx.Response(401, json={"errorMessages": ["Not authenticated"]})
        )
        async with AsyncJira(url=BASE_URL, email="a@b.com", api_token="tok") as client:
            with pytest.raises(AuthenticationError):
                await client._request("GET", "/rest/api/3/test")
