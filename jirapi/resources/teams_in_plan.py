"""Resource classes for the Teams in plan API group."""

from __future__ import annotations

from jirapi._resource import AsyncAPIResource, SyncAPIResource
from jirapi.models import (
    AddAtlassianTeamRequest,
    CreatePlanOnlyTeamRequest,
    GetAtlassianTeamResponse,
    GetPlanOnlyTeamResponse,
    PageWithCursorGetTeamResponseForPage,
)


class TeamsInPlan(SyncAPIResource):
    """Synchronous resource for the Teams in plan API group."""

    def get_teams(
        self, plan_id: str, *, cursor: str | None = None, max_results: int | None = None
    ) -> PageWithCursorGetTeamResponseForPage:
        """Get teams in plan paginated"""
        params = self._client._build_params(**{"cursor": cursor, "maxResults": max_results})
        resp = self._client._request("GET", f"/rest/api/3/plans/plan/{plan_id}/team", params=params)
        return PageWithCursorGetTeamResponseForPage.model_validate(resp.json())

    def add_atlassian_team(self, plan_id: str, body: AddAtlassianTeamRequest) -> None:
        """Add Atlassian team to plan"""
        resp = self._client._request(
            "POST",
            f"/rest/api/3/plans/plan/{plan_id}/team/atlassian",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    def remove_atlassian_team(self, plan_id: str, atlassian_team_id: str) -> None:
        """Remove Atlassian team from plan"""
        resp = self._client._request(
            "DELETE", f"/rest/api/3/plans/plan/{plan_id}/team/atlassian/{atlassian_team_id}"
        )
        return None

    def get_atlassian_team(self, plan_id: str, atlassian_team_id: str) -> GetAtlassianTeamResponse:
        """Get Atlassian team in plan"""
        resp = self._client._request(
            "GET", f"/rest/api/3/plans/plan/{plan_id}/team/atlassian/{atlassian_team_id}"
        )
        return GetAtlassianTeamResponse.model_validate(resp.json())

    def update_atlassian_team(self, plan_id: str, atlassian_team_id: str) -> None:
        """Update Atlassian team in plan"""
        resp = self._client._request(
            "PUT", f"/rest/api/3/plans/plan/{plan_id}/team/atlassian/{atlassian_team_id}"
        )
        return None

    def create_plan_only_team(self, plan_id: str, body: CreatePlanOnlyTeamRequest) -> None:
        """Create plan-only team"""
        resp = self._client._request(
            "POST",
            f"/rest/api/3/plans/plan/{plan_id}/team/planonly",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    def delete_plan_only_team(self, plan_id: str, plan_only_team_id: str) -> None:
        """Delete plan-only team"""
        resp = self._client._request(
            "DELETE", f"/rest/api/3/plans/plan/{plan_id}/team/planonly/{plan_only_team_id}"
        )
        return None

    def get_plan_only_team(self, plan_id: str, plan_only_team_id: str) -> GetPlanOnlyTeamResponse:
        """Get plan-only team"""
        resp = self._client._request(
            "GET", f"/rest/api/3/plans/plan/{plan_id}/team/planonly/{plan_only_team_id}"
        )
        return GetPlanOnlyTeamResponse.model_validate(resp.json())

    def update_plan_only_team(self, plan_id: str, plan_only_team_id: str) -> None:
        """Update plan-only team"""
        resp = self._client._request(
            "PUT", f"/rest/api/3/plans/plan/{plan_id}/team/planonly/{plan_only_team_id}"
        )
        return None


class AsyncTeamsInPlan(AsyncAPIResource):
    """Asynchronous resource for the Teams in plan API group."""

    async def get_teams(
        self, plan_id: str, *, cursor: str | None = None, max_results: int | None = None
    ) -> PageWithCursorGetTeamResponseForPage:
        """Get teams in plan paginated"""
        params = self._client._build_params(**{"cursor": cursor, "maxResults": max_results})
        resp = await self._client._request(
            "GET", f"/rest/api/3/plans/plan/{plan_id}/team", params=params
        )
        return PageWithCursorGetTeamResponseForPage.model_validate(resp.json())

    async def add_atlassian_team(self, plan_id: str, body: AddAtlassianTeamRequest) -> None:
        """Add Atlassian team to plan"""
        resp = await self._client._request(
            "POST",
            f"/rest/api/3/plans/plan/{plan_id}/team/atlassian",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    async def remove_atlassian_team(self, plan_id: str, atlassian_team_id: str) -> None:
        """Remove Atlassian team from plan"""
        resp = await self._client._request(
            "DELETE", f"/rest/api/3/plans/plan/{plan_id}/team/atlassian/{atlassian_team_id}"
        )
        return None

    async def get_atlassian_team(
        self, plan_id: str, atlassian_team_id: str
    ) -> GetAtlassianTeamResponse:
        """Get Atlassian team in plan"""
        resp = await self._client._request(
            "GET", f"/rest/api/3/plans/plan/{plan_id}/team/atlassian/{atlassian_team_id}"
        )
        return GetAtlassianTeamResponse.model_validate(resp.json())

    async def update_atlassian_team(self, plan_id: str, atlassian_team_id: str) -> None:
        """Update Atlassian team in plan"""
        resp = await self._client._request(
            "PUT", f"/rest/api/3/plans/plan/{plan_id}/team/atlassian/{atlassian_team_id}"
        )
        return None

    async def create_plan_only_team(self, plan_id: str, body: CreatePlanOnlyTeamRequest) -> None:
        """Create plan-only team"""
        resp = await self._client._request(
            "POST",
            f"/rest/api/3/plans/plan/{plan_id}/team/planonly",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    async def delete_plan_only_team(self, plan_id: str, plan_only_team_id: str) -> None:
        """Delete plan-only team"""
        resp = await self._client._request(
            "DELETE", f"/rest/api/3/plans/plan/{plan_id}/team/planonly/{plan_only_team_id}"
        )
        return None

    async def get_plan_only_team(
        self, plan_id: str, plan_only_team_id: str
    ) -> GetPlanOnlyTeamResponse:
        """Get plan-only team"""
        resp = await self._client._request(
            "GET", f"/rest/api/3/plans/plan/{plan_id}/team/planonly/{plan_only_team_id}"
        )
        return GetPlanOnlyTeamResponse.model_validate(resp.json())

    async def update_plan_only_team(self, plan_id: str, plan_only_team_id: str) -> None:
        """Update plan-only team"""
        resp = await self._client._request(
            "PUT", f"/rest/api/3/plans/plan/{plan_id}/team/planonly/{plan_only_team_id}"
        )
        return None
