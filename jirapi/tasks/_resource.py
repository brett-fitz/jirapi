"""Resource classes for tasks."""

from __future__ import annotations

from jirapi._resource import AsyncAPIResource, SyncAPIResource
from jirapi.models import TaskProgressBeanObject


class Tasks(SyncAPIResource):
    """Synchronous resource for tasks."""

    def get(self, task_id: str) -> TaskProgressBeanObject:
        """Get task"""
        resp = self._client._request("GET", f"/rest/api/3/task/{task_id}")
        return TaskProgressBeanObject.model_validate(resp.json())

    def cancel(self, task_id: str) -> None:
        """Cancel task"""
        self._client._request("POST", f"/rest/api/3/task/{task_id}/cancel")
        return None


class AsyncTasks(AsyncAPIResource):
    """Asynchronous resource for tasks."""

    async def get(self, task_id: str) -> TaskProgressBeanObject:
        """Get task"""
        resp = await self._client._request("GET", f"/rest/api/3/task/{task_id}")
        return TaskProgressBeanObject.model_validate(resp.json())

    async def cancel(self, task_id: str) -> None:
        """Cancel task"""
        await self._client._request("POST", f"/rest/api/3/task/{task_id}/cancel")
        return None
