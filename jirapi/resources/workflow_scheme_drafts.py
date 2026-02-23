"""Resource classes for the Workflow scheme drafts API group."""

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
    """Synchronous resource for the Workflow scheme drafts API group."""

    def create_workflow_scheme_draft_from_parent(self, id_: str) -> WorkflowScheme:
        """Create draft workflow scheme"""
        resp = self._client._request("POST", f"/rest/api/3/workflowscheme/{id_}/createdraft")
        return WorkflowScheme.model_validate(resp.json())

    def delete_workflow_scheme_draft(self, id_: str) -> None:
        """Delete draft workflow scheme"""
        resp = self._client._request("DELETE", f"/rest/api/3/workflowscheme/{id_}/draft")
        return None

    def get_workflow_scheme_draft(self, id_: str) -> WorkflowScheme:
        """Get draft workflow scheme"""
        resp = self._client._request("GET", f"/rest/api/3/workflowscheme/{id_}/draft")
        return WorkflowScheme.model_validate(resp.json())

    def update_workflow_scheme_draft(self, id_: str, body: WorkflowScheme) -> WorkflowScheme:
        """Update draft workflow scheme"""
        resp = self._client._request(
            "PUT",
            f"/rest/api/3/workflowscheme/{id_}/draft",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return WorkflowScheme.model_validate(resp.json())

    def delete_draft_default_workflow(self, id_: str) -> WorkflowScheme:
        """Delete draft default workflow"""
        resp = self._client._request("DELETE", f"/rest/api/3/workflowscheme/{id_}/draft/default")
        return WorkflowScheme.model_validate(resp.json())

    def get_draft_default_workflow(self, id_: str) -> DefaultWorkflow:
        """Get draft default workflow"""
        resp = self._client._request("GET", f"/rest/api/3/workflowscheme/{id_}/draft/default")
        return DefaultWorkflow.model_validate(resp.json())

    def update_draft_default_workflow(self, id_: str, body: DefaultWorkflow) -> WorkflowScheme:
        """Update draft default workflow"""
        resp = self._client._request(
            "PUT",
            f"/rest/api/3/workflowscheme/{id_}/draft/default",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return WorkflowScheme.model_validate(resp.json())

    def delete_workflow_scheme_draft_issue_type(self, id_: str, issue_type: str) -> WorkflowScheme:
        """Delete workflow for issue type in draft workflow scheme"""
        resp = self._client._request(
            "DELETE", f"/rest/api/3/workflowscheme/{id_}/draft/issuetype/{issue_type}"
        )
        return WorkflowScheme.model_validate(resp.json())

    def get_workflow_scheme_draft_issue_type(
        self, id_: str, issue_type: str
    ) -> IssueTypeWorkflowMapping:
        """Get workflow for issue type in draft workflow scheme"""
        resp = self._client._request(
            "GET", f"/rest/api/3/workflowscheme/{id_}/draft/issuetype/{issue_type}"
        )
        return IssueTypeWorkflowMapping.model_validate(resp.json())

    def set_workflow_scheme_draft_issue_type(
        self, id_: str, issue_type: str, body: IssueTypeWorkflowMapping
    ) -> WorkflowScheme:
        """Set workflow for issue type in draft workflow scheme"""
        resp = self._client._request(
            "PUT",
            f"/rest/api/3/workflowscheme/{id_}/draft/issuetype/{issue_type}",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return WorkflowScheme.model_validate(resp.json())

    def publish_draft_workflow_scheme(
        self, id_: str, body: PublishDraftWorkflowScheme, *, validate_only: bool | None = None
    ) -> None:
        """Publish draft workflow scheme"""
        params = self._client._build_params(**{"validateOnly": validate_only})
        resp = self._client._request(
            "POST",
            f"/rest/api/3/workflowscheme/{id_}/draft/publish",
            params=params,
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    def delete_draft_workflow_mapping(self, id_: str, *, workflow_name: str) -> None:
        """Delete issue types for workflow in draft workflow scheme"""
        params = self._client._build_params(**{"workflowName": workflow_name})
        resp = self._client._request(
            "DELETE", f"/rest/api/3/workflowscheme/{id_}/draft/workflow", params=params
        )
        return None

    def get_draft_workflow(
        self, id_: str, *, workflow_name: str | None = None
    ) -> IssueTypesWorkflowMapping:
        """Get issue types for workflows in draft workflow scheme"""
        params = self._client._build_params(**{"workflowName": workflow_name})
        resp = self._client._request(
            "GET", f"/rest/api/3/workflowscheme/{id_}/draft/workflow", params=params
        )
        return IssueTypesWorkflowMapping.model_validate(resp.json())

    def update_draft_workflow_mapping(
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
    """Asynchronous resource for the Workflow scheme drafts API group."""

    async def create_workflow_scheme_draft_from_parent(self, id_: str) -> WorkflowScheme:
        """Create draft workflow scheme"""
        resp = await self._client._request("POST", f"/rest/api/3/workflowscheme/{id_}/createdraft")
        return WorkflowScheme.model_validate(resp.json())

    async def delete_workflow_scheme_draft(self, id_: str) -> None:
        """Delete draft workflow scheme"""
        resp = await self._client._request("DELETE", f"/rest/api/3/workflowscheme/{id_}/draft")
        return None

    async def get_workflow_scheme_draft(self, id_: str) -> WorkflowScheme:
        """Get draft workflow scheme"""
        resp = await self._client._request("GET", f"/rest/api/3/workflowscheme/{id_}/draft")
        return WorkflowScheme.model_validate(resp.json())

    async def update_workflow_scheme_draft(self, id_: str, body: WorkflowScheme) -> WorkflowScheme:
        """Update draft workflow scheme"""
        resp = await self._client._request(
            "PUT",
            f"/rest/api/3/workflowscheme/{id_}/draft",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return WorkflowScheme.model_validate(resp.json())

    async def delete_draft_default_workflow(self, id_: str) -> WorkflowScheme:
        """Delete draft default workflow"""
        resp = await self._client._request(
            "DELETE", f"/rest/api/3/workflowscheme/{id_}/draft/default"
        )
        return WorkflowScheme.model_validate(resp.json())

    async def get_draft_default_workflow(self, id_: str) -> DefaultWorkflow:
        """Get draft default workflow"""
        resp = await self._client._request("GET", f"/rest/api/3/workflowscheme/{id_}/draft/default")
        return DefaultWorkflow.model_validate(resp.json())

    async def update_draft_default_workflow(
        self, id_: str, body: DefaultWorkflow
    ) -> WorkflowScheme:
        """Update draft default workflow"""
        resp = await self._client._request(
            "PUT",
            f"/rest/api/3/workflowscheme/{id_}/draft/default",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return WorkflowScheme.model_validate(resp.json())

    async def delete_workflow_scheme_draft_issue_type(
        self, id_: str, issue_type: str
    ) -> WorkflowScheme:
        """Delete workflow for issue type in draft workflow scheme"""
        resp = await self._client._request(
            "DELETE", f"/rest/api/3/workflowscheme/{id_}/draft/issuetype/{issue_type}"
        )
        return WorkflowScheme.model_validate(resp.json())

    async def get_workflow_scheme_draft_issue_type(
        self, id_: str, issue_type: str
    ) -> IssueTypeWorkflowMapping:
        """Get workflow for issue type in draft workflow scheme"""
        resp = await self._client._request(
            "GET", f"/rest/api/3/workflowscheme/{id_}/draft/issuetype/{issue_type}"
        )
        return IssueTypeWorkflowMapping.model_validate(resp.json())

    async def set_workflow_scheme_draft_issue_type(
        self, id_: str, issue_type: str, body: IssueTypeWorkflowMapping
    ) -> WorkflowScheme:
        """Set workflow for issue type in draft workflow scheme"""
        resp = await self._client._request(
            "PUT",
            f"/rest/api/3/workflowscheme/{id_}/draft/issuetype/{issue_type}",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return WorkflowScheme.model_validate(resp.json())

    async def publish_draft_workflow_scheme(
        self, id_: str, body: PublishDraftWorkflowScheme, *, validate_only: bool | None = None
    ) -> None:
        """Publish draft workflow scheme"""
        params = self._client._build_params(**{"validateOnly": validate_only})
        resp = await self._client._request(
            "POST",
            f"/rest/api/3/workflowscheme/{id_}/draft/publish",
            params=params,
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    async def delete_draft_workflow_mapping(self, id_: str, *, workflow_name: str) -> None:
        """Delete issue types for workflow in draft workflow scheme"""
        params = self._client._build_params(**{"workflowName": workflow_name})
        resp = await self._client._request(
            "DELETE", f"/rest/api/3/workflowscheme/{id_}/draft/workflow", params=params
        )
        return None

    async def get_draft_workflow(
        self, id_: str, *, workflow_name: str | None = None
    ) -> IssueTypesWorkflowMapping:
        """Get issue types for workflows in draft workflow scheme"""
        params = self._client._build_params(**{"workflowName": workflow_name})
        resp = await self._client._request(
            "GET", f"/rest/api/3/workflowscheme/{id_}/draft/workflow", params=params
        )
        return IssueTypesWorkflowMapping.model_validate(resp.json())

    async def update_draft_workflow_mapping(
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
