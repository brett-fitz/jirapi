"""Resource classes for the Workflow schemes API group."""

from __future__ import annotations

from jirapi._resource import AsyncAPIResource, SyncAPIResource
from jirapi.models import (
    DefaultWorkflow,
    IssueTypesWorkflowMapping,
    IssueTypeWorkflowMapping,
    PageBeanWorkflowScheme,
    WorkflowScheme,
    WorkflowSchemeProjectSwitchBean,
    WorkflowSchemeProjectUsageDTO,
    WorkflowSchemeReadRequest,
    WorkflowSchemeReadResponse,
    WorkflowSchemeUpdateRequest,
    WorkflowSchemeUpdateRequiredMappingsRequest,
    WorkflowSchemeUpdateRequiredMappingsResponse,
)


class WorkflowSchemes(SyncAPIResource):
    """Synchronous resource for the Workflow schemes API group."""

    def get_all_workflow_schemes(
        self, *, start_at: int | None = None, max_results: int | None = None
    ) -> PageBeanWorkflowScheme:
        """Get all workflow schemes"""
        params = self._client._build_params(**{"startAt": start_at, "maxResults": max_results})
        resp = self._client._request("GET", "/rest/api/3/workflowscheme", params=params)
        return PageBeanWorkflowScheme.model_validate(resp.json())

    def create_workflow_scheme(self, body: WorkflowScheme) -> WorkflowScheme:
        """Create workflow scheme"""
        resp = self._client._request(
            "POST",
            "/rest/api/3/workflowscheme",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return WorkflowScheme.model_validate(resp.json())

    def switch_workflow_scheme_for_project(self, body: WorkflowSchemeProjectSwitchBean) -> None:
        """Switch workflow scheme for project"""
        resp = self._client._request(
            "POST",
            "/rest/api/3/workflowscheme/project/switch",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    def read_workflow_schemes(self, body: WorkflowSchemeReadRequest) -> WorkflowSchemeReadResponse:
        """Bulk get workflow schemes"""
        resp = self._client._request(
            "POST",
            "/rest/api/3/workflowscheme/read",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return WorkflowSchemeReadResponse.model_validate(resp.json())

    def update_schemes(self, body: WorkflowSchemeUpdateRequest) -> None:
        """Update workflow scheme"""
        resp = self._client._request(
            "POST",
            "/rest/api/3/workflowscheme/update",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    def get_required_workflow_scheme_mappings(
        self, body: WorkflowSchemeUpdateRequiredMappingsRequest
    ) -> WorkflowSchemeUpdateRequiredMappingsResponse:
        """Get required status mappings for workflow scheme update"""
        resp = self._client._request(
            "POST",
            "/rest/api/3/workflowscheme/update/mappings",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return WorkflowSchemeUpdateRequiredMappingsResponse.model_validate(resp.json())

    def delete_workflow_scheme(self, id_: str) -> None:
        """Delete workflow scheme"""
        resp = self._client._request("DELETE", f"/rest/api/3/workflowscheme/{id_}")
        return None

    def get_workflow_scheme(
        self, id_: str, *, return_draft_if_exists: bool | None = None
    ) -> WorkflowScheme:
        """Get workflow scheme"""
        params = self._client._build_params(**{"returnDraftIfExists": return_draft_if_exists})
        resp = self._client._request("GET", f"/rest/api/3/workflowscheme/{id_}", params=params)
        return WorkflowScheme.model_validate(resp.json())

    def update_workflow_scheme(self, id_: str, body: WorkflowScheme) -> WorkflowScheme:
        """Classic update workflow scheme"""
        resp = self._client._request(
            "PUT",
            f"/rest/api/3/workflowscheme/{id_}",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return WorkflowScheme.model_validate(resp.json())

    def delete_default_workflow(
        self, id_: str, *, update_draft_if_needed: bool | None = None
    ) -> WorkflowScheme:
        """Delete default workflow"""
        params = self._client._build_params(**{"updateDraftIfNeeded": update_draft_if_needed})
        resp = self._client._request(
            "DELETE", f"/rest/api/3/workflowscheme/{id_}/default", params=params
        )
        return WorkflowScheme.model_validate(resp.json())

    def get_default_workflow(
        self, id_: str, *, return_draft_if_exists: bool | None = None
    ) -> DefaultWorkflow:
        """Get default workflow"""
        params = self._client._build_params(**{"returnDraftIfExists": return_draft_if_exists})
        resp = self._client._request(
            "GET", f"/rest/api/3/workflowscheme/{id_}/default", params=params
        )
        return DefaultWorkflow.model_validate(resp.json())

    def update_default_workflow(self, id_: str, body: DefaultWorkflow) -> WorkflowScheme:
        """Update default workflow"""
        resp = self._client._request(
            "PUT",
            f"/rest/api/3/workflowscheme/{id_}/default",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return WorkflowScheme.model_validate(resp.json())

    def delete_workflow_scheme_issue_type(
        self, id_: str, issue_type: str, *, update_draft_if_needed: bool | None = None
    ) -> WorkflowScheme:
        """Delete workflow for issue type in workflow scheme"""
        params = self._client._build_params(**{"updateDraftIfNeeded": update_draft_if_needed})
        resp = self._client._request(
            "DELETE", f"/rest/api/3/workflowscheme/{id_}/issuetype/{issue_type}", params=params
        )
        return WorkflowScheme.model_validate(resp.json())

    def get_workflow_scheme_issue_type(
        self, id_: str, issue_type: str, *, return_draft_if_exists: bool | None = None
    ) -> IssueTypeWorkflowMapping:
        """Get workflow for issue type in workflow scheme"""
        params = self._client._build_params(**{"returnDraftIfExists": return_draft_if_exists})
        resp = self._client._request(
            "GET", f"/rest/api/3/workflowscheme/{id_}/issuetype/{issue_type}", params=params
        )
        return IssueTypeWorkflowMapping.model_validate(resp.json())

    def set_workflow_scheme_issue_type(
        self, id_: str, issue_type: str, body: IssueTypeWorkflowMapping
    ) -> WorkflowScheme:
        """Set workflow for issue type in workflow scheme"""
        resp = self._client._request(
            "PUT",
            f"/rest/api/3/workflowscheme/{id_}/issuetype/{issue_type}",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return WorkflowScheme.model_validate(resp.json())

    def delete_workflow_mapping(
        self, id_: str, *, workflow_name: str, update_draft_if_needed: bool | None = None
    ) -> None:
        """Delete issue types for workflow in workflow scheme"""
        params = self._client._build_params(
            **{"workflowName": workflow_name, "updateDraftIfNeeded": update_draft_if_needed}
        )
        resp = self._client._request(
            "DELETE", f"/rest/api/3/workflowscheme/{id_}/workflow", params=params
        )
        return None

    def get_workflow(
        self,
        id_: str,
        *,
        workflow_name: str | None = None,
        return_draft_if_exists: bool | None = None,
    ) -> IssueTypesWorkflowMapping:
        """Get issue types for workflows in workflow scheme"""
        params = self._client._build_params(
            **{"workflowName": workflow_name, "returnDraftIfExists": return_draft_if_exists}
        )
        resp = self._client._request(
            "GET", f"/rest/api/3/workflowscheme/{id_}/workflow", params=params
        )
        return IssueTypesWorkflowMapping.model_validate(resp.json())

    def update_workflow_mapping(
        self, id_: str, body: IssueTypesWorkflowMapping, *, workflow_name: str
    ) -> WorkflowScheme:
        """Set issue types for workflow in workflow scheme"""
        params = self._client._build_params(**{"workflowName": workflow_name})
        resp = self._client._request(
            "PUT",
            f"/rest/api/3/workflowscheme/{id_}/workflow",
            params=params,
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return WorkflowScheme.model_validate(resp.json())

    def get_project_usages_for_workflow_scheme(
        self,
        workflow_scheme_id: str,
        *,
        next_page_token: str | None = None,
        max_results: int | None = None,
    ) -> WorkflowSchemeProjectUsageDTO:
        """Get projects which are using a given workflow scheme"""
        params = self._client._build_params(
            **{"nextPageToken": next_page_token, "maxResults": max_results}
        )
        resp = self._client._request(
            "GET", f"/rest/api/3/workflowscheme/{workflow_scheme_id}/projectUsages", params=params
        )
        return WorkflowSchemeProjectUsageDTO.model_validate(resp.json())


class AsyncWorkflowSchemes(AsyncAPIResource):
    """Asynchronous resource for the Workflow schemes API group."""

    async def get_all_workflow_schemes(
        self, *, start_at: int | None = None, max_results: int | None = None
    ) -> PageBeanWorkflowScheme:
        """Get all workflow schemes"""
        params = self._client._build_params(**{"startAt": start_at, "maxResults": max_results})
        resp = await self._client._request("GET", "/rest/api/3/workflowscheme", params=params)
        return PageBeanWorkflowScheme.model_validate(resp.json())

    async def create_workflow_scheme(self, body: WorkflowScheme) -> WorkflowScheme:
        """Create workflow scheme"""
        resp = await self._client._request(
            "POST",
            "/rest/api/3/workflowscheme",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return WorkflowScheme.model_validate(resp.json())

    async def switch_workflow_scheme_for_project(
        self, body: WorkflowSchemeProjectSwitchBean
    ) -> None:
        """Switch workflow scheme for project"""
        resp = await self._client._request(
            "POST",
            "/rest/api/3/workflowscheme/project/switch",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    async def read_workflow_schemes(
        self, body: WorkflowSchemeReadRequest
    ) -> WorkflowSchemeReadResponse:
        """Bulk get workflow schemes"""
        resp = await self._client._request(
            "POST",
            "/rest/api/3/workflowscheme/read",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return WorkflowSchemeReadResponse.model_validate(resp.json())

    async def update_schemes(self, body: WorkflowSchemeUpdateRequest) -> None:
        """Update workflow scheme"""
        resp = await self._client._request(
            "POST",
            "/rest/api/3/workflowscheme/update",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    async def get_required_workflow_scheme_mappings(
        self, body: WorkflowSchemeUpdateRequiredMappingsRequest
    ) -> WorkflowSchemeUpdateRequiredMappingsResponse:
        """Get required status mappings for workflow scheme update"""
        resp = await self._client._request(
            "POST",
            "/rest/api/3/workflowscheme/update/mappings",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return WorkflowSchemeUpdateRequiredMappingsResponse.model_validate(resp.json())

    async def delete_workflow_scheme(self, id_: str) -> None:
        """Delete workflow scheme"""
        resp = await self._client._request("DELETE", f"/rest/api/3/workflowscheme/{id_}")
        return None

    async def get_workflow_scheme(
        self, id_: str, *, return_draft_if_exists: bool | None = None
    ) -> WorkflowScheme:
        """Get workflow scheme"""
        params = self._client._build_params(**{"returnDraftIfExists": return_draft_if_exists})
        resp = await self._client._request(
            "GET", f"/rest/api/3/workflowscheme/{id_}", params=params
        )
        return WorkflowScheme.model_validate(resp.json())

    async def update_workflow_scheme(self, id_: str, body: WorkflowScheme) -> WorkflowScheme:
        """Classic update workflow scheme"""
        resp = await self._client._request(
            "PUT",
            f"/rest/api/3/workflowscheme/{id_}",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return WorkflowScheme.model_validate(resp.json())

    async def delete_default_workflow(
        self, id_: str, *, update_draft_if_needed: bool | None = None
    ) -> WorkflowScheme:
        """Delete default workflow"""
        params = self._client._build_params(**{"updateDraftIfNeeded": update_draft_if_needed})
        resp = await self._client._request(
            "DELETE", f"/rest/api/3/workflowscheme/{id_}/default", params=params
        )
        return WorkflowScheme.model_validate(resp.json())

    async def get_default_workflow(
        self, id_: str, *, return_draft_if_exists: bool | None = None
    ) -> DefaultWorkflow:
        """Get default workflow"""
        params = self._client._build_params(**{"returnDraftIfExists": return_draft_if_exists})
        resp = await self._client._request(
            "GET", f"/rest/api/3/workflowscheme/{id_}/default", params=params
        )
        return DefaultWorkflow.model_validate(resp.json())

    async def update_default_workflow(self, id_: str, body: DefaultWorkflow) -> WorkflowScheme:
        """Update default workflow"""
        resp = await self._client._request(
            "PUT",
            f"/rest/api/3/workflowscheme/{id_}/default",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return WorkflowScheme.model_validate(resp.json())

    async def delete_workflow_scheme_issue_type(
        self, id_: str, issue_type: str, *, update_draft_if_needed: bool | None = None
    ) -> WorkflowScheme:
        """Delete workflow for issue type in workflow scheme"""
        params = self._client._build_params(**{"updateDraftIfNeeded": update_draft_if_needed})
        resp = await self._client._request(
            "DELETE", f"/rest/api/3/workflowscheme/{id_}/issuetype/{issue_type}", params=params
        )
        return WorkflowScheme.model_validate(resp.json())

    async def get_workflow_scheme_issue_type(
        self, id_: str, issue_type: str, *, return_draft_if_exists: bool | None = None
    ) -> IssueTypeWorkflowMapping:
        """Get workflow for issue type in workflow scheme"""
        params = self._client._build_params(**{"returnDraftIfExists": return_draft_if_exists})
        resp = await self._client._request(
            "GET", f"/rest/api/3/workflowscheme/{id_}/issuetype/{issue_type}", params=params
        )
        return IssueTypeWorkflowMapping.model_validate(resp.json())

    async def set_workflow_scheme_issue_type(
        self, id_: str, issue_type: str, body: IssueTypeWorkflowMapping
    ) -> WorkflowScheme:
        """Set workflow for issue type in workflow scheme"""
        resp = await self._client._request(
            "PUT",
            f"/rest/api/3/workflowscheme/{id_}/issuetype/{issue_type}",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return WorkflowScheme.model_validate(resp.json())

    async def delete_workflow_mapping(
        self, id_: str, *, workflow_name: str, update_draft_if_needed: bool | None = None
    ) -> None:
        """Delete issue types for workflow in workflow scheme"""
        params = self._client._build_params(
            **{"workflowName": workflow_name, "updateDraftIfNeeded": update_draft_if_needed}
        )
        resp = await self._client._request(
            "DELETE", f"/rest/api/3/workflowscheme/{id_}/workflow", params=params
        )
        return None

    async def get_workflow(
        self,
        id_: str,
        *,
        workflow_name: str | None = None,
        return_draft_if_exists: bool | None = None,
    ) -> IssueTypesWorkflowMapping:
        """Get issue types for workflows in workflow scheme"""
        params = self._client._build_params(
            **{"workflowName": workflow_name, "returnDraftIfExists": return_draft_if_exists}
        )
        resp = await self._client._request(
            "GET", f"/rest/api/3/workflowscheme/{id_}/workflow", params=params
        )
        return IssueTypesWorkflowMapping.model_validate(resp.json())

    async def update_workflow_mapping(
        self, id_: str, body: IssueTypesWorkflowMapping, *, workflow_name: str
    ) -> WorkflowScheme:
        """Set issue types for workflow in workflow scheme"""
        params = self._client._build_params(**{"workflowName": workflow_name})
        resp = await self._client._request(
            "PUT",
            f"/rest/api/3/workflowscheme/{id_}/workflow",
            params=params,
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return WorkflowScheme.model_validate(resp.json())

    async def get_project_usages_for_workflow_scheme(
        self,
        workflow_scheme_id: str,
        *,
        next_page_token: str | None = None,
        max_results: int | None = None,
    ) -> WorkflowSchemeProjectUsageDTO:
        """Get projects which are using a given workflow scheme"""
        params = self._client._build_params(
            **{"nextPageToken": next_page_token, "maxResults": max_results}
        )
        resp = await self._client._request(
            "GET", f"/rest/api/3/workflowscheme/{workflow_scheme_id}/projectUsages", params=params
        )
        return WorkflowSchemeProjectUsageDTO.model_validate(resp.json())
