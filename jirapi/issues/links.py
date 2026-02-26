"""Resource classes for issues.links."""

from __future__ import annotations

from jirapi._resource import AsyncAPIResource, SyncAPIResource
from jirapi.models import IssueLink, LinkIssueRequestJson


class IssueLinks(SyncAPIResource):
    """Synchronous resource for issues.links."""

    def create(self, body: LinkIssueRequestJson) -> None:
        """Create issue link"""
        self._client._request(
            "POST", "/rest/api/3/issueLink", json=body.model_dump(by_alias=True, exclude_none=True)
        )
        return None

    def delete(self, link_id: str) -> None:
        """Delete issue link"""
        self._client._request("DELETE", f"/rest/api/3/issueLink/{link_id}")
        return None

    def get(self, link_id: str) -> IssueLink:
        """Get issue link"""
        resp = self._client._request("GET", f"/rest/api/3/issueLink/{link_id}")
        return IssueLink.model_validate(resp.json())


class AsyncIssueLinks(AsyncAPIResource):
    """Asynchronous resource for issues.links."""

    async def create(self, body: LinkIssueRequestJson) -> None:
        """Create issue link"""
        await self._client._request(
            "POST", "/rest/api/3/issueLink", json=body.model_dump(by_alias=True, exclude_none=True)
        )
        return None

    async def delete(self, link_id: str) -> None:
        """Delete issue link"""
        await self._client._request("DELETE", f"/rest/api/3/issueLink/{link_id}")
        return None

    async def get(self, link_id: str) -> IssueLink:
        """Get issue link"""
        resp = await self._client._request("GET", f"/rest/api/3/issueLink/{link_id}")
        return IssueLink.model_validate(resp.json())
