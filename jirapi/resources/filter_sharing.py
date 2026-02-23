"""Resource classes for the Filter sharing API group."""

from __future__ import annotations

from jirapi._resource import AsyncAPIResource, SyncAPIResource
from jirapi.models import DefaultShareScope, SharePermission, SharePermissionInputBean


class FilterSharing(SyncAPIResource):
    """Synchronous resource for the Filter sharing API group."""

    def get_default_share_scope(self) -> DefaultShareScope:
        """Get default share scope"""
        resp = self._client._request("GET", "/rest/api/3/filter/defaultShareScope")
        return DefaultShareScope.model_validate(resp.json())

    def set_default_share_scope(self, body: DefaultShareScope) -> DefaultShareScope:
        """Set default share scope"""
        resp = self._client._request(
            "PUT",
            "/rest/api/3/filter/defaultShareScope",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return DefaultShareScope.model_validate(resp.json())

    def get_share_permissions(self, id_: str) -> SharePermission:
        """Get share permissions"""
        resp = self._client._request("GET", f"/rest/api/3/filter/{id_}/permission")
        return SharePermission.model_validate(resp.json())

    def add_share_permission(self, id_: str, body: SharePermissionInputBean) -> SharePermission:
        """Add share permission"""
        resp = self._client._request(
            "POST",
            f"/rest/api/3/filter/{id_}/permission",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return SharePermission.model_validate(resp.json())

    def delete_share_permission(self, id_: str, permission_id: str) -> None:
        """Delete share permission"""
        resp = self._client._request(
            "DELETE", f"/rest/api/3/filter/{id_}/permission/{permission_id}"
        )
        return None

    def get_share_permission(self, id_: str, permission_id: str) -> SharePermission:
        """Get share permission"""
        resp = self._client._request("GET", f"/rest/api/3/filter/{id_}/permission/{permission_id}")
        return SharePermission.model_validate(resp.json())


class AsyncFilterSharing(AsyncAPIResource):
    """Asynchronous resource for the Filter sharing API group."""

    async def get_default_share_scope(self) -> DefaultShareScope:
        """Get default share scope"""
        resp = await self._client._request("GET", "/rest/api/3/filter/defaultShareScope")
        return DefaultShareScope.model_validate(resp.json())

    async def set_default_share_scope(self, body: DefaultShareScope) -> DefaultShareScope:
        """Set default share scope"""
        resp = await self._client._request(
            "PUT",
            "/rest/api/3/filter/defaultShareScope",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return DefaultShareScope.model_validate(resp.json())

    async def get_share_permissions(self, id_: str) -> SharePermission:
        """Get share permissions"""
        resp = await self._client._request("GET", f"/rest/api/3/filter/{id_}/permission")
        return SharePermission.model_validate(resp.json())

    async def add_share_permission(
        self, id_: str, body: SharePermissionInputBean
    ) -> SharePermission:
        """Add share permission"""
        resp = await self._client._request(
            "POST",
            f"/rest/api/3/filter/{id_}/permission",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return SharePermission.model_validate(resp.json())

    async def delete_share_permission(self, id_: str, permission_id: str) -> None:
        """Delete share permission"""
        resp = await self._client._request(
            "DELETE", f"/rest/api/3/filter/{id_}/permission/{permission_id}"
        )
        return None

    async def get_share_permission(self, id_: str, permission_id: str) -> SharePermission:
        """Get share permission"""
        resp = await self._client._request(
            "GET", f"/rest/api/3/filter/{id_}/permission/{permission_id}"
        )
        return SharePermission.model_validate(resp.json())
