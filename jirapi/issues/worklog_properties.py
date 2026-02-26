"""Resource classes for issues.worklog_properties."""

from __future__ import annotations

from jirapi._resource import AsyncAPIResource, SyncAPIResource
from jirapi.models import EntityProperty, PropertyKeys


class IssueWorklogProperties(SyncAPIResource):
    """Synchronous resource for issues.worklog_properties."""

    def get_keys(self, issue_id_or_key: str, worklog_id: str) -> PropertyKeys:
        """Get worklog property keys"""
        resp = self._client._request(
            "GET", f"/rest/api/3/issue/{issue_id_or_key}/worklog/{worklog_id}/properties"
        )
        return PropertyKeys.model_validate(resp.json())

    def delete(self, issue_id_or_key: str, worklog_id: str, property_key: str) -> None:
        """Delete worklog property"""
        self._client._request(
            "DELETE",
            f"/rest/api/3/issue/{issue_id_or_key}/worklog/{worklog_id}/properties/{property_key}",
        )
        return None

    def get(self, issue_id_or_key: str, worklog_id: str, property_key: str) -> EntityProperty:
        """Get worklog property"""
        resp = self._client._request(
            "GET",
            f"/rest/api/3/issue/{issue_id_or_key}/worklog/{worklog_id}/properties/{property_key}",
        )
        return EntityProperty.model_validate(resp.json())

    def set(self, issue_id_or_key: str, worklog_id: str, property_key: str) -> None:
        """Set worklog property"""
        self._client._request(
            "PUT",
            f"/rest/api/3/issue/{issue_id_or_key}/worklog/{worklog_id}/properties/{property_key}",
        )
        return None


class AsyncIssueWorklogProperties(AsyncAPIResource):
    """Asynchronous resource for issues.worklog_properties."""

    async def get_keys(self, issue_id_or_key: str, worklog_id: str) -> PropertyKeys:
        """Get worklog property keys"""
        resp = await self._client._request(
            "GET", f"/rest/api/3/issue/{issue_id_or_key}/worklog/{worklog_id}/properties"
        )
        return PropertyKeys.model_validate(resp.json())

    async def delete(self, issue_id_or_key: str, worklog_id: str, property_key: str) -> None:
        """Delete worklog property"""
        await self._client._request(
            "DELETE",
            f"/rest/api/3/issue/{issue_id_or_key}/worklog/{worklog_id}/properties/{property_key}",
        )
        return None

    async def get(self, issue_id_or_key: str, worklog_id: str, property_key: str) -> EntityProperty:
        """Get worklog property"""
        resp = await self._client._request(
            "GET",
            f"/rest/api/3/issue/{issue_id_or_key}/worklog/{worklog_id}/properties/{property_key}",
        )
        return EntityProperty.model_validate(resp.json())

    async def set(self, issue_id_or_key: str, worklog_id: str, property_key: str) -> None:
        """Set worklog property"""
        await self._client._request(
            "PUT",
            f"/rest/api/3/issue/{issue_id_or_key}/worklog/{worklog_id}/properties/{property_key}",
        )
        return None
