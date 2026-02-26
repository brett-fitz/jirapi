"""Resource classes for permissions."""

from __future__ import annotations

from jirapi._resource import AsyncAPIResource, SyncAPIResource
from jirapi.models import (
    BulkPermissionGrants,
    BulkPermissionsRequest,
    PermissionGrant,
    PermissionGrants,
    PermissionScheme,
    PermissionSchemes,
    PermissionsKeys,
    PermittedProjects,
)
from jirapi.models import Permissions as PermissionsModel


class Permissions(SyncAPIResource):
    """Synchronous resource for permissions."""

    def get_my(
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

    def list(self) -> PermissionsModel:
        """Get all permissions"""
        resp = self._client._request("GET", "/rest/api/3/permissions")
        return PermissionsModel.model_validate(resp.json())

    def get_bulk(self, body: BulkPermissionsRequest) -> BulkPermissionGrants:
        """Get bulk permissions"""
        resp = self._client._request(
            "POST",
            "/rest/api/3/permissions/check",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return BulkPermissionGrants.model_validate(resp.json())

    def get_permitted_projects(self, body: PermissionsKeys) -> PermittedProjects:
        """Get permitted projects"""
        resp = self._client._request(
            "POST",
            "/rest/api/3/permissions/project",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return PermittedProjects.model_validate(resp.json())

    def list_schemes(self, *, expand: str | None = None) -> PermissionSchemes:
        """Get all permission schemes"""
        params = self._client._build_params(**{"expand": expand})
        resp = self._client._request("GET", "/rest/api/3/permissionscheme", params=params)
        return PermissionSchemes.model_validate(resp.json())

    def create_scheme(
        self, body: PermissionScheme, *, expand: str | None = None
    ) -> PermissionScheme:
        """Create permission scheme"""
        params = self._client._build_params(**{"expand": expand})
        resp = self._client._request(
            "POST",
            "/rest/api/3/permissionscheme",
            params=params,
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return PermissionScheme.model_validate(resp.json())

    def delete_scheme(self, scheme_id: str) -> None:
        """Delete permission scheme"""
        self._client._request("DELETE", f"/rest/api/3/permissionscheme/{scheme_id}")
        return None

    def get_scheme(self, scheme_id: str, *, expand: str | None = None) -> PermissionScheme:
        """Get permission scheme"""
        params = self._client._build_params(**{"expand": expand})
        resp = self._client._request(
            "GET", f"/rest/api/3/permissionscheme/{scheme_id}", params=params
        )
        return PermissionScheme.model_validate(resp.json())

    def update_scheme(
        self, scheme_id: str, body: PermissionScheme, *, expand: str | None = None
    ) -> PermissionScheme:
        """Update permission scheme"""
        params = self._client._build_params(**{"expand": expand})
        resp = self._client._request(
            "PUT",
            f"/rest/api/3/permissionscheme/{scheme_id}",
            params=params,
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return PermissionScheme.model_validate(resp.json())

    def list_grants(self, scheme_id: str, *, expand: str | None = None) -> PermissionGrants:
        """Get permission scheme grants"""
        params = self._client._build_params(**{"expand": expand})
        resp = self._client._request(
            "GET", f"/rest/api/3/permissionscheme/{scheme_id}/permission", params=params
        )
        return PermissionGrants.model_validate(resp.json())

    def create_grant(
        self, scheme_id: str, body: PermissionGrant, *, expand: str | None = None
    ) -> PermissionGrant:
        """Create permission grant"""
        params = self._client._build_params(**{"expand": expand})
        resp = self._client._request(
            "POST",
            f"/rest/api/3/permissionscheme/{scheme_id}/permission",
            params=params,
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return PermissionGrant.model_validate(resp.json())

    def delete_grant(self, scheme_id: str, permission_id: str) -> None:
        """Delete permission scheme grant"""
        self._client._request(
            "DELETE", f"/rest/api/3/permissionscheme/{scheme_id}/permission/{permission_id}"
        )
        return None

    def get_grant(
        self, scheme_id: str, permission_id: str, *, expand: str | None = None
    ) -> PermissionGrant:
        """Get permission scheme grant"""
        params = self._client._build_params(**{"expand": expand})
        resp = self._client._request(
            "GET",
            f"/rest/api/3/permissionscheme/{scheme_id}/permission/{permission_id}",
            params=params,
        )
        return PermissionGrant.model_validate(resp.json())


class AsyncPermissions(AsyncAPIResource):
    """Asynchronous resource for permissions."""

    async def get_my(
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

    async def list(self) -> PermissionsModel:
        """Get all permissions"""
        resp = await self._client._request("GET", "/rest/api/3/permissions")
        return PermissionsModel.model_validate(resp.json())

    async def get_bulk(self, body: BulkPermissionsRequest) -> BulkPermissionGrants:
        """Get bulk permissions"""
        resp = await self._client._request(
            "POST",
            "/rest/api/3/permissions/check",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return BulkPermissionGrants.model_validate(resp.json())

    async def get_permitted_projects(self, body: PermissionsKeys) -> PermittedProjects:
        """Get permitted projects"""
        resp = await self._client._request(
            "POST",
            "/rest/api/3/permissions/project",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return PermittedProjects.model_validate(resp.json())

    async def list_schemes(self, *, expand: str | None = None) -> PermissionSchemes:
        """Get all permission schemes"""
        params = self._client._build_params(**{"expand": expand})
        resp = await self._client._request("GET", "/rest/api/3/permissionscheme", params=params)
        return PermissionSchemes.model_validate(resp.json())

    async def create_scheme(
        self, body: PermissionScheme, *, expand: str | None = None
    ) -> PermissionScheme:
        """Create permission scheme"""
        params = self._client._build_params(**{"expand": expand})
        resp = await self._client._request(
            "POST",
            "/rest/api/3/permissionscheme",
            params=params,
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return PermissionScheme.model_validate(resp.json())

    async def delete_scheme(self, scheme_id: str) -> None:
        """Delete permission scheme"""
        await self._client._request("DELETE", f"/rest/api/3/permissionscheme/{scheme_id}")
        return None

    async def get_scheme(self, scheme_id: str, *, expand: str | None = None) -> PermissionScheme:
        """Get permission scheme"""
        params = self._client._build_params(**{"expand": expand})
        resp = await self._client._request(
            "GET", f"/rest/api/3/permissionscheme/{scheme_id}", params=params
        )
        return PermissionScheme.model_validate(resp.json())

    async def update_scheme(
        self, scheme_id: str, body: PermissionScheme, *, expand: str | None = None
    ) -> PermissionScheme:
        """Update permission scheme"""
        params = self._client._build_params(**{"expand": expand})
        resp = await self._client._request(
            "PUT",
            f"/rest/api/3/permissionscheme/{scheme_id}",
            params=params,
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return PermissionScheme.model_validate(resp.json())

    async def list_grants(self, scheme_id: str, *, expand: str | None = None) -> PermissionGrants:
        """Get permission scheme grants"""
        params = self._client._build_params(**{"expand": expand})
        resp = await self._client._request(
            "GET", f"/rest/api/3/permissionscheme/{scheme_id}/permission", params=params
        )
        return PermissionGrants.model_validate(resp.json())

    async def create_grant(
        self, scheme_id: str, body: PermissionGrant, *, expand: str | None = None
    ) -> PermissionGrant:
        """Create permission grant"""
        params = self._client._build_params(**{"expand": expand})
        resp = await self._client._request(
            "POST",
            f"/rest/api/3/permissionscheme/{scheme_id}/permission",
            params=params,
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return PermissionGrant.model_validate(resp.json())

    async def delete_grant(self, scheme_id: str, permission_id: str) -> None:
        """Delete permission scheme grant"""
        await self._client._request(
            "DELETE", f"/rest/api/3/permissionscheme/{scheme_id}/permission/{permission_id}"
        )
        return None

    async def get_grant(
        self, scheme_id: str, permission_id: str, *, expand: str | None = None
    ) -> PermissionGrant:
        """Get permission scheme grant"""
        params = self._client._build_params(**{"expand": expand})
        resp = await self._client._request(
            "GET",
            f"/rest/api/3/permissionscheme/{scheme_id}/permission/{permission_id}",
            params=params,
        )
        return PermissionGrant.model_validate(resp.json())
