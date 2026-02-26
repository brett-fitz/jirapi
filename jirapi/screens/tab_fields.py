"""Resource classes for screens.tab_fields."""

from __future__ import annotations

from jirapi._resource import AsyncAPIResource, SyncAPIResource
from jirapi.models import AddField, MoveField, ScreenableField


class ScreenTabFields(SyncAPIResource):
    """Synchronous resource for screens.tab_fields."""

    def list(
        self, screen_id: str, tab_id: str, *, project_key: str | None = None
    ) -> ScreenableField:
        """Get all screen tab fields"""
        params = self._client._build_params(**{"projectKey": project_key})
        resp = self._client._request(
            "GET", f"/rest/api/3/screens/{screen_id}/tabs/{tab_id}/fields", params=params
        )
        return ScreenableField.model_validate(resp.json())

    def add(self, screen_id: str, tab_id: str, body: AddField) -> ScreenableField:
        """Add screen tab field"""
        resp = self._client._request(
            "POST",
            f"/rest/api/3/screens/{screen_id}/tabs/{tab_id}/fields",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return ScreenableField.model_validate(resp.json())

    def remove(self, screen_id: str, tab_id: str, id_: str) -> None:
        """Remove screen tab field"""
        self._client._request(
            "DELETE", f"/rest/api/3/screens/{screen_id}/tabs/{tab_id}/fields/{id_}"
        )
        return None

    def move(self, screen_id: str, tab_id: str, id_: str, body: MoveField) -> None:
        """Move screen tab field"""
        self._client._request(
            "POST",
            f"/rest/api/3/screens/{screen_id}/tabs/{tab_id}/fields/{id_}/move",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None


class AsyncScreenTabFields(AsyncAPIResource):
    """Asynchronous resource for screens.tab_fields."""

    async def list(
        self, screen_id: str, tab_id: str, *, project_key: str | None = None
    ) -> ScreenableField:
        """Get all screen tab fields"""
        params = self._client._build_params(**{"projectKey": project_key})
        resp = await self._client._request(
            "GET", f"/rest/api/3/screens/{screen_id}/tabs/{tab_id}/fields", params=params
        )
        return ScreenableField.model_validate(resp.json())

    async def add(self, screen_id: str, tab_id: str, body: AddField) -> ScreenableField:
        """Add screen tab field"""
        resp = await self._client._request(
            "POST",
            f"/rest/api/3/screens/{screen_id}/tabs/{tab_id}/fields",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return ScreenableField.model_validate(resp.json())

    async def remove(self, screen_id: str, tab_id: str, id_: str) -> None:
        """Remove screen tab field"""
        await self._client._request(
            "DELETE", f"/rest/api/3/screens/{screen_id}/tabs/{tab_id}/fields/{id_}"
        )
        return None

    async def move(self, screen_id: str, tab_id: str, id_: str, body: MoveField) -> None:
        """Move screen tab field"""
        await self._client._request(
            "POST",
            f"/rest/api/3/screens/{screen_id}/tabs/{tab_id}/fields/{id_}/move",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None
