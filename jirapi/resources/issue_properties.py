"""Resource classes for the Issue properties API group."""

from __future__ import annotations

from jirapi._resource import AsyncAPIResource, SyncAPIResource
from jirapi.models import (
    BulkIssuePropertyUpdateRequest,
    EntityProperty,
    IssueEntityProperties,
    IssueFilterForBulkPropertyDelete,
    MultiIssueEntityProperties,
    PropertyKeys,
)


class IssueProperties(SyncAPIResource):
    """Synchronous resource for the Issue properties API group."""

    def bulk_set_issues_properties_list(self, body: IssueEntityProperties) -> None:
        """Bulk set issues properties by list"""
        resp = self._client._request(
            "POST",
            "/rest/api/3/issue/properties",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    def bulk_set_issue_properties_by_issue(self, body: MultiIssueEntityProperties) -> None:
        """Bulk set issue properties by issue"""
        resp = self._client._request(
            "POST",
            "/rest/api/3/issue/properties/multi",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    def bulk_delete_issue_property(
        self, property_key: str, body: IssueFilterForBulkPropertyDelete
    ) -> None:
        """Bulk delete issue property"""
        resp = self._client._request(
            "DELETE",
            f"/rest/api/3/issue/properties/{property_key}",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    def bulk_set_issue_property(
        self, property_key: str, body: BulkIssuePropertyUpdateRequest
    ) -> None:
        """Bulk set issue property"""
        resp = self._client._request(
            "PUT",
            f"/rest/api/3/issue/properties/{property_key}",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    def get_issue_property_keys(self, issue_id_or_key: str) -> PropertyKeys:
        """Get issue property keys"""
        resp = self._client._request("GET", f"/rest/api/3/issue/{issue_id_or_key}/properties")
        return PropertyKeys.model_validate(resp.json())

    def delete_issue_property(self, issue_id_or_key: str, property_key: str) -> None:
        """Delete issue property"""
        resp = self._client._request(
            "DELETE", f"/rest/api/3/issue/{issue_id_or_key}/properties/{property_key}"
        )
        return None

    def get_issue_property(self, issue_id_or_key: str, property_key: str) -> EntityProperty:
        """Get issue property"""
        resp = self._client._request(
            "GET", f"/rest/api/3/issue/{issue_id_or_key}/properties/{property_key}"
        )
        return EntityProperty.model_validate(resp.json())

    def set_issue_property(self, issue_id_or_key: str, property_key: str) -> None:
        """Set issue property"""
        resp = self._client._request(
            "PUT", f"/rest/api/3/issue/{issue_id_or_key}/properties/{property_key}"
        )
        return None


class AsyncIssueProperties(AsyncAPIResource):
    """Asynchronous resource for the Issue properties API group."""

    async def bulk_set_issues_properties_list(self, body: IssueEntityProperties) -> None:
        """Bulk set issues properties by list"""
        resp = await self._client._request(
            "POST",
            "/rest/api/3/issue/properties",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    async def bulk_set_issue_properties_by_issue(self, body: MultiIssueEntityProperties) -> None:
        """Bulk set issue properties by issue"""
        resp = await self._client._request(
            "POST",
            "/rest/api/3/issue/properties/multi",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    async def bulk_delete_issue_property(
        self, property_key: str, body: IssueFilterForBulkPropertyDelete
    ) -> None:
        """Bulk delete issue property"""
        resp = await self._client._request(
            "DELETE",
            f"/rest/api/3/issue/properties/{property_key}",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    async def bulk_set_issue_property(
        self, property_key: str, body: BulkIssuePropertyUpdateRequest
    ) -> None:
        """Bulk set issue property"""
        resp = await self._client._request(
            "PUT",
            f"/rest/api/3/issue/properties/{property_key}",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    async def get_issue_property_keys(self, issue_id_or_key: str) -> PropertyKeys:
        """Get issue property keys"""
        resp = await self._client._request("GET", f"/rest/api/3/issue/{issue_id_or_key}/properties")
        return PropertyKeys.model_validate(resp.json())

    async def delete_issue_property(self, issue_id_or_key: str, property_key: str) -> None:
        """Delete issue property"""
        resp = await self._client._request(
            "DELETE", f"/rest/api/3/issue/{issue_id_or_key}/properties/{property_key}"
        )
        return None

    async def get_issue_property(self, issue_id_or_key: str, property_key: str) -> EntityProperty:
        """Get issue property"""
        resp = await self._client._request(
            "GET", f"/rest/api/3/issue/{issue_id_or_key}/properties/{property_key}"
        )
        return EntityProperty.model_validate(resp.json())

    async def set_issue_property(self, issue_id_or_key: str, property_key: str) -> None:
        """Set issue property"""
        resp = await self._client._request(
            "PUT", f"/rest/api/3/issue/{issue_id_or_key}/properties/{property_key}"
        )
        return None
