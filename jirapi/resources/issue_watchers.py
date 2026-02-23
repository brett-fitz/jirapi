"""Resource classes for the Issue watchers API group."""

from __future__ import annotations

from jirapi._resource import AsyncAPIResource, SyncAPIResource
from jirapi.models import BulkIssueIsWatching, IssueList, Watchers


class IssueWatchers(SyncAPIResource):
    """Synchronous resource for the Issue watchers API group."""

    def get_is_watching_issue_bulk(self, body: IssueList) -> BulkIssueIsWatching:
        """Get is watching issue bulk"""
        resp = self._client._request(
            "POST",
            "/rest/api/3/issue/watching",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return BulkIssueIsWatching.model_validate(resp.json())

    def remove_watcher(
        self, issue_id_or_key: str, *, username: str | None = None, account_id: str | None = None
    ) -> None:
        """Delete watcher"""
        params = self._client._build_params(**{"username": username, "accountId": account_id})
        resp = self._client._request(
            "DELETE", f"/rest/api/3/issue/{issue_id_or_key}/watchers", params=params
        )
        return None

    def get_issue_watchers(self, issue_id_or_key: str) -> Watchers:
        """Get issue watchers"""
        resp = self._client._request("GET", f"/rest/api/3/issue/{issue_id_or_key}/watchers")
        return Watchers.model_validate(resp.json())

    def add_watcher(self, issue_id_or_key: str) -> None:
        """Add watcher"""
        resp = self._client._request("POST", f"/rest/api/3/issue/{issue_id_or_key}/watchers")
        return None


class AsyncIssueWatchers(AsyncAPIResource):
    """Asynchronous resource for the Issue watchers API group."""

    async def get_is_watching_issue_bulk(self, body: IssueList) -> BulkIssueIsWatching:
        """Get is watching issue bulk"""
        resp = await self._client._request(
            "POST",
            "/rest/api/3/issue/watching",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return BulkIssueIsWatching.model_validate(resp.json())

    async def remove_watcher(
        self, issue_id_or_key: str, *, username: str | None = None, account_id: str | None = None
    ) -> None:
        """Delete watcher"""
        params = self._client._build_params(**{"username": username, "accountId": account_id})
        resp = await self._client._request(
            "DELETE", f"/rest/api/3/issue/{issue_id_or_key}/watchers", params=params
        )
        return None

    async def get_issue_watchers(self, issue_id_or_key: str) -> Watchers:
        """Get issue watchers"""
        resp = await self._client._request("GET", f"/rest/api/3/issue/{issue_id_or_key}/watchers")
        return Watchers.model_validate(resp.json())

    async def add_watcher(self, issue_id_or_key: str) -> None:
        """Add watcher"""
        resp = await self._client._request("POST", f"/rest/api/3/issue/{issue_id_or_key}/watchers")
        return None
