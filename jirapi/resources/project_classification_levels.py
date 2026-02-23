"""Resource classes for the Project classification levels API group."""

from __future__ import annotations

from jirapi._resource import AsyncAPIResource, SyncAPIResource
from jirapi.models import UpdateDefaultProjectClassificationBean


class ProjectClassificationLevels(SyncAPIResource):
    """Synchronous resource for the Project classification levels API group."""

    def remove_default_project_classification(self, project_id_or_key: str) -> None:
        """Remove the default data classification level from a project"""
        self._client._request(
            "DELETE", f"/rest/api/3/project/{project_id_or_key}/classification-level/default"
        )
        return None

    def get_default_project_classification(self, project_id_or_key: str) -> None:
        """Get the default data classification level of a project"""
        self._client._request(
            "GET", f"/rest/api/3/project/{project_id_or_key}/classification-level/default"
        )
        return None

    def update_default_project_classification(
        self, project_id_or_key: str, body: UpdateDefaultProjectClassificationBean
    ) -> None:
        """Update the default data classification level of a project"""
        self._client._request(
            "PUT",
            f"/rest/api/3/project/{project_id_or_key}/classification-level/default",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None


class AsyncProjectClassificationLevels(AsyncAPIResource):
    """Asynchronous resource for the Project classification levels API group."""

    async def remove_default_project_classification(self, project_id_or_key: str) -> None:
        """Remove the default data classification level from a project"""
        await self._client._request(
            "DELETE", f"/rest/api/3/project/{project_id_or_key}/classification-level/default"
        )
        return None

    async def get_default_project_classification(self, project_id_or_key: str) -> None:
        """Get the default data classification level of a project"""
        await self._client._request(
            "GET", f"/rest/api/3/project/{project_id_or_key}/classification-level/default"
        )
        return None

    async def update_default_project_classification(
        self, project_id_or_key: str, body: UpdateDefaultProjectClassificationBean
    ) -> None:
        """Update the default data classification level of a project"""
        await self._client._request(
            "PUT",
            f"/rest/api/3/project/{project_id_or_key}/classification-level/default",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None
