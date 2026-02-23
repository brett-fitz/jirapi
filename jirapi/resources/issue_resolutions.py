"""Resource classes for the Issue resolutions API group."""

from __future__ import annotations

from jirapi._resource import AsyncAPIResource, SyncAPIResource
from jirapi.models import (
    CreateResolutionDetails,
    PageBeanResolutionJsonBean,
    ReorderIssueResolutionsRequest,
    Resolution,
    ResolutionId,
    SetDefaultResolutionRequest,
    UpdateResolutionDetails,
)


class IssueResolutions(SyncAPIResource):
    """Synchronous resource for the Issue resolutions API group."""

    def create_resolution(self, body: CreateResolutionDetails) -> ResolutionId:
        """Create resolution"""
        resp = self._client._request(
            "POST", "/rest/api/3/resolution", json=body.model_dump(by_alias=True, exclude_none=True)
        )
        return ResolutionId.model_validate(resp.json())

    def set_default_resolution(self, body: SetDefaultResolutionRequest) -> None:
        """Set default resolution"""
        self._client._request(
            "PUT",
            "/rest/api/3/resolution/default",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    def move_resolutions(self, body: ReorderIssueResolutionsRequest) -> None:
        """Move resolutions"""
        self._client._request(
            "PUT",
            "/rest/api/3/resolution/move",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    def search_resolutions(
        self,
        *,
        start_at: str | None = None,
        max_results: str | None = None,
        id_: list[str] | None = None,
        only_default: bool | None = None,
    ) -> PageBeanResolutionJsonBean:
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
        return PageBeanResolutionJsonBean.model_validate(resp.json())

    def delete_resolution(self, id_: str, *, replace_with: str) -> None:
        """Delete resolution"""
        params = self._client._build_params(**{"replaceWith": replace_with})
        self._client._request("DELETE", f"/rest/api/3/resolution/{id_}", params=params)
        return None

    def get_resolution(self, id_: str) -> Resolution:
        """Get resolution"""
        resp = self._client._request("GET", f"/rest/api/3/resolution/{id_}")
        return Resolution.model_validate(resp.json())

    def update_resolution(self, id_: str, body: UpdateResolutionDetails) -> None:
        """Update resolution"""
        self._client._request(
            "PUT",
            f"/rest/api/3/resolution/{id_}",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None


class AsyncIssueResolutions(AsyncAPIResource):
    """Asynchronous resource for the Issue resolutions API group."""

    async def create_resolution(self, body: CreateResolutionDetails) -> ResolutionId:
        """Create resolution"""
        resp = await self._client._request(
            "POST", "/rest/api/3/resolution", json=body.model_dump(by_alias=True, exclude_none=True)
        )
        return ResolutionId.model_validate(resp.json())

    async def set_default_resolution(self, body: SetDefaultResolutionRequest) -> None:
        """Set default resolution"""
        await self._client._request(
            "PUT",
            "/rest/api/3/resolution/default",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    async def move_resolutions(self, body: ReorderIssueResolutionsRequest) -> None:
        """Move resolutions"""
        await self._client._request(
            "PUT",
            "/rest/api/3/resolution/move",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    async def search_resolutions(
        self,
        *,
        start_at: str | None = None,
        max_results: str | None = None,
        id_: list[str] | None = None,
        only_default: bool | None = None,
    ) -> PageBeanResolutionJsonBean:
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
        return PageBeanResolutionJsonBean.model_validate(resp.json())

    async def delete_resolution(self, id_: str, *, replace_with: str) -> None:
        """Delete resolution"""
        params = self._client._build_params(**{"replaceWith": replace_with})
        await self._client._request("DELETE", f"/rest/api/3/resolution/{id_}", params=params)
        return None

    async def get_resolution(self, id_: str) -> Resolution:
        """Get resolution"""
        resp = await self._client._request("GET", f"/rest/api/3/resolution/{id_}")
        return Resolution.model_validate(resp.json())

    async def update_resolution(self, id_: str, body: UpdateResolutionDetails) -> None:
        """Update resolution"""
        await self._client._request(
            "PUT",
            f"/rest/api/3/resolution/{id_}",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None
