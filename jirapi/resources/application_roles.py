"""Resource classes for the Application roles API group."""

from __future__ import annotations

from jirapi._resource import AsyncAPIResource, SyncAPIResource
from jirapi.models import ApplicationRole


class ApplicationRoles(SyncAPIResource):
    """Synchronous resource for the Application roles API group."""

    def get_all_application_roles(self) -> ApplicationRole:
        """Get all application roles"""
        resp = self._client._request("GET", "/rest/api/3/applicationrole")
        return ApplicationRole.model_validate(resp.json())

    def get_application_role(self, key: str) -> ApplicationRole:
        """Get application role"""
        resp = self._client._request("GET", f"/rest/api/3/applicationrole/{key}")
        return ApplicationRole.model_validate(resp.json())


class AsyncApplicationRoles(AsyncAPIResource):
    """Asynchronous resource for the Application roles API group."""

    async def get_all_application_roles(self) -> ApplicationRole:
        """Get all application roles"""
        resp = await self._client._request("GET", "/rest/api/3/applicationrole")
        return ApplicationRole.model_validate(resp.json())

    async def get_application_role(self, key: str) -> ApplicationRole:
        """Get application role"""
        resp = await self._client._request("GET", f"/rest/api/3/applicationrole/{key}")
        return ApplicationRole.model_validate(resp.json())
