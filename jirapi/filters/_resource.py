"""Resource classes for filters."""

from __future__ import annotations

from jirapi._resource import AsyncAPIResource, SyncAPIResource
from jirapi.models import (
    ChangeFilterOwner,
    ColumnItem,
    ColumnRequestBody,
    DefaultShareScope,
    Filter,
    PageBeanFilterDetails,
    SharePermission,
    SharePermissionInput,
)


class Filters(SyncAPIResource):
    """Synchronous resource for filters."""

    def create(
        self,
        body: Filter,
        *,
        expand: str | None = None,
        override_share_permissions: bool | None = None,
    ) -> Filter:
        """Create filter"""
        params = self._client._build_params(
            **{"expand": expand, "overrideSharePermissions": override_share_permissions}
        )
        resp = self._client._request(
            "POST",
            "/rest/api/3/filter",
            params=params,
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return Filter.model_validate(resp.json())

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

    def get_favourites(self, *, expand: str | None = None) -> Filter:
        """Get favorite filters"""
        params = self._client._build_params(**{"expand": expand})
        resp = self._client._request("GET", "/rest/api/3/filter/favourite", params=params)
        return Filter.model_validate(resp.json())

    def get_mine(
        self, *, expand: str | None = None, include_favourites: bool | None = None
    ) -> Filter:
        """Get my filters"""
        params = self._client._build_params(
            **{"expand": expand, "includeFavourites": include_favourites}
        )
        resp = self._client._request("GET", "/rest/api/3/filter/my", params=params)
        return Filter.model_validate(resp.json())

    def list(
        self,
        *,
        filter_name: str | None = None,
        account_id: str | None = None,
        owner: str | None = None,
        groupname: str | None = None,
        group_id: str | None = None,
        project_id: int | None = None,
        id_: list[str] | None = None,
        order_by: str | None = None,
        start_at: int | None = None,
        max_results: int | None = None,
        expand: str | None = None,
        override_share_permissions: bool | None = None,
        is_substring_match: bool | None = None,
    ) -> PageBeanFilterDetails:
        """Search for filters"""
        params = self._client._build_params(
            **{
                "filterName": filter_name,
                "accountId": account_id,
                "owner": owner,
                "groupname": groupname,
                "groupId": group_id,
                "projectId": project_id,
                "id": id_,
                "orderBy": order_by,
                "startAt": start_at,
                "maxResults": max_results,
                "expand": expand,
                "overrideSharePermissions": override_share_permissions,
                "isSubstringMatch": is_substring_match,
            }
        )
        resp = self._client._request("GET", "/rest/api/3/filter/search", params=params)
        return PageBeanFilterDetails.model_validate(resp.json())

    def delete(self, id_: str) -> None:
        """Delete filter"""
        self._client._request("DELETE", f"/rest/api/3/filter/{id_}")
        return None

    def get(
        self, id_: str, *, expand: str | None = None, override_share_permissions: bool | None = None
    ) -> Filter:
        """Get filter"""
        params = self._client._build_params(
            **{"expand": expand, "overrideSharePermissions": override_share_permissions}
        )
        resp = self._client._request("GET", f"/rest/api/3/filter/{id_}", params=params)
        return Filter.model_validate(resp.json())

    def update(
        self,
        id_: str,
        body: Filter,
        *,
        expand: str | None = None,
        override_share_permissions: bool | None = None,
    ) -> Filter:
        """Update filter"""
        params = self._client._build_params(
            **{"expand": expand, "overrideSharePermissions": override_share_permissions}
        )
        resp = self._client._request(
            "PUT",
            f"/rest/api/3/filter/{id_}",
            params=params,
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return Filter.model_validate(resp.json())

    def reset_columns(self, id_: str) -> None:
        """Reset columns"""
        self._client._request("DELETE", f"/rest/api/3/filter/{id_}/columns")
        return None

    def get_columns(self, id_: str) -> ColumnItem:
        """Get columns"""
        resp = self._client._request("GET", f"/rest/api/3/filter/{id_}/columns")
        return ColumnItem.model_validate(resp.json())

    def set_columns(self, id_: str, body: ColumnRequestBody) -> None:
        """Set columns"""
        self._client._request(
            "PUT",
            f"/rest/api/3/filter/{id_}/columns",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    def remove_favourite(self, id_: str, *, expand: str | None = None) -> Filter:
        """Remove filter as favorite"""
        params = self._client._build_params(**{"expand": expand})
        resp = self._client._request("DELETE", f"/rest/api/3/filter/{id_}/favourite", params=params)
        return Filter.model_validate(resp.json())

    def add_favourite(self, id_: str, *, expand: str | None = None) -> Filter:
        """Add filter as favorite"""
        params = self._client._build_params(**{"expand": expand})
        resp = self._client._request("PUT", f"/rest/api/3/filter/{id_}/favourite", params=params)
        return Filter.model_validate(resp.json())

    def change_owner(self, id_: str, body: ChangeFilterOwner) -> None:
        """Change filter owner"""
        self._client._request(
            "PUT",
            f"/rest/api/3/filter/{id_}/owner",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    def get_share_permissions(self, id_: str) -> SharePermission:
        """Get share permissions"""
        resp = self._client._request("GET", f"/rest/api/3/filter/{id_}/permission")
        return SharePermission.model_validate(resp.json())

    def add_share_permission(self, id_: str, body: SharePermissionInput) -> SharePermission:
        """Add share permission"""
        resp = self._client._request(
            "POST",
            f"/rest/api/3/filter/{id_}/permission",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return SharePermission.model_validate(resp.json())

    def delete_share_permission(self, id_: str, permission_id: str) -> None:
        """Delete share permission"""
        self._client._request("DELETE", f"/rest/api/3/filter/{id_}/permission/{permission_id}")
        return None

    def get_share_permission(self, id_: str, permission_id: str) -> SharePermission:
        """Get share permission"""
        resp = self._client._request("GET", f"/rest/api/3/filter/{id_}/permission/{permission_id}")
        return SharePermission.model_validate(resp.json())


class AsyncFilters(AsyncAPIResource):
    """Asynchronous resource for filters."""

    async def create(
        self,
        body: Filter,
        *,
        expand: str | None = None,
        override_share_permissions: bool | None = None,
    ) -> Filter:
        """Create filter"""
        params = self._client._build_params(
            **{"expand": expand, "overrideSharePermissions": override_share_permissions}
        )
        resp = await self._client._request(
            "POST",
            "/rest/api/3/filter",
            params=params,
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return Filter.model_validate(resp.json())

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

    async def get_favourites(self, *, expand: str | None = None) -> Filter:
        """Get favorite filters"""
        params = self._client._build_params(**{"expand": expand})
        resp = await self._client._request("GET", "/rest/api/3/filter/favourite", params=params)
        return Filter.model_validate(resp.json())

    async def get_mine(
        self, *, expand: str | None = None, include_favourites: bool | None = None
    ) -> Filter:
        """Get my filters"""
        params = self._client._build_params(
            **{"expand": expand, "includeFavourites": include_favourites}
        )
        resp = await self._client._request("GET", "/rest/api/3/filter/my", params=params)
        return Filter.model_validate(resp.json())

    async def list(
        self,
        *,
        filter_name: str | None = None,
        account_id: str | None = None,
        owner: str | None = None,
        groupname: str | None = None,
        group_id: str | None = None,
        project_id: int | None = None,
        id_: list[str] | None = None,
        order_by: str | None = None,
        start_at: int | None = None,
        max_results: int | None = None,
        expand: str | None = None,
        override_share_permissions: bool | None = None,
        is_substring_match: bool | None = None,
    ) -> PageBeanFilterDetails:
        """Search for filters"""
        params = self._client._build_params(
            **{
                "filterName": filter_name,
                "accountId": account_id,
                "owner": owner,
                "groupname": groupname,
                "groupId": group_id,
                "projectId": project_id,
                "id": id_,
                "orderBy": order_by,
                "startAt": start_at,
                "maxResults": max_results,
                "expand": expand,
                "overrideSharePermissions": override_share_permissions,
                "isSubstringMatch": is_substring_match,
            }
        )
        resp = await self._client._request("GET", "/rest/api/3/filter/search", params=params)
        return PageBeanFilterDetails.model_validate(resp.json())

    async def delete(self, id_: str) -> None:
        """Delete filter"""
        await self._client._request("DELETE", f"/rest/api/3/filter/{id_}")
        return None

    async def get(
        self, id_: str, *, expand: str | None = None, override_share_permissions: bool | None = None
    ) -> Filter:
        """Get filter"""
        params = self._client._build_params(
            **{"expand": expand, "overrideSharePermissions": override_share_permissions}
        )
        resp = await self._client._request("GET", f"/rest/api/3/filter/{id_}", params=params)
        return Filter.model_validate(resp.json())

    async def update(
        self,
        id_: str,
        body: Filter,
        *,
        expand: str | None = None,
        override_share_permissions: bool | None = None,
    ) -> Filter:
        """Update filter"""
        params = self._client._build_params(
            **{"expand": expand, "overrideSharePermissions": override_share_permissions}
        )
        resp = await self._client._request(
            "PUT",
            f"/rest/api/3/filter/{id_}",
            params=params,
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return Filter.model_validate(resp.json())

    async def reset_columns(self, id_: str) -> None:
        """Reset columns"""
        await self._client._request("DELETE", f"/rest/api/3/filter/{id_}/columns")
        return None

    async def get_columns(self, id_: str) -> ColumnItem:
        """Get columns"""
        resp = await self._client._request("GET", f"/rest/api/3/filter/{id_}/columns")
        return ColumnItem.model_validate(resp.json())

    async def set_columns(self, id_: str, body: ColumnRequestBody) -> None:
        """Set columns"""
        await self._client._request(
            "PUT",
            f"/rest/api/3/filter/{id_}/columns",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    async def remove_favourite(self, id_: str, *, expand: str | None = None) -> Filter:
        """Remove filter as favorite"""
        params = self._client._build_params(**{"expand": expand})
        resp = await self._client._request(
            "DELETE", f"/rest/api/3/filter/{id_}/favourite", params=params
        )
        return Filter.model_validate(resp.json())

    async def add_favourite(self, id_: str, *, expand: str | None = None) -> Filter:
        """Add filter as favorite"""
        params = self._client._build_params(**{"expand": expand})
        resp = await self._client._request(
            "PUT", f"/rest/api/3/filter/{id_}/favourite", params=params
        )
        return Filter.model_validate(resp.json())

    async def change_owner(self, id_: str, body: ChangeFilterOwner) -> None:
        """Change filter owner"""
        await self._client._request(
            "PUT",
            f"/rest/api/3/filter/{id_}/owner",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    async def get_share_permissions(self, id_: str) -> SharePermission:
        """Get share permissions"""
        resp = await self._client._request("GET", f"/rest/api/3/filter/{id_}/permission")
        return SharePermission.model_validate(resp.json())

    async def add_share_permission(self, id_: str, body: SharePermissionInput) -> SharePermission:
        """Add share permission"""
        resp = await self._client._request(
            "POST",
            f"/rest/api/3/filter/{id_}/permission",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return SharePermission.model_validate(resp.json())

    async def delete_share_permission(self, id_: str, permission_id: str) -> None:
        """Delete share permission"""
        await self._client._request(
            "DELETE", f"/rest/api/3/filter/{id_}/permission/{permission_id}"
        )
        return None

    async def get_share_permission(self, id_: str, permission_id: str) -> SharePermission:
        """Get share permission"""
        resp = await self._client._request(
            "GET", f"/rest/api/3/filter/{id_}/permission/{permission_id}"
        )
        return SharePermission.model_validate(resp.json())
