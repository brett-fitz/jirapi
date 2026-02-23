"""Resource classes for the Issue type properties API group."""

from __future__ import annotations

from jirapi._resource import AsyncAPIResource, SyncAPIResource
from jirapi.models import EntityProperty, PropertyKeys


class IssueTypeProperties(SyncAPIResource):
    """Synchronous resource for the Issue type properties API group."""

    def get_issue_type_property_keys(self, issue_type_id: str) -> PropertyKeys:
        """Get issue type property keys"""
        resp = self._client._request("GET", f"/rest/api/3/issuetype/{issue_type_id}/properties")
        return PropertyKeys.model_validate(resp.json())

    def delete_issue_type_property(self, issue_type_id: str, property_key: str) -> None:
        """Delete issue type property"""
        self._client._request(
            "DELETE", f"/rest/api/3/issuetype/{issue_type_id}/properties/{property_key}"
        )
        return None

    def get_issue_type_property(self, issue_type_id: str, property_key: str) -> EntityProperty:
        """Get issue type property"""
        resp = self._client._request(
            "GET", f"/rest/api/3/issuetype/{issue_type_id}/properties/{property_key}"
        )
        return EntityProperty.model_validate(resp.json())

    def set_issue_type_property(self, issue_type_id: str, property_key: str) -> None:
        """Set issue type property"""
        self._client._request(
            "PUT", f"/rest/api/3/issuetype/{issue_type_id}/properties/{property_key}"
        )
        return None


class AsyncIssueTypeProperties(AsyncAPIResource):
    """Asynchronous resource for the Issue type properties API group."""

    async def get_issue_type_property_keys(self, issue_type_id: str) -> PropertyKeys:
        """Get issue type property keys"""
        resp = await self._client._request(
            "GET", f"/rest/api/3/issuetype/{issue_type_id}/properties"
        )
        return PropertyKeys.model_validate(resp.json())

    async def delete_issue_type_property(self, issue_type_id: str, property_key: str) -> None:
        """Delete issue type property"""
        await self._client._request(
            "DELETE", f"/rest/api/3/issuetype/{issue_type_id}/properties/{property_key}"
        )
        return None

    async def get_issue_type_property(
        self, issue_type_id: str, property_key: str
    ) -> EntityProperty:
        """Get issue type property"""
        resp = await self._client._request(
            "GET", f"/rest/api/3/issuetype/{issue_type_id}/properties/{property_key}"
        )
        return EntityProperty.model_validate(resp.json())

    async def set_issue_type_property(self, issue_type_id: str, property_key: str) -> None:
        """Set issue type property"""
        await self._client._request(
            "PUT", f"/rest/api/3/issuetype/{issue_type_id}/properties/{property_key}"
        )
        return None
