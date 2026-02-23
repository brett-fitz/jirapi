"""Resource classes for the Issue priorities API group."""

from __future__ import annotations

from jirapi._resource import AsyncAPIResource, SyncAPIResource
from jirapi.models import Priority, ReorderIssuePriorities, SetDefaultPriorityRequest


class IssuePriorities(SyncAPIResource):
    """Synchronous resource for the Issue priorities API group."""

    def set_default_priority(self, body: SetDefaultPriorityRequest) -> None:
        """Set default priority"""
        self._client._request(
            "PUT",
            "/rest/api/3/priority/default",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    def move_priorities(self, body: ReorderIssuePriorities) -> None:
        """Move priorities"""
        self._client._request(
            "PUT",
            "/rest/api/3/priority/move",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    def delete_priority(self, id_: str) -> None:
        """Delete priority"""
        self._client._request("DELETE", f"/rest/api/3/priority/{id_}")
        return None

    def get_priority(self, id_: str) -> Priority:
        """Get priority"""
        resp = self._client._request("GET", f"/rest/api/3/priority/{id_}")
        return Priority.model_validate(resp.json())


class AsyncIssuePriorities(AsyncAPIResource):
    """Asynchronous resource for the Issue priorities API group."""

    async def set_default_priority(self, body: SetDefaultPriorityRequest) -> None:
        """Set default priority"""
        await self._client._request(
            "PUT",
            "/rest/api/3/priority/default",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    async def move_priorities(self, body: ReorderIssuePriorities) -> None:
        """Move priorities"""
        await self._client._request(
            "PUT",
            "/rest/api/3/priority/move",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    async def delete_priority(self, id_: str) -> None:
        """Delete priority"""
        await self._client._request("DELETE", f"/rest/api/3/priority/{id_}")
        return None

    async def get_priority(self, id_: str) -> Priority:
        """Get priority"""
        resp = await self._client._request("GET", f"/rest/api/3/priority/{id_}")
        return Priority.model_validate(resp.json())
