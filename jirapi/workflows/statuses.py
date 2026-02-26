"""Resource classes for workflows.statuses."""

from __future__ import annotations

from jirapi._resource import AsyncAPIResource, SyncAPIResource
from jirapi.models import StatusDetails


class WorkflowStatuses(SyncAPIResource):
    """Synchronous resource for workflows.statuses."""

    def list(self) -> StatusDetails:
        """Get all statuses"""
        resp = self._client._request("GET", "/rest/api/3/status")
        return StatusDetails.model_validate(resp.json())

    def get(self, id_or_name: str) -> StatusDetails:
        """Get status"""
        resp = self._client._request("GET", f"/rest/api/3/status/{id_or_name}")
        return StatusDetails.model_validate(resp.json())


class AsyncWorkflowStatuses(AsyncAPIResource):
    """Asynchronous resource for workflows.statuses."""

    async def list(self) -> StatusDetails:
        """Get all statuses"""
        resp = await self._client._request("GET", "/rest/api/3/status")
        return StatusDetails.model_validate(resp.json())

    async def get(self, id_or_name: str) -> StatusDetails:
        """Get status"""
        resp = await self._client._request("GET", f"/rest/api/3/status/{id_or_name}")
        return StatusDetails.model_validate(resp.json())
