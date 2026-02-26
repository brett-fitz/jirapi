"""Resource classes for projects.types."""

from __future__ import annotations

from jirapi._resource import AsyncAPIResource, SyncAPIResource
from jirapi.models import ProjectType


class ProjectTypes(SyncAPIResource):
    """Synchronous resource for projects.types."""

    def list(self) -> ProjectType:
        """Get all project types"""
        resp = self._client._request("GET", "/rest/api/3/project/type")
        return ProjectType.model_validate(resp.json())

    def list_accessible(self) -> ProjectType:
        """Get licensed project types"""
        resp = self._client._request("GET", "/rest/api/3/project/type/accessible")
        return ProjectType.model_validate(resp.json())

    def get_by_key(self, project_type_key: str) -> ProjectType:
        """Get project type by key"""
        resp = self._client._request("GET", f"/rest/api/3/project/type/{project_type_key}")
        return ProjectType.model_validate(resp.json())

    def get_accessible_by_key(self, project_type_key: str) -> ProjectType:
        """Get accessible project type by key"""
        resp = self._client._request(
            "GET", f"/rest/api/3/project/type/{project_type_key}/accessible"
        )
        return ProjectType.model_validate(resp.json())


class AsyncProjectTypes(AsyncAPIResource):
    """Asynchronous resource for projects.types."""

    async def list(self) -> ProjectType:
        """Get all project types"""
        resp = await self._client._request("GET", "/rest/api/3/project/type")
        return ProjectType.model_validate(resp.json())

    async def list_accessible(self) -> ProjectType:
        """Get licensed project types"""
        resp = await self._client._request("GET", "/rest/api/3/project/type/accessible")
        return ProjectType.model_validate(resp.json())

    async def get_by_key(self, project_type_key: str) -> ProjectType:
        """Get project type by key"""
        resp = await self._client._request("GET", f"/rest/api/3/project/type/{project_type_key}")
        return ProjectType.model_validate(resp.json())

    async def get_accessible_by_key(self, project_type_key: str) -> ProjectType:
        """Get accessible project type by key"""
        resp = await self._client._request(
            "GET", f"/rest/api/3/project/type/{project_type_key}/accessible"
        )
        return ProjectType.model_validate(resp.json())
