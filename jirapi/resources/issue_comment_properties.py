"""Resource classes for the Issue comment properties API group."""

from __future__ import annotations

from jirapi._resource import AsyncAPIResource, SyncAPIResource
from jirapi.models import EntityProperty, PropertyKeys


class IssueCommentProperties(SyncAPIResource):
    """Synchronous resource for the Issue comment properties API group."""

    def get_comment_property_keys(self, comment_id: str) -> PropertyKeys:
        """Get comment property keys"""
        resp = self._client._request("GET", f"/rest/api/3/comment/{comment_id}/properties")
        return PropertyKeys.model_validate(resp.json())

    def delete_comment_property(self, comment_id: str, property_key: str) -> None:
        """Delete comment property"""
        self._client._request(
            "DELETE", f"/rest/api/3/comment/{comment_id}/properties/{property_key}"
        )
        return None

    def get_comment_property(self, comment_id: str, property_key: str) -> EntityProperty:
        """Get comment property"""
        resp = self._client._request(
            "GET", f"/rest/api/3/comment/{comment_id}/properties/{property_key}"
        )
        return EntityProperty.model_validate(resp.json())

    def set_comment_property(self, comment_id: str, property_key: str) -> None:
        """Set comment property"""
        self._client._request("PUT", f"/rest/api/3/comment/{comment_id}/properties/{property_key}")
        return None


class AsyncIssueCommentProperties(AsyncAPIResource):
    """Asynchronous resource for the Issue comment properties API group."""

    async def get_comment_property_keys(self, comment_id: str) -> PropertyKeys:
        """Get comment property keys"""
        resp = await self._client._request("GET", f"/rest/api/3/comment/{comment_id}/properties")
        return PropertyKeys.model_validate(resp.json())

    async def delete_comment_property(self, comment_id: str, property_key: str) -> None:
        """Delete comment property"""
        await self._client._request(
            "DELETE", f"/rest/api/3/comment/{comment_id}/properties/{property_key}"
        )
        return None

    async def get_comment_property(self, comment_id: str, property_key: str) -> EntityProperty:
        """Get comment property"""
        resp = await self._client._request(
            "GET", f"/rest/api/3/comment/{comment_id}/properties/{property_key}"
        )
        return EntityProperty.model_validate(resp.json())

    async def set_comment_property(self, comment_id: str, property_key: str) -> None:
        """Set comment property"""
        await self._client._request(
            "PUT", f"/rest/api/3/comment/{comment_id}/properties/{property_key}"
        )
        return None
