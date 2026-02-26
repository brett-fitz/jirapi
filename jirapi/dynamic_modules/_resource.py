"""Resource classes for dynamic_modules."""

from __future__ import annotations

from jirapi._resource import AsyncAPIResource, SyncAPIResource
from jirapi.models import ConnectModules


class DynamicModules(SyncAPIResource):
    """Synchronous resource for dynamic_modules."""

    def remove(self, *, module_key: list[str] | None = None) -> None:
        """Remove modules"""
        params = self._client._build_params(**{"moduleKey": module_key})
        self._client._request(
            "DELETE", "/rest/atlassian-connect/1/app/module/dynamic", params=params
        )
        return None

    def get(self) -> ConnectModules:
        """Get modules"""
        resp = self._client._request("GET", "/rest/atlassian-connect/1/app/module/dynamic")
        return ConnectModules.model_validate(resp.json())

    def register(self, body: ConnectModules) -> None:
        """Register modules"""
        self._client._request(
            "POST",
            "/rest/atlassian-connect/1/app/module/dynamic",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None


class AsyncDynamicModules(AsyncAPIResource):
    """Asynchronous resource for dynamic_modules."""

    async def remove(self, *, module_key: list[str] | None = None) -> None:
        """Remove modules"""
        params = self._client._build_params(**{"moduleKey": module_key})
        await self._client._request(
            "DELETE", "/rest/atlassian-connect/1/app/module/dynamic", params=params
        )
        return None

    async def get(self) -> ConnectModules:
        """Get modules"""
        resp = await self._client._request("GET", "/rest/atlassian-connect/1/app/module/dynamic")
        return ConnectModules.model_validate(resp.json())

    async def register(self, body: ConnectModules) -> None:
        """Register modules"""
        await self._client._request(
            "POST",
            "/rest/atlassian-connect/1/app/module/dynamic",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None
