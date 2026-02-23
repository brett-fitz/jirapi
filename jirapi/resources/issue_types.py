"""Resource classes for the Issue types API group."""

from __future__ import annotations

from jirapi._resource import AsyncAPIResource, SyncAPIResource
from jirapi.models import Avatar, IssueTypeCreateBean, IssueTypeDetails, IssueTypeUpdateBean


class IssueTypes(SyncAPIResource):
    """Synchronous resource for the Issue types API group."""

    def get_issue_all_types(self) -> IssueTypeDetails:
        """Get all issue types for user"""
        resp = self._client._request("GET", "/rest/api/3/issuetype")
        return IssueTypeDetails.model_validate(resp.json())

    def create_issue_type(self, body: IssueTypeCreateBean) -> IssueTypeDetails:
        """Create issue type"""
        resp = self._client._request(
            "POST", "/rest/api/3/issuetype", json=body.model_dump(by_alias=True, exclude_none=True)
        )
        return IssueTypeDetails.model_validate(resp.json())

    def get_issue_types_for_project(
        self, *, project_id: int, level: int | None = None
    ) -> IssueTypeDetails:
        """Get issue types for project"""
        params = self._client._build_params(**{"projectId": project_id, "level": level})
        resp = self._client._request("GET", "/rest/api/3/issuetype/project", params=params)
        return IssueTypeDetails.model_validate(resp.json())

    def delete_issue_type(self, id_: str, *, alternative_issue_type_id: str | None = None) -> None:
        """Delete issue type"""
        params = self._client._build_params(**{"alternativeIssueTypeId": alternative_issue_type_id})
        self._client._request("DELETE", f"/rest/api/3/issuetype/{id_}", params=params)
        return None

    def get_issue_type(self, id_: str) -> IssueTypeDetails:
        """Get issue type"""
        resp = self._client._request("GET", f"/rest/api/3/issuetype/{id_}")
        return IssueTypeDetails.model_validate(resp.json())

    def update_issue_type(self, id_: str, body: IssueTypeUpdateBean) -> IssueTypeDetails:
        """Update issue type"""
        resp = self._client._request(
            "PUT",
            f"/rest/api/3/issuetype/{id_}",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return IssueTypeDetails.model_validate(resp.json())

    def get_alternative_issue_types(self, id_: str) -> IssueTypeDetails:
        """Get alternative issue types"""
        resp = self._client._request("GET", f"/rest/api/3/issuetype/{id_}/alternatives")
        return IssueTypeDetails.model_validate(resp.json())

    def create_issue_type_avatar(
        self, id_: str, *, x: int | None = None, y: int | None = None, size: int
    ) -> Avatar:
        """Load issue type avatar"""
        params = self._client._build_params(**{"x": x, "y": y, "size": size})
        resp = self._client._request("POST", f"/rest/api/3/issuetype/{id_}/avatar2", params=params)
        return Avatar.model_validate(resp.json())


class AsyncIssueTypes(AsyncAPIResource):
    """Asynchronous resource for the Issue types API group."""

    async def get_issue_all_types(self) -> IssueTypeDetails:
        """Get all issue types for user"""
        resp = await self._client._request("GET", "/rest/api/3/issuetype")
        return IssueTypeDetails.model_validate(resp.json())

    async def create_issue_type(self, body: IssueTypeCreateBean) -> IssueTypeDetails:
        """Create issue type"""
        resp = await self._client._request(
            "POST", "/rest/api/3/issuetype", json=body.model_dump(by_alias=True, exclude_none=True)
        )
        return IssueTypeDetails.model_validate(resp.json())

    async def get_issue_types_for_project(
        self, *, project_id: int, level: int | None = None
    ) -> IssueTypeDetails:
        """Get issue types for project"""
        params = self._client._build_params(**{"projectId": project_id, "level": level})
        resp = await self._client._request("GET", "/rest/api/3/issuetype/project", params=params)
        return IssueTypeDetails.model_validate(resp.json())

    async def delete_issue_type(
        self, id_: str, *, alternative_issue_type_id: str | None = None
    ) -> None:
        """Delete issue type"""
        params = self._client._build_params(**{"alternativeIssueTypeId": alternative_issue_type_id})
        await self._client._request("DELETE", f"/rest/api/3/issuetype/{id_}", params=params)
        return None

    async def get_issue_type(self, id_: str) -> IssueTypeDetails:
        """Get issue type"""
        resp = await self._client._request("GET", f"/rest/api/3/issuetype/{id_}")
        return IssueTypeDetails.model_validate(resp.json())

    async def update_issue_type(self, id_: str, body: IssueTypeUpdateBean) -> IssueTypeDetails:
        """Update issue type"""
        resp = await self._client._request(
            "PUT",
            f"/rest/api/3/issuetype/{id_}",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return IssueTypeDetails.model_validate(resp.json())

    async def get_alternative_issue_types(self, id_: str) -> IssueTypeDetails:
        """Get alternative issue types"""
        resp = await self._client._request("GET", f"/rest/api/3/issuetype/{id_}/alternatives")
        return IssueTypeDetails.model_validate(resp.json())

    async def create_issue_type_avatar(
        self, id_: str, *, x: int | None = None, y: int | None = None, size: int
    ) -> Avatar:
        """Load issue type avatar"""
        params = self._client._build_params(**{"x": x, "y": y, "size": size})
        resp = await self._client._request(
            "POST", f"/rest/api/3/issuetype/{id_}/avatar2", params=params
        )
        return Avatar.model_validate(resp.json())
