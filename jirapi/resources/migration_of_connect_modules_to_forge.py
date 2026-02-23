"""Resource classes for the Migration of Connect modules to Forge API group."""

from __future__ import annotations

from jirapi._resource import AsyncAPIResource, SyncAPIResource
from jirapi.models import TaskProgress


class MigrationOfConnectModulesToForge(SyncAPIResource):
    """Synchronous resource for the Migration of Connect modules to Forge API group."""

    def fetch_migration_task_get(
        self, connect_key: str, jira_issue_fields_key: str
    ) -> TaskProgress:
        """Get Connect issue field migration task"""
        resp = self._client._request(
            "GET", f"/rest/atlassian-connect/1/migration/{connect_key}/{jira_issue_fields_key}/task"
        )
        return TaskProgress.model_validate(resp.json())


class AsyncMigrationOfConnectModulesToForge(AsyncAPIResource):
    """Asynchronous resource for the Migration of Connect modules to Forge API group."""

    async def fetch_migration_task_get(
        self, connect_key: str, jira_issue_fields_key: str
    ) -> TaskProgress:
        """Get Connect issue field migration task"""
        resp = await self._client._request(
            "GET", f"/rest/atlassian-connect/1/migration/{connect_key}/{jira_issue_fields_key}/task"
        )
        return TaskProgress.model_validate(resp.json())
