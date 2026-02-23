"""Resource classes for the Server info API group."""

from __future__ import annotations

from jirapi._resource import AsyncAPIResource, SyncAPIResource
from jirapi.models import ServerInformation


class ServerInfo(SyncAPIResource):
    """Synchronous resource for the Server info API group."""

    def get_server_info(self) -> ServerInformation:
        """Get Jira instance info"""
        resp = self._client._request("GET", "/rest/api/3/serverInfo")
        return ServerInformation.model_validate(resp.json())


class AsyncServerInfo(AsyncAPIResource):
    """Asynchronous resource for the Server info API group."""

    async def get_server_info(self) -> ServerInformation:
        """Get Jira instance info"""
        resp = await self._client._request("GET", "/rest/api/3/serverInfo")
        return ServerInformation.model_validate(resp.json())
