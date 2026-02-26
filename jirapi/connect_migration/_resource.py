"""Resource classes for connect_migration."""

from __future__ import annotations

from jirapi._resource import AsyncAPIResource, SyncAPIResource
from jirapi.models import TaskProgress


class ConnectMigration(SyncAPIResource):
    """Synchronous resource for connect_migration."""

    def fetch_task(self, connect_key: str, jira_issue_fields_key: str) -> TaskProgress:
        """Get Connect issue field migration task"""
        resp = self._client._request(
            "GET", f"/rest/atlassian-connect/1/migration/{connect_key}/{jira_issue_fields_key}/task"
        )
        return TaskProgress.model_validate(resp.json())


class AsyncConnectMigration(AsyncAPIResource):
    """Asynchronous resource for connect_migration."""

    async def fetch_task(self, connect_key: str, jira_issue_fields_key: str) -> TaskProgress:
        """Get Connect issue field migration task"""
        resp = await self._client._request(
            "GET", f"/rest/atlassian-connect/1/migration/{connect_key}/{jira_issue_fields_key}/task"
        )
        return TaskProgress.model_validate(resp.json())
