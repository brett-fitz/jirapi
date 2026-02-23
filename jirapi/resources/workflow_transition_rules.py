"""Resource classes for the Workflow transition rules API group."""

from __future__ import annotations

from jirapi._resource import AsyncAPIResource, SyncAPIResource
from jirapi.models import (
    PageBeanWorkflowTransitionRules,
    WorkflowsWithTransitionRulesDetails,
    WorkflowTransitionRulesUpdate,
    WorkflowTransitionRulesUpdateErrors,
)


class WorkflowTransitionRules(SyncAPIResource):
    """Synchronous resource for the Workflow transition rules API group."""

    def get_workflow_transition_rule_configurations(
        self,
        *,
        start_at: int | None = None,
        max_results: int | None = None,
        types: list[str],
        keys: list[str] | None = None,
        workflow_names: list[str] | None = None,
        with_tags: list[str] | None = None,
        draft: bool | None = None,
        expand: str | None = None,
    ) -> PageBeanWorkflowTransitionRules:
        """Get workflow transition rule configurations"""
        params = self._client._build_params(
            **{
                "startAt": start_at,
                "maxResults": max_results,
                "types": types,
                "keys": keys,
                "workflowNames": workflow_names,
                "withTags": with_tags,
                "draft": draft,
                "expand": expand,
            }
        )
        resp = self._client._request("GET", "/rest/api/3/workflow/rule/config", params=params)
        return PageBeanWorkflowTransitionRules.model_validate(resp.json())

    def update_workflow_transition_rule_configurations(
        self, body: WorkflowTransitionRulesUpdate
    ) -> WorkflowTransitionRulesUpdateErrors:
        """Update workflow transition rule configurations"""
        resp = self._client._request(
            "PUT",
            "/rest/api/3/workflow/rule/config",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return WorkflowTransitionRulesUpdateErrors.model_validate(resp.json())

    def delete_workflow_transition_rule_configurations(
        self, body: WorkflowsWithTransitionRulesDetails
    ) -> WorkflowTransitionRulesUpdateErrors:
        """Delete workflow transition rule configurations"""
        resp = self._client._request(
            "PUT",
            "/rest/api/3/workflow/rule/config/delete",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return WorkflowTransitionRulesUpdateErrors.model_validate(resp.json())


class AsyncWorkflowTransitionRules(AsyncAPIResource):
    """Asynchronous resource for the Workflow transition rules API group."""

    async def get_workflow_transition_rule_configurations(
        self,
        *,
        start_at: int | None = None,
        max_results: int | None = None,
        types: list[str],
        keys: list[str] | None = None,
        workflow_names: list[str] | None = None,
        with_tags: list[str] | None = None,
        draft: bool | None = None,
        expand: str | None = None,
    ) -> PageBeanWorkflowTransitionRules:
        """Get workflow transition rule configurations"""
        params = self._client._build_params(
            **{
                "startAt": start_at,
                "maxResults": max_results,
                "types": types,
                "keys": keys,
                "workflowNames": workflow_names,
                "withTags": with_tags,
                "draft": draft,
                "expand": expand,
            }
        )
        resp = await self._client._request("GET", "/rest/api/3/workflow/rule/config", params=params)
        return PageBeanWorkflowTransitionRules.model_validate(resp.json())

    async def update_workflow_transition_rule_configurations(
        self, body: WorkflowTransitionRulesUpdate
    ) -> WorkflowTransitionRulesUpdateErrors:
        """Update workflow transition rule configurations"""
        resp = await self._client._request(
            "PUT",
            "/rest/api/3/workflow/rule/config",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return WorkflowTransitionRulesUpdateErrors.model_validate(resp.json())

    async def delete_workflow_transition_rule_configurations(
        self, body: WorkflowsWithTransitionRulesDetails
    ) -> WorkflowTransitionRulesUpdateErrors:
        """Delete workflow transition rule configurations"""
        resp = await self._client._request(
            "PUT",
            "/rest/api/3/workflow/rule/config/delete",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return WorkflowTransitionRulesUpdateErrors.model_validate(resp.json())
