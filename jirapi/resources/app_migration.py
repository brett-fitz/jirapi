"""Resource classes for the App migration API group."""

from __future__ import annotations

from jirapi._resource import AsyncAPIResource, SyncAPIResource
from jirapi.models import (
    ConnectCustomFieldValues,
    EntityPropertyDetails,
    WorkflowRulesSearch,
    WorkflowRulesSearchDetails,
)


class AppMigration(SyncAPIResource):
    """Synchronous resource for the App migration API group."""

    def update_issue_fields_put(self, body: ConnectCustomFieldValues) -> None:
        """Bulk update custom field value"""
        self._client._request(
            "PUT",
            "/rest/atlassian-connect/1/migration/field",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    def update_entity_properties_value_put(
        self, entity_type: str, body: EntityPropertyDetails
    ) -> None:
        """Bulk update entity properties"""
        self._client._request(
            "PUT",
            f"/rest/atlassian-connect/1/migration/properties/{entity_type}",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    def workflow_rule_search_post(self, body: WorkflowRulesSearch) -> WorkflowRulesSearchDetails:
        """Get workflow transition rule configurations"""
        resp = self._client._request(
            "POST",
            "/rest/atlassian-connect/1/migration/workflow/rule/search",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return WorkflowRulesSearchDetails.model_validate(resp.json())


class AsyncAppMigration(AsyncAPIResource):
    """Asynchronous resource for the App migration API group."""

    async def update_issue_fields_put(self, body: ConnectCustomFieldValues) -> None:
        """Bulk update custom field value"""
        await self._client._request(
            "PUT",
            "/rest/atlassian-connect/1/migration/field",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    async def update_entity_properties_value_put(
        self, entity_type: str, body: EntityPropertyDetails
    ) -> None:
        """Bulk update entity properties"""
        await self._client._request(
            "PUT",
            f"/rest/atlassian-connect/1/migration/properties/{entity_type}",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    async def workflow_rule_search_post(
        self, body: WorkflowRulesSearch
    ) -> WorkflowRulesSearchDetails:
        """Get workflow transition rule configurations"""
        resp = await self._client._request(
            "POST",
            "/rest/atlassian-connect/1/migration/workflow/rule/search",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return WorkflowRulesSearchDetails.model_validate(resp.json())
