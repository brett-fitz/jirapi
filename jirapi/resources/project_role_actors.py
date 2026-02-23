"""Resource classes for the Project role actors API group."""

from __future__ import annotations

from jirapi._resource import AsyncAPIResource, SyncAPIResource
from jirapi.models import ActorInputBean, ActorsMap, ProjectRole, ProjectRoleActorsUpdateBean


class ProjectRoleActors(SyncAPIResource):
    """Synchronous resource for the Project role actors API group."""

    def delete_actor(
        self,
        project_id_or_key: str,
        id_: str,
        *,
        user: str | None = None,
        group: str | None = None,
        group_id: str | None = None,
    ) -> None:
        """Delete actors from project role"""
        params = self._client._build_params(**{"user": user, "group": group, "groupId": group_id})
        resp = self._client._request(
            "DELETE", f"/rest/api/3/project/{project_id_or_key}/role/{id_}", params=params
        )
        return None

    def add_actor_users(self, project_id_or_key: str, id_: str, body: ActorsMap) -> ProjectRole:
        """Add actors to project role"""
        resp = self._client._request(
            "POST",
            f"/rest/api/3/project/{project_id_or_key}/role/{id_}",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return ProjectRole.model_validate(resp.json())

    def set_actors(
        self, project_id_or_key: str, id_: str, body: ProjectRoleActorsUpdateBean
    ) -> ProjectRole:
        """Set actors for project role"""
        resp = self._client._request(
            "PUT",
            f"/rest/api/3/project/{project_id_or_key}/role/{id_}",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return ProjectRole.model_validate(resp.json())

    def delete_project_role_actors_from_role(
        self,
        id_: str,
        *,
        user: str | None = None,
        group_id: str | None = None,
        group: str | None = None,
    ) -> ProjectRole:
        """Delete default actors from project role"""
        params = self._client._build_params(**{"user": user, "groupId": group_id, "group": group})
        resp = self._client._request("DELETE", f"/rest/api/3/role/{id_}/actors", params=params)
        return ProjectRole.model_validate(resp.json())

    def get_project_role_actors_for_role(self, id_: str) -> ProjectRole:
        """Get default actors for project role"""
        resp = self._client._request("GET", f"/rest/api/3/role/{id_}/actors")
        return ProjectRole.model_validate(resp.json())

    def add_project_role_actors_to_role(self, id_: str, body: ActorInputBean) -> ProjectRole:
        """Add default actors to project role"""
        resp = self._client._request(
            "POST",
            f"/rest/api/3/role/{id_}/actors",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return ProjectRole.model_validate(resp.json())


class AsyncProjectRoleActors(AsyncAPIResource):
    """Asynchronous resource for the Project role actors API group."""

    async def delete_actor(
        self,
        project_id_or_key: str,
        id_: str,
        *,
        user: str | None = None,
        group: str | None = None,
        group_id: str | None = None,
    ) -> None:
        """Delete actors from project role"""
        params = self._client._build_params(**{"user": user, "group": group, "groupId": group_id})
        resp = await self._client._request(
            "DELETE", f"/rest/api/3/project/{project_id_or_key}/role/{id_}", params=params
        )
        return None

    async def add_actor_users(
        self, project_id_or_key: str, id_: str, body: ActorsMap
    ) -> ProjectRole:
        """Add actors to project role"""
        resp = await self._client._request(
            "POST",
            f"/rest/api/3/project/{project_id_or_key}/role/{id_}",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return ProjectRole.model_validate(resp.json())

    async def set_actors(
        self, project_id_or_key: str, id_: str, body: ProjectRoleActorsUpdateBean
    ) -> ProjectRole:
        """Set actors for project role"""
        resp = await self._client._request(
            "PUT",
            f"/rest/api/3/project/{project_id_or_key}/role/{id_}",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return ProjectRole.model_validate(resp.json())

    async def delete_project_role_actors_from_role(
        self,
        id_: str,
        *,
        user: str | None = None,
        group_id: str | None = None,
        group: str | None = None,
    ) -> ProjectRole:
        """Delete default actors from project role"""
        params = self._client._build_params(**{"user": user, "groupId": group_id, "group": group})
        resp = await self._client._request(
            "DELETE", f"/rest/api/3/role/{id_}/actors", params=params
        )
        return ProjectRole.model_validate(resp.json())

    async def get_project_role_actors_for_role(self, id_: str) -> ProjectRole:
        """Get default actors for project role"""
        resp = await self._client._request("GET", f"/rest/api/3/role/{id_}/actors")
        return ProjectRole.model_validate(resp.json())

    async def add_project_role_actors_to_role(self, id_: str, body: ActorInputBean) -> ProjectRole:
        """Add default actors to project role"""
        resp = await self._client._request(
            "POST",
            f"/rest/api/3/role/{id_}/actors",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return ProjectRole.model_validate(resp.json())
