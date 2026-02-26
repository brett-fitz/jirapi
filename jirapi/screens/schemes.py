"""Resource classes for screens.schemes."""

from __future__ import annotations

from jirapi._resource import AsyncAPIResource, SyncAPIResource
from jirapi.models import (
    PageBeanScreenScheme,
    ScreenSchemeDetails,
    ScreenSchemeId,
    UpdateScreenSchemeDetails,
)


class ScreenSchemes(SyncAPIResource):
    """Synchronous resource for screens.schemes."""

    def list(
        self,
        *,
        start_at: int | None = None,
        max_results: int | None = None,
        id_: list[str] | None = None,
        expand: str | None = None,
        query_string: str | None = None,
        order_by: str | None = None,
    ) -> PageBeanScreenScheme:
        """Get screen schemes"""
        params = self._client._build_params(
            **{
                "startAt": start_at,
                "maxResults": max_results,
                "id": id_,
                "expand": expand,
                "queryString": query_string,
                "orderBy": order_by,
            }
        )
        resp = self._client._request("GET", "/rest/api/3/screenscheme", params=params)
        return PageBeanScreenScheme.model_validate(resp.json())

    def create(self, body: ScreenSchemeDetails) -> ScreenSchemeId:
        """Create screen scheme"""
        resp = self._client._request(
            "POST",
            "/rest/api/3/screenscheme",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return ScreenSchemeId.model_validate(resp.json())

    def delete(self, screen_scheme_id: str) -> None:
        """Delete screen scheme"""
        self._client._request("DELETE", f"/rest/api/3/screenscheme/{screen_scheme_id}")
        return None

    def update(self, screen_scheme_id: str, body: UpdateScreenSchemeDetails) -> None:
        """Update screen scheme"""
        self._client._request(
            "PUT",
            f"/rest/api/3/screenscheme/{screen_scheme_id}",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None


class AsyncScreenSchemes(AsyncAPIResource):
    """Asynchronous resource for screens.schemes."""

    async def list(
        self,
        *,
        start_at: int | None = None,
        max_results: int | None = None,
        id_: list[str] | None = None,
        expand: str | None = None,
        query_string: str | None = None,
        order_by: str | None = None,
    ) -> PageBeanScreenScheme:
        """Get screen schemes"""
        params = self._client._build_params(
            **{
                "startAt": start_at,
                "maxResults": max_results,
                "id": id_,
                "expand": expand,
                "queryString": query_string,
                "orderBy": order_by,
            }
        )
        resp = await self._client._request("GET", "/rest/api/3/screenscheme", params=params)
        return PageBeanScreenScheme.model_validate(resp.json())

    async def create(self, body: ScreenSchemeDetails) -> ScreenSchemeId:
        """Create screen scheme"""
        resp = await self._client._request(
            "POST",
            "/rest/api/3/screenscheme",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return ScreenSchemeId.model_validate(resp.json())

    async def delete(self, screen_scheme_id: str) -> None:
        """Delete screen scheme"""
        await self._client._request("DELETE", f"/rest/api/3/screenscheme/{screen_scheme_id}")
        return None

    async def update(self, screen_scheme_id: str, body: UpdateScreenSchemeDetails) -> None:
        """Update screen scheme"""
        await self._client._request(
            "PUT",
            f"/rest/api/3/screenscheme/{screen_scheme_id}",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None
