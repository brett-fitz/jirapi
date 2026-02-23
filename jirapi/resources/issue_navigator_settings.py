"""Resource classes for the Issue navigator settings API group."""

from __future__ import annotations

from jirapi._resource import AsyncAPIResource, SyncAPIResource
from jirapi.models import ColumnItem


class IssueNavigatorSettings(SyncAPIResource):
    """Synchronous resource for the Issue navigator settings API group."""

    def get_issue_navigator_default_columns(self) -> ColumnItem:
        """Get issue navigator default columns"""
        resp = self._client._request("GET", "/rest/api/3/settings/columns")
        return ColumnItem.model_validate(resp.json())

    def set_issue_navigator_default_columns(self) -> None:
        """Set issue navigator default columns"""
        resp = self._client._request("PUT", "/rest/api/3/settings/columns")
        return None


class AsyncIssueNavigatorSettings(AsyncAPIResource):
    """Asynchronous resource for the Issue navigator settings API group."""

    async def get_issue_navigator_default_columns(self) -> ColumnItem:
        """Get issue navigator default columns"""
        resp = await self._client._request("GET", "/rest/api/3/settings/columns")
        return ColumnItem.model_validate(resp.json())

    async def set_issue_navigator_default_columns(self) -> None:
        """Set issue navigator default columns"""
        resp = await self._client._request("PUT", "/rest/api/3/settings/columns")
        return None
