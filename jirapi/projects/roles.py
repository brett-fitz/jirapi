"""Resource classes for projects.roles."""

from __future__ import annotations

from typing import Any

from jirapi._resource import AsyncAPIResource, SyncAPIResource
from jirapi.models import (
    ActorInput,
    ActorsMap,
    CreateUpdateRoleRequest,
    ProjectRole,
    ProjectRoleActorsUpdate,
    ProjectRoleDetails,
)


class ProjectRoles(SyncAPIResource):
    """Synchronous resource for projects.roles."""

    def list(self, project_id_or_key: str) -> dict[str, Any]:
        """Get project roles for project"""
        resp = self._client._request("GET", f"/rest/api/3/project/{project_id_or_key}/role")
        return resp.json()

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
        self._client._request(
            "DELETE", f"/rest/api/3/project/{project_id_or_key}/role/{id_}", params=params
        )
        return None

    def get(
        self, project_id_or_key: str, id_: str, *, exclude_inactive_users: bool | None = None
    ) -> ProjectRole:
        """Get project role for project"""
        params = self._client._build_params(**{"excludeInactiveUsers": exclude_inactive_users})
        resp = self._client._request(
            "GET", f"/rest/api/3/project/{project_id_or_key}/role/{id_}", params=params
        )
        return ProjectRole.model_validate(resp.json())

    def add_actors(self, project_id_or_key: str, id_: str, body: ActorsMap) -> ProjectRole:
        """Add actors to project role"""
        resp = self._client._request(
            "POST",
            f"/rest/api/3/project/{project_id_or_key}/role/{id_}",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return ProjectRole.model_validate(resp.json())

    def set_actors(
        self, project_id_or_key: str, id_: str, body: ProjectRoleActorsUpdate
    ) -> ProjectRole:
        """Set actors for project role"""
        resp = self._client._request(
            "PUT",
            f"/rest/api/3/project/{project_id_or_key}/role/{id_}",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return ProjectRole.model_validate(resp.json())

    def get_details(
        self,
        project_id_or_key: str,
        *,
        current_member: bool | None = None,
        exclude_connect_addons: bool | None = None,
        exclude_other_service_roles: bool | None = None,
    ) -> ProjectRoleDetails:
        """Get project role details"""
        params = self._client._build_params(
            **{
                "currentMember": current_member,
                "excludeConnectAddons": exclude_connect_addons,
                "excludeOtherServiceRoles": exclude_other_service_roles,
            }
        )
        resp = self._client._request(
            "GET", f"/rest/api/3/project/{project_id_or_key}/roledetails", params=params
        )
        return ProjectRoleDetails.model_validate(resp.json())

    def get_all(self) -> ProjectRole:
        """Get all project roles"""
        resp = self._client._request("GET", "/rest/api/3/role")
        return ProjectRole.model_validate(resp.json())

    def create(self, body: CreateUpdateRoleRequest) -> ProjectRole:
        """Create project role"""
        resp = self._client._request(
            "POST", "/rest/api/3/role", json=body.model_dump(by_alias=True, exclude_none=True)
        )
        return ProjectRole.model_validate(resp.json())

    def delete(self, id_: str, *, swap: int | None = None) -> None:
        """Delete project role"""
        params = self._client._build_params(**{"swap": swap})
        self._client._request("DELETE", f"/rest/api/3/role/{id_}", params=params)
        return None

    def get_by_id(self, id_: str) -> ProjectRole:
        """Get project role by ID"""
        resp = self._client._request("GET", f"/rest/api/3/role/{id_}")
        return ProjectRole.model_validate(resp.json())

    def partial_update(self, id_: str, body: CreateUpdateRoleRequest) -> ProjectRole:
        """Partial update project role"""
        resp = self._client._request(
            "POST",
            f"/rest/api/3/role/{id_}",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return ProjectRole.model_validate(resp.json())

    def full_update(self, id_: str, body: CreateUpdateRoleRequest) -> ProjectRole:
        """Fully update project role"""
        resp = self._client._request(
            "PUT", f"/rest/api/3/role/{id_}", json=body.model_dump(by_alias=True, exclude_none=True)
        )
        return ProjectRole.model_validate(resp.json())

    def delete_actors_from_role(
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

    def get_actors_for_role(self, id_: str) -> ProjectRole:
        """Get default actors for project role"""
        resp = self._client._request("GET", f"/rest/api/3/role/{id_}/actors")
        return ProjectRole.model_validate(resp.json())

    def add_actors_to_role(self, id_: str, body: ActorInput) -> ProjectRole:
        """Add default actors to project role"""
        resp = self._client._request(
            "POST",
            f"/rest/api/3/role/{id_}/actors",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return ProjectRole.model_validate(resp.json())


class AsyncProjectRoles(AsyncAPIResource):
    """Asynchronous resource for projects.roles."""

    async def list(self, project_id_or_key: str) -> dict[str, Any]:
        """Get project roles for project"""
        resp = await self._client._request("GET", f"/rest/api/3/project/{project_id_or_key}/role")
        return resp.json()

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
        await self._client._request(
            "DELETE", f"/rest/api/3/project/{project_id_or_key}/role/{id_}", params=params
        )
        return None

    async def get(
        self, project_id_or_key: str, id_: str, *, exclude_inactive_users: bool | None = None
    ) -> ProjectRole:
        """Get project role for project"""
        params = self._client._build_params(**{"excludeInactiveUsers": exclude_inactive_users})
        resp = await self._client._request(
            "GET", f"/rest/api/3/project/{project_id_or_key}/role/{id_}", params=params
        )
        return ProjectRole.model_validate(resp.json())

    async def add_actors(self, project_id_or_key: str, id_: str, body: ActorsMap) -> ProjectRole:
        """Add actors to project role"""
        resp = await self._client._request(
            "POST",
            f"/rest/api/3/project/{project_id_or_key}/role/{id_}",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return ProjectRole.model_validate(resp.json())

    async def set_actors(
        self, project_id_or_key: str, id_: str, body: ProjectRoleActorsUpdate
    ) -> ProjectRole:
        """Set actors for project role"""
        resp = await self._client._request(
            "PUT",
            f"/rest/api/3/project/{project_id_or_key}/role/{id_}",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return ProjectRole.model_validate(resp.json())

    async def get_details(
        self,
        project_id_or_key: str,
        *,
        current_member: bool | None = None,
        exclude_connect_addons: bool | None = None,
        exclude_other_service_roles: bool | None = None,
    ) -> ProjectRoleDetails:
        """Get project role details"""
        params = self._client._build_params(
            **{
                "currentMember": current_member,
                "excludeConnectAddons": exclude_connect_addons,
                "excludeOtherServiceRoles": exclude_other_service_roles,
            }
        )
        resp = await self._client._request(
            "GET", f"/rest/api/3/project/{project_id_or_key}/roledetails", params=params
        )
        return ProjectRoleDetails.model_validate(resp.json())

    async def get_all(self) -> ProjectRole:
        """Get all project roles"""
        resp = await self._client._request("GET", "/rest/api/3/role")
        return ProjectRole.model_validate(resp.json())

    async def create(self, body: CreateUpdateRoleRequest) -> ProjectRole:
        """Create project role"""
        resp = await self._client._request(
            "POST", "/rest/api/3/role", json=body.model_dump(by_alias=True, exclude_none=True)
        )
        return ProjectRole.model_validate(resp.json())

    async def delete(self, id_: str, *, swap: int | None = None) -> None:
        """Delete project role"""
        params = self._client._build_params(**{"swap": swap})
        await self._client._request("DELETE", f"/rest/api/3/role/{id_}", params=params)
        return None

    async def get_by_id(self, id_: str) -> ProjectRole:
        """Get project role by ID"""
        resp = await self._client._request("GET", f"/rest/api/3/role/{id_}")
        return ProjectRole.model_validate(resp.json())

    async def partial_update(self, id_: str, body: CreateUpdateRoleRequest) -> ProjectRole:
        """Partial update project role"""
        resp = await self._client._request(
            "POST",
            f"/rest/api/3/role/{id_}",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return ProjectRole.model_validate(resp.json())

    async def full_update(self, id_: str, body: CreateUpdateRoleRequest) -> ProjectRole:
        """Fully update project role"""
        resp = await self._client._request(
            "PUT", f"/rest/api/3/role/{id_}", json=body.model_dump(by_alias=True, exclude_none=True)
        )
        return ProjectRole.model_validate(resp.json())

    async def delete_actors_from_role(
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

    async def get_actors_for_role(self, id_: str) -> ProjectRole:
        """Get default actors for project role"""
        resp = await self._client._request("GET", f"/rest/api/3/role/{id_}/actors")
        return ProjectRole.model_validate(resp.json())

    async def add_actors_to_role(self, id_: str, body: ActorInput) -> ProjectRole:
        """Add default actors to project role"""
        resp = await self._client._request(
            "POST",
            f"/rest/api/3/role/{id_}/actors",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return ProjectRole.model_validate(resp.json())
