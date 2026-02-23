"""Resource classes for the Issue votes API group."""

from __future__ import annotations

from jirapi._resource import AsyncAPIResource, SyncAPIResource
from jirapi.models import Votes


class IssueVotes(SyncAPIResource):
    """Synchronous resource for the Issue votes API group."""

    def remove_vote(self, issue_id_or_key: str) -> None:
        """Delete vote"""
        resp = self._client._request("DELETE", f"/rest/api/3/issue/{issue_id_or_key}/votes")
        return None

    def get_votes(self, issue_id_or_key: str) -> Votes:
        """Get votes"""
        resp = self._client._request("GET", f"/rest/api/3/issue/{issue_id_or_key}/votes")
        return Votes.model_validate(resp.json())

    def add_vote(self, issue_id_or_key: str) -> None:
        """Add vote"""
        resp = self._client._request("POST", f"/rest/api/3/issue/{issue_id_or_key}/votes")
        return None


class AsyncIssueVotes(AsyncAPIResource):
    """Asynchronous resource for the Issue votes API group."""

    async def remove_vote(self, issue_id_or_key: str) -> None:
        """Delete vote"""
        resp = await self._client._request("DELETE", f"/rest/api/3/issue/{issue_id_or_key}/votes")
        return None

    async def get_votes(self, issue_id_or_key: str) -> Votes:
        """Get votes"""
        resp = await self._client._request("GET", f"/rest/api/3/issue/{issue_id_or_key}/votes")
        return Votes.model_validate(resp.json())

    async def add_vote(self, issue_id_or_key: str) -> None:
        """Add vote"""
        resp = await self._client._request("POST", f"/rest/api/3/issue/{issue_id_or_key}/votes")
        return None
