"""Resource classes for the UI modifications (apps) API group."""

from __future__ import annotations

from jirapi._resource import AsyncAPIResource, SyncAPIResource
from jirapi.models import (
    CreateUiModificationDetails,
    PageBeanUiModificationDetails,
    UiModificationIdentifiers,
    UpdateUiModificationDetails,
)


class UiModificationsApps(SyncAPIResource):
    """Synchronous resource for the UI modifications (apps) API group."""

    def get_ui_modifications(
        self,
        *,
        start_at: int | None = None,
        max_results: int | None = None,
        expand: str | None = None,
    ) -> PageBeanUiModificationDetails:
        """Get UI modifications"""
        params = self._client._build_params(
            **{"startAt": start_at, "maxResults": max_results, "expand": expand}
        )
        resp = self._client._request("GET", "/rest/api/3/uiModifications", params=params)
        return PageBeanUiModificationDetails.model_validate(resp.json())

    def create_ui_modification(
        self, body: CreateUiModificationDetails
    ) -> UiModificationIdentifiers:
        """Create UI modification"""
        resp = self._client._request(
            "POST",
            "/rest/api/3/uiModifications",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return UiModificationIdentifiers.model_validate(resp.json())

    def delete_ui_modification(self, ui_modification_id: str) -> None:
        """Delete UI modification"""
        self._client._request("DELETE", f"/rest/api/3/uiModifications/{ui_modification_id}")
        return None

    def update_ui_modification(
        self, ui_modification_id: str, body: UpdateUiModificationDetails
    ) -> None:
        """Update UI modification"""
        self._client._request(
            "PUT",
            f"/rest/api/3/uiModifications/{ui_modification_id}",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None


class AsyncUiModificationsApps(AsyncAPIResource):
    """Asynchronous resource for the UI modifications (apps) API group."""

    async def get_ui_modifications(
        self,
        *,
        start_at: int | None = None,
        max_results: int | None = None,
        expand: str | None = None,
    ) -> PageBeanUiModificationDetails:
        """Get UI modifications"""
        params = self._client._build_params(
            **{"startAt": start_at, "maxResults": max_results, "expand": expand}
        )
        resp = await self._client._request("GET", "/rest/api/3/uiModifications", params=params)
        return PageBeanUiModificationDetails.model_validate(resp.json())

    async def create_ui_modification(
        self, body: CreateUiModificationDetails
    ) -> UiModificationIdentifiers:
        """Create UI modification"""
        resp = await self._client._request(
            "POST",
            "/rest/api/3/uiModifications",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return UiModificationIdentifiers.model_validate(resp.json())

    async def delete_ui_modification(self, ui_modification_id: str) -> None:
        """Delete UI modification"""
        await self._client._request("DELETE", f"/rest/api/3/uiModifications/{ui_modification_id}")
        return None

    async def update_ui_modification(
        self, ui_modification_id: str, body: UpdateUiModificationDetails
    ) -> None:
        """Update UI modification"""
        await self._client._request(
            "PUT",
            f"/rest/api/3/uiModifications/{ui_modification_id}",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None
