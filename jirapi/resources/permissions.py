"""Resource classes for the Permissions API group."""

from __future__ import annotations

from jirapi._resource import AsyncAPIResource, SyncAPIResource
from jirapi.models import (
    BulkPermissionGrants,
    BulkPermissionsRequestBean,
    PermissionsKeysBean,
    PermittedProjects,
)
from jirapi.models import Permissions as PermissionsModel


class Permissions(SyncAPIResource):
    """Synchronous resource for the Permissions API group."""

    def get_my_permissions(
        self,
        *,
        project_key: str | None = None,
        project_id: str | None = None,
        issue_key: str | None = None,
        issue_id: str | None = None,
        permissions: str | None = None,
        project_uuid: str | None = None,
        project_configuration_uuid: str | None = None,
        comment_id: str | None = None,
    ) -> PermissionsModel:
        """Get my permissions"""
        params = self._client._build_params(
            **{
                "projectKey": project_key,
                "projectId": project_id,
                "issueKey": issue_key,
                "issueId": issue_id,
                "permissions": permissions,
                "projectUuid": project_uuid,
                "projectConfigurationUuid": project_configuration_uuid,
                "commentId": comment_id,
            }
        )
        resp = self._client._request("GET", "/rest/api/3/mypermissions", params=params)
        return PermissionsModel.model_validate(resp.json())

    def get_all_permissions(self) -> PermissionsModel:
        """Get all permissions"""
        resp = self._client._request("GET", "/rest/api/3/permissions")
        return PermissionsModel.model_validate(resp.json())

    def get_bulk_permissions(self, body: BulkPermissionsRequestBean) -> BulkPermissionGrants:
        """Get bulk permissions"""
        resp = self._client._request(
            "POST",
            "/rest/api/3/permissions/check",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return BulkPermissionGrants.model_validate(resp.json())

    def get_permitted_projects(self, body: PermissionsKeysBean) -> PermittedProjects:
        """Get permitted projects"""
        resp = self._client._request(
            "POST",
            "/rest/api/3/permissions/project",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return PermittedProjects.model_validate(resp.json())


class AsyncPermissions(AsyncAPIResource):
    """Asynchronous resource for the Permissions API group."""

    async def get_my_permissions(
        self,
        *,
        project_key: str | None = None,
        project_id: str | None = None,
        issue_key: str | None = None,
        issue_id: str | None = None,
        permissions: str | None = None,
        project_uuid: str | None = None,
        project_configuration_uuid: str | None = None,
        comment_id: str | None = None,
    ) -> PermissionsModel:
        """Get my permissions"""
        params = self._client._build_params(
            **{
                "projectKey": project_key,
                "projectId": project_id,
                "issueKey": issue_key,
                "issueId": issue_id,
                "permissions": permissions,
                "projectUuid": project_uuid,
                "projectConfigurationUuid": project_configuration_uuid,
                "commentId": comment_id,
            }
        )
        resp = await self._client._request("GET", "/rest/api/3/mypermissions", params=params)
        return PermissionsModel.model_validate(resp.json())

    async def get_all_permissions(self) -> PermissionsModel:
        """Get all permissions"""
        resp = await self._client._request("GET", "/rest/api/3/permissions")
        return PermissionsModel.model_validate(resp.json())

    async def get_bulk_permissions(self, body: BulkPermissionsRequestBean) -> BulkPermissionGrants:
        """Get bulk permissions"""
        resp = await self._client._request(
            "POST",
            "/rest/api/3/permissions/check",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return BulkPermissionGrants.model_validate(resp.json())

    async def get_permitted_projects(self, body: PermissionsKeysBean) -> PermittedProjects:
        """Get permitted projects"""
        resp = await self._client._request(
            "POST",
            "/rest/api/3/permissions/project",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return PermittedProjects.model_validate(resp.json())
