"""Resource classes for issues.votes."""

from __future__ import annotations

from jirapi._resource import AsyncAPIResource, SyncAPIResource
from jirapi.models import Votes


class IssueVotes(SyncAPIResource):
    """Synchronous resource for issues.votes."""

    def remove(self, issue_id_or_key: str) -> None:
        """Delete vote"""
        self._client._request("DELETE", f"/rest/api/3/issue/{issue_id_or_key}/votes")
        return None

    def list(self, issue_id_or_key: str) -> Votes:
        """Get votes"""
        resp = self._client._request("GET", f"/rest/api/3/issue/{issue_id_or_key}/votes")
        return Votes.model_validate(resp.json())

    def add(self, issue_id_or_key: str) -> None:
        """Add vote"""
        self._client._request("POST", f"/rest/api/3/issue/{issue_id_or_key}/votes")
        return None


class AsyncIssueVotes(AsyncAPIResource):
    """Asynchronous resource for issues.votes."""

    async def remove(self, issue_id_or_key: str) -> None:
        """Delete vote"""
        await self._client._request("DELETE", f"/rest/api/3/issue/{issue_id_or_key}/votes")
        return None

    async def list(self, issue_id_or_key: str) -> Votes:
        """Get votes"""
        resp = await self._client._request("GET", f"/rest/api/3/issue/{issue_id_or_key}/votes")
        return Votes.model_validate(resp.json())

    async def add(self, issue_id_or_key: str) -> None:
        """Add vote"""
        await self._client._request("POST", f"/rest/api/3/issue/{issue_id_or_key}/votes")
        return None
