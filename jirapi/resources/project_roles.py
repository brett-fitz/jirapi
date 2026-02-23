"""Resource classes for the Project roles API group."""

from __future__ import annotations

from typing import Any

from jirapi._resource import AsyncAPIResource, SyncAPIResource
from jirapi.models import CreateUpdateRoleRequestBean, ProjectRole, ProjectRoleDetails


class ProjectRoles(SyncAPIResource):
    """Synchronous resource for the Project roles API group."""

    def get_project_roles(self, project_id_or_key: str) -> dict[str, Any]:
        """Get project roles for project"""
        resp = self._client._request("GET", f"/rest/api/3/project/{project_id_or_key}/role")
        return resp.json()

    def get_project_role(
        self, project_id_or_key: str, id_: str, *, exclude_inactive_users: bool | None = None
    ) -> ProjectRole:
        """Get project role for project"""
        params = self._client._build_params(**{"excludeInactiveUsers": exclude_inactive_users})
        resp = self._client._request(
            "GET", f"/rest/api/3/project/{project_id_or_key}/role/{id_}", params=params
        )
        return ProjectRole.model_validate(resp.json())

    def get_project_role_details(
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

    def get_all_project_roles(self) -> ProjectRole:
        """Get all project roles"""
        resp = self._client._request("GET", "/rest/api/3/role")
        return ProjectRole.model_validate(resp.json())

    def create_project_role(self, body: CreateUpdateRoleRequestBean) -> ProjectRole:
        """Create project role"""
        resp = self._client._request(
            "POST", "/rest/api/3/role", json=body.model_dump(by_alias=True, exclude_none=True)
        )
        return ProjectRole.model_validate(resp.json())

    def delete_project_role(self, id_: str, *, swap: int | None = None) -> None:
        """Delete project role"""
        params = self._client._build_params(**{"swap": swap})
        self._client._request("DELETE", f"/rest/api/3/role/{id_}", params=params)
        return None

    def get_project_role_by_id(self, id_: str) -> ProjectRole:
        """Get project role by ID"""
        resp = self._client._request("GET", f"/rest/api/3/role/{id_}")
        return ProjectRole.model_validate(resp.json())

    def partial_update_project_role(
        self, id_: str, body: CreateUpdateRoleRequestBean
    ) -> ProjectRole:
        """Partial update project role"""
        resp = self._client._request(
            "POST",
            f"/rest/api/3/role/{id_}",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return ProjectRole.model_validate(resp.json())

    def fully_update_project_role(self, id_: str, body: CreateUpdateRoleRequestBean) -> ProjectRole:
        """Fully update project role"""
        resp = self._client._request(
            "PUT", f"/rest/api/3/role/{id_}", json=body.model_dump(by_alias=True, exclude_none=True)
        )
        return ProjectRole.model_validate(resp.json())


class AsyncProjectRoles(AsyncAPIResource):
    """Asynchronous resource for the Project roles API group."""

    async def get_project_roles(self, project_id_or_key: str) -> dict[str, Any]:
        """Get project roles for project"""
        resp = await self._client._request("GET", f"/rest/api/3/project/{project_id_or_key}/role")
        return resp.json()

    async def get_project_role(
        self, project_id_or_key: str, id_: str, *, exclude_inactive_users: bool | None = None
    ) -> ProjectRole:
        """Get project role for project"""
        params = self._client._build_params(**{"excludeInactiveUsers": exclude_inactive_users})
        resp = await self._client._request(
            "GET", f"/rest/api/3/project/{project_id_or_key}/role/{id_}", params=params
        )
        return ProjectRole.model_validate(resp.json())

    async def get_project_role_details(
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

    async def get_all_project_roles(self) -> ProjectRole:
        """Get all project roles"""
        resp = await self._client._request("GET", "/rest/api/3/role")
        return ProjectRole.model_validate(resp.json())

    async def create_project_role(self, body: CreateUpdateRoleRequestBean) -> ProjectRole:
        """Create project role"""
        resp = await self._client._request(
            "POST", "/rest/api/3/role", json=body.model_dump(by_alias=True, exclude_none=True)
        )
        return ProjectRole.model_validate(resp.json())

    async def delete_project_role(self, id_: str, *, swap: int | None = None) -> None:
        """Delete project role"""
        params = self._client._build_params(**{"swap": swap})
        await self._client._request("DELETE", f"/rest/api/3/role/{id_}", params=params)
        return None

    async def get_project_role_by_id(self, id_: str) -> ProjectRole:
        """Get project role by ID"""
        resp = await self._client._request("GET", f"/rest/api/3/role/{id_}")
        return ProjectRole.model_validate(resp.json())

    async def partial_update_project_role(
        self, id_: str, body: CreateUpdateRoleRequestBean
    ) -> ProjectRole:
        """Partial update project role"""
        resp = await self._client._request(
            "POST",
            f"/rest/api/3/role/{id_}",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return ProjectRole.model_validate(resp.json())

    async def fully_update_project_role(
        self, id_: str, body: CreateUpdateRoleRequestBean
    ) -> ProjectRole:
        """Fully update project role"""
        resp = await self._client._request(
            "PUT", f"/rest/api/3/role/{id_}", json=body.model_dump(by_alias=True, exclude_none=True)
        )
        return ProjectRole.model_validate(resp.json())
