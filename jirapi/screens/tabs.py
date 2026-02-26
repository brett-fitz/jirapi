"""Resource classes for screens.tabs."""

from __future__ import annotations

from jirapi._resource import AsyncAPIResource, SyncAPIResource
from jirapi.models import ScreenableTab


class ScreenTabs(SyncAPIResource):
    """Synchronous resource for screens.tabs."""

    def list_bulk(
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
        self._client._request("GET", "/rest/api/3/screens/tabs", params=params)
        return None

    def list(self, screen_id: str, *, project_key: str | None = None) -> ScreenableTab:
        """Get all screen tabs"""
        params = self._client._build_params(**{"projectKey": project_key})
        resp = self._client._request("GET", f"/rest/api/3/screens/{screen_id}/tabs", params=params)
        return ScreenableTab.model_validate(resp.json())

    def add(self, screen_id: str, body: ScreenableTab) -> ScreenableTab:
        """Create screen tab"""
        resp = self._client._request(
            "POST",
            f"/rest/api/3/screens/{screen_id}/tabs",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return ScreenableTab.model_validate(resp.json())

    def delete(self, screen_id: str, tab_id: str) -> None:
        """Delete screen tab"""
        self._client._request("DELETE", f"/rest/api/3/screens/{screen_id}/tabs/{tab_id}")
        return None

    def rename(self, screen_id: str, tab_id: str, body: ScreenableTab) -> ScreenableTab:
        """Update screen tab"""
        resp = self._client._request(
            "PUT",
            f"/rest/api/3/screens/{screen_id}/tabs/{tab_id}",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return ScreenableTab.model_validate(resp.json())

    def move(self, screen_id: str, tab_id: str, pos: str) -> None:
        """Move screen tab"""
        self._client._request("POST", f"/rest/api/3/screens/{screen_id}/tabs/{tab_id}/move/{pos}")
        return None


class AsyncScreenTabs(AsyncAPIResource):
    """Asynchronous resource for screens.tabs."""

    async def list_bulk(
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
        await self._client._request("GET", "/rest/api/3/screens/tabs", params=params)
        return None

    async def list(self, screen_id: str, *, project_key: str | None = None) -> ScreenableTab:
        """Get all screen tabs"""
        params = self._client._build_params(**{"projectKey": project_key})
        resp = await self._client._request(
            "GET", f"/rest/api/3/screens/{screen_id}/tabs", params=params
        )
        return ScreenableTab.model_validate(resp.json())

    async def add(self, screen_id: str, body: ScreenableTab) -> ScreenableTab:
        """Create screen tab"""
        resp = await self._client._request(
            "POST",
            f"/rest/api/3/screens/{screen_id}/tabs",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return ScreenableTab.model_validate(resp.json())

    async def delete(self, screen_id: str, tab_id: str) -> None:
        """Delete screen tab"""
        await self._client._request("DELETE", f"/rest/api/3/screens/{screen_id}/tabs/{tab_id}")
        return None

    async def rename(self, screen_id: str, tab_id: str, body: ScreenableTab) -> ScreenableTab:
        """Update screen tab"""
        resp = await self._client._request(
            "PUT",
            f"/rest/api/3/screens/{screen_id}/tabs/{tab_id}",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return ScreenableTab.model_validate(resp.json())

    async def move(self, screen_id: str, tab_id: str, pos: str) -> None:
        """Move screen tab"""
        await self._client._request(
            "POST", f"/rest/api/3/screens/{screen_id}/tabs/{tab_id}/move/{pos}"
        )
        return None
