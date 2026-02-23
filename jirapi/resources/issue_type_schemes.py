"""Resource classes for the Issue type schemes API group."""

from __future__ import annotations

from jirapi._resource import AsyncAPIResource, SyncAPIResource
from jirapi.models import (
    IssueTypeIds,
    IssueTypeSchemeDetails,
    IssueTypeSchemeID,
    IssueTypeSchemeProjectAssociation,
    IssueTypeSchemeUpdateDetails,
    OrderOfIssueTypes,
    PageBeanIssueTypeScheme,
    PageBeanIssueTypeSchemeMapping,
    PageBeanIssueTypeSchemeProjects,
)


class IssueTypeSchemes(SyncAPIResource):
    """Synchronous resource for the Issue type schemes API group."""

    def get_all_issue_type_schemes(
        self,
        *,
        start_at: int | None = None,
        max_results: int | None = None,
        id_: list[str] | None = None,
        order_by: str | None = None,
        expand: str | None = None,
        query_string: str | None = None,
    ) -> PageBeanIssueTypeScheme:
        """Get all issue type schemes"""
        params = self._client._build_params(
            **{
                "startAt": start_at,
                "maxResults": max_results,
                "id": id_,
                "orderBy": order_by,
                "expand": expand,
                "queryString": query_string,
            }
        )
        resp = self._client._request("GET", "/rest/api/3/issuetypescheme", params=params)
        return PageBeanIssueTypeScheme.model_validate(resp.json())

    def create_issue_type_scheme(self, body: IssueTypeSchemeDetails) -> IssueTypeSchemeID:
        """Create issue type scheme"""
        resp = self._client._request(
            "POST",
            "/rest/api/3/issuetypescheme",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return IssueTypeSchemeID.model_validate(resp.json())

    def get_issue_type_schemes_mapping(
        self,
        *,
        start_at: int | None = None,
        max_results: int | None = None,
        issue_type_scheme_id: list[str] | None = None,
    ) -> PageBeanIssueTypeSchemeMapping:
        """Get issue type scheme items"""
        params = self._client._build_params(
            **{
                "startAt": start_at,
                "maxResults": max_results,
                "issueTypeSchemeId": issue_type_scheme_id,
            }
        )
        resp = self._client._request("GET", "/rest/api/3/issuetypescheme/mapping", params=params)
        return PageBeanIssueTypeSchemeMapping.model_validate(resp.json())

    def get_issue_type_scheme_for_projects(
        self, *, start_at: int | None = None, max_results: int | None = None, project_id: list[str]
    ) -> PageBeanIssueTypeSchemeProjects:
        """Get issue type schemes for projects"""
        params = self._client._build_params(
            **{"startAt": start_at, "maxResults": max_results, "projectId": project_id}
        )
        resp = self._client._request("GET", "/rest/api/3/issuetypescheme/project", params=params)
        return PageBeanIssueTypeSchemeProjects.model_validate(resp.json())

    def assign_issue_type_scheme_to_project(self, body: IssueTypeSchemeProjectAssociation) -> None:
        """Assign issue type scheme to project"""
        resp = self._client._request(
            "PUT",
            "/rest/api/3/issuetypescheme/project",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    def delete_issue_type_scheme(self, issue_type_scheme_id: str) -> None:
        """Delete issue type scheme"""
        resp = self._client._request(
            "DELETE", f"/rest/api/3/issuetypescheme/{issue_type_scheme_id}"
        )
        return None

    def update_issue_type_scheme(
        self, issue_type_scheme_id: str, body: IssueTypeSchemeUpdateDetails
    ) -> None:
        """Update issue type scheme"""
        resp = self._client._request(
            "PUT",
            f"/rest/api/3/issuetypescheme/{issue_type_scheme_id}",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    def add_issue_types_to_issue_type_scheme(
        self, issue_type_scheme_id: str, body: IssueTypeIds
    ) -> None:
        """Add issue types to issue type scheme"""
        resp = self._client._request(
            "PUT",
            f"/rest/api/3/issuetypescheme/{issue_type_scheme_id}/issuetype",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    def reorder_issue_types_in_issue_type_scheme(
        self, issue_type_scheme_id: str, body: OrderOfIssueTypes
    ) -> None:
        """Change order of issue types"""
        resp = self._client._request(
            "PUT",
            f"/rest/api/3/issuetypescheme/{issue_type_scheme_id}/issuetype/move",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    def remove_issue_type_from_issue_type_scheme(
        self, issue_type_scheme_id: str, issue_type_id: str
    ) -> None:
        """Remove issue type from issue type scheme"""
        resp = self._client._request(
            "DELETE",
            f"/rest/api/3/issuetypescheme/{issue_type_scheme_id}/issuetype/{issue_type_id}",
        )
        return None


class AsyncIssueTypeSchemes(AsyncAPIResource):
    """Asynchronous resource for the Issue type schemes API group."""

    async def get_all_issue_type_schemes(
        self,
        *,
        start_at: int | None = None,
        max_results: int | None = None,
        id_: list[str] | None = None,
        order_by: str | None = None,
        expand: str | None = None,
        query_string: str | None = None,
    ) -> PageBeanIssueTypeScheme:
        """Get all issue type schemes"""
        params = self._client._build_params(
            **{
                "startAt": start_at,
                "maxResults": max_results,
                "id": id_,
                "orderBy": order_by,
                "expand": expand,
                "queryString": query_string,
            }
        )
        resp = await self._client._request("GET", "/rest/api/3/issuetypescheme", params=params)
        return PageBeanIssueTypeScheme.model_validate(resp.json())

    async def create_issue_type_scheme(self, body: IssueTypeSchemeDetails) -> IssueTypeSchemeID:
        """Create issue type scheme"""
        resp = await self._client._request(
            "POST",
            "/rest/api/3/issuetypescheme",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return IssueTypeSchemeID.model_validate(resp.json())

    async def get_issue_type_schemes_mapping(
        self,
        *,
        start_at: int | None = None,
        max_results: int | None = None,
        issue_type_scheme_id: list[str] | None = None,
    ) -> PageBeanIssueTypeSchemeMapping:
        """Get issue type scheme items"""
        params = self._client._build_params(
            **{
                "startAt": start_at,
                "maxResults": max_results,
                "issueTypeSchemeId": issue_type_scheme_id,
            }
        )
        resp = await self._client._request(
            "GET", "/rest/api/3/issuetypescheme/mapping", params=params
        )
        return PageBeanIssueTypeSchemeMapping.model_validate(resp.json())

    async def get_issue_type_scheme_for_projects(
        self, *, start_at: int | None = None, max_results: int | None = None, project_id: list[str]
    ) -> PageBeanIssueTypeSchemeProjects:
        """Get issue type schemes for projects"""
        params = self._client._build_params(
            **{"startAt": start_at, "maxResults": max_results, "projectId": project_id}
        )
        resp = await self._client._request(
            "GET", "/rest/api/3/issuetypescheme/project", params=params
        )
        return PageBeanIssueTypeSchemeProjects.model_validate(resp.json())

    async def assign_issue_type_scheme_to_project(
        self, body: IssueTypeSchemeProjectAssociation
    ) -> None:
        """Assign issue type scheme to project"""
        resp = await self._client._request(
            "PUT",
            "/rest/api/3/issuetypescheme/project",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    async def delete_issue_type_scheme(self, issue_type_scheme_id: str) -> None:
        """Delete issue type scheme"""
        resp = await self._client._request(
            "DELETE", f"/rest/api/3/issuetypescheme/{issue_type_scheme_id}"
        )
        return None

    async def update_issue_type_scheme(
        self, issue_type_scheme_id: str, body: IssueTypeSchemeUpdateDetails
    ) -> None:
        """Update issue type scheme"""
        resp = await self._client._request(
            "PUT",
            f"/rest/api/3/issuetypescheme/{issue_type_scheme_id}",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    async def add_issue_types_to_issue_type_scheme(
        self, issue_type_scheme_id: str, body: IssueTypeIds
    ) -> None:
        """Add issue types to issue type scheme"""
        resp = await self._client._request(
            "PUT",
            f"/rest/api/3/issuetypescheme/{issue_type_scheme_id}/issuetype",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    async def reorder_issue_types_in_issue_type_scheme(
        self, issue_type_scheme_id: str, body: OrderOfIssueTypes
    ) -> None:
        """Change order of issue types"""
        resp = await self._client._request(
            "PUT",
            f"/rest/api/3/issuetypescheme/{issue_type_scheme_id}/issuetype/move",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    async def remove_issue_type_from_issue_type_scheme(
        self, issue_type_scheme_id: str, issue_type_id: str
    ) -> None:
        """Remove issue type from issue type scheme"""
        resp = await self._client._request(
            "DELETE",
            f"/rest/api/3/issuetypescheme/{issue_type_scheme_id}/issuetype/{issue_type_id}",
        )
        return None
