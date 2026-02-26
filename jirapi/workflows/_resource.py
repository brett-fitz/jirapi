"""Resource classes for workflows."""

from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING

from jirapi._resource import AsyncAPIResource, SyncAPIResource
from jirapi.models import (
    DefaultWorkflowEditorResponse,
    WorkflowCapabilities,
    WorkflowCreateRequest,
    WorkflowCreateResponse,
    WorkflowCreateValidateRequest,
    WorkflowHistoryListRequest,
    WorkflowHistoryListResponseDTO,
    WorkflowHistoryReadRequest,
    WorkflowHistoryReadResponseDTO,
    WorkflowPreviewRequest,
    WorkflowPreviewResponse,
    WorkflowProjectIssueTypeUsageDTO,
    WorkflowProjectUsageDTO,
    WorkflowReadRequest,
    WorkflowReadResponse,
    WorkflowSchemeUsageDTO,
    WorkflowSearchResponse,
    WorkflowUpdateRequest,
    WorkflowUpdateResponse,
    WorkflowUpdateValidateRequest,
    WorkflowValidationErrorList,
)


if TYPE_CHECKING:
    from jirapi.workflows.scheme_drafts import AsyncWorkflowSchemeDrafts, WorkflowSchemeDrafts
    from jirapi.workflows.scheme_project_associations import (
        AsyncWorkflowSchemeProjectAssociations,
        WorkflowSchemeProjectAssociations,
    )
    from jirapi.workflows.schemes import AsyncWorkflowSchemes, WorkflowSchemes
    from jirapi.workflows.status_categories import (
        AsyncWorkflowStatusCategories,
        WorkflowStatusCategories,
    )
    from jirapi.workflows.statuses import AsyncWorkflowStatuses, WorkflowStatuses
    from jirapi.workflows.transition_rules import (
        AsyncWorkflowTransitionRules,
        WorkflowTransitionRules,
    )


