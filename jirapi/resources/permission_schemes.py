"""Resource classes for the Permission schemes API group."""

from __future__ import annotations

from jirapi._resource import AsyncAPIResource, SyncAPIResource
from jirapi.models import PermissionGrant, PermissionGrants, PermissionScheme
from jirapi.models import PermissionSchemes as PermissionSchemesModel


class PermissionSchemes(SyncAPIResource):
    """Synchronous resource for the Permission schemes API group."""

    def get_all_permission_schemes(self, *, expand: str | None = None) -> PermissionSchemesModel:
        """Get all permission schemes"""
        params = self._client._build_params(**{"expand": expand})
        resp = self._client._request("GET", "/rest/api/3/permissionscheme", params=params)
        return PermissionSchemesModel.model_validate(resp.json())

    def create_permission_scheme(
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

    def delete_permission_scheme(self, scheme_id: str) -> None:
        """Delete permission scheme"""
        resp = self._client._request("DELETE", f"/rest/api/3/permissionscheme/{scheme_id}")
        return None

    def get_permission_scheme(
        self, scheme_id: str, *, expand: str | None = None
    ) -> PermissionScheme:
        """Get permission scheme"""
        params = self._client._build_params(**{"expand": expand})
        resp = self._client._request(
            "GET", f"/rest/api/3/permissionscheme/{scheme_id}", params=params
        )
        return PermissionScheme.model_validate(resp.json())

    def update_permission_scheme(
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

    def get_permission_scheme_grants(
        self, scheme_id: str, *, expand: str | None = None
    ) -> PermissionGrants:
        """Get permission scheme grants"""
        params = self._client._build_params(**{"expand": expand})
        resp = self._client._request(
            "GET", f"/rest/api/3/permissionscheme/{scheme_id}/permission", params=params
        )
        return PermissionGrants.model_validate(resp.json())

    def create_permission_grant(
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

    def delete_permission_scheme_entity(self, scheme_id: str, permission_id: str) -> None:
        """Delete permission scheme grant"""
        resp = self._client._request(
            "DELETE", f"/rest/api/3/permissionscheme/{scheme_id}/permission/{permission_id}"
        )
        return None

    def get_permission_scheme_grant(
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


class AsyncPermissionSchemes(AsyncAPIResource):
    """Asynchronous resource for the Permission schemes API group."""

    async def get_all_permission_schemes(
        self, *, expand: str | None = None
    ) -> PermissionSchemesModel:
        """Get all permission schemes"""
        params = self._client._build_params(**{"expand": expand})
        resp = await self._client._request("GET", "/rest/api/3/permissionscheme", params=params)
        return PermissionSchemesModel.model_validate(resp.json())

    async def create_permission_scheme(
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

    async def delete_permission_scheme(self, scheme_id: str) -> None:
        """Delete permission scheme"""
        resp = await self._client._request("DELETE", f"/rest/api/3/permissionscheme/{scheme_id}")
        return None

    async def get_permission_scheme(
        self, scheme_id: str, *, expand: str | None = None
    ) -> PermissionScheme:
        """Get permission scheme"""
        params = self._client._build_params(**{"expand": expand})
        resp = await self._client._request(
            "GET", f"/rest/api/3/permissionscheme/{scheme_id}", params=params
        )
        return PermissionScheme.model_validate(resp.json())

    async def update_permission_scheme(
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

    async def get_permission_scheme_grants(
        self, scheme_id: str, *, expand: str | None = None
    ) -> PermissionGrants:
        """Get permission scheme grants"""
        params = self._client._build_params(**{"expand": expand})
        resp = await self._client._request(
            "GET", f"/rest/api/3/permissionscheme/{scheme_id}/permission", params=params
        )
        return PermissionGrants.model_validate(resp.json())

    async def create_permission_grant(
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

    async def delete_permission_scheme_entity(self, scheme_id: str, permission_id: str) -> None:
        """Delete permission scheme grant"""
        resp = await self._client._request(
            "DELETE", f"/rest/api/3/permissionscheme/{scheme_id}/permission/{permission_id}"
        )
        return None

    async def get_permission_scheme_grant(
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
