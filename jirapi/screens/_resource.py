"""Resource classes for screens."""

from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING

from jirapi._resource import AsyncAPIResource, SyncAPIResource
from jirapi.models import (
    PageBeanScreen,
    PageBeanScreenWithTab,
    Screen,
    ScreenableField,
    ScreenDetails,
    UpdateScreenDetails,
)


if TYPE_CHECKING:
    from jirapi.screens.issue_type_screen_schemes import (
        AsyncScreenIssueTypeScreenSchemes,
        ScreenIssueTypeScreenSchemes,
    )
    from jirapi.screens.schemes import AsyncScreenSchemes, ScreenSchemes
    from jirapi.screens.tab_fields import AsyncScreenTabFields, ScreenTabFields
    from jirapi.screens.tabs import AsyncScreenTabs, ScreenTabs


class Screens(SyncAPIResource):
    """Synchronous resource for screens."""

    @cached_property
    def issue_type_screen_schemes(self) -> ScreenIssueTypeScreenSchemes:
        from jirapi.screens.issue_type_screen_schemes import ScreenIssueTypeScreenSchemes

        return ScreenIssueTypeScreenSchemes(self._client)

    @cached_property
    def schemes(self) -> ScreenSchemes:
        from jirapi.screens.schemes import ScreenSchemes

        return ScreenSchemes(self._client)

    @cached_property
    def tab_fields(self) -> ScreenTabFields:
        from jirapi.screens.tab_fields import ScreenTabFields

        return ScreenTabFields(self._client)

    @cached_property
    def tabs(self) -> ScreenTabs:
        from jirapi.screens.tabs import ScreenTabs

        return ScreenTabs(self._client)

    def get_for_field(
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

    def get(
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

    def create(self, body: ScreenDetails) -> Screen:
        """Create screen"""
        resp = self._client._request(
            "POST", "/rest/api/3/screens", json=body.model_dump(by_alias=True, exclude_none=True)
        )
        return Screen.model_validate(resp.json())

    def add_field_to_default(self, field_id: str) -> None:
        """Add field to default screen"""
        self._client._request("POST", f"/rest/api/3/screens/addToDefault/{field_id}")
        return None

    def delete(self, screen_id: str) -> None:
        """Delete screen"""
        self._client._request("DELETE", f"/rest/api/3/screens/{screen_id}")
        return None

    def update(self, screen_id: str, body: UpdateScreenDetails) -> Screen:
        """Update screen"""
        resp = self._client._request(
            "PUT",
            f"/rest/api/3/screens/{screen_id}",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return Screen.model_validate(resp.json())

    def get_available_fields(self, screen_id: str) -> ScreenableField:
        """Get available screen fields"""
        resp = self._client._request("GET", f"/rest/api/3/screens/{screen_id}/availableFields")
        return ScreenableField.model_validate(resp.json())


class AsyncScreens(AsyncAPIResource):
    """Asynchronous resource for screens."""

    @cached_property
    def issue_type_screen_schemes(self) -> AsyncScreenIssueTypeScreenSchemes:
        from jirapi.screens.issue_type_screen_schemes import AsyncScreenIssueTypeScreenSchemes

        return AsyncScreenIssueTypeScreenSchemes(self._client)

    @cached_property
    def schemes(self) -> AsyncScreenSchemes:
        from jirapi.screens.schemes import AsyncScreenSchemes

        return AsyncScreenSchemes(self._client)

    @cached_property
    def tab_fields(self) -> AsyncScreenTabFields:
        from jirapi.screens.tab_fields import AsyncScreenTabFields

        return AsyncScreenTabFields(self._client)

    @cached_property
    def tabs(self) -> AsyncScreenTabs:
        from jirapi.screens.tabs import AsyncScreenTabs

        return AsyncScreenTabs(self._client)

    async def get_for_field(
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

    async def get(
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

    async def create(self, body: ScreenDetails) -> Screen:
        """Create screen"""
        resp = await self._client._request(
            "POST", "/rest/api/3/screens", json=body.model_dump(by_alias=True, exclude_none=True)
        )
        return Screen.model_validate(resp.json())

    async def add_field_to_default(self, field_id: str) -> None:
        """Add field to default screen"""
        await self._client._request("POST", f"/rest/api/3/screens/addToDefault/{field_id}")
        return None

    async def delete(self, screen_id: str) -> None:
        """Delete screen"""
        await self._client._request("DELETE", f"/rest/api/3/screens/{screen_id}")
        return None

    async def update(self, screen_id: str, body: UpdateScreenDetails) -> Screen:
        """Update screen"""
        resp = await self._client._request(
            "PUT",
            f"/rest/api/3/screens/{screen_id}",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return Screen.model_validate(resp.json())

    async def get_available_fields(self, screen_id: str) -> ScreenableField:
        """Get available screen fields"""
        resp = await self._client._request(
            "GET", f"/rest/api/3/screens/{screen_id}/availableFields"
        )
        return ScreenableField.model_validate(resp.json())
