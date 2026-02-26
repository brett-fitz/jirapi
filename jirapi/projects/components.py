"""Resource classes for projects.components."""

from __future__ import annotations

from jirapi._resource import AsyncAPIResource, SyncAPIResource
from jirapi.models import (
    ComponentIssuesCount,
    PageBean2ComponentJson,
    PageBeanComponentWithIssueCount,
    ProjectComponent,
)


class ProjectComponents(SyncAPIResource):
    """Synchronous resource for projects.components."""

    def find_for_projects(
        self,
        *,
        project_ids_or_keys: list[str] | None = None,
        start_at: int | None = None,
        max_results: int | None = None,
        order_by: str | None = None,
        query: str | None = None,
    ) -> PageBean2ComponentJson:
        """Find components for projects"""
        params = self._client._build_params(
            **{
                "projectIdsOrKeys": project_ids_or_keys,
                "startAt": start_at,
                "maxResults": max_results,
                "orderBy": order_by,
                "query": query,
            }
        )
        resp = self._client._request("GET", "/rest/api/3/component", params=params)
        return PageBean2ComponentJson.model_validate(resp.json())

    def create(self, body: ProjectComponent) -> ProjectComponent:
        """Create component"""
        resp = self._client._request(
            "POST", "/rest/api/3/component", json=body.model_dump(by_alias=True, exclude_none=True)
        )
        return ProjectComponent.model_validate(resp.json())

    def delete(self, id_: str, *, move_issues_to: str | None = None) -> None:
        """Delete component"""
        params = self._client._build_params(**{"moveIssuesTo": move_issues_to})
        self._client._request("DELETE", f"/rest/api/3/component/{id_}", params=params)
        return None

    def get(self, id_: str) -> ProjectComponent:
        """Get component"""
        resp = self._client._request("GET", f"/rest/api/3/component/{id_}")
        return ProjectComponent.model_validate(resp.json())

    def update(self, id_: str, body: ProjectComponent) -> ProjectComponent:
        """Update component"""
        resp = self._client._request(
            "PUT",
            f"/rest/api/3/component/{id_}",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return ProjectComponent.model_validate(resp.json())

    def get_related_issues(self, id_: str) -> ComponentIssuesCount:
        """Get component issues count"""
        resp = self._client._request("GET", f"/rest/api/3/component/{id_}/relatedIssueCounts")
        return ComponentIssuesCount.model_validate(resp.json())

    def list(
        self,
        project_id_or_key: str,
        *,
        start_at: int | None = None,
        max_results: int | None = None,
        order_by: str | None = None,
        component_source: str | None = None,
        query: str | None = None,
    ) -> PageBeanComponentWithIssueCount:
        """Get project components paginated"""
        params = self._client._build_params(
            **{
                "startAt": start_at,
                "maxResults": max_results,
                "orderBy": order_by,
                "componentSource": component_source,
                "query": query,
            }
        )
        resp = self._client._request(
            "GET", f"/rest/api/3/project/{project_id_or_key}/component", params=params
        )
        return PageBeanComponentWithIssueCount.model_validate(resp.json())

    def list_all(
        self, project_id_or_key: str, *, component_source: str | None = None
    ) -> ProjectComponent:
        """Get project components"""
        params = self._client._build_params(**{"componentSource": component_source})
        resp = self._client._request(
            "GET", f"/rest/api/3/project/{project_id_or_key}/components", params=params
        )
        return ProjectComponent.model_validate(resp.json())


class AsyncProjectComponents(AsyncAPIResource):
    """Asynchronous resource for projects.components."""

    async def find_for_projects(
        self,
        *,
        project_ids_or_keys: list[str] | None = None,
        start_at: int | None = None,
        max_results: int | None = None,
        order_by: str | None = None,
        query: str | None = None,
    ) -> PageBean2ComponentJson:
        """Find components for projects"""
        params = self._client._build_params(
            **{
                "projectIdsOrKeys": project_ids_or_keys,
                "startAt": start_at,
                "maxResults": max_results,
                "orderBy": order_by,
                "query": query,
            }
        )
        resp = await self._client._request("GET", "/rest/api/3/component", params=params)
        return PageBean2ComponentJson.model_validate(resp.json())

    async def create(self, body: ProjectComponent) -> ProjectComponent:
        """Create component"""
        resp = await self._client._request(
            "POST", "/rest/api/3/component", json=body.model_dump(by_alias=True, exclude_none=True)
        )
        return ProjectComponent.model_validate(resp.json())

    async def delete(self, id_: str, *, move_issues_to: str | None = None) -> None:
        """Delete component"""
        params = self._client._build_params(**{"moveIssuesTo": move_issues_to})
        await self._client._request("DELETE", f"/rest/api/3/component/{id_}", params=params)
        return None

    async def get(self, id_: str) -> ProjectComponent:
        """Get component"""
        resp = await self._client._request("GET", f"/rest/api/3/component/{id_}")
        return ProjectComponent.model_validate(resp.json())

    async def update(self, id_: str, body: ProjectComponent) -> ProjectComponent:
        """Update component"""
        resp = await self._client._request(
            "PUT",
            f"/rest/api/3/component/{id_}",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return ProjectComponent.model_validate(resp.json())

    async def get_related_issues(self, id_: str) -> ComponentIssuesCount:
        """Get component issues count"""
        resp = await self._client._request("GET", f"/rest/api/3/component/{id_}/relatedIssueCounts")
        return ComponentIssuesCount.model_validate(resp.json())

    async def list(
        self,
        project_id_or_key: str,
        *,
        start_at: int | None = None,
        max_results: int | None = None,
        order_by: str | None = None,
        component_source: str | None = None,
        query: str | None = None,
    ) -> PageBeanComponentWithIssueCount:
        """Get project components paginated"""
        params = self._client._build_params(
            **{
                "startAt": start_at,
                "maxResults": max_results,
                "orderBy": order_by,
                "componentSource": component_source,
                "query": query,
            }
        )
        resp = await self._client._request(
            "GET", f"/rest/api/3/project/{project_id_or_key}/component", params=params
        )
        return PageBeanComponentWithIssueCount.model_validate(resp.json())

    async def list_all(
        self, project_id_or_key: str, *, component_source: str | None = None
    ) -> ProjectComponent:
        """Get project components"""
        params = self._client._build_params(**{"componentSource": component_source})
        resp = await self._client._request(
            "GET", f"/rest/api/3/project/{project_id_or_key}/components", params=params
        )
        return ProjectComponent.model_validate(resp.json())
