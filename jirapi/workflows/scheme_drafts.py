"""Resource classes for workflows.scheme_drafts."""

from __future__ import annotations

from jirapi._resource import AsyncAPIResource, SyncAPIResource
from jirapi.models import (
    DefaultWorkflow,
    IssueTypesWorkflowMapping,
    IssueTypeWorkflowMapping,
    PublishDraftWorkflowScheme,
    WorkflowScheme,
)


class WorkflowSchemeDrafts(SyncAPIResource):
    """Synchronous resource for workflows.scheme_drafts."""

    def create_from_parent(self, id_: str) -> WorkflowScheme:
        """Create draft workflow scheme"""
        resp = self._client._request("POST", f"/rest/api/3/workflowscheme/{id_}/createdraft")
        return WorkflowScheme.model_validate(resp.json())

    def delete(self, id_: str) -> None:
        """Delete draft workflow scheme"""
        self._client._request("DELETE", f"/rest/api/3/workflowscheme/{id_}/draft")
        return None

    def get(self, id_: str) -> WorkflowScheme:
        """Get draft workflow scheme"""
        resp = self._client._request("GET", f"/rest/api/3/workflowscheme/{id_}/draft")
        return WorkflowScheme.model_validate(resp.json())

    def update(self, id_: str, body: WorkflowScheme) -> WorkflowScheme:
        """Update draft workflow scheme"""
        resp = self._client._request(
            "PUT",
            f"/rest/api/3/workflowscheme/{id_}/draft",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return WorkflowScheme.model_validate(resp.json())

    def delete_default_workflow(self, id_: str) -> WorkflowScheme:
        """Delete draft default workflow"""
        resp = self._client._request("DELETE", f"/rest/api/3/workflowscheme/{id_}/draft/default")
        return WorkflowScheme.model_validate(resp.json())

    def get_default_workflow(self, id_: str) -> DefaultWorkflow:
        """Get draft default workflow"""
        resp = self._client._request("GET", f"/rest/api/3/workflowscheme/{id_}/draft/default")
        return DefaultWorkflow.model_validate(resp.json())

    def update_default_workflow(self, id_: str, body: DefaultWorkflow) -> WorkflowScheme:
        """Update draft default workflow"""
        resp = self._client._request(
            "PUT",
            f"/rest/api/3/workflowscheme/{id_}/draft/default",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return WorkflowScheme.model_validate(resp.json())

    def delete_issue_type(self, id_: str, issue_type: str) -> WorkflowScheme:
        """Delete workflow for issue type in draft workflow scheme"""
        resp = self._client._request(
            "DELETE", f"/rest/api/3/workflowscheme/{id_}/draft/issuetype/{issue_type}"
        )
        return WorkflowScheme.model_validate(resp.json())

    def get_issue_type(self, id_: str, issue_type: str) -> IssueTypeWorkflowMapping:
        """Get workflow for issue type in draft workflow scheme"""
        resp = self._client._request(
            "GET", f"/rest/api/3/workflowscheme/{id_}/draft/issuetype/{issue_type}"
        )
        return IssueTypeWorkflowMapping.model_validate(resp.json())

    def set_issue_type(
        self, id_: str, issue_type: str, body: IssueTypeWorkflowMapping
    ) -> WorkflowScheme:
        """Set workflow for issue type in draft workflow scheme"""
        resp = self._client._request(
            "PUT",
            f"/rest/api/3/workflowscheme/{id_}/draft/issuetype/{issue_type}",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return WorkflowScheme.model_validate(resp.json())

    def publish(
        self, id_: str, body: PublishDraftWorkflowScheme, *, validate_only: bool | None = None
    ) -> None:
        """Publish draft workflow scheme"""
        params = self._client._build_params(**{"validateOnly": validate_only})
        self._client._request(
            "POST",
            f"/rest/api/3/workflowscheme/{id_}/draft/publish",
            params=params,
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    def delete_mapping(self, id_: str, *, workflow_name: str) -> None:
        """Delete issue types for workflow in draft workflow scheme"""
        params = self._client._build_params(**{"workflowName": workflow_name})
        self._client._request(
            "DELETE", f"/rest/api/3/workflowscheme/{id_}/draft/workflow", params=params
        )
        return None

    def get_workflow(
        self, id_: str, *, workflow_name: str | None = None
    ) -> IssueTypesWorkflowMapping:
        """Get issue types for workflows in draft workflow scheme"""
        params = self._client._build_params(**{"workflowName": workflow_name})
        resp = self._client._request(
            "GET", f"/rest/api/3/workflowscheme/{id_}/draft/workflow", params=params
        )
        return IssueTypesWorkflowMapping.model_validate(resp.json())

    def update_mapping(
        self, id_: str, body: IssueTypesWorkflowMapping, *, workflow_name: str
    ) -> WorkflowScheme:
        """Set issue types for workflow in workflow scheme"""
        params = self._client._build_params(**{"workflowName": workflow_name})
        resp = self._client._request(
            "PUT",
            f"/rest/api/3/workflowscheme/{id_}/draft/workflow",
            params=params,
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return WorkflowScheme.model_validate(resp.json())


class AsyncWorkflowSchemeDrafts(AsyncAPIResource):
    """Asynchronous resource for workflows.scheme_drafts."""

    async def create_from_parent(self, id_: str) -> WorkflowScheme:
        """Create draft workflow scheme"""
        resp = await self._client._request("POST", f"/rest/api/3/workflowscheme/{id_}/createdraft")
        return WorkflowScheme.model_validate(resp.json())

    async def delete(self, id_: str) -> None:
        """Delete draft workflow scheme"""
        await self._client._request("DELETE", f"/rest/api/3/workflowscheme/{id_}/draft")
        return None

    async def get(self, id_: str) -> WorkflowScheme:
        """Get draft workflow scheme"""
        resp = await self._client._request("GET", f"/rest/api/3/workflowscheme/{id_}/draft")
        return WorkflowScheme.model_validate(resp.json())

    async def update(self, id_: str, body: WorkflowScheme) -> WorkflowScheme:
        """Update draft workflow scheme"""
        resp = await self._client._request(
            "PUT",
            f"/rest/api/3/workflowscheme/{id_}/draft",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return WorkflowScheme.model_validate(resp.json())

    async def delete_default_workflow(self, id_: str) -> WorkflowScheme:
        """Delete draft default workflow"""
        resp = await self._client._request(
            "DELETE", f"/rest/api/3/workflowscheme/{id_}/draft/default"
        )
        return WorkflowScheme.model_validate(resp.json())

    async def get_default_workflow(self, id_: str) -> DefaultWorkflow:
        """Get draft default workflow"""
        resp = await self._client._request("GET", f"/rest/api/3/workflowscheme/{id_}/draft/default")
        return DefaultWorkflow.model_validate(resp.json())

    async def update_default_workflow(self, id_: str, body: DefaultWorkflow) -> WorkflowScheme:
        """Update draft default workflow"""
        resp = await self._client._request(
            "PUT",
            f"/rest/api/3/workflowscheme/{id_}/draft/default",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return WorkflowScheme.model_validate(resp.json())

    async def delete_issue_type(self, id_: str, issue_type: str) -> WorkflowScheme:
        """Delete workflow for issue type in draft workflow scheme"""
        resp = await self._client._request(
            "DELETE", f"/rest/api/3/workflowscheme/{id_}/draft/issuetype/{issue_type}"
        )
        return WorkflowScheme.model_validate(resp.json())

    async def get_issue_type(self, id_: str, issue_type: str) -> IssueTypeWorkflowMapping:
        """Get workflow for issue type in draft workflow scheme"""
        resp = await self._client._request(
            "GET", f"/rest/api/3/workflowscheme/{id_}/draft/issuetype/{issue_type}"
        )
        return IssueTypeWorkflowMapping.model_validate(resp.json())

    async def set_issue_type(
        self, id_: str, issue_type: str, body: IssueTypeWorkflowMapping
    ) -> WorkflowScheme:
        """Set workflow for issue type in draft workflow scheme"""
        resp = await self._client._request(
            "PUT",
            f"/rest/api/3/workflowscheme/{id_}/draft/issuetype/{issue_type}",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return WorkflowScheme.model_validate(resp.json())

    async def publish(
        self, id_: str, body: PublishDraftWorkflowScheme, *, validate_only: bool | None = None
    ) -> None:
        """Publish draft workflow scheme"""
        params = self._client._build_params(**{"validateOnly": validate_only})
        await self._client._request(
            "POST",
            f"/rest/api/3/workflowscheme/{id_}/draft/publish",
            params=params,
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    async def delete_mapping(self, id_: str, *, workflow_name: str) -> None:
        """Delete issue types for workflow in draft workflow scheme"""
        params = self._client._build_params(**{"workflowName": workflow_name})
        await self._client._request(
            "DELETE", f"/rest/api/3/workflowscheme/{id_}/draft/workflow", params=params
        )
        return None

    async def get_workflow(
        self, id_: str, *, workflow_name: str | None = None
    ) -> IssueTypesWorkflowMapping:
        """Get issue types for workflows in draft workflow scheme"""
        params = self._client._build_params(**{"workflowName": workflow_name})
        resp = await self._client._request(
            "GET", f"/rest/api/3/workflowscheme/{id_}/draft/workflow", params=params
        )
        return IssueTypesWorkflowMapping.model_validate(resp.json())

    async def update_mapping(
        self, id_: str, body: IssueTypesWorkflowMapping, *, workflow_name: str
    ) -> WorkflowScheme:
        """Set issue types for workflow in workflow scheme"""
        params = self._client._build_params(**{"workflowName": workflow_name})
        resp = await self._client._request(
            "PUT",
            f"/rest/api/3/workflowscheme/{id_}/draft/workflow",
            params=params,
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return WorkflowScheme.model_validate(resp.json())
