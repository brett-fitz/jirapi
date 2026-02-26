"""Resource classes for app_data_policies."""

from __future__ import annotations

from jirapi._resource import AsyncAPIResource, SyncAPIResource
from jirapi.models import ProjectDataPolicies, WorkspaceDataPolicy


class AppDataPolicies(SyncAPIResource):
    """Synchronous resource for app_data_policies."""

    def get_policy(self) -> WorkspaceDataPolicy:
        """Get data policy for the workspace"""
        resp = self._client._request("GET", "/rest/api/3/data-policy")
        return WorkspaceDataPolicy.model_validate(resp.json())

    def get_policies(self, *, ids: str | None = None) -> ProjectDataPolicies:
        """Get data policy for projects"""
        params = self._client._build_params(**{"ids": ids})
        resp = self._client._request("GET", "/rest/api/3/data-policy/project", params=params)
        return ProjectDataPolicies.model_validate(resp.json())


class AsyncAppDataPolicies(AsyncAPIResource):
    """Asynchronous resource for app_data_policies."""

    async def get_policy(self) -> WorkspaceDataPolicy:
        """Get data policy for the workspace"""
        resp = await self._client._request("GET", "/rest/api/3/data-policy")
        return WorkspaceDataPolicy.model_validate(resp.json())

    async def get_policies(self, *, ids: str | None = None) -> ProjectDataPolicies:
        """Get data policy for projects"""
        params = self._client._build_params(**{"ids": ids})
        resp = await self._client._request("GET", "/rest/api/3/data-policy/project", params=params)
        return ProjectDataPolicies.model_validate(resp.json())
