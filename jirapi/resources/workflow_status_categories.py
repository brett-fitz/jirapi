"""Resource classes for the Workflow status categories API group."""

from __future__ import annotations

from jirapi._resource import AsyncAPIResource, SyncAPIResource
from jirapi.models import StatusCategory


class WorkflowStatusCategories(SyncAPIResource):
    """Synchronous resource for the Workflow status categories API group."""

    def get_status_categories(self) -> StatusCategory:
        """Get all status categories"""
        resp = self._client._request("GET", "/rest/api/3/statuscategory")
        return StatusCategory.model_validate(resp.json())

    def get_status_category(self, id_or_key: str) -> StatusCategory:
        """Get status category"""
        resp = self._client._request("GET", f"/rest/api/3/statuscategory/{id_or_key}")
        return StatusCategory.model_validate(resp.json())


class AsyncWorkflowStatusCategories(AsyncAPIResource):
    """Asynchronous resource for the Workflow status categories API group."""

    async def get_status_categories(self) -> StatusCategory:
        """Get all status categories"""
        resp = await self._client._request("GET", "/rest/api/3/statuscategory")
        return StatusCategory.model_validate(resp.json())

    async def get_status_category(self, id_or_key: str) -> StatusCategory:
        """Get status category"""
        resp = await self._client._request("GET", f"/rest/api/3/statuscategory/{id_or_key}")
        return StatusCategory.model_validate(resp.json())
