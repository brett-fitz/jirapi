"""Resource classes for the Screens API group."""

from __future__ import annotations

from jirapi._resource import AsyncAPIResource, SyncAPIResource
from jirapi.models import (
    PageBeanScreen,
    PageBeanScreenWithTab,
    Screen,
    ScreenableField,
    ScreenDetails,
    UpdateScreenDetails,
)


class Screens(SyncAPIResource):
    """Synchronous resource for the Screens API group."""

    def get_screens_for_field(
        self,
        field_id: str,
        *,
        start_at: int | None = None,
        max_results: int | None = None,
        expand: str | None = None,
    ) -> PageBeanScreenWithTab:
        """Get screens for a field"""
        params = self._client._build_params(
            **{"startAt": start_at, "maxResults": max_results, "expand": expand}
        )
        resp = self._client._request("GET", f"/rest/api/3/field/{field_id}/screens", params=params)
        return PageBeanScreenWithTab.model_validate(resp.json())

    def get_screens(
        self,
        *,
        start_at: int | None = None,
        max_results: int | None = None,
        id_: list[str] | None = None,
        query_string: str | None = None,
        scope: list[str] | None = None,
        order_by: str | None = None,
    ) -> PageBeanScreen:
        """Get screens"""
        params = self._client._build_params(
            **{
                "startAt": start_at,
                "maxResults": max_results,
                "id": id_,
                "queryString": query_string,
                "scope": scope,
                "orderBy": order_by,
            }
        )
        resp = self._client._request("GET", "/rest/api/3/screens", params=params)
        return PageBeanScreen.model_validate(resp.json())

    def create_screen(self, body: ScreenDetails) -> Screen:
        """Create screen"""
        resp = self._client._request(
            "POST", "/rest/api/3/screens", json=body.model_dump(by_alias=True, exclude_none=True)
        )
        return Screen.model_validate(resp.json())

    def add_field_to_default_screen(self, field_id: str) -> None:
        """Add field to default screen"""
        resp = self._client._request("POST", f"/rest/api/3/screens/addToDefault/{field_id}")
        return None

    def delete_screen(self, screen_id: str) -> None:
        """Delete screen"""
        resp = self._client._request("DELETE", f"/rest/api/3/screens/{screen_id}")
        return None

    def update_screen(self, screen_id: str, body: UpdateScreenDetails) -> Screen:
        """Update screen"""
        resp = self._client._request(
            "PUT",
            f"/rest/api/3/screens/{screen_id}",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return Screen.model_validate(resp.json())

    def get_available_screen_fields(self, screen_id: str) -> ScreenableField:
        """Get available screen fields"""
        resp = self._client._request("GET", f"/rest/api/3/screens/{screen_id}/availableFields")
        return ScreenableField.model_validate(resp.json())


class AsyncScreens(AsyncAPIResource):
    """Asynchronous resource for the Screens API group."""

    async def get_screens_for_field(
        self,
        field_id: str,
        *,
        start_at: int | None = None,
        max_results: int | None = None,
        expand: str | None = None,
    ) -> PageBeanScreenWithTab:
        """Get screens for a field"""
        params = self._client._build_params(
            **{"startAt": start_at, "maxResults": max_results, "expand": expand}
        )
        resp = await self._client._request(
            "GET", f"/rest/api/3/field/{field_id}/screens", params=params
        )
        return PageBeanScreenWithTab.model_validate(resp.json())

    async def get_screens(
        self,
        *,
        start_at: int | None = None,
        max_results: int | None = None,
        id_: list[str] | None = None,
        query_string: str | None = None,
        scope: list[str] | None = None,
        order_by: str | None = None,
    ) -> PageBeanScreen:
        """Get screens"""
        params = self._client._build_params(
            **{
                "startAt": start_at,
                "maxResults": max_results,
                "id": id_,
                "queryString": query_string,
                "scope": scope,
                "orderBy": order_by,
            }
        )
        resp = await self._client._request("GET", "/rest/api/3/screens", params=params)
        return PageBeanScreen.model_validate(resp.json())

    async def create_screen(self, body: ScreenDetails) -> Screen:
        """Create screen"""
        resp = await self._client._request(
            "POST", "/rest/api/3/screens", json=body.model_dump(by_alias=True, exclude_none=True)
        )
        return Screen.model_validate(resp.json())

    async def add_field_to_default_screen(self, field_id: str) -> None:
        """Add field to default screen"""
        resp = await self._client._request("POST", f"/rest/api/3/screens/addToDefault/{field_id}")
        return None

    async def delete_screen(self, screen_id: str) -> None:
        """Delete screen"""
        resp = await self._client._request("DELETE", f"/rest/api/3/screens/{screen_id}")
        return None

    async def update_screen(self, screen_id: str, body: UpdateScreenDetails) -> Screen:
        """Update screen"""
        resp = await self._client._request(
            "PUT",
            f"/rest/api/3/screens/{screen_id}",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return Screen.model_validate(resp.json())

    async def get_available_screen_fields(self, screen_id: str) -> ScreenableField:
        """Get available screen fields"""
        resp = await self._client._request(
            "GET", f"/rest/api/3/screens/{screen_id}/availableFields"
        )
        return ScreenableField.model_validate(resp.json())
