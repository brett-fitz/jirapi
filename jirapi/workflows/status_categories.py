"""Resource classes for workflows.status_categories."""

from __future__ import annotations

from jirapi._resource import AsyncAPIResource, SyncAPIResource
from jirapi.models import StatusCategory3


class WorkflowStatusCategories(SyncAPIResource):
    """Synchronous resource for workflows.status_categories."""

    def list(self) -> list[StatusCategory3]:
        """Get all status categories"""
        resp = self._client._request("GET", "/rest/api/3/statuscategory")
        return [StatusCategory3.model_validate(item) for item in resp.json()]

    def get(self, id_or_key: str) -> StatusCategory3:
        """Get status category"""
        resp = self._client._request("GET", f"/rest/api/3/statuscategory/{id_or_key}")
        return StatusCategory3.model_validate(resp.json())


class AsyncWorkflowStatusCategories(AsyncAPIResource):
    """Asynchronous resource for workflows.status_categories."""

    async def list(self) -> list[StatusCategory3]:
        """Get all status categories"""
        resp = await self._client._request("GET", "/rest/api/3/statuscategory")
        return [StatusCategory3.model_validate(item) for item in resp.json()]

    async def get(self, id_or_key: str) -> StatusCategory3:
        """Get status category"""
        resp = await self._client._request("GET", f"/rest/api/3/statuscategory/{id_or_key}")
        return StatusCategory3.model_validate(resp.json())
