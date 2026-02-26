"""Resource classes for workflows.scheme_project_associations."""

from __future__ import annotations

from jirapi._resource import AsyncAPIResource, SyncAPIResource
from jirapi.models import ContainerOfWorkflowSchemeAssociations, WorkflowSchemeProjectAssociation


class WorkflowSchemeProjectAssociations(SyncAPIResource):
    """Synchronous resource for workflows.scheme_project_associations."""

    def list(self, *, project_id: list[str]) -> ContainerOfWorkflowSchemeAssociations:
        """Get workflow scheme project associations"""
        params = self._client._build_params(**{"projectId": project_id})
        resp = self._client._request("GET", "/rest/api/3/workflowscheme/project", params=params)
        return ContainerOfWorkflowSchemeAssociations.model_validate(resp.json())

    def assign(self, body: WorkflowSchemeProjectAssociation) -> None:
        """Assign workflow scheme to project"""
        self._client._request(
            "PUT",
            "/rest/api/3/workflowscheme/project",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None


class AsyncWorkflowSchemeProjectAssociations(AsyncAPIResource):
    """Asynchronous resource for workflows.scheme_project_associations."""

    async def list(self, *, project_id: list[str]) -> ContainerOfWorkflowSchemeAssociations:
        """Get workflow scheme project associations"""
        params = self._client._build_params(**{"projectId": project_id})
        resp = await self._client._request(
            "GET", "/rest/api/3/workflowscheme/project", params=params
        )
        return ContainerOfWorkflowSchemeAssociations.model_validate(resp.json())

    async def assign(self, body: WorkflowSchemeProjectAssociation) -> None:
        """Assign workflow scheme to project"""
        await self._client._request(
            "PUT",
            "/rest/api/3/workflowscheme/project",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None
