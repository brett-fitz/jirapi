"""Resource classes for issues.properties."""

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
    """Synchronous resource for issues.properties."""

    def bulk_set_by_list(self, body: IssueEntityProperties) -> None:
        """Bulk set issues properties by list"""
        self._client._request(
            "POST",
            "/rest/api/3/issue/properties",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    def bulk_set_by_issue(self, body: MultiIssueEntityProperties) -> None:
        """Bulk set issue properties by issue"""
        self._client._request(
            "POST",
            "/rest/api/3/issue/properties/multi",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    def bulk_delete(self, property_key: str, body: IssueFilterForBulkPropertyDelete) -> None:
        """Bulk delete issue property"""
        self._client._request(
            "DELETE",
            f"/rest/api/3/issue/properties/{property_key}",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    def bulk_set(self, property_key: str, body: BulkIssuePropertyUpdateRequest) -> None:
        """Bulk set issue property"""
        self._client._request(
            "PUT",
            f"/rest/api/3/issue/properties/{property_key}",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    def get_keys(self, issue_id_or_key: str) -> PropertyKeys:
        """Get issue property keys"""
        resp = self._client._request("GET", f"/rest/api/3/issue/{issue_id_or_key}/properties")
        return PropertyKeys.model_validate(resp.json())

    def delete(self, issue_id_or_key: str, property_key: str) -> None:
        """Delete issue property"""
        self._client._request(
            "DELETE", f"/rest/api/3/issue/{issue_id_or_key}/properties/{property_key}"
        )
        return None

    def get(self, issue_id_or_key: str, property_key: str) -> EntityProperty:
        """Get issue property"""
        resp = self._client._request(
            "GET", f"/rest/api/3/issue/{issue_id_or_key}/properties/{property_key}"
        )
        return EntityProperty.model_validate(resp.json())

    def set(self, issue_id_or_key: str, property_key: str) -> None:
        """Set issue property"""
        self._client._request(
            "PUT", f"/rest/api/3/issue/{issue_id_or_key}/properties/{property_key}"
        )
        return None


class AsyncIssueProperties(AsyncAPIResource):
    """Asynchronous resource for issues.properties."""

    async def bulk_set_by_list(self, body: IssueEntityProperties) -> None:
        """Bulk set issues properties by list"""
        await self._client._request(
            "POST",
            "/rest/api/3/issue/properties",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    async def bulk_set_by_issue(self, body: MultiIssueEntityProperties) -> None:
        """Bulk set issue properties by issue"""
        await self._client._request(
            "POST",
            "/rest/api/3/issue/properties/multi",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    async def bulk_delete(self, property_key: str, body: IssueFilterForBulkPropertyDelete) -> None:
        """Bulk delete issue property"""
        await self._client._request(
            "DELETE",
            f"/rest/api/3/issue/properties/{property_key}",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    async def bulk_set(self, property_key: str, body: BulkIssuePropertyUpdateRequest) -> None:
        """Bulk set issue property"""
        await self._client._request(
            "PUT",
            f"/rest/api/3/issue/properties/{property_key}",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    async def get_keys(self, issue_id_or_key: str) -> PropertyKeys:
        """Get issue property keys"""
        resp = await self._client._request("GET", f"/rest/api/3/issue/{issue_id_or_key}/properties")
        return PropertyKeys.model_validate(resp.json())

    async def delete(self, issue_id_or_key: str, property_key: str) -> None:
        """Delete issue property"""
        await self._client._request(
            "DELETE", f"/rest/api/3/issue/{issue_id_or_key}/properties/{property_key}"
        )
        return None

    async def get(self, issue_id_or_key: str, property_key: str) -> EntityProperty:
        """Get issue property"""
        resp = await self._client._request(
            "GET", f"/rest/api/3/issue/{issue_id_or_key}/properties/{property_key}"
        )
        return EntityProperty.model_validate(resp.json())

    async def set(self, issue_id_or_key: str, property_key: str) -> None:
        """Set issue property"""
        await self._client._request(
            "PUT", f"/rest/api/3/issue/{issue_id_or_key}/properties/{property_key}"
        )
        return None
