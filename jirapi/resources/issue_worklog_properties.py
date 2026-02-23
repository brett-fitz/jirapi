"""Resource classes for the Issue worklog properties API group."""

from __future__ import annotations

from jirapi._resource import AsyncAPIResource, SyncAPIResource
from jirapi.models import EntityProperty, PropertyKeys


class IssueWorklogProperties(SyncAPIResource):
    """Synchronous resource for the Issue worklog properties API group."""

    def get_worklog_property_keys(self, issue_id_or_key: str, worklog_id: str) -> PropertyKeys:
        """Get worklog property keys"""
        resp = self._client._request(
            "GET", f"/rest/api/3/issue/{issue_id_or_key}/worklog/{worklog_id}/properties"
        )
        return PropertyKeys.model_validate(resp.json())

    def delete_worklog_property(
        self, issue_id_or_key: str, worklog_id: str, property_key: str
    ) -> None:
        """Delete worklog property"""
        self._client._request(
            "DELETE",
            f"/rest/api/3/issue/{issue_id_or_key}/worklog/{worklog_id}/properties/{property_key}",
        )
        return None

    def get_worklog_property(
        self, issue_id_or_key: str, worklog_id: str, property_key: str
    ) -> EntityProperty:
        """Get worklog property"""
        resp = self._client._request(
            "GET",
            f"/rest/api/3/issue/{issue_id_or_key}/worklog/{worklog_id}/properties/{property_key}",
        )
        return EntityProperty.model_validate(resp.json())

    def set_worklog_property(
        self, issue_id_or_key: str, worklog_id: str, property_key: str
    ) -> None:
        """Set worklog property"""
        self._client._request(
            "PUT",
            f"/rest/api/3/issue/{issue_id_or_key}/worklog/{worklog_id}/properties/{property_key}",
        )
        return None


class AsyncIssueWorklogProperties(AsyncAPIResource):
    """Asynchronous resource for the Issue worklog properties API group."""

    async def get_worklog_property_keys(
        self, issue_id_or_key: str, worklog_id: str
    ) -> PropertyKeys:
        """Get worklog property keys"""
        resp = await self._client._request(
            "GET", f"/rest/api/3/issue/{issue_id_or_key}/worklog/{worklog_id}/properties"
        )
        return PropertyKeys.model_validate(resp.json())

    async def delete_worklog_property(
        self, issue_id_or_key: str, worklog_id: str, property_key: str
    ) -> None:
        """Delete worklog property"""
        await self._client._request(
            "DELETE",
            f"/rest/api/3/issue/{issue_id_or_key}/worklog/{worklog_id}/properties/{property_key}",
        )
        return None

    async def get_worklog_property(
        self, issue_id_or_key: str, worklog_id: str, property_key: str
    ) -> EntityProperty:
        """Get worklog property"""
        resp = await self._client._request(
            "GET",
            f"/rest/api/3/issue/{issue_id_or_key}/worklog/{worklog_id}/properties/{property_key}",
        )
        return EntityProperty.model_validate(resp.json())

    async def set_worklog_property(
        self, issue_id_or_key: str, worklog_id: str, property_key: str
    ) -> None:
        """Set worklog property"""
        await self._client._request(
            "PUT",
            f"/rest/api/3/issue/{issue_id_or_key}/worklog/{worklog_id}/properties/{property_key}",
        )
        return None
