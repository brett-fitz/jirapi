"""Resource classes for the Issue links API group."""

from __future__ import annotations

from jirapi._resource import AsyncAPIResource, SyncAPIResource
from jirapi.models import IssueLink, LinkIssueRequestJsonBean


class IssueLinks(SyncAPIResource):
    """Synchronous resource for the Issue links API group."""

    def link_issues(self, body: LinkIssueRequestJsonBean) -> None:
        """Create issue link"""
        resp = self._client._request(
            "POST", "/rest/api/3/issueLink", json=body.model_dump(by_alias=True, exclude_none=True)
        )
        return None

    def delete_issue_link(self, link_id: str) -> None:
        """Delete issue link"""
        resp = self._client._request("DELETE", f"/rest/api/3/issueLink/{link_id}")
        return None

    def get_issue_link(self, link_id: str) -> IssueLink:
        """Get issue link"""
        resp = self._client._request("GET", f"/rest/api/3/issueLink/{link_id}")
        return IssueLink.model_validate(resp.json())


class AsyncIssueLinks(AsyncAPIResource):
    """Asynchronous resource for the Issue links API group."""

    async def link_issues(self, body: LinkIssueRequestJsonBean) -> None:
        """Create issue link"""
        resp = await self._client._request(
            "POST", "/rest/api/3/issueLink", json=body.model_dump(by_alias=True, exclude_none=True)
        )
        return None

    async def delete_issue_link(self, link_id: str) -> None:
        """Delete issue link"""
        resp = await self._client._request("DELETE", f"/rest/api/3/issueLink/{link_id}")
        return None

    async def get_issue_link(self, link_id: str) -> IssueLink:
        """Get issue link"""
        resp = await self._client._request("GET", f"/rest/api/3/issueLink/{link_id}")
        return IssueLink.model_validate(resp.json())
