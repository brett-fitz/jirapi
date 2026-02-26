"""Resource classes for application_roles."""

from __future__ import annotations

from jirapi._resource import AsyncAPIResource, SyncAPIResource
from jirapi.models import ApplicationRole


class ApplicationRoles(SyncAPIResource):
    """Synchronous resource for application_roles."""

    def get_all(self) -> ApplicationRole:
        """Get all application roles"""
        resp = self._client._request("GET", "/rest/api/3/applicationrole")
        return ApplicationRole.model_validate(resp.json())

    def get(self, key: str) -> ApplicationRole:
        """Get application role"""
        resp = self._client._request("GET", f"/rest/api/3/applicationrole/{key}")
        return ApplicationRole.model_validate(resp.json())


class AsyncApplicationRoles(AsyncAPIResource):
    """Asynchronous resource for application_roles."""

    async def get_all(self) -> ApplicationRole:
        """Get all application roles"""
        resp = await self._client._request("GET", "/rest/api/3/applicationrole")
        return ApplicationRole.model_validate(resp.json())

    async def get(self, key: str) -> ApplicationRole:
        """Get application role"""
        resp = await self._client._request("GET", f"/rest/api/3/applicationrole/{key}")
        return ApplicationRole.model_validate(resp.json())
