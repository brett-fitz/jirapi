"""Resource classes for the Dashboards API group."""

from __future__ import annotations

from jirapi._resource import AsyncAPIResource, SyncAPIResource
from jirapi.models import (
    AvailableDashboardGadgetsResponse,
    BulkEditShareableEntityRequest,
    BulkEditShareableEntityResponse,
    Dashboard,
    DashboardDetails,
    DashboardGadget,
    DashboardGadgetResponse,
    DashboardGadgetSettings,
    DashboardGadgetUpdateRequest,
    EntityProperty,
    PageBeanDashboard,
    PageOfDashboards,
    PropertyKeys,
)


class Dashboards(SyncAPIResource):
    """Synchronous resource for the Dashboards API group."""

    def get_all_dashboards(
        self,
        *,
        filter_: str | None = None,
        start_at: int | None = None,
        max_results: int | None = None,
    ) -> PageOfDashboards:
        """Get all dashboards"""
        params = self._client._build_params(
            **{"filter": filter_, "startAt": start_at, "maxResults": max_results}
        )
        resp = self._client._request("GET", "/rest/api/3/dashboard", params=params)
        return PageOfDashboards.model_validate(resp.json())

    def create_dashboard(
        self, body: DashboardDetails, *, extend_admin_permissions: bool | None = None
    ) -> Dashboard:
        """Create dashboard"""
        params = self._client._build_params(**{"extendAdminPermissions": extend_admin_permissions})
        resp = self._client._request(
            "POST",
            "/rest/api/3/dashboard",
            params=params,
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return Dashboard.model_validate(resp.json())

    def bulk_edit_dashboards(
        self, body: BulkEditShareableEntityRequest
    ) -> BulkEditShareableEntityResponse:
        """Bulk edit dashboards"""
        resp = self._client._request(
            "PUT",
            "/rest/api/3/dashboard/bulk/edit",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return BulkEditShareableEntityResponse.model_validate(resp.json())

    def get_all_available_dashboard_gadgets(self) -> AvailableDashboardGadgetsResponse:
        """Get available gadgets"""
        resp = self._client._request("GET", "/rest/api/3/dashboard/gadgets")
        return AvailableDashboardGadgetsResponse.model_validate(resp.json())

    def get_dashboards_paginated(
        self,
        *,
        dashboard_name: str | None = None,
        account_id: str | None = None,
        owner: str | None = None,
        groupname: str | None = None,
        group_id: str | None = None,
        project_id: int | None = None,
        order_by: str | None = None,
        start_at: int | None = None,
        max_results: int | None = None,
        status: str | None = None,
        expand: str | None = None,
    ) -> PageBeanDashboard:
        """Search for dashboards"""
        params = self._client._build_params(
            **{
                "dashboardName": dashboard_name,
                "accountId": account_id,
                "owner": owner,
                "groupname": groupname,
                "groupId": group_id,
                "projectId": project_id,
                "orderBy": order_by,
                "startAt": start_at,
                "maxResults": max_results,
                "status": status,
                "expand": expand,
            }
        )
        resp = self._client._request("GET", "/rest/api/3/dashboard/search", params=params)
        return PageBeanDashboard.model_validate(resp.json())

    def get_all_gadgets(
        self,
        dashboard_id: str,
        *,
        module_key: list[str] | None = None,
        uri: list[str] | None = None,
        gadget_id: list[str] | None = None,
    ) -> DashboardGadgetResponse:
        """Get gadgets"""
        params = self._client._build_params(
            **{"moduleKey": module_key, "uri": uri, "gadgetId": gadget_id}
        )
        resp = self._client._request(
            "GET", f"/rest/api/3/dashboard/{dashboard_id}/gadget", params=params
        )
        return DashboardGadgetResponse.model_validate(resp.json())

    def add_gadget(self, dashboard_id: str, body: DashboardGadgetSettings) -> DashboardGadget:
        """Add gadget to dashboard"""
        resp = self._client._request(
            "POST",
            f"/rest/api/3/dashboard/{dashboard_id}/gadget",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return DashboardGadget.model_validate(resp.json())

    def remove_gadget(self, dashboard_id: str, gadget_id: str) -> None:
        """Remove gadget from dashboard"""
        self._client._request("DELETE", f"/rest/api/3/dashboard/{dashboard_id}/gadget/{gadget_id}")
        return None

    def update_gadget(
        self, dashboard_id: str, gadget_id: str, body: DashboardGadgetUpdateRequest
    ) -> None:
        """Update gadget on dashboard"""
        self._client._request(
            "PUT",
            f"/rest/api/3/dashboard/{dashboard_id}/gadget/{gadget_id}",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    def get_dashboard_item_property_keys(self, dashboard_id: str, item_id: str) -> PropertyKeys:
        """Get dashboard item property keys"""
        resp = self._client._request(
            "GET", f"/rest/api/3/dashboard/{dashboard_id}/items/{item_id}/properties"
        )
        return PropertyKeys.model_validate(resp.json())

    def delete_dashboard_item_property(
        self, dashboard_id: str, item_id: str, property_key: str
    ) -> None:
        """Delete dashboard item property"""
        self._client._request(
            "DELETE",
            f"/rest/api/3/dashboard/{dashboard_id}/items/{item_id}/properties/{property_key}",
        )
        return None

    def get_dashboard_item_property(
        self, dashboard_id: str, item_id: str, property_key: str
    ) -> EntityProperty:
        """Get dashboard item property"""
        resp = self._client._request(
            "GET", f"/rest/api/3/dashboard/{dashboard_id}/items/{item_id}/properties/{property_key}"
        )
        return EntityProperty.model_validate(resp.json())

    def set_dashboard_item_property(
        self, dashboard_id: str, item_id: str, property_key: str
    ) -> None:
        """Set dashboard item property"""
        self._client._request(
            "PUT", f"/rest/api/3/dashboard/{dashboard_id}/items/{item_id}/properties/{property_key}"
        )
        return None

    def delete_dashboard(self, id_: str) -> None:
        """Delete dashboard"""
        self._client._request("DELETE", f"/rest/api/3/dashboard/{id_}")
        return None

    def get_dashboard(self, id_: str) -> Dashboard:
        """Get dashboard"""
        resp = self._client._request("GET", f"/rest/api/3/dashboard/{id_}")
        return Dashboard.model_validate(resp.json())

    def update_dashboard(
        self, id_: str, body: DashboardDetails, *, extend_admin_permissions: bool | None = None
    ) -> Dashboard:
        """Update dashboard"""
        params = self._client._build_params(**{"extendAdminPermissions": extend_admin_permissions})
        resp = self._client._request(
            "PUT",
            f"/rest/api/3/dashboard/{id_}",
            params=params,
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return Dashboard.model_validate(resp.json())

    def copy_dashboard(
        self, id_: str, body: DashboardDetails, *, extend_admin_permissions: bool | None = None
    ) -> Dashboard:
        """Copy dashboard"""
        params = self._client._build_params(**{"extendAdminPermissions": extend_admin_permissions})
        resp = self._client._request(
            "POST",
            f"/rest/api/3/dashboard/{id_}/copy",
            params=params,
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return Dashboard.model_validate(resp.json())


class AsyncDashboards(AsyncAPIResource):
    """Asynchronous resource for the Dashboards API group."""

    async def get_all_dashboards(
        self,
        *,
        filter_: str | None = None,
        start_at: int | None = None,
        max_results: int | None = None,
    ) -> PageOfDashboards:
        """Get all dashboards"""
        params = self._client._build_params(
            **{"filter": filter_, "startAt": start_at, "maxResults": max_results}
        )
        resp = await self._client._request("GET", "/rest/api/3/dashboard", params=params)
        return PageOfDashboards.model_validate(resp.json())

    async def create_dashboard(
        self, body: DashboardDetails, *, extend_admin_permissions: bool | None = None
    ) -> Dashboard:
        """Create dashboard"""
        params = self._client._build_params(**{"extendAdminPermissions": extend_admin_permissions})
        resp = await self._client._request(
            "POST",
            "/rest/api/3/dashboard",
            params=params,
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return Dashboard.model_validate(resp.json())

    async def bulk_edit_dashboards(
        self, body: BulkEditShareableEntityRequest
    ) -> BulkEditShareableEntityResponse:
        """Bulk edit dashboards"""
        resp = await self._client._request(
            "PUT",
            "/rest/api/3/dashboard/bulk/edit",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return BulkEditShareableEntityResponse.model_validate(resp.json())

    async def get_all_available_dashboard_gadgets(self) -> AvailableDashboardGadgetsResponse:
        """Get available gadgets"""
        resp = await self._client._request("GET", "/rest/api/3/dashboard/gadgets")
        return AvailableDashboardGadgetsResponse.model_validate(resp.json())

    async def get_dashboards_paginated(
        self,
        *,
        dashboard_name: str | None = None,
        account_id: str | None = None,
        owner: str | None = None,
        groupname: str | None = None,
        group_id: str | None = None,
        project_id: int | None = None,
        order_by: str | None = None,
        start_at: int | None = None,
        max_results: int | None = None,
        status: str | None = None,
        expand: str | None = None,
    ) -> PageBeanDashboard:
        """Search for dashboards"""
        params = self._client._build_params(
            **{
                "dashboardName": dashboard_name,
                "accountId": account_id,
                "owner": owner,
                "groupname": groupname,
                "groupId": group_id,
                "projectId": project_id,
                "orderBy": order_by,
                "startAt": start_at,
                "maxResults": max_results,
                "status": status,
                "expand": expand,
            }
        )
        resp = await self._client._request("GET", "/rest/api/3/dashboard/search", params=params)
        return PageBeanDashboard.model_validate(resp.json())

    async def get_all_gadgets(
        self,
        dashboard_id: str,
        *,
        module_key: list[str] | None = None,
        uri: list[str] | None = None,
        gadget_id: list[str] | None = None,
    ) -> DashboardGadgetResponse:
        """Get gadgets"""
        params = self._client._build_params(
            **{"moduleKey": module_key, "uri": uri, "gadgetId": gadget_id}
        )
        resp = await self._client._request(
            "GET", f"/rest/api/3/dashboard/{dashboard_id}/gadget", params=params
        )
        return DashboardGadgetResponse.model_validate(resp.json())

    async def add_gadget(self, dashboard_id: str, body: DashboardGadgetSettings) -> DashboardGadget:
        """Add gadget to dashboard"""
        resp = await self._client._request(
            "POST",
            f"/rest/api/3/dashboard/{dashboard_id}/gadget",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return DashboardGadget.model_validate(resp.json())

    async def remove_gadget(self, dashboard_id: str, gadget_id: str) -> None:
        """Remove gadget from dashboard"""
        await self._client._request(
            "DELETE", f"/rest/api/3/dashboard/{dashboard_id}/gadget/{gadget_id}"
        )
        return None

    async def update_gadget(
        self, dashboard_id: str, gadget_id: str, body: DashboardGadgetUpdateRequest
    ) -> None:
        """Update gadget on dashboard"""
        await self._client._request(
            "PUT",
            f"/rest/api/3/dashboard/{dashboard_id}/gadget/{gadget_id}",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    async def get_dashboard_item_property_keys(
        self, dashboard_id: str, item_id: str
    ) -> PropertyKeys:
        """Get dashboard item property keys"""
        resp = await self._client._request(
            "GET", f"/rest/api/3/dashboard/{dashboard_id}/items/{item_id}/properties"
        )
        return PropertyKeys.model_validate(resp.json())

    async def delete_dashboard_item_property(
        self, dashboard_id: str, item_id: str, property_key: str
    ) -> None:
        """Delete dashboard item property"""
        await self._client._request(
            "DELETE",
            f"/rest/api/3/dashboard/{dashboard_id}/items/{item_id}/properties/{property_key}",
        )
        return None

    async def get_dashboard_item_property(
        self, dashboard_id: str, item_id: str, property_key: str
    ) -> EntityProperty:
        """Get dashboard item property"""
        resp = await self._client._request(
            "GET", f"/rest/api/3/dashboard/{dashboard_id}/items/{item_id}/properties/{property_key}"
        )
        return EntityProperty.model_validate(resp.json())

    async def set_dashboard_item_property(
        self, dashboard_id: str, item_id: str, property_key: str
    ) -> None:
        """Set dashboard item property"""
        await self._client._request(
            "PUT", f"/rest/api/3/dashboard/{dashboard_id}/items/{item_id}/properties/{property_key}"
        )
        return None

    async def delete_dashboard(self, id_: str) -> None:
        """Delete dashboard"""
        await self._client._request("DELETE", f"/rest/api/3/dashboard/{id_}")
        return None

    async def get_dashboard(self, id_: str) -> Dashboard:
        """Get dashboard"""
        resp = await self._client._request("GET", f"/rest/api/3/dashboard/{id_}")
        return Dashboard.model_validate(resp.json())

    async def update_dashboard(
        self, id_: str, body: DashboardDetails, *, extend_admin_permissions: bool | None = None
    ) -> Dashboard:
        """Update dashboard"""
        params = self._client._build_params(**{"extendAdminPermissions": extend_admin_permissions})
        resp = await self._client._request(
            "PUT",
            f"/rest/api/3/dashboard/{id_}",
            params=params,
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return Dashboard.model_validate(resp.json())

    async def copy_dashboard(
        self, id_: str, body: DashboardDetails, *, extend_admin_permissions: bool | None = None
    ) -> Dashboard:
        """Copy dashboard"""
        params = self._client._build_params(**{"extendAdminPermissions": extend_admin_permissions})
        resp = await self._client._request(
            "POST",
            f"/rest/api/3/dashboard/{id_}/copy",
            params=params,
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return Dashboard.model_validate(resp.json())
