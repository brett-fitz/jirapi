"""Resource classes for screens.issue_type_screen_schemes."""

from __future__ import annotations

from jirapi._resource import AsyncAPIResource, SyncAPIResource
from jirapi.models import (
    IssueTypeIds,
    IssueTypeScreenSchemeDetails,
    IssueTypeScreenSchemeId,
    IssueTypeScreenSchemeMappingDetails,
    IssueTypeScreenSchemeProjectAssociation,
    IssueTypeScreenSchemeUpdateDetails,
    PageBeanIssueTypeScreenScheme,
    PageBeanIssueTypeScreenSchemeItem,
    PageBeanIssueTypeScreenSchemesProjects,
    PageBeanProjectDetails,
    UpdateDefaultScreenScheme,
)


class ScreenIssueTypeScreenSchemes(SyncAPIResource):
    """Synchronous resource for screens.issue_type_screen_schemes."""

    def list(
        self,
        *,
        start_at: int | None = None,
        max_results: int | None = None,
        id_: list[str] | None = None,
        query_string: str | None = None,
        order_by: str | None = None,
        expand: str | None = None,
    ) -> PageBeanIssueTypeScreenScheme:
        """Get issue type screen schemes"""
        params = self._client._build_params(
            **{
                "startAt": start_at,
                "maxResults": max_results,
                "id": id_,
                "queryString": query_string,
                "orderBy": order_by,
                "expand": expand,
            }
        )
        resp = self._client._request("GET", "/rest/api/3/issuetypescreenscheme", params=params)
        return PageBeanIssueTypeScreenScheme.model_validate(resp.json())

    def create(self, body: IssueTypeScreenSchemeDetails) -> IssueTypeScreenSchemeId:
        """Create issue type screen scheme"""
        resp = self._client._request(
            "POST",
            "/rest/api/3/issuetypescreenscheme",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return IssueTypeScreenSchemeId.model_validate(resp.json())

    def get_mappings(
        self,
        *,
        start_at: int | None = None,
        max_results: int | None = None,
        issue_type_screen_scheme_id: list[str] | None = None,
    ) -> PageBeanIssueTypeScreenSchemeItem:
        """Get issue type screen scheme items"""
        params = self._client._build_params(
            **{
                "startAt": start_at,
                "maxResults": max_results,
                "issueTypeScreenSchemeId": issue_type_screen_scheme_id,
            }
        )
        resp = self._client._request(
            "GET", "/rest/api/3/issuetypescreenscheme/mapping", params=params
        )
        return PageBeanIssueTypeScreenSchemeItem.model_validate(resp.json())

    def get_project_associations(
        self, *, start_at: int | None = None, max_results: int | None = None, project_id: list[str]
    ) -> PageBeanIssueTypeScreenSchemesProjects:
        """Get issue type screen schemes for projects"""
        params = self._client._build_params(
            **{"startAt": start_at, "maxResults": max_results, "projectId": project_id}
        )
        resp = self._client._request(
            "GET", "/rest/api/3/issuetypescreenscheme/project", params=params
        )
        return PageBeanIssueTypeScreenSchemesProjects.model_validate(resp.json())

    def assign_to_project(self, body: IssueTypeScreenSchemeProjectAssociation) -> None:
        """Assign issue type screen scheme to project"""
        self._client._request(
            "PUT",
            "/rest/api/3/issuetypescreenscheme/project",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    def delete(self, issue_type_screen_scheme_id: str) -> None:
        """Delete issue type screen scheme"""
        self._client._request(
            "DELETE", f"/rest/api/3/issuetypescreenscheme/{issue_type_screen_scheme_id}"
        )
        return None

    def update(
        self, issue_type_screen_scheme_id: str, body: IssueTypeScreenSchemeUpdateDetails
    ) -> None:
        """Update issue type screen scheme"""
        self._client._request(
            "PUT",
            f"/rest/api/3/issuetypescreenscheme/{issue_type_screen_scheme_id}",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    def append_mappings(
        self, issue_type_screen_scheme_id: str, body: IssueTypeScreenSchemeMappingDetails
    ) -> None:
        """Append mappings to issue type screen scheme"""
        self._client._request(
            "PUT",
            f"/rest/api/3/issuetypescreenscheme/{issue_type_screen_scheme_id}/mapping",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    def update_default(
        self, issue_type_screen_scheme_id: str, body: UpdateDefaultScreenScheme
    ) -> None:
        """Update issue type screen scheme default screen scheme"""
        self._client._request(
            "PUT",
            f"/rest/api/3/issuetypescreenscheme/{issue_type_screen_scheme_id}/mapping/default",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    def remove_mappings(self, issue_type_screen_scheme_id: str, body: IssueTypeIds) -> None:
        """Remove mappings from issue type screen scheme"""
        self._client._request(
            "POST",
            f"/rest/api/3/issuetypescreenscheme/{issue_type_screen_scheme_id}/mapping/remove",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    def get_projects(
        self,
        issue_type_screen_scheme_id: str,
        *,
        start_at: int | None = None,
        max_results: int | None = None,
        query: str | None = None,
    ) -> PageBeanProjectDetails:
        """Get issue type screen scheme projects"""
        params = self._client._build_params(
            **{"startAt": start_at, "maxResults": max_results, "query": query}
        )
        resp = self._client._request(
            "GET",
            f"/rest/api/3/issuetypescreenscheme/{issue_type_screen_scheme_id}/project",
            params=params,
        )
        return PageBeanProjectDetails.model_validate(resp.json())


class AsyncScreenIssueTypeScreenSchemes(AsyncAPIResource):
    """Asynchronous resource for screens.issue_type_screen_schemes."""

    async def list(
        self,
        *,
        start_at: int | None = None,
        max_results: int | None = None,
        id_: list[str] | None = None,
        query_string: str | None = None,
        order_by: str | None = None,
        expand: str | None = None,
    ) -> PageBeanIssueTypeScreenScheme:
        """Get issue type screen schemes"""
        params = self._client._build_params(
            **{
                "startAt": start_at,
                "maxResults": max_results,
                "id": id_,
                "queryString": query_string,
                "orderBy": order_by,
                "expand": expand,
            }
        )
        resp = await self._client._request(
            "GET", "/rest/api/3/issuetypescreenscheme", params=params
        )
        return PageBeanIssueTypeScreenScheme.model_validate(resp.json())

    async def create(self, body: IssueTypeScreenSchemeDetails) -> IssueTypeScreenSchemeId:
        """Create issue type screen scheme"""
        resp = await self._client._request(
            "POST",
            "/rest/api/3/issuetypescreenscheme",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return IssueTypeScreenSchemeId.model_validate(resp.json())

    async def get_mappings(
        self,
        *,
        start_at: int | None = None,
        max_results: int | None = None,
        issue_type_screen_scheme_id: list[str] | None = None,
    ) -> PageBeanIssueTypeScreenSchemeItem:
        """Get issue type screen scheme items"""
        params = self._client._build_params(
            **{
                "startAt": start_at,
                "maxResults": max_results,
                "issueTypeScreenSchemeId": issue_type_screen_scheme_id,
            }
        )
        resp = await self._client._request(
            "GET", "/rest/api/3/issuetypescreenscheme/mapping", params=params
        )
        return PageBeanIssueTypeScreenSchemeItem.model_validate(resp.json())

    async def get_project_associations(
        self, *, start_at: int | None = None, max_results: int | None = None, project_id: list[str]
    ) -> PageBeanIssueTypeScreenSchemesProjects:
        """Get issue type screen schemes for projects"""
        params = self._client._build_params(
            **{"startAt": start_at, "maxResults": max_results, "projectId": project_id}
        )
        resp = await self._client._request(
            "GET", "/rest/api/3/issuetypescreenscheme/project", params=params
        )
        return PageBeanIssueTypeScreenSchemesProjects.model_validate(resp.json())

    async def assign_to_project(self, body: IssueTypeScreenSchemeProjectAssociation) -> None:
        """Assign issue type screen scheme to project"""
        await self._client._request(
            "PUT",
            "/rest/api/3/issuetypescreenscheme/project",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    async def delete(self, issue_type_screen_scheme_id: str) -> None:
        """Delete issue type screen scheme"""
        await self._client._request(
            "DELETE", f"/rest/api/3/issuetypescreenscheme/{issue_type_screen_scheme_id}"
        )
        return None

    async def update(
        self, issue_type_screen_scheme_id: str, body: IssueTypeScreenSchemeUpdateDetails
    ) -> None:
        """Update issue type screen scheme"""
        await self._client._request(
            "PUT",
            f"/rest/api/3/issuetypescreenscheme/{issue_type_screen_scheme_id}",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    async def append_mappings(
        self, issue_type_screen_scheme_id: str, body: IssueTypeScreenSchemeMappingDetails
    ) -> None:
        """Append mappings to issue type screen scheme"""
        await self._client._request(
            "PUT",
            f"/rest/api/3/issuetypescreenscheme/{issue_type_screen_scheme_id}/mapping",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    async def update_default(
        self, issue_type_screen_scheme_id: str, body: UpdateDefaultScreenScheme
    ) -> None:
        """Update issue type screen scheme default screen scheme"""
        await self._client._request(
            "PUT",
            f"/rest/api/3/issuetypescreenscheme/{issue_type_screen_scheme_id}/mapping/default",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    async def remove_mappings(self, issue_type_screen_scheme_id: str, body: IssueTypeIds) -> None:
        """Remove mappings from issue type screen scheme"""
        await self._client._request(
            "POST",
            f"/rest/api/3/issuetypescreenscheme/{issue_type_screen_scheme_id}/mapping/remove",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    async def get_projects(
        self,
        issue_type_screen_scheme_id: str,
        *,
        start_at: int | None = None,
        max_results: int | None = None,
        query: str | None = None,
    ) -> PageBeanProjectDetails:
        """Get issue type screen scheme projects"""
        params = self._client._build_params(
            **{"startAt": start_at, "maxResults": max_results, "query": query}
        )
        resp = await self._client._request(
            "GET",
            f"/rest/api/3/issuetypescreenscheme/{issue_type_screen_scheme_id}/project",
            params=params,
        )
        return PageBeanProjectDetails.model_validate(resp.json())
