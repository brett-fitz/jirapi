"""Resource classes for fields.custom_field_associations."""

from __future__ import annotations

from jirapi._resource import AsyncAPIResource, SyncAPIResource
from jirapi.models import FieldAssociationsRequest


class FieldCustomFieldAssociations(SyncAPIResource):
    """Synchronous resource for fields.custom_field_associations."""

    def remove(self, body: FieldAssociationsRequest) -> None:
        """Remove associations"""
        self._client._request(
            "DELETE",
            "/rest/api/3/field/association",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    def create(self, body: FieldAssociationsRequest) -> None:
        """Create associations"""
        self._client._request(
            "PUT",
            "/rest/api/3/field/association",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None


class AsyncFieldCustomFieldAssociations(AsyncAPIResource):
    """Asynchronous resource for fields.custom_field_associations."""

    async def remove(self, body: FieldAssociationsRequest) -> None:
        """Remove associations"""
        await self._client._request(
            "DELETE",
            "/rest/api/3/field/association",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    async def create(self, body: FieldAssociationsRequest) -> None:
        """Create associations"""
        await self._client._request(
            "PUT",
            "/rest/api/3/field/association",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None
