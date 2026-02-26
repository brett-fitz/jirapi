"""Resource classes for classification_levels."""

from __future__ import annotations

from jirapi._resource import AsyncAPIResource, SyncAPIResource
from jirapi.models import DataClassificationLevels


class ClassificationLevels(SyncAPIResource):
    """Synchronous resource for classification_levels."""

    def get_all_user_data(
        self, *, status: list[str] | None = None, order_by: str | None = None
    ) -> DataClassificationLevels:
        """Get all classification levels"""
        params = self._client._build_params(**{"status": status, "orderBy": order_by})
        resp = self._client._request("GET", "/rest/api/3/classification-levels", params=params)
        return DataClassificationLevels.model_validate(resp.json())


class AsyncClassificationLevels(AsyncAPIResource):
    """Asynchronous resource for classification_levels."""

    async def get_all_user_data(
        self, *, status: list[str] | None = None, order_by: str | None = None
    ) -> DataClassificationLevels:
        """Get all classification levels"""
        params = self._client._build_params(**{"status": status, "orderBy": order_by})
        resp = await self._client._request(
            "GET", "/rest/api/3/classification-levels", params=params
        )
        return DataClassificationLevels.model_validate(resp.json())
