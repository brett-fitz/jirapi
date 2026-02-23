"""Resource classes for the Myself API group."""

from __future__ import annotations

from jirapi._resource import AsyncAPIResource, SyncAPIResource
from jirapi.models import Locale, User


class Myself(SyncAPIResource):
    """Synchronous resource for the Myself API group."""

    def remove_preference(self, *, key: str) -> None:
        """Delete preference"""
        params = self._client._build_params(**{"key": key})
        self._client._request("DELETE", "/rest/api/3/mypreferences", params=params)
        return None

    def get_preference(self, *, key: str) -> str:
        """Get preference"""
        params = self._client._build_params(**{"key": key})
        resp = self._client._request("GET", "/rest/api/3/mypreferences", params=params)
        return resp.json()

    def set_preference(self, *, key: str) -> None:
        """Set preference"""
        params = self._client._build_params(**{"key": key})
        self._client._request("PUT", "/rest/api/3/mypreferences", params=params)
        return None

    def get_locale(self) -> Locale:
        """Get locale"""
        resp = self._client._request("GET", "/rest/api/3/mypreferences/locale")
        return Locale.model_validate(resp.json())

    def get_current_user(self, *, expand: str | None = None) -> User:
        """Get current user"""
        params = self._client._build_params(**{"expand": expand})
        resp = self._client._request("GET", "/rest/api/3/myself", params=params)
        return User.model_validate(resp.json())


class AsyncMyself(AsyncAPIResource):
    """Asynchronous resource for the Myself API group."""

    async def remove_preference(self, *, key: str) -> None:
        """Delete preference"""
        params = self._client._build_params(**{"key": key})
        await self._client._request("DELETE", "/rest/api/3/mypreferences", params=params)
        return None

    async def get_preference(self, *, key: str) -> str:
        """Get preference"""
        params = self._client._build_params(**{"key": key})
        resp = await self._client._request("GET", "/rest/api/3/mypreferences", params=params)
        return resp.json()

    async def set_preference(self, *, key: str) -> None:
        """Set preference"""
        params = self._client._build_params(**{"key": key})
        await self._client._request("PUT", "/rest/api/3/mypreferences", params=params)
        return None

    async def get_locale(self) -> Locale:
        """Get locale"""
        resp = await self._client._request("GET", "/rest/api/3/mypreferences/locale")
        return Locale.model_validate(resp.json())

    async def get_current_user(self, *, expand: str | None = None) -> User:
        """Get current user"""
        params = self._client._build_params(**{"expand": expand})
        resp = await self._client._request("GET", "/rest/api/3/myself", params=params)
        return User.model_validate(resp.json())
