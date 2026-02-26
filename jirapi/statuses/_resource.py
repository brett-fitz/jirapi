"""Resource classes for statuses."""

from __future__ import annotations

from jirapi._resource import AsyncAPIResource, SyncAPIResource
from jirapi.models import (
    JiraStatus,
    PageOfStatuses,
    StatusCreateRequest,
    StatusProjectIssueTypeUsageDTO,
    StatusProjectUsageDTO,
    StatusUpdateRequest,
    StatusWorkflowUsageDTO,
)


class Statuses(SyncAPIResource):
    """Synchronous resource for statuses."""

    def delete_by_id(self, *, id_: list[str]) -> None:
        """Bulk delete Statuses"""
        params = self._client._build_params(**{"id": id_})
        self._client._request("DELETE", "/rest/api/3/statuses", params=params)
        return None

    def get_by_id(self, *, id_: list[str]) -> JiraStatus:
        """Bulk get statuses"""
        params = self._client._build_params(**{"id": id_})
        resp = self._client._request("GET", "/rest/api/3/statuses", params=params)
        return JiraStatus.model_validate(resp.json())

    def create(self, body: StatusCreateRequest) -> JiraStatus:
        """Bulk create statuses"""
        resp = self._client._request(
            "POST", "/rest/api/3/statuses", json=body.model_dump(by_alias=True, exclude_none=True)
        )
        return JiraStatus.model_validate(resp.json())

    def update(self, body: StatusUpdateRequest) -> None:
        """Bulk update statuses"""
        self._client._request(
            "PUT", "/rest/api/3/statuses", json=body.model_dump(by_alias=True, exclude_none=True)
        )
        return None

    def get_by_name(self, *, name: list[str], project_id: str | None = None) -> JiraStatus:
        """Bulk get statuses by name"""
        params = self._client._build_params(**{"name": name, "projectId": project_id})
        resp = self._client._request("GET", "/rest/api/3/statuses/byNames", params=params)
        return JiraStatus.model_validate(resp.json())

    def search(
        self,
        *,
        project_id: str | None = None,
        start_at: int | None = None,
        max_results: int | None = None,
        search_string: str | None = None,
        status_category: str | None = None,
    ) -> PageOfStatuses:
        """Search statuses paginated"""
        params = self._client._build_params(
            **{
                "projectId": project_id,
                "startAt": start_at,
                "maxResults": max_results,
                "searchString": search_string,
                "statusCategory": status_category,
            }
        )
        resp = self._client._request("GET", "/rest/api/3/statuses/search", params=params)
        return PageOfStatuses.model_validate(resp.json())

    def get_project_issue_type_usages(
        self,
        status_id: str,
        project_id: str,
        *,
        next_page_token: str | None = None,
        max_results: int | None = None,
    ) -> StatusProjectIssueTypeUsageDTO:
        """Get issue type usages by status and project"""
        params = self._client._build_params(
            **{"nextPageToken": next_page_token, "maxResults": max_results}
        )
        resp = self._client._request(
            "GET",
            f"/rest/api/3/statuses/{status_id}/project/{project_id}/issueTypeUsages",
            params=params,
        )
        return StatusProjectIssueTypeUsageDTO.model_validate(resp.json())

    def get_project_usages(
        self, status_id: str, *, next_page_token: str | None = None, max_results: int | None = None
    ) -> StatusProjectUsageDTO:
        """Get project usages by status"""
        params = self._client._build_params(
            **{"nextPageToken": next_page_token, "maxResults": max_results}
        )
        resp = self._client._request(
            "GET", f"/rest/api/3/statuses/{status_id}/projectUsages", params=params
        )
        return StatusProjectUsageDTO.model_validate(resp.json())

    def get_workflow_usages(
        self, status_id: str, *, next_page_token: str | None = None, max_results: int | None = None
    ) -> StatusWorkflowUsageDTO:
        """Get workflow usages by status"""
        params = self._client._build_params(
            **{"nextPageToken": next_page_token, "maxResults": max_results}
        )
        resp = self._client._request(
            "GET", f"/rest/api/3/statuses/{status_id}/workflowUsages", params=params
        )
        return StatusWorkflowUsageDTO.model_validate(resp.json())


