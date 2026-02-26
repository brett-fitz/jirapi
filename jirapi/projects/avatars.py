"""Resource classes for projects.avatars."""

from __future__ import annotations

from jirapi._resource import AsyncAPIResource, SyncAPIResource
from jirapi.models import Avatar
from jirapi.models import ProjectAvatars as ProjectAvatarsModel


class ProjectAvatars(SyncAPIResource):
    """Synchronous resource for projects.avatars."""

    def update(self, project_id_or_key: str, body: Avatar) -> None:
        """Set project avatar"""
        self._client._request(
            "PUT",
            f"/rest/api/3/project/{project_id_or_key}/avatar",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    def delete(self, project_id_or_key: str, id_: str) -> None:
        """Delete project avatar"""
        self._client._request("DELETE", f"/rest/api/3/project/{project_id_or_key}/avatar/{id_}")
        return None

    def create(
        self,
        project_id_or_key: str,
        *,
        x: int | None = None,
        y: int | None = None,
        size: int | None = None,
    ) -> Avatar:
        """Load project avatar"""
        params = self._client._build_params(**{"x": x, "y": y, "size": size})
        resp = self._client._request(
            "POST", f"/rest/api/3/project/{project_id_or_key}/avatar2", params=params
        )
        return Avatar.model_validate(resp.json())

    def list(self, project_id_or_key: str) -> ProjectAvatarsModel:
        """Get all project avatars"""
        resp = self._client._request("GET", f"/rest/api/3/project/{project_id_or_key}/avatars")
        return ProjectAvatarsModel.model_validate(resp.json())


class AsyncProjectAvatars(AsyncAPIResource):
    """Asynchronous resource for projects.avatars."""

    async def update(self, project_id_or_key: str, body: Avatar) -> None:
        """Set project avatar"""
        await self._client._request(
            "PUT",
            f"/rest/api/3/project/{project_id_or_key}/avatar",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    async def delete(self, project_id_or_key: str, id_: str) -> None:
        """Delete project avatar"""
        await self._client._request(
            "DELETE", f"/rest/api/3/project/{project_id_or_key}/avatar/{id_}"
        )
        return None

    async def create(
        self,
        project_id_or_key: str,
        *,
        x: int | None = None,
        y: int | None = None,
        size: int | None = None,
    ) -> Avatar:
        """Load project avatar"""
        params = self._client._build_params(**{"x": x, "y": y, "size": size})
        resp = await self._client._request(
            "POST", f"/rest/api/3/project/{project_id_or_key}/avatar2", params=params
        )
        return Avatar.model_validate(resp.json())

    async def list(self, project_id_or_key: str) -> ProjectAvatarsModel:
        """Get all project avatars"""
        resp = await self._client._request(
            "GET", f"/rest/api/3/project/{project_id_or_key}/avatars"
        )
        return ProjectAvatarsModel.model_validate(resp.json())
