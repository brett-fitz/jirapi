"""Resource classes for priorities."""

from __future__ import annotations

from jirapi._resource import AsyncAPIResource, SyncAPIResource
from jirapi.models import (
    CreatePrioritySchemeDetails,
    PageBeanPrioritySchemeWithPaginatedPrioritiesAndProjects,
    PageBeanPriorityWithSequence,
    PageBeanProject,
    Priority,
    PrioritySchemeId,
    ReorderIssuePriorities,
    SetDefaultPriorityRequest,
    SuggestedMappingsRequest,
    UpdatePrioritySchemeRequest,
    UpdatePrioritySchemeResponse,
)


class Priorities(SyncAPIResource):
    """Synchronous resource for priorities."""

    def set_default(self, body: SetDefaultPriorityRequest) -> None:
        """Set default priority"""
        self._client._request(
            "PUT",
            "/rest/api/3/priority/default",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    def move(self, body: ReorderIssuePriorities) -> None:
        """Move priorities"""
        self._client._request(
            "PUT",
            "/rest/api/3/priority/move",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    def delete(self, id_: str) -> None:
        """Delete priority"""
        self._client._request("DELETE", f"/rest/api/3/priority/{id_}")
        return None

    def get(self, id_: str) -> Priority:
        """Get priority"""
        resp = self._client._request("GET", f"/rest/api/3/priority/{id_}")
        return Priority.model_validate(resp.json())

    def list_schemes(
        self,
        *,
        start_at: str | None = None,
        max_results: str | None = None,
        priority_id: list[str] | None = None,
        scheme_id: list[str] | None = None,
        scheme_name: str | None = None,
        only_default: bool | None = None,
        order_by: str | None = None,
        expand: str | None = None,
    ) -> PageBeanPrioritySchemeWithPaginatedPrioritiesAndProjects:
        """Get priority schemes"""
        params = self._client._build_params(
            **{
                "startAt": start_at,
                "maxResults": max_results,
                "priorityId": priority_id,
                "schemeId": scheme_id,
                "schemeName": scheme_name,
                "onlyDefault": only_default,
                "orderBy": order_by,
                "expand": expand,
            }
        )
        resp = self._client._request("GET", "/rest/api/3/priorityscheme", params=params)
        return PageBeanPrioritySchemeWithPaginatedPrioritiesAndProjects.model_validate(resp.json())

    def create_scheme(self, body: CreatePrioritySchemeDetails) -> PrioritySchemeId:
        """Create priority scheme"""
        resp = self._client._request(
            "POST",
            "/rest/api/3/priorityscheme",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return PrioritySchemeId.model_validate(resp.json())

    def get_suggested_for_mappings(
        self, body: SuggestedMappingsRequest
    ) -> PageBeanPriorityWithSequence:
        """Suggested priorities for mappings"""
        resp = self._client._request(
            "POST",
            "/rest/api/3/priorityscheme/mappings",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return PageBeanPriorityWithSequence.model_validate(resp.json())

    def get_available_by_scheme(
        self,
        *,
        start_at: str | None = None,
        max_results: str | None = None,
        query: str | None = None,
        scheme_id: str,
        exclude: list[str] | None = None,
    ) -> PageBeanPriorityWithSequence:
        """Get available priorities by priority scheme"""
        params = self._client._build_params(
            **{
                "startAt": start_at,
                "maxResults": max_results,
                "query": query,
                "schemeId": scheme_id,
                "exclude": exclude,
            }
        )
        resp = self._client._request(
            "GET", "/rest/api/3/priorityscheme/priorities/available", params=params
        )
        return PageBeanPriorityWithSequence.model_validate(resp.json())

    def delete_scheme(self, scheme_id: str) -> None:
        """Delete priority scheme"""
        self._client._request("DELETE", f"/rest/api/3/priorityscheme/{scheme_id}")
        return None

    def update_scheme(
        self, scheme_id: str, body: UpdatePrioritySchemeRequest
    ) -> UpdatePrioritySchemeResponse:
        """Update priority scheme"""
        resp = self._client._request(
            "PUT",
            f"/rest/api/3/priorityscheme/{scheme_id}",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return UpdatePrioritySchemeResponse.model_validate(resp.json())

    def get_by_scheme(
        self, scheme_id: str, *, start_at: str | None = None, max_results: str | None = None
    ) -> PageBeanPriorityWithSequence:
        """Get priorities by priority scheme"""
        params = self._client._build_params(**{"startAt": start_at, "maxResults": max_results})
        resp = self._client._request(
            "GET", f"/rest/api/3/priorityscheme/{scheme_id}/priorities", params=params
        )
        return PageBeanPriorityWithSequence.model_validate(resp.json())

    def get_projects_by_scheme(
        self,
        scheme_id: str,
        *,
        start_at: str | None = None,
        max_results: str | None = None,
        project_id: list[str] | None = None,
        query: str | None = None,
    ) -> PageBeanProject:
        """Get projects by priority scheme"""
        params = self._client._build_params(
            **{
                "startAt": start_at,
                "maxResults": max_results,
                "projectId": project_id,
                "query": query,
            }
        )
        resp = self._client._request(
            "GET", f"/rest/api/3/priorityscheme/{scheme_id}/projects", params=params
        )
        return PageBeanProject.model_validate(resp.json())


class AsyncPriorities(AsyncAPIResource):
    """Asynchronous resource for priorities."""

    async def set_default(self, body: SetDefaultPriorityRequest) -> None:
        """Set default priority"""
        await self._client._request(
            "PUT",
            "/rest/api/3/priority/default",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    async def move(self, body: ReorderIssuePriorities) -> None:
        """Move priorities"""
        await self._client._request(
            "PUT",
            "/rest/api/3/priority/move",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    async def delete(self, id_: str) -> None:
        """Delete priority"""
        await self._client._request("DELETE", f"/rest/api/3/priority/{id_}")
        return None

    async def get(self, id_: str) -> Priority:
        """Get priority"""
        resp = await self._client._request("GET", f"/rest/api/3/priority/{id_}")
        return Priority.model_validate(resp.json())

    async def list_schemes(
        self,
        *,
        start_at: str | None = None,
        max_results: str | None = None,
        priority_id: list[str] | None = None,
        scheme_id: list[str] | None = None,
        scheme_name: str | None = None,
        only_default: bool | None = None,
        order_by: str | None = None,
        expand: str | None = None,
    ) -> PageBeanPrioritySchemeWithPaginatedPrioritiesAndProjects:
        """Get priority schemes"""
        params = self._client._build_params(
            **{
                "startAt": start_at,
                "maxResults": max_results,
                "priorityId": priority_id,
                "schemeId": scheme_id,
                "schemeName": scheme_name,
                "onlyDefault": only_default,
                "orderBy": order_by,
                "expand": expand,
            }
        )
        resp = await self._client._request("GET", "/rest/api/3/priorityscheme", params=params)
        return PageBeanPrioritySchemeWithPaginatedPrioritiesAndProjects.model_validate(resp.json())

    async def create_scheme(self, body: CreatePrioritySchemeDetails) -> PrioritySchemeId:
        """Create priority scheme"""
        resp = await self._client._request(
            "POST",
            "/rest/api/3/priorityscheme",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return PrioritySchemeId.model_validate(resp.json())

    async def get_suggested_for_mappings(
        self, body: SuggestedMappingsRequest
    ) -> PageBeanPriorityWithSequence:
        """Suggested priorities for mappings"""
        resp = await self._client._request(
            "POST",
            "/rest/api/3/priorityscheme/mappings",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return PageBeanPriorityWithSequence.model_validate(resp.json())

    async def get_available_by_scheme(
        self,
        *,
        start_at: str | None = None,
        max_results: str | None = None,
        query: str | None = None,
        scheme_id: str,
        exclude: list[str] | None = None,
    ) -> PageBeanPriorityWithSequence:
        """Get available priorities by priority scheme"""
        params = self._client._build_params(
            **{
                "startAt": start_at,
                "maxResults": max_results,
                "query": query,
                "schemeId": scheme_id,
                "exclude": exclude,
            }
        )
        resp = await self._client._request(
            "GET", "/rest/api/3/priorityscheme/priorities/available", params=params
        )
        return PageBeanPriorityWithSequence.model_validate(resp.json())

    async def delete_scheme(self, scheme_id: str) -> None:
        """Delete priority scheme"""
        await self._client._request("DELETE", f"/rest/api/3/priorityscheme/{scheme_id}")
        return None

    async def update_scheme(
        self, scheme_id: str, body: UpdatePrioritySchemeRequest
    ) -> UpdatePrioritySchemeResponse:
        """Update priority scheme"""
        resp = await self._client._request(
            "PUT",
            f"/rest/api/3/priorityscheme/{scheme_id}",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return UpdatePrioritySchemeResponse.model_validate(resp.json())

    async def get_by_scheme(
        self, scheme_id: str, *, start_at: str | None = None, max_results: str | None = None
    ) -> PageBeanPriorityWithSequence:
        """Get priorities by priority scheme"""
        params = self._client._build_params(**{"startAt": start_at, "maxResults": max_results})
        resp = await self._client._request(
            "GET", f"/rest/api/3/priorityscheme/{scheme_id}/priorities", params=params
        )
        return PageBeanPriorityWithSequence.model_validate(resp.json())

    async def get_projects_by_scheme(
        self,
        scheme_id: str,
        *,
        start_at: str | None = None,
        max_results: str | None = None,
        project_id: list[str] | None = None,
        query: str | None = None,
    ) -> PageBeanProject:
        """Get projects by priority scheme"""
        params = self._client._build_params(
            **{
                "startAt": start_at,
                "maxResults": max_results,
                "projectId": project_id,
                "query": query,
            }
        )
        resp = await self._client._request(
            "GET", f"/rest/api/3/priorityscheme/{scheme_id}/projects", params=params
        )
        return PageBeanProject.model_validate(resp.json())
