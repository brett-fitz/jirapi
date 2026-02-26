"""Resource classes for resolutions."""

from __future__ import annotations

from jirapi._resource import AsyncAPIResource, SyncAPIResource
from jirapi.models import (
    CreateResolutionDetails,
    PageBeanResolutionJson,
    ReorderIssueResolutionsRequest,
    Resolution,
    ResolutionId,
    SetDefaultResolutionRequest,
    UpdateResolutionDetails,
)


class Resolutions(SyncAPIResource):
    """Synchronous resource for resolutions."""

    def create(self, body: CreateResolutionDetails) -> ResolutionId:
        """Create resolution"""
        resp = self._client._request(
            "POST", "/rest/api/3/resolution", json=body.model_dump(by_alias=True, exclude_none=True)
        )
        return ResolutionId.model_validate(resp.json())

    def set_default(self, body: SetDefaultResolutionRequest) -> None:
        """Set default resolution"""
        self._client._request(
            "PUT",
            "/rest/api/3/resolution/default",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    def move(self, body: ReorderIssueResolutionsRequest) -> None:
        """Move resolutions"""
        self._client._request(
            "PUT",
            "/rest/api/3/resolution/move",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    def search(
        self,
        *,
        start_at: str | None = None,
        max_results: str | None = None,
        id_: list[str] | None = None,
        only_default: bool | None = None,
    ) -> PageBeanResolutionJson:
        """Search resolutions"""
        params = self._client._build_params(
            **{
                "startAt": start_at,
                "maxResults": max_results,
                "id": id_,
                "onlyDefault": only_default,
            }
        )
        resp = self._client._request("GET", "/rest/api/3/resolution/search", params=params)
        return PageBeanResolutionJson.model_validate(resp.json())

    def delete(self, id_: str, *, replace_with: str) -> None:
        """Delete resolution"""
        params = self._client._build_params(**{"replaceWith": replace_with})
        self._client._request("DELETE", f"/rest/api/3/resolution/{id_}", params=params)
        return None

    def get(self, id_: str) -> Resolution:
        """Get resolution"""
        resp = self._client._request("GET", f"/rest/api/3/resolution/{id_}")
        return Resolution.model_validate(resp.json())

    def update(self, id_: str, body: UpdateResolutionDetails) -> None:
        """Update resolution"""
        self._client._request(
            "PUT",
            f"/rest/api/3/resolution/{id_}",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None


class AsyncResolutions(AsyncAPIResource):
    """Asynchronous resource for resolutions."""

    async def create(self, body: CreateResolutionDetails) -> ResolutionId:
        """Create resolution"""
        resp = await self._client._request(
            "POST", "/rest/api/3/resolution", json=body.model_dump(by_alias=True, exclude_none=True)
        )
        return ResolutionId.model_validate(resp.json())

    async def set_default(self, body: SetDefaultResolutionRequest) -> None:
        """Set default resolution"""
        await self._client._request(
            "PUT",
            "/rest/api/3/resolution/default",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    async def move(self, body: ReorderIssueResolutionsRequest) -> None:
        """Move resolutions"""
        await self._client._request(
            "PUT",
            "/rest/api/3/resolution/move",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    async def search(
        self,
        *,
        start_at: str | None = None,
        max_results: str | None = None,
        id_: list[str] | None = None,
        only_default: bool | None = None,
    ) -> PageBeanResolutionJson:
        """Search resolutions"""
        params = self._client._build_params(
            **{
                "startAt": start_at,
                "maxResults": max_results,
                "id": id_,
                "onlyDefault": only_default,
            }
        )
        resp = await self._client._request("GET", "/rest/api/3/resolution/search", params=params)
        return PageBeanResolutionJson.model_validate(resp.json())

    async def delete(self, id_: str, *, replace_with: str) -> None:
        """Delete resolution"""
        params = self._client._build_params(**{"replaceWith": replace_with})
        await self._client._request("DELETE", f"/rest/api/3/resolution/{id_}", params=params)
        return None

    async def get(self, id_: str) -> Resolution:
        """Get resolution"""
        resp = await self._client._request("GET", f"/rest/api/3/resolution/{id_}")
        return Resolution.model_validate(resp.json())

    async def update(self, id_: str, body: UpdateResolutionDetails) -> None:
        """Update resolution"""
        await self._client._request(
            "PUT",
            f"/rest/api/3/resolution/{id_}",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None