class AsyncStatuses(AsyncAPIResource):
    """Asynchronous resource for statuses."""

    async def delete_by_id(self, *, id_: list[str]) -> None:
        """Bulk delete Statuses"""
        params = self._client._build_params(**{"id": id_})
        await self._client._request("DELETE", "/rest/api/3/statuses", params=params)
        return None

    async def get_by_id(self, *, id_: list[str]) -> JiraStatus:
        """Bulk get statuses"""
        params = self._client._build_params(**{"id": id_})
        resp = await self._client._request("GET", "/rest/api/3/statuses", params=params)
        return JiraStatus.model_validate(resp.json())

    async def create(self, body: StatusCreateRequest) -> JiraStatus:
        """Bulk create statuses"""
        resp = await self._client._request(
            "POST", "/rest/api/3/statuses", json=body.model_dump(by_alias=True, exclude_none=True)
        )
        return JiraStatus.model_validate(resp.json())

    async def update(self, body: StatusUpdateRequest) -> None:
        """Bulk update statuses"""
        await self._client._request(
            "PUT", "/rest/api/3/statuses", json=body.model_dump(by_alias=True, exclude_none=True)
        )
        return None

    async def get_by_name(self, *, name: list[str], project_id: str | None = None) -> JiraStatus:
        """Bulk get statuses by name"""
        params = self._client._build_params(**{"name": name, "projectId": project_id})
        resp = await self._client._request("GET", "/rest/api/3/statuses/byNames", params=params)
        return JiraStatus.model_validate(resp.json())

    async def search(
        self,
        *,
        project_id: str | None = None,
        start_at: int | None = None,
        max_results: int | None = None,
        search_string: str | None = None,
        status_category: str | None = None,
    ) -> PageOfStatuses:
        """Search statuses paginated"""
        params = self._client._build_params(
            **{
                "projectId": project_id,
                "startAt": start_at,
                "maxResults": max_results,
                "searchString": search_string,
                "statusCategory": status_category,
            }
        )
        resp = await self._client._request("GET", "/rest/api/3/statuses/search", params=params)
        return PageOfStatuses.model_validate(resp.json())

    async def get_project_issue_type_usages(
        self,
        status_id: str,
        project_id: str,
        *,
        next_page_token: str | None = None,
        max_results: int | None = None,
    ) -> StatusProjectIssueTypeUsageDTO:
        """Get issue type usages by status and project"""
        params = self._client._build_params(
            **{"nextPageToken": next_page_token, "maxResults": max_results}
        )
        resp = await self._client._request(
            "GET",
            f"/rest/api/3/statuses/{status_id}/project/{project_id}/issueTypeUsages",
            params=params,
        )
        return StatusProjectIssueTypeUsageDTO.model_validate(resp.json())

    async def get_project_usages(
        self, status_id: str, *, next_page_token: str | None = None, max_results: int | None = None
    ) -> StatusProjectUsageDTO:
        """Get project usages by status"""
        params = self._client._build_params(
            **{"nextPageToken": next_page_token, "maxResults": max_results}
        )
        resp = await self._client._request(
            "GET", f"/rest/api/3/statuses/{status_id}/projectUsages", params=params
        )
        return StatusProjectUsageDTO.model_validate(resp.json())

    async def get_workflow_usages(
        self, status_id: str, *, next_page_token: str | None = None, max_results: int | None = None
    ) -> StatusWorkflowUsageDTO:
        """Get workflow usages by status"""
        params = self._client._build_params(
            **{"nextPageToken": next_page_token, "maxResults": max_results}
        )
        resp = await self._client._request(
            "GET", f"/rest/api/3/statuses/{status_id}/workflowUsages", params=params
        )
        return StatusWorkflowUsageDTO.model_validate(resp.json())
