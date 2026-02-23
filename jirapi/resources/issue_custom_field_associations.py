"""Resource classes for the Issue custom field associations API group."""

from __future__ import annotations

from jirapi._resource import AsyncAPIResource, SyncAPIResource
from jirapi.models import FieldAssociationsRequest


class IssueCustomFieldAssociations(SyncAPIResource):
    """Synchronous resource for the Issue custom field associations API group."""

    def remove_associations(self, body: FieldAssociationsRequest) -> None:
        """Remove associations"""
        resp = self._client._request(
            "DELETE",
            "/rest/api/3/field/association",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    def create_associations(self, body: FieldAssociationsRequest) -> None:
        """Create associations"""
        resp = self._client._request(
            "PUT",
            "/rest/api/3/field/association",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None


class AsyncIssueCustomFieldAssociations(AsyncAPIResource):
    """Asynchronous resource for the Issue custom field associations API group."""

    async def remove_associations(self, body: FieldAssociationsRequest) -> None:
        """Remove associations"""
        resp = await self._client._request(
            "DELETE",
            "/rest/api/3/field/association",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    async def create_associations(self, body: FieldAssociationsRequest) -> None:
        """Create associations"""
        resp = await self._client._request(
            "PUT",
            "/rest/api/3/field/association",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None
