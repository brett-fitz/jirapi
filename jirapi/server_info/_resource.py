"""Resource classes for server_info."""

from __future__ import annotations

from jirapi._resource import AsyncAPIResource, SyncAPIResource
from jirapi.models import ServerInformation


class ServerInfo(SyncAPIResource):
    """Synchronous resource for server_info."""

    def get(self) -> ServerInformation:
        """Get Jira instance info"""
        resp = self._client._request("GET", "/rest/api/3/serverInfo")
        return ServerInformation.model_validate(resp.json())


class AsyncServerInfo(AsyncAPIResource):
    """Asynchronous resource for server_info."""

    async def get(self) -> ServerInformation:
        """Get Jira instance info"""
        resp = await self._client._request("GET", "/rest/api/3/serverInfo")
        return ServerInformation.model_validate(resp.json())
