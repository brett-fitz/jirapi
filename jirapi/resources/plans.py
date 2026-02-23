"""Resource classes for the Plans API group."""

from __future__ import annotations

from jirapi._resource import AsyncAPIResource, SyncAPIResource
from jirapi.models import (
    CreatePlanRequest,
    DuplicatePlanRequest,
    GetPlanResponse,
    PageWithCursorGetPlanResponseForPage,
)


class Plans(SyncAPIResource):
    """Synchronous resource for the Plans API group."""

    def get_plans(
        self,
        *,
        include_trashed: bool | None = None,
        include_archived: bool | None = None,
        cursor: str | None = None,
        max_results: int | None = None,
    ) -> PageWithCursorGetPlanResponseForPage:
        """Get plans paginated"""
        params = self._client._build_params(
            **{
                "includeTrashed": include_trashed,
                "includeArchived": include_archived,
                "cursor": cursor,
                "maxResults": max_results,
            }
        )
        resp = self._client._request("GET", "/rest/api/3/plans/plan", params=params)
        return PageWithCursorGetPlanResponseForPage.model_validate(resp.json())

    def create_plan(self, body: CreatePlanRequest, *, use_group_id: bool | None = None) -> None:
        """Create plan"""
        params = self._client._build_params(**{"useGroupId": use_group_id})
        resp = self._client._request(
            "POST",
            "/rest/api/3/plans/plan",
            params=params,
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    def get_plan(self, plan_id: str, *, use_group_id: bool | None = None) -> GetPlanResponse:
        """Get plan"""
        params = self._client._build_params(**{"useGroupId": use_group_id})
        resp = self._client._request("GET", f"/rest/api/3/plans/plan/{plan_id}", params=params)
        return GetPlanResponse.model_validate(resp.json())

    def update_plan(self, plan_id: str, *, use_group_id: bool | None = None) -> None:
        """Update plan"""
        params = self._client._build_params(**{"useGroupId": use_group_id})
        resp = self._client._request("PUT", f"/rest/api/3/plans/plan/{plan_id}", params=params)
        return None

    def archive_plan(self, plan_id: str) -> None:
        """Archive plan"""
        resp = self._client._request("PUT", f"/rest/api/3/plans/plan/{plan_id}/archive")
        return None

    def duplicate_plan(self, plan_id: str, body: DuplicatePlanRequest) -> None:
        """Duplicate plan"""
        resp = self._client._request(
            "POST",
            f"/rest/api/3/plans/plan/{plan_id}/duplicate",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    def trash_plan(self, plan_id: str) -> None:
        """Trash plan"""
        resp = self._client._request("PUT", f"/rest/api/3/plans/plan/{plan_id}/trash")
        return None


class AsyncPlans(AsyncAPIResource):
    """Asynchronous resource for the Plans API group."""

    async def get_plans(
        self,
        *,
        include_trashed: bool | None = None,
        include_archived: bool | None = None,
        cursor: str | None = None,
        max_results: int | None = None,
    ) -> PageWithCursorGetPlanResponseForPage:
        """Get plans paginated"""
        params = self._client._build_params(
            **{
                "includeTrashed": include_trashed,
                "includeArchived": include_archived,
                "cursor": cursor,
                "maxResults": max_results,
            }
        )
        resp = await self._client._request("GET", "/rest/api/3/plans/plan", params=params)
        return PageWithCursorGetPlanResponseForPage.model_validate(resp.json())

    async def create_plan(
        self, body: CreatePlanRequest, *, use_group_id: bool | None = None
    ) -> None:
        """Create plan"""
        params = self._client._build_params(**{"useGroupId": use_group_id})
        resp = await self._client._request(
            "POST",
            "/rest/api/3/plans/plan",
            params=params,
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    async def get_plan(self, plan_id: str, *, use_group_id: bool | None = None) -> GetPlanResponse:
        """Get plan"""
        params = self._client._build_params(**{"useGroupId": use_group_id})
        resp = await self._client._request(
            "GET", f"/rest/api/3/plans/plan/{plan_id}", params=params
        )
        return GetPlanResponse.model_validate(resp.json())

    async def update_plan(self, plan_id: str, *, use_group_id: bool | None = None) -> None:
        """Update plan"""
        params = self._client._build_params(**{"useGroupId": use_group_id})
        resp = await self._client._request(
            "PUT", f"/rest/api/3/plans/plan/{plan_id}", params=params
        )
        return None

    async def archive_plan(self, plan_id: str) -> None:
        """Archive plan"""
        resp = await self._client._request("PUT", f"/rest/api/3/plans/plan/{plan_id}/archive")
        return None

    async def duplicate_plan(self, plan_id: str, body: DuplicatePlanRequest) -> None:
        """Duplicate plan"""
        resp = await self._client._request(
            "POST",
            f"/rest/api/3/plans/plan/{plan_id}/duplicate",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    async def trash_plan(self, plan_id: str) -> None:
        """Trash plan"""
        resp = await self._client._request("PUT", f"/rest/api/3/plans/plan/{plan_id}/trash")
        return None