class Workflows(SyncAPIResource):
    """Synchronous resource for workflows."""

    @cached_property
    def scheme_drafts(self) -> WorkflowSchemeDrafts:
        from jirapi.workflows.scheme_drafts import WorkflowSchemeDrafts

        return WorkflowSchemeDrafts(self._client)

    @cached_property
    def scheme_project_associations(self) -> WorkflowSchemeProjectAssociations:
        from jirapi.workflows.scheme_project_associations import WorkflowSchemeProjectAssociations

        return WorkflowSchemeProjectAssociations(self._client)

    @cached_property
    def schemes(self) -> WorkflowSchemes:
        from jirapi.workflows.schemes import WorkflowSchemes

        return WorkflowSchemes(self._client)

    @cached_property
    def status_categories(self) -> WorkflowStatusCategories:
        from jirapi.workflows.status_categories import WorkflowStatusCategories

        return WorkflowStatusCategories(self._client)

    @cached_property
    def statuses(self) -> WorkflowStatuses:
        from jirapi.workflows.statuses import WorkflowStatuses

        return WorkflowStatuses(self._client)

    @cached_property
    def transition_rules(self) -> WorkflowTransitionRules:
        from jirapi.workflows.transition_rules import WorkflowTransitionRules

        return WorkflowTransitionRules(self._client)

    def read_from_history(self, body: WorkflowHistoryReadRequest) -> WorkflowHistoryReadResponseDTO:
        """Read workflow version from history"""
        resp = self._client._request(
            "POST",
            "/rest/api/3/workflow/history",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return WorkflowHistoryReadResponseDTO.model_validate(resp.json())

    def list_history(
        self, body: WorkflowHistoryListRequest, *, expand: str | None = None
    ) -> WorkflowHistoryListResponseDTO:
        """List workflow history entries"""
        params = self._client._build_params(**{"expand": expand})
        resp = self._client._request(
            "POST",
            "/rest/api/3/workflow/history/list",
            params=params,
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return WorkflowHistoryListResponseDTO.model_validate(resp.json())

    def delete_inactive(self, entity_id: str) -> None:
        """Delete inactive workflow"""
        self._client._request("DELETE", f"/rest/api/3/workflow/{entity_id}")
        return None

    def get_project_issue_type_usages(
        self,
        workflow_id: str,
        project_id: str,
        *,
        next_page_token: str | None = None,
        max_results: int | None = None,
    ) -> WorkflowProjectIssueTypeUsageDTO:
        """Get issue types in a project that are using a given workflow"""
        params = self._client._build_params(
            **{"nextPageToken": next_page_token, "maxResults": max_results}
        )
        resp = self._client._request(
            "GET",
            f"/rest/api/3/workflow/{workflow_id}/project/{project_id}/issueTypeUsages",
            params=params,
        )
        return WorkflowProjectIssueTypeUsageDTO.model_validate(resp.json())

    def get_project_usages(
        self,
        workflow_id: str,
        *,
        next_page_token: str | None = None,
        max_results: int | None = None,
    ) -> WorkflowProjectUsageDTO:
        """Get projects using a given workflow"""
        params = self._client._build_params(
            **{"nextPageToken": next_page_token, "maxResults": max_results}
        )
        resp = self._client._request(
            "GET", f"/rest/api/3/workflow/{workflow_id}/projectUsages", params=params
        )
        return WorkflowProjectUsageDTO.model_validate(resp.json())

    def get_scheme_usages(
        self,
        workflow_id: str,
        *,
        next_page_token: str | None = None,
        max_results: int | None = None,
    ) -> WorkflowSchemeUsageDTO:
        """Get workflow schemes which are using a given workflow"""
        params = self._client._build_params(
            **{"nextPageToken": next_page_token, "maxResults": max_results}
        )
        resp = self._client._request(
            "GET", f"/rest/api/3/workflow/{workflow_id}/workflowSchemes", params=params
        )
        return WorkflowSchemeUsageDTO.model_validate(resp.json())

    def read(self, body: WorkflowReadRequest) -> WorkflowReadResponse:
        """Bulk get workflows"""
        resp = self._client._request(
            "POST", "/rest/api/3/workflows", json=body.model_dump(by_alias=True, exclude_none=True)
        )
        return WorkflowReadResponse.model_validate(resp.json())

    def get_capabilities(
        self,
        *,
        workflow_id: str | None = None,
        project_id: str | None = None,
        issue_type_id: str | None = None,
    ) -> WorkflowCapabilities:
        """Get available workflow capabilities"""
        params = self._client._build_params(
            **{"workflowId": workflow_id, "projectId": project_id, "issueTypeId": issue_type_id}
        )
        resp = self._client._request("GET", "/rest/api/3/workflows/capabilities", params=params)
        return WorkflowCapabilities.model_validate(resp.json())

    def create(self, body: WorkflowCreateRequest) -> WorkflowCreateResponse:
        """Bulk create workflows"""
        resp = self._client._request(
            "POST",
            "/rest/api/3/workflows/create",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return WorkflowCreateResponse.model_validate(resp.json())

    def validate_create(self, body: WorkflowCreateValidateRequest) -> WorkflowValidationErrorList:
        """Validate create workflows"""
        resp = self._client._request(
            "POST",
            "/rest/api/3/workflows/create/validation",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return WorkflowValidationErrorList.model_validate(resp.json())

    def get_default_editor(self) -> DefaultWorkflowEditorResponse:
        """Get the user's default workflow editor"""
        resp = self._client._request("GET", "/rest/api/3/workflows/defaultEditor")
        return DefaultWorkflowEditorResponse.model_validate(resp.json())

    def read_previews(self, body: WorkflowPreviewRequest) -> WorkflowPreviewResponse:
        """Preview workflow"""
        resp = self._client._request(
            "POST",
            "/rest/api/3/workflows/preview",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return WorkflowPreviewResponse.model_validate(resp.json())

    def search(
        self,
        *,
        start_at: int | None = None,
        max_results: int | None = None,
        expand: str | None = None,
        query_string: str | None = None,
        order_by: str | None = None,
        scope: str | None = None,
        is_active: bool | None = None,
    ) -> WorkflowSearchResponse:
        """Search workflows"""
        params = self._client._build_params(
            **{
                "startAt": start_at,
                "maxResults": max_results,
                "expand": expand,
                "queryString": query_string,
                "orderBy": order_by,
                "scope": scope,
                "isActive": is_active,
            }
        )
        resp = self._client._request("GET", "/rest/api/3/workflows/search", params=params)
        return WorkflowSearchResponse.model_validate(resp.json())

    def update(self, body: WorkflowUpdateRequest) -> WorkflowUpdateResponse:
        """Bulk update workflows"""
        resp = self._client._request(
            "POST",
            "/rest/api/3/workflows/update",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return WorkflowUpdateResponse.model_validate(resp.json())

    def validate_update(self, body: WorkflowUpdateValidateRequest) -> WorkflowValidationErrorList:
        """Validate update workflows"""
        resp = self._client._request(
            "POST",
            "/rest/api/3/workflows/update/validation",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return WorkflowValidationErrorList.model_validate(resp.json())


class AsyncWorkflows(AsyncAPIResource):
    """Asynchronous resource for workflows."""

    @cached_property
    def scheme_drafts(self) -> AsyncWorkflowSchemeDrafts:
        from jirapi.workflows.scheme_drafts import AsyncWorkflowSchemeDrafts

        return AsyncWorkflowSchemeDrafts(self._client)

    @cached_property
    def scheme_project_associations(self) -> AsyncWorkflowSchemeProjectAssociations:
        from jirapi.workflows.scheme_project_associations import (
            AsyncWorkflowSchemeProjectAssociations,
        )

        return AsyncWorkflowSchemeProjectAssociations(self._client)

    @cached_property
    def schemes(self) -> AsyncWorkflowSchemes:
        from jirapi.workflows.schemes import AsyncWorkflowSchemes

        return AsyncWorkflowSchemes(self._client)

    @cached_property
    def status_categories(self) -> AsyncWorkflowStatusCategories:
        from jirapi.workflows.status_categories import AsyncWorkflowStatusCategories

        return AsyncWorkflowStatusCategories(self._client)

    @cached_property
    def statuses(self) -> AsyncWorkflowStatuses:
        from jirapi.workflows.statuses import AsyncWorkflowStatuses

        return AsyncWorkflowStatuses(self._client)

    @cached_property
    def transition_rules(self) -> AsyncWorkflowTransitionRules:
        from jirapi.workflows.transition_rules import AsyncWorkflowTransitionRules

        return AsyncWorkflowTransitionRules(self._client)

    async def read_from_history(
        self, body: WorkflowHistoryReadRequest
    ) -> WorkflowHistoryReadResponseDTO:
        """Read workflow version from history"""
        resp = await self._client._request(
            "POST",
            "/rest/api/3/workflow/history",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return WorkflowHistoryReadResponseDTO.model_validate(resp.json())

    async def list_history(
        self, body: WorkflowHistoryListRequest, *, expand: str | None = None
    ) -> WorkflowHistoryListResponseDTO:
        """List workflow history entries"""
        params = self._client._build_params(**{"expand": expand})
        resp = await self._client._request(
            "POST",
            "/rest/api/3/workflow/history/list",
            params=params,
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return WorkflowHistoryListResponseDTO.model_validate(resp.json())

    async def delete_inactive(self, entity_id: str) -> None:
        """Delete inactive workflow"""
        await self._client._request("DELETE", f"/rest/api/3/workflow/{entity_id}")
        return None

    async def get_project_issue_type_usages(
        self,
        workflow_id: str,
        project_id: str,
        *,
        next_page_token: str | None = None,
        max_results: int | None = None,
    ) -> WorkflowProjectIssueTypeUsageDTO:
        """Get issue types in a project that are using a given workflow"""
        params = self._client._build_params(
            **{"nextPageToken": next_page_token, "maxResults": max_results}
        )
        resp = await self._client._request(
            "GET",
            f"/rest/api/3/workflow/{workflow_id}/project/{project_id}/issueTypeUsages",
            params=params,
        )
        return WorkflowProjectIssueTypeUsageDTO.model_validate(resp.json())

    async def get_project_usages(
        self,
        workflow_id: str,
        *,
        next_page_token: str | None = None,
        max_results: int | None = None,
    ) -> WorkflowProjectUsageDTO:
        """Get projects using a given workflow"""
        params = self._client._build_params(
            **{"nextPageToken": next_page_token, "maxResults": max_results}
        )
        resp = await self._client._request(
            "GET", f"/rest/api/3/workflow/{workflow_id}/projectUsages", params=params
        )
        return WorkflowProjectUsageDTO.model_validate(resp.json())

    async def get_scheme_usages(
        self,
        workflow_id: str,
        *,
        next_page_token: str | None = None,
        max_results: int | None = None,
    ) -> WorkflowSchemeUsageDTO:
        """Get workflow schemes which are using a given workflow"""
        params = self._client._build_params(
            **{"nextPageToken": next_page_token, "maxResults": max_results}
        )
        resp = await self._client._request(
            "GET", f"/rest/api/3/workflow/{workflow_id}/workflowSchemes", params=params
        )
        return WorkflowSchemeUsageDTO.model_validate(resp.json())

    async def read(self, body: WorkflowReadRequest) -> WorkflowReadResponse:
        """Bulk get workflows"""
        resp = await self._client._request(
            "POST", "/rest/api/3/workflows", json=body.model_dump(by_alias=True, exclude_none=True)
        )
        return WorkflowReadResponse.model_validate(resp.json())

    async def get_capabilities(
        self,
        *,
        workflow_id: str | None = None,
        project_id: str | None = None,
        issue_type_id: str | None = None,
    ) -> WorkflowCapabilities:
        """Get available workflow capabilities"""
        params = self._client._build_params(
            **{"workflowId": workflow_id, "projectId": project_id, "issueTypeId": issue_type_id}
        )
        resp = await self._client._request(
            "GET", "/rest/api/3/workflows/capabilities", params=params
        )
        return WorkflowCapabilities.model_validate(resp.json())

    async def create(self, body: WorkflowCreateRequest) -> WorkflowCreateResponse:
        """Bulk create workflows"""
        resp = await self._client._request(
            "POST",
            "/rest/api/3/workflows/create",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return WorkflowCreateResponse.model_validate(resp.json())

    async def validate_create(
        self, body: WorkflowCreateValidateRequest
    ) -> WorkflowValidationErrorList:
        """Validate create workflows"""
        resp = await self._client._request(
            "POST",
            "/rest/api/3/workflows/create/validation",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return WorkflowValidationErrorList.model_validate(resp.json())

    async def get_default_editor(self) -> DefaultWorkflowEditorResponse:
        """Get the user's default workflow editor"""
        resp = await self._client._request("GET", "/rest/api/3/workflows/defaultEditor")
        return DefaultWorkflowEditorResponse.model_validate(resp.json())

    async def read_previews(self, body: WorkflowPreviewRequest) -> WorkflowPreviewResponse:
        """Preview workflow"""
        resp = await self._client._request(
            "POST",
            "/rest/api/3/workflows/preview",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return WorkflowPreviewResponse.model_validate(resp.json())

    async def search(
        self,
        *,
        start_at: int | None = None,
        max_results: int | None = None,
        expand: str | None = None,
        query_string: str | None = None,
        order_by: str | None = None,
        scope: str | None = None,
        is_active: bool | None = None,
    ) -> WorkflowSearchResponse:
        """Search workflows"""
        params = self._client._build_params(
            **{
                "startAt": start_at,
                "maxResults": max_results,
                "expand": expand,
                "queryString": query_string,
                "orderBy": order_by,
                "scope": scope,
                "isActive": is_active,
            }
        )
        resp = await self._client._request("GET", "/rest/api/3/workflows/search", params=params)
        return WorkflowSearchResponse.model_validate(resp.json())

    async def update(self, body: WorkflowUpdateRequest) -> WorkflowUpdateResponse:
        """Bulk update workflows"""
        resp = await self._client._request(
            "POST",
            "/rest/api/3/workflows/update",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return WorkflowUpdateResponse.model_validate(resp.json())

    async def validate_update(
        self, body: WorkflowUpdateValidateRequest
    ) -> WorkflowValidationErrorList:
        """Validate update workflows"""
        resp = await self._client._request(
            "POST",
            "/rest/api/3/workflows/update/validation",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return WorkflowValidationErrorList.model_validate(resp.json())
