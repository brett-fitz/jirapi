"""Resource classes for the Labels API group."""

from __future__ import annotations

from jirapi._resource import AsyncAPIResource, SyncAPIResource
from jirapi.models import PageBeanString


class Labels(SyncAPIResource):
    """Synchronous resource for the Labels API group."""

    def get_all_labels(
        self, *, start_at: int | None = None, max_results: int | None = None
    ) -> PageBeanString:
        """Get all labels"""
        params = self._client._build_params(**{"startAt": start_at, "maxResults": max_results})
        resp = self._client._request("GET", "/rest/api/3/label", params=params)
        return PageBeanString.model_validate(resp.json())


class AsyncLabels(AsyncAPIResource):
    """Asynchronous resource for the Labels API group."""

    async def get_all_labels(
        self, *, start_at: int | None = None, max_results: int | None = None
    ) -> PageBeanString:
        """Get all labels"""
        params = self._client._build_params(**{"startAt": start_at, "maxResults": max_results})
        resp = await self._client._request("GET", "/rest/api/3/label", params=params)
        return PageBeanString.model_validate(resp.json())
