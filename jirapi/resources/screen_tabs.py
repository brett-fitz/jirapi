"""Resource classes for the Screen tabs API group."""

from __future__ import annotations

from jirapi._resource import AsyncAPIResource, SyncAPIResource
from jirapi.models import ScreenableTab


class ScreenTabs(SyncAPIResource):
    """Synchronous resource for the Screen tabs API group."""

    def get_bulk_screen_tabs(
        self,
        *,
        screen_id: list[str] | None = None,
        tab_id: list[str] | None = None,
        start_at: int | None = None,
        max_result: int | None = None,
    ) -> None:
        """Get bulk screen tabs"""
        params = self._client._build_params(
            **{"screenId": screen_id, "tabId": tab_id, "startAt": start_at, "maxResult": max_result}
        )
        resp = self._client._request("GET", "/rest/api/3/screens/tabs", params=params)
        return None

    def get_all_screen_tabs(
        self, screen_id: str, *, project_key: str | None = None
    ) -> ScreenableTab:
        """Get all screen tabs"""
        params = self._client._build_params(**{"projectKey": project_key})
        resp = self._client._request("GET", f"/rest/api/3/screens/{screen_id}/tabs", params=params)
        return ScreenableTab.model_validate(resp.json())

    def add_screen_tab(self, screen_id: str, body: ScreenableTab) -> ScreenableTab:
        """Create screen tab"""
        resp = self._client._request(
            "POST",
            f"/rest/api/3/screens/{screen_id}/tabs",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return ScreenableTab.model_validate(resp.json())

    def delete_screen_tab(self, screen_id: str, tab_id: str) -> None:
        """Delete screen tab"""
        resp = self._client._request("DELETE", f"/rest/api/3/screens/{screen_id}/tabs/{tab_id}")
        return None

    def rename_screen_tab(self, screen_id: str, tab_id: str, body: ScreenableTab) -> ScreenableTab:
        """Update screen tab"""
        resp = self._client._request(
            "PUT",
            f"/rest/api/3/screens/{screen_id}/tabs/{tab_id}",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return ScreenableTab.model_validate(resp.json())

    def move_screen_tab(self, screen_id: str, tab_id: str, pos: str) -> None:
        """Move screen tab"""
        resp = self._client._request(
            "POST", f"/rest/api/3/screens/{screen_id}/tabs/{tab_id}/move/{pos}"
        )
        return None


class AsyncScreenTabs(AsyncAPIResource):
    """Asynchronous resource for the Screen tabs API group."""

    async def get_bulk_screen_tabs(
        self,
        *,
        screen_id: list[str] | None = None,
        tab_id: list[str] | None = None,
        start_at: int | None = None,
        max_result: int | None = None,
    ) -> None:
        """Get bulk screen tabs"""
        params = self._client._build_params(
            **{"screenId": screen_id, "tabId": tab_id, "startAt": start_at, "maxResult": max_result}
        )
        resp = await self._client._request("GET", "/rest/api/3/screens/tabs", params=params)
        return None

    async def get_all_screen_tabs(
        self, screen_id: str, *, project_key: str | None = None
    ) -> ScreenableTab:
        """Get all screen tabs"""
        params = self._client._build_params(**{"projectKey": project_key})
        resp = await self._client._request(
            "GET", f"/rest/api/3/screens/{screen_id}/tabs", params=params
        )
        return ScreenableTab.model_validate(resp.json())

    async def add_screen_tab(self, screen_id: str, body: ScreenableTab) -> ScreenableTab:
        """Create screen tab"""
        resp = await self._client._request(
            "POST",
            f"/rest/api/3/screens/{screen_id}/tabs",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return ScreenableTab.model_validate(resp.json())

    async def delete_screen_tab(self, screen_id: str, tab_id: str) -> None:
        """Delete screen tab"""
        resp = await self._client._request(
            "DELETE", f"/rest/api/3/screens/{screen_id}/tabs/{tab_id}"
        )
        return None

    async def rename_screen_tab(
        self, screen_id: str, tab_id: str, body: ScreenableTab
    ) -> ScreenableTab:
        """Update screen tab"""
        resp = await self._client._request(
            "PUT",
            f"/rest/api/3/screens/{screen_id}/tabs/{tab_id}",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return ScreenableTab.model_validate(resp.json())

    async def move_screen_tab(self, screen_id: str, tab_id: str, pos: str) -> None:
        """Move screen tab"""
        resp = await self._client._request(
            "POST", f"/rest/api/3/screens/{screen_id}/tabs/{tab_id}/move/{pos}"
        )
        return None
