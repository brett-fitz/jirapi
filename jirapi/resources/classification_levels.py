"""Resource classes for the Classification levels API group."""

from __future__ import annotations

from jirapi._resource import AsyncAPIResource, SyncAPIResource
from jirapi.models import DataClassificationLevelsBean


class ClassificationLevels(SyncAPIResource):
    """Synchronous resource for the Classification levels API group."""

    def get_all_user_data_classification_levels(
        self, *, status: list[str] | None = None, order_by: str | None = None
    ) -> DataClassificationLevelsBean:
        """Get all classification levels"""
        params = self._client._build_params(**{"status": status, "orderBy": order_by})
        resp = self._client._request("GET", "/rest/api/3/classification-levels", params=params)
        return DataClassificationLevelsBean.model_validate(resp.json())


class AsyncClassificationLevels(AsyncAPIResource):
    """Asynchronous resource for the Classification levels API group."""

    async def get_all_user_data_classification_levels(
        self, *, status: list[str] | None = None, order_by: str | None = None
    ) -> DataClassificationLevelsBean:
        """Get all classification levels"""
        params = self._client._build_params(**{"status": status, "orderBy": order_by})
        resp = await self._client._request(
            "GET", "/rest/api/3/classification-levels", params=params
        )
        return DataClassificationLevelsBean.model_validate(resp.json())
