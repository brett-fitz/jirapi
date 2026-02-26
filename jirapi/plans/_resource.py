"""Resource classes for plans."""

from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING

from jirapi._resource import AsyncAPIResource, SyncAPIResource
from jirapi.models import (
    CreatePlanRequest,
    DuplicatePlanRequest,
    GetPlanResponse,
    PageWithCursorGetPlanResponseForPage,
)


if TYPE_CHECKING:
    from jirapi.plans.teams import AsyncPlanTeams, PlanTeams


class Plans(SyncAPIResource):
    """Synchronous resource for plans."""

    @cached_property
    def teams(self) -> PlanTeams:
        from jirapi.plans.teams import PlanTeams

        return PlanTeams(self._client)

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

    def create(self, body: CreatePlanRequest, *, use_group_id: bool | None = None) -> int:
        """Create plan"""
        params = self._client._build_params(**{"useGroupId": use_group_id})
        resp = self._client._request(
            "POST",
            "/rest/api/3/plans/plan",
            params=params,
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return resp.json()

    def get_plan(self, plan_id: str, *, use_group_id: bool | None = None) -> GetPlanResponse:
        """Get plan"""
        params = self._client._build_params(**{"useGroupId": use_group_id})
        resp = self._client._request("GET", f"/rest/api/3/plans/plan/{plan_id}", params=params)
        return GetPlanResponse.model_validate(resp.json())

    def update(self, plan_id: str, *, use_group_id: bool | None = None) -> None:
        """Update plan"""
        params = self._client._build_params(**{"useGroupId": use_group_id})
        self._client._request("PUT", f"/rest/api/3/plans/plan/{plan_id}", params=params)
        return None

    def archive(self, plan_id: str) -> None:
        """Archive plan"""
        self._client._request("PUT", f"/rest/api/3/plans/plan/{plan_id}/archive")
        return None

    def duplicate(self, plan_id: str, body: DuplicatePlanRequest) -> int:
        """Duplicate plan"""
        resp = self._client._request(
            "POST",
            f"/rest/api/3/plans/plan/{plan_id}/duplicate",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return resp.json()

    def trash(self, plan_id: str) -> None:
        """Trash plan"""
        self._client._request("PUT", f"/rest/api/3/plans/plan/{plan_id}/trash")
        return None


class AsyncPlans(AsyncAPIResource):
    """Asynchronous resource for plans."""

    @cached_property
    def teams(self) -> AsyncPlanTeams:
        from jirapi.plans.teams import AsyncPlanTeams

        return AsyncPlanTeams(self._client)

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

    async def create(self, body: CreatePlanRequest, *, use_group_id: bool | None = None) -> int:
        """Create plan"""
        params = self._client._build_params(**{"useGroupId": use_group_id})
        resp = await self._client._request(
            "POST",
            "/rest/api/3/plans/plan",
            params=params,
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return resp.json()

    async def get_plan(self, plan_id: str, *, use_group_id: bool | None = None) -> GetPlanResponse:
        """Get plan"""
        params = self._client._build_params(**{"useGroupId": use_group_id})
        resp = await self._client._request(
            "GET", f"/rest/api/3/plans/plan/{plan_id}", params=params
        )
        return GetPlanResponse.model_validate(resp.json())

    async def update(self, plan_id: str, *, use_group_id: bool | None = None) -> None:
        """Update plan"""
        params = self._client._build_params(**{"useGroupId": use_group_id})
        await self._client._request("PUT", f"/rest/api/3/plans/plan/{plan_id}", params=params)
        return None

    async def archive(self, plan_id: str) -> None:
        """Archive plan"""
        await self._client._request("PUT", f"/rest/api/3/plans/plan/{plan_id}/archive")
        return None

    async def duplicate(self, plan_id: str, body: DuplicatePlanRequest) -> int:
        """Duplicate plan"""
        resp = await self._client._request(
            "POST",
            f"/rest/api/3/plans/plan/{plan_id}/duplicate",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return resp.json()

    async def trash(self, plan_id: str) -> None:
        """Trash plan"""
        await self._client._request("PUT", f"/rest/api/3/plans/plan/{plan_id}/trash")
        return None
