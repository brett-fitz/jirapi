"""Resource classes for the Issue link types API group."""

from __future__ import annotations

from jirapi._resource import AsyncAPIResource, SyncAPIResource
from jirapi.models import IssueLinkType
from jirapi.models import IssueLinkTypes as IssueLinkTypesModel


class IssueLinkTypes(SyncAPIResource):
    """Synchronous resource for the Issue link types API group."""

    def get_issue_link_types(self) -> IssueLinkTypesModel:
        """Get issue link types"""
        resp = self._client._request("GET", "/rest/api/3/issueLinkType")
        return IssueLinkTypesModel.model_validate(resp.json())

    def create_issue_link_type(self, body: IssueLinkType) -> IssueLinkType:
        """Create issue link type"""
        resp = self._client._request(
            "POST",
            "/rest/api/3/issueLinkType",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return IssueLinkType.model_validate(resp.json())

    def delete_issue_link_type(self, issue_link_type_id: str) -> None:
        """Delete issue link type"""
        self._client._request("DELETE", f"/rest/api/3/issueLinkType/{issue_link_type_id}")
        return None

    def get_issue_link_type(self, issue_link_type_id: str) -> IssueLinkType:
        """Get issue link type"""
        resp = self._client._request("GET", f"/rest/api/3/issueLinkType/{issue_link_type_id}")
        return IssueLinkType.model_validate(resp.json())

    def update_issue_link_type(self, issue_link_type_id: str, body: IssueLinkType) -> IssueLinkType:
        """Update issue link type"""
        resp = self._client._request(
            "PUT",
            f"/rest/api/3/issueLinkType/{issue_link_type_id}",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return IssueLinkType.model_validate(resp.json())


class AsyncIssueLinkTypes(AsyncAPIResource):
    """Asynchronous resource for the Issue link types API group."""

    async def get_issue_link_types(self) -> IssueLinkTypesModel:
        """Get issue link types"""
        resp = await self._client._request("GET", "/rest/api/3/issueLinkType")
        return IssueLinkTypesModel.model_validate(resp.json())

    async def create_issue_link_type(self, body: IssueLinkType) -> IssueLinkType:
        """Create issue link type"""
        resp = await self._client._request(
            "POST",
            "/rest/api/3/issueLinkType",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return IssueLinkType.model_validate(resp.json())

    async def delete_issue_link_type(self, issue_link_type_id: str) -> None:
        """Delete issue link type"""
        await self._client._request("DELETE", f"/rest/api/3/issueLinkType/{issue_link_type_id}")
        return None

    async def get_issue_link_type(self, issue_link_type_id: str) -> IssueLinkType:
        """Get issue link type"""
        resp = await self._client._request("GET", f"/rest/api/3/issueLinkType/{issue_link_type_id}")
        return IssueLinkType.model_validate(resp.json())

    async def update_issue_link_type(
        self, issue_link_type_id: str, body: IssueLinkType
    ) -> IssueLinkType:
        """Update issue link type"""
        resp = await self._client._request(
            "PUT",
            f"/rest/api/3/issueLinkType/{issue_link_type_id}",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return IssueLinkType.model_validate(resp.json())
