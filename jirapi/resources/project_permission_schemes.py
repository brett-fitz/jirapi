"""Resource classes for the Project permission schemes API group."""

from __future__ import annotations

from jirapi._resource import AsyncAPIResource, SyncAPIResource
from jirapi.models import IdBean, PermissionScheme, ProjectIssueSecurityLevels, SecurityScheme


class ProjectPermissionSchemes(SyncAPIResource):
    """Synchronous resource for the Project permission schemes API group."""

    def get_project_issue_security_scheme(self, project_key_or_id: str) -> SecurityScheme:
        """Get project issue security scheme"""
        resp = self._client._request(
            "GET", f"/rest/api/3/project/{project_key_or_id}/issuesecuritylevelscheme"
        )
        return SecurityScheme.model_validate(resp.json())

    def get_assigned_permission_scheme(
        self, project_key_or_id: str, *, expand: str | None = None
    ) -> PermissionScheme:
        """Get assigned permission scheme"""
        params = self._client._build_params(**{"expand": expand})
        resp = self._client._request(
            "GET", f"/rest/api/3/project/{project_key_or_id}/permissionscheme", params=params
        )
        return PermissionScheme.model_validate(resp.json())

    def assign_permission_scheme(
        self, project_key_or_id: str, body: IdBean, *, expand: str | None = None
    ) -> PermissionScheme:
        """Assign permission scheme"""
        params = self._client._build_params(**{"expand": expand})
        resp = self._client._request(
            "PUT",
            f"/rest/api/3/project/{project_key_or_id}/permissionscheme",
            params=params,
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return PermissionScheme.model_validate(resp.json())

    def get_security_levels_for_project(self, project_key_or_id: str) -> ProjectIssueSecurityLevels:
        """Get project issue security levels"""
        resp = self._client._request(
            "GET", f"/rest/api/3/project/{project_key_or_id}/securitylevel"
        )
        return ProjectIssueSecurityLevels.model_validate(resp.json())


class AsyncProjectPermissionSchemes(AsyncAPIResource):
    """Asynchronous resource for the Project permission schemes API group."""

    async def get_project_issue_security_scheme(self, project_key_or_id: str) -> SecurityScheme:
        """Get project issue security scheme"""
        resp = await self._client._request(
            "GET", f"/rest/api/3/project/{project_key_or_id}/issuesecuritylevelscheme"
        )
        return SecurityScheme.model_validate(resp.json())

    async def get_assigned_permission_scheme(
        self, project_key_or_id: str, *, expand: str | None = None
    ) -> PermissionScheme:
        """Get assigned permission scheme"""
        params = self._client._build_params(**{"expand": expand})
        resp = await self._client._request(
            "GET", f"/rest/api/3/project/{project_key_or_id}/permissionscheme", params=params
        )
        return PermissionScheme.model_validate(resp.json())

    async def assign_permission_scheme(
        self, project_key_or_id: str, body: IdBean, *, expand: str | None = None
    ) -> PermissionScheme:
        """Assign permission scheme"""
        params = self._client._build_params(**{"expand": expand})
        resp = await self._client._request(
            "PUT",
            f"/rest/api/3/project/{project_key_or_id}/permissionscheme",
            params=params,
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return PermissionScheme.model_validate(resp.json())

    async def get_security_levels_for_project(
        self, project_key_or_id: str
    ) -> ProjectIssueSecurityLevels:
        """Get project issue security levels"""
        resp = await self._client._request(
            "GET", f"/rest/api/3/project/{project_key_or_id}/securitylevel"
        )
        return ProjectIssueSecurityLevels.model_validate(resp.json())
