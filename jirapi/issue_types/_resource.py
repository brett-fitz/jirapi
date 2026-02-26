"""Resource classes for issue_types."""

from __future__ import annotations

from jirapi._resource import AsyncAPIResource, SyncAPIResource
from jirapi.models import (
    Avatar,
    EntityProperty,
    IssueTypeCreate,
    IssueTypeDetails,
    IssueTypeIds,
    IssueTypeSchemeDetails,
    IssueTypeSchemeID,
    IssueTypeSchemeProjectAssociation,
    IssueTypeSchemeUpdateDetails,
    IssueTypeUpdate,
    OrderOfIssueTypes,
    PageBeanIssueTypeScheme,
    PageBeanIssueTypeSchemeMapping,
    PageBeanIssueTypeSchemeProjects,
    PropertyKeys,
)


class IssueTypes(SyncAPIResource):
    """Synchronous resource for issue_types."""

    def list(self) -> IssueTypeDetails:
        """Get all issue types for user"""
        resp = self._client._request("GET", "/rest/api/3/issuetype")
        return IssueTypeDetails.model_validate(resp.json())

    def create(self, body: IssueTypeCreate) -> IssueTypeDetails:
        """Create issue type"""
        resp = self._client._request(
            "POST", "/rest/api/3/issuetype", json=body.model_dump(by_alias=True, exclude_none=True)
        )
        return IssueTypeDetails.model_validate(resp.json())

    def list_for_project(self, *, project_id: int, level: int | None = None) -> IssueTypeDetails:
        """Get issue types for project"""
        params = self._client._build_params(**{"projectId": project_id, "level": level})
        resp = self._client._request("GET", "/rest/api/3/issuetype/project", params=params)
        return IssueTypeDetails.model_validate(resp.json())

    def delete(self, id_: str, *, alternative_issue_type_id: str | None = None) -> None:
        """Delete issue type"""
        params = self._client._build_params(**{"alternativeIssueTypeId": alternative_issue_type_id})
        self._client._request("DELETE", f"/rest/api/3/issuetype/{id_}", params=params)
        return None

    def get(self, id_: str) -> IssueTypeDetails:
        """Get issue type"""
        resp = self._client._request("GET", f"/rest/api/3/issuetype/{id_}")
        return IssueTypeDetails.model_validate(resp.json())

    def update(self, id_: str, body: IssueTypeUpdate) -> IssueTypeDetails:
        """Update issue type"""
        resp = self._client._request(
            "PUT",
            f"/rest/api/3/issuetype/{id_}",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return IssueTypeDetails.model_validate(resp.json())

    def get_alternatives(self, id_: str) -> IssueTypeDetails:
        """Get alternative issue types"""
        resp = self._client._request("GET", f"/rest/api/3/issuetype/{id_}/alternatives")
        return IssueTypeDetails.model_validate(resp.json())

    def create_avatar(
        self, id_: str, *, x: int | None = None, y: int | None = None, size: int
    ) -> Avatar:
        """Load issue type avatar"""
        params = self._client._build_params(**{"x": x, "y": y, "size": size})
        resp = self._client._request("POST", f"/rest/api/3/issuetype/{id_}/avatar2", params=params)
        return Avatar.model_validate(resp.json())

    def get_property_keys(self, issue_type_id: str) -> PropertyKeys:
        """Get issue type property keys"""
        resp = self._client._request("GET", f"/rest/api/3/issuetype/{issue_type_id}/properties")
        return PropertyKeys.model_validate(resp.json())

    def delete_property(self, issue_type_id: str, property_key: str) -> None:
        """Delete issue type property"""
        self._client._request(
            "DELETE", f"/rest/api/3/issuetype/{issue_type_id}/properties/{property_key}"
        )
        return None

    def get_property(self, issue_type_id: str, property_key: str) -> EntityProperty:
        """Get issue type property"""
        resp = self._client._request(
            "GET", f"/rest/api/3/issuetype/{issue_type_id}/properties/{property_key}"
        )
        return EntityProperty.model_validate(resp.json())

    def set_property(self, issue_type_id: str, property_key: str) -> None:
        """Set issue type property"""
        self._client._request(
            "PUT", f"/rest/api/3/issuetype/{issue_type_id}/properties/{property_key}"
        )
        return None

    def list_schemes(
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

    def create_scheme(self, body: IssueTypeSchemeDetails) -> IssueTypeSchemeID:
        """Create issue type scheme"""
        resp = self._client._request(
            "POST",
            "/rest/api/3/issuetypescheme",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return IssueTypeSchemeID.model_validate(resp.json())

    def get_scheme_mappings(
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

    def get_schemes_for_projects(
        self, *, start_at: int | None = None, max_results: int | None = None, project_id: list[str]
    ) -> PageBeanIssueTypeSchemeProjects:
        """Get issue type schemes for projects"""
        params = self._client._build_params(
            **{"startAt": start_at, "maxResults": max_results, "projectId": project_id}
        )
        resp = self._client._request("GET", "/rest/api/3/issuetypescheme/project", params=params)
        return PageBeanIssueTypeSchemeProjects.model_validate(resp.json())

    def assign_scheme_to_project(self, body: IssueTypeSchemeProjectAssociation) -> None:
        """Assign issue type scheme to project"""
        self._client._request(
            "PUT",
            "/rest/api/3/issuetypescheme/project",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    def delete_scheme(self, issue_type_scheme_id: str) -> None:
        """Delete issue type scheme"""
        self._client._request("DELETE", f"/rest/api/3/issuetypescheme/{issue_type_scheme_id}")
        return None

    def update_scheme(self, issue_type_scheme_id: str, body: IssueTypeSchemeUpdateDetails) -> None:
        """Update issue type scheme"""
        self._client._request(
            "PUT",
            f"/rest/api/3/issuetypescheme/{issue_type_scheme_id}",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    def add_to_scheme(self, issue_type_scheme_id: str, body: IssueTypeIds) -> None:
        """Add issue types to issue type scheme"""
        self._client._request(
            "PUT",
            f"/rest/api/3/issuetypescheme/{issue_type_scheme_id}/issuetype",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    def reorder_in_scheme(self, issue_type_scheme_id: str, body: OrderOfIssueTypes) -> None:
        """Change order of issue types"""
        self._client._request(
            "PUT",
            f"/rest/api/3/issuetypescheme/{issue_type_scheme_id}/issuetype/move",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    def remove_from_scheme(self, issue_type_scheme_id: str, issue_type_id: str) -> None:
        """Remove issue type from issue type scheme"""
        self._client._request(
            "DELETE",
            f"/rest/api/3/issuetypescheme/{issue_type_scheme_id}/issuetype/{issue_type_id}",
        )
        return None


class AsyncIssueTypes(AsyncAPIResource):
    """Asynchronous resource for issue_types."""

    async def list(self) -> IssueTypeDetails:
        """Get all issue types for user"""
        resp = await self._client._request("GET", "/rest/api/3/issuetype")
        return IssueTypeDetails.model_validate(resp.json())

    async def create(self, body: IssueTypeCreate) -> IssueTypeDetails:
        """Create issue type"""
        resp = await self._client._request(
            "POST", "/rest/api/3/issuetype", json=body.model_dump(by_alias=True, exclude_none=True)
        )
        return IssueTypeDetails.model_validate(resp.json())

    async def list_for_project(
        self, *, project_id: int, level: int | None = None
    ) -> IssueTypeDetails:
        """Get issue types for project"""
        params = self._client._build_params(**{"projectId": project_id, "level": level})
        resp = await self._client._request("GET", "/rest/api/3/issuetype/project", params=params)
        return IssueTypeDetails.model_validate(resp.json())

    async def delete(self, id_: str, *, alternative_issue_type_id: str | None = None) -> None:
        """Delete issue type"""
        params = self._client._build_params(**{"alternativeIssueTypeId": alternative_issue_type_id})
        await self._client._request("DELETE", f"/rest/api/3/issuetype/{id_}", params=params)
        return None

    async def get(self, id_: str) -> IssueTypeDetails:
        """Get issue type"""
        resp = await self._client._request("GET", f"/rest/api/3/issuetype/{id_}")
        return IssueTypeDetails.model_validate(resp.json())

    async def update(self, id_: str, body: IssueTypeUpdate) -> IssueTypeDetails:
        """Update issue type"""
        resp = await self._client._request(
            "PUT",
            f"/rest/api/3/issuetype/{id_}",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return IssueTypeDetails.model_validate(resp.json())

    async def get_alternatives(self, id_: str) -> IssueTypeDetails:
        """Get alternative issue types"""
        resp = await self._client._request("GET", f"/rest/api/3/issuetype/{id_}/alternatives")
        return IssueTypeDetails.model_validate(resp.json())

    async def create_avatar(
        self, id_: str, *, x: int | None = None, y: int | None = None, size: int
    ) -> Avatar:
        """Load issue type avatar"""
        params = self._client._build_params(**{"x": x, "y": y, "size": size})
        resp = await self._client._request(
            "POST", f"/rest/api/3/issuetype/{id_}/avatar2", params=params
        )
        return Avatar.model_validate(resp.json())

    async def get_property_keys(self, issue_type_id: str) -> PropertyKeys:
        """Get issue type property keys"""
        resp = await self._client._request(
            "GET", f"/rest/api/3/issuetype/{issue_type_id}/properties"
        )
        return PropertyKeys.model_validate(resp.json())

    async def delete_property(self, issue_type_id: str, property_key: str) -> None:
        """Delete issue type property"""
        await self._client._request(
            "DELETE", f"/rest/api/3/issuetype/{issue_type_id}/properties/{property_key}"
        )
        return None

    async def get_property(self, issue_type_id: str, property_key: str) -> EntityProperty:
        """Get issue type property"""
        resp = await self._client._request(
            "GET", f"/rest/api/3/issuetype/{issue_type_id}/properties/{property_key}"
        )
        return EntityProperty.model_validate(resp.json())

    async def set_property(self, issue_type_id: str, property_key: str) -> None:
        """Set issue type property"""
        await self._client._request(
            "PUT", f"/rest/api/3/issuetype/{issue_type_id}/properties/{property_key}"
        )
        return None

    async def list_schemes(
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

    async def create_scheme(self, body: IssueTypeSchemeDetails) -> IssueTypeSchemeID:
        """Create issue type scheme"""
        resp = await self._client._request(
            "POST",
            "/rest/api/3/issuetypescheme",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return IssueTypeSchemeID.model_validate(resp.json())

    async def get_scheme_mappings(
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

    async def get_schemes_for_projects(
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

    async def assign_scheme_to_project(self, body: IssueTypeSchemeProjectAssociation) -> None:
        """Assign issue type scheme to project"""
        await self._client._request(
            "PUT",
            "/rest/api/3/issuetypescheme/project",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    async def delete_scheme(self, issue_type_scheme_id: str) -> None:
        """Delete issue type scheme"""
        await self._client._request("DELETE", f"/rest/api/3/issuetypescheme/{issue_type_scheme_id}")
        return None

    async def update_scheme(
        self, issue_type_scheme_id: str, body: IssueTypeSchemeUpdateDetails
    ) -> None:
        """Update issue type scheme"""
        await self._client._request(
            "PUT",
            f"/rest/api/3/issuetypescheme/{issue_type_scheme_id}",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    async def add_to_scheme(self, issue_type_scheme_id: str, body: IssueTypeIds) -> None:
        """Add issue types to issue type scheme"""
        await self._client._request(
            "PUT",
            f"/rest/api/3/issuetypescheme/{issue_type_scheme_id}/issuetype",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    async def reorder_in_scheme(self, issue_type_scheme_id: str, body: OrderOfIssueTypes) -> None:
        """Change order of issue types"""
        await self._client._request(
            "PUT",
            f"/rest/api/3/issuetypescheme/{issue_type_scheme_id}/issuetype/move",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    async def remove_from_scheme(self, issue_type_scheme_id: str, issue_type_id: str) -> None:
        """Remove issue type from issue type scheme"""
        await self._client._request(
            "DELETE",
            f"/rest/api/3/issuetypescheme/{issue_type_scheme_id}/issuetype/{issue_type_id}",
        )
        return None
