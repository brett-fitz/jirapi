"""Resource classes for projects.permission_schemes."""

from __future__ import annotations

from jirapi._resource import AsyncAPIResource, SyncAPIResource
from jirapi.models import Id, PermissionScheme, ProjectIssueSecurityLevels, SecurityScheme


class ProjectPermissionSchemes(SyncAPIResource):
    """Synchronous resource for projects.permission_schemes."""

    def get_issue_security_scheme(self, project_key_or_id: str) -> SecurityScheme:
        """Get project issue security scheme"""
        resp = self._client._request(
            "GET", f"/rest/api/3/project/{project_key_or_id}/issuesecuritylevelscheme"
        )
        return SecurityScheme.model_validate(resp.json())

    def get_assigned(
        self, project_key_or_id: str, *, expand: str | None = None
    ) -> PermissionScheme:
        """Get assigned permission scheme"""
        params = self._client._build_params(**{"expand": expand})
        resp = self._client._request(
            "GET", f"/rest/api/3/project/{project_key_or_id}/permissionscheme", params=params
        )
        return PermissionScheme.model_validate(resp.json())

    def assign(
        self, project_key_or_id: str, body: Id, *, expand: str | None = None
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

    def get_security_levels(self, project_key_or_id: str) -> ProjectIssueSecurityLevels:
        """Get project issue security levels"""
        resp = self._client._request(
            "GET", f"/rest/api/3/project/{project_key_or_id}/securitylevel"
        )
        return ProjectIssueSecurityLevels.model_validate(resp.json())


class AsyncProjectPermissionSchemes(AsyncAPIResource):
    """Asynchronous resource for projects.permission_schemes."""

    async def get_issue_security_scheme(self, project_key_or_id: str) -> SecurityScheme:
        """Get project issue security scheme"""
        resp = await self._client._request(
            "GET", f"/rest/api/3/project/{project_key_or_id}/issuesecuritylevelscheme"
        )
        return SecurityScheme.model_validate(resp.json())

    async def get_assigned(
        self, project_key_or_id: str, *, expand: str | None = None
    ) -> PermissionScheme:
        """Get assigned permission scheme"""
        params = self._client._build_params(**{"expand": expand})
        resp = await self._client._request(
            "GET", f"/rest/api/3/project/{project_key_or_id}/permissionscheme", params=params
        )
        return PermissionScheme.model_validate(resp.json())

    async def assign(
        self, project_key_or_id: str, body: Id, *, expand: str | None = None
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

    async def get_security_levels(self, project_key_or_id: str) -> ProjectIssueSecurityLevels:
        """Get project issue security levels"""
        resp = await self._client._request(
            "GET", f"/rest/api/3/project/{project_key_or_id}/securitylevel"
        )
        return ProjectIssueSecurityLevels.model_validate(resp.json())
