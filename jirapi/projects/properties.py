"""Resource classes for projects.properties."""

from __future__ import annotations

from jirapi._resource import AsyncAPIResource, SyncAPIResource
from jirapi.models import EntityProperty, PropertyKeys


class ProjectProperties(SyncAPIResource):
    """Synchronous resource for projects.properties."""

    def get_keys(self, project_id_or_key: str) -> PropertyKeys:
        """Get project property keys"""
        resp = self._client._request("GET", f"/rest/api/3/project/{project_id_or_key}/properties")
        return PropertyKeys.model_validate(resp.json())

    def delete(self, project_id_or_key: str, property_key: str) -> None:
        """Delete project property"""
        self._client._request(
            "DELETE", f"/rest/api/3/project/{project_id_or_key}/properties/{property_key}"
        )
        return None

    def get(self, project_id_or_key: str, property_key: str) -> EntityProperty:
        """Get project property"""
        resp = self._client._request(
            "GET", f"/rest/api/3/project/{project_id_or_key}/properties/{property_key}"
        )
        return EntityProperty.model_validate(resp.json())

    def set(self, project_id_or_key: str, property_key: str) -> None:
        """Set project property"""
        self._client._request(
            "PUT", f"/rest/api/3/project/{project_id_or_key}/properties/{property_key}"
        )
        return None


class AsyncProjectProperties(AsyncAPIResource):
    """Asynchronous resource for projects.properties."""

    async def get_keys(self, project_id_or_key: str) -> PropertyKeys:
        """Get project property keys"""
        resp = await self._client._request(
            "GET", f"/rest/api/3/project/{project_id_or_key}/properties"
        )
        return PropertyKeys.model_validate(resp.json())

    async def delete(self, project_id_or_key: str, property_key: str) -> None:
        """Delete project property"""
        await self._client._request(
            "DELETE", f"/rest/api/3/project/{project_id_or_key}/properties/{property_key}"
        )
        return None

    async def get(self, project_id_or_key: str, property_key: str) -> EntityProperty:
        """Get project property"""
        resp = await self._client._request(
            "GET", f"/rest/api/3/project/{project_id_or_key}/properties/{property_key}"
        )
        return EntityProperty.model_validate(resp.json())

    async def set(self, project_id_or_key: str, property_key: str) -> None:
        """Set project property"""
        await self._client._request(
            "PUT", f"/rest/api/3/project/{project_id_or_key}/properties/{property_key}"
        )
        return None
