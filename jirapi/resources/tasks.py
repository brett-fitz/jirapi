"""Resource classes for the Tasks API group."""

from __future__ import annotations

from jirapi._resource import AsyncAPIResource, SyncAPIResource
from jirapi.models import TaskProgressBeanObject


class Tasks(SyncAPIResource):
    """Synchronous resource for the Tasks API group."""

    def get_task(self, task_id: str) -> TaskProgressBeanObject:
        """Get task"""
        resp = self._client._request("GET", f"/rest/api/3/task/{task_id}")
        return TaskProgressBeanObject.model_validate(resp.json())

    def cancel_task(self, task_id: str) -> None:
        """Cancel task"""
        resp = self._client._request("POST", f"/rest/api/3/task/{task_id}/cancel")
        return None


class AsyncTasks(AsyncAPIResource):
    """Asynchronous resource for the Tasks API group."""

    async def get_task(self, task_id: str) -> TaskProgressBeanObject:
        """Get task"""
        resp = await self._client._request("GET", f"/rest/api/3/task/{task_id}")
        return TaskProgressBeanObject.model_validate(resp.json())

    async def cancel_task(self, task_id: str) -> None:
        """Cancel task"""
        resp = await self._client._request("POST", f"/rest/api/3/task/{task_id}/cancel")
        return None
