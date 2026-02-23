"""Resource classes for the Priority schemes API group."""

from __future__ import annotations

from jirapi._resource import AsyncAPIResource, SyncAPIResource
from jirapi.models import (
    CreatePrioritySchemeDetails,
    PageBeanPrioritySchemeWithPaginatedPrioritiesAndProjects,
    PageBeanPriorityWithSequence,
    PageBeanProject,
    PrioritySchemeId,
    SuggestedMappingsRequestBean,
    UpdatePrioritySchemeRequestBean,
    UpdatePrioritySchemeResponseBean,
)


class PrioritySchemes(SyncAPIResource):
    """Synchronous resource for the Priority schemes API group."""

    def get_priority_schemes(
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

    def create_priority_scheme(self, body: CreatePrioritySchemeDetails) -> PrioritySchemeId:
        """Create priority scheme"""
        resp = self._client._request(
            "POST",
            "/rest/api/3/priorityscheme",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return PrioritySchemeId.model_validate(resp.json())

    def suggested_priorities_for_mappings(
        self, body: SuggestedMappingsRequestBean
    ) -> PageBeanPriorityWithSequence:
        """Suggested priorities for mappings"""
        resp = self._client._request(
            "POST",
            "/rest/api/3/priorityscheme/mappings",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return PageBeanPriorityWithSequence.model_validate(resp.json())

    def get_available_priorities_by_priority_scheme(
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

    def delete_priority_scheme(self, scheme_id: str) -> None:
        """Delete priority scheme"""
        resp = self._client._request("DELETE", f"/rest/api/3/priorityscheme/{scheme_id}")
        return None

    def update_priority_scheme(
        self, scheme_id: str, body: UpdatePrioritySchemeRequestBean
    ) -> UpdatePrioritySchemeResponseBean:
        """Update priority scheme"""
        resp = self._client._request(
            "PUT",
            f"/rest/api/3/priorityscheme/{scheme_id}",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return UpdatePrioritySchemeResponseBean.model_validate(resp.json())

    def get_priorities_by_priority_scheme(
        self, scheme_id: str, *, start_at: str | None = None, max_results: str | None = None
    ) -> PageBeanPriorityWithSequence:
        """Get priorities by priority scheme"""
        params = self._client._build_params(**{"startAt": start_at, "maxResults": max_results})
        resp = self._client._request(
            "GET", f"/rest/api/3/priorityscheme/{scheme_id}/priorities", params=params
        )
        return PageBeanPriorityWithSequence.model_validate(resp.json())

    def get_projects_by_priority_scheme(
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


class AsyncPrioritySchemes(AsyncAPIResource):
    """Asynchronous resource for the Priority schemes API group."""

    async def get_priority_schemes(
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

    async def create_priority_scheme(self, body: CreatePrioritySchemeDetails) -> PrioritySchemeId:
        """Create priority scheme"""
        resp = await self._client._request(
            "POST",
            "/rest/api/3/priorityscheme",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return PrioritySchemeId.model_validate(resp.json())

    async def suggested_priorities_for_mappings(
        self, body: SuggestedMappingsRequestBean
    ) -> PageBeanPriorityWithSequence:
        """Suggested priorities for mappings"""
        resp = await self._client._request(
            "POST",
            "/rest/api/3/priorityscheme/mappings",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return PageBeanPriorityWithSequence.model_validate(resp.json())

    async def get_available_priorities_by_priority_scheme(
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

    async def delete_priority_scheme(self, scheme_id: str) -> None:
        """Delete priority scheme"""
        resp = await self._client._request("DELETE", f"/rest/api/3/priorityscheme/{scheme_id}")
        return None

    async def update_priority_scheme(
        self, scheme_id: str, body: UpdatePrioritySchemeRequestBean
    ) -> UpdatePrioritySchemeResponseBean:
        """Update priority scheme"""
        resp = await self._client._request(
            "PUT",
            f"/rest/api/3/priorityscheme/{scheme_id}",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return UpdatePrioritySchemeResponseBean.model_validate(resp.json())

    async def get_priorities_by_priority_scheme(
        self, scheme_id: str, *, start_at: str | None = None, max_results: str | None = None
    ) -> PageBeanPriorityWithSequence:
        """Get priorities by priority scheme"""
        params = self._client._build_params(**{"startAt": start_at, "maxResults": max_results})
        resp = await self._client._request(
            "GET", f"/rest/api/3/priorityscheme/{scheme_id}/priorities", params=params
        )
        return PageBeanPriorityWithSequence.model_validate(resp.json())

    async def get_projects_by_priority_scheme(
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
