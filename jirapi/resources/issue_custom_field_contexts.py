"""Resource classes for the Issue custom field contexts API group."""

from __future__ import annotations

from jirapi._resource import AsyncAPIResource, SyncAPIResource
from jirapi.models import (
    CreateCustomFieldContext,
    CustomFieldContextDefaultValueUpdate,
    CustomFieldContextUpdateDetails,
    IssueTypeIds,
    PageBeanContextForProjectAndIssueType,
    PageBeanCustomFieldContext,
    PageBeanCustomFieldContextDefaultValue,
    PageBeanCustomFieldContextProjectMapping,
    PageBeanIssueTypeToContextMapping,
    ProjectIds,
    ProjectIssueTypeMappings,
)


class IssueCustomFieldContexts(SyncAPIResource):
    """Synchronous resource for the Issue custom field contexts API group."""

    def get_contexts_for_field(
        self,
        field_id: str,
        *,
        is_any_issue_type: bool | None = None,
        is_global_context: bool | None = None,
        context_id: list[str] | None = None,
        start_at: int | None = None,
        max_results: int | None = None,
    ) -> PageBeanCustomFieldContext:
        """Get custom field contexts"""
        params = self._client._build_params(
            **{
                "isAnyIssueType": is_any_issue_type,
                "isGlobalContext": is_global_context,
                "contextId": context_id,
                "startAt": start_at,
                "maxResults": max_results,
            }
        )
        resp = self._client._request("GET", f"/rest/api/3/field/{field_id}/context", params=params)
        return PageBeanCustomFieldContext.model_validate(resp.json())

    def create_custom_field_context(
        self, field_id: str, body: CreateCustomFieldContext
    ) -> CreateCustomFieldContext:
        """Create custom field context"""
        resp = self._client._request(
            "POST",
            f"/rest/api/3/field/{field_id}/context",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return CreateCustomFieldContext.model_validate(resp.json())

    def get_default_values(
        self,
        field_id: str,
        *,
        context_id: list[str] | None = None,
        start_at: int | None = None,
        max_results: int | None = None,
    ) -> PageBeanCustomFieldContextDefaultValue:
        """Get custom field contexts default values"""
        params = self._client._build_params(
            **{"contextId": context_id, "startAt": start_at, "maxResults": max_results}
        )
        resp = self._client._request(
            "GET", f"/rest/api/3/field/{field_id}/context/defaultValue", params=params
        )
        return PageBeanCustomFieldContextDefaultValue.model_validate(resp.json())

    def set_default_values(self, field_id: str, body: CustomFieldContextDefaultValueUpdate) -> None:
        """Set custom field contexts default values"""
        resp = self._client._request(
            "PUT",
            f"/rest/api/3/field/{field_id}/context/defaultValue",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    def get_issue_type_mappings_for_contexts(
        self,
        field_id: str,
        *,
        context_id: list[str] | None = None,
        start_at: int | None = None,
        max_results: int | None = None,
    ) -> PageBeanIssueTypeToContextMapping:
        """Get issue types for custom field context"""
        params = self._client._build_params(
            **{"contextId": context_id, "startAt": start_at, "maxResults": max_results}
        )
        resp = self._client._request(
            "GET", f"/rest/api/3/field/{field_id}/context/issuetypemapping", params=params
        )
        return PageBeanIssueTypeToContextMapping.model_validate(resp.json())

    def get_custom_field_contexts_for_projects_and_issue_types(
        self,
        field_id: str,
        body: ProjectIssueTypeMappings,
        *,
        start_at: int | None = None,
        max_results: int | None = None,
    ) -> PageBeanContextForProjectAndIssueType:
        """Get custom field contexts for projects and issue types"""
        params = self._client._build_params(**{"startAt": start_at, "maxResults": max_results})
        resp = self._client._request(
            "POST",
            f"/rest/api/3/field/{field_id}/context/mapping",
            params=params,
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return PageBeanContextForProjectAndIssueType.model_validate(resp.json())

    def get_project_context_mapping(
        self,
        field_id: str,
        *,
        context_id: list[str] | None = None,
        start_at: int | None = None,
        max_results: int | None = None,
    ) -> PageBeanCustomFieldContextProjectMapping:
        """Get project mappings for custom field context"""
        params = self._client._build_params(
            **{"contextId": context_id, "startAt": start_at, "maxResults": max_results}
        )
        resp = self._client._request(
            "GET", f"/rest/api/3/field/{field_id}/context/projectmapping", params=params
        )
        return PageBeanCustomFieldContextProjectMapping.model_validate(resp.json())

    def delete_custom_field_context(self, field_id: str, context_id: str) -> None:
        """Delete custom field context"""
        resp = self._client._request("DELETE", f"/rest/api/3/field/{field_id}/context/{context_id}")
        return None

    def update_custom_field_context(
        self, field_id: str, context_id: str, body: CustomFieldContextUpdateDetails
    ) -> None:
        """Update custom field context"""
        resp = self._client._request(
            "PUT",
            f"/rest/api/3/field/{field_id}/context/{context_id}",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    def add_issue_types_to_context(
        self, field_id: str, context_id: str, body: IssueTypeIds
    ) -> None:
        """Add issue types to context"""
        resp = self._client._request(
            "PUT",
            f"/rest/api/3/field/{field_id}/context/{context_id}/issuetype",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    def remove_issue_types_from_context(
        self, field_id: str, context_id: str, body: IssueTypeIds
    ) -> None:
        """Remove issue types from context"""
        resp = self._client._request(
            "POST",
            f"/rest/api/3/field/{field_id}/context/{context_id}/issuetype/remove",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    def assign_projects_to_custom_field_context(
        self, field_id: str, context_id: str, body: ProjectIds
    ) -> None:
        """Assign custom field context to projects"""
        resp = self._client._request(
            "PUT",
            f"/rest/api/3/field/{field_id}/context/{context_id}/project",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    def remove_custom_field_context_from_projects(
        self, field_id: str, context_id: str, body: ProjectIds
    ) -> None:
        """Remove custom field context from projects"""
        resp = self._client._request(
            "POST",
            f"/rest/api/3/field/{field_id}/context/{context_id}/project/remove",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None


class AsyncIssueCustomFieldContexts(AsyncAPIResource):
    """Asynchronous resource for the Issue custom field contexts API group."""

    async def get_contexts_for_field(
        self,
        field_id: str,
        *,
        is_any_issue_type: bool | None = None,
        is_global_context: bool | None = None,
        context_id: list[str] | None = None,
        start_at: int | None = None,
        max_results: int | None = None,
    ) -> PageBeanCustomFieldContext:
        """Get custom field contexts"""
        params = self._client._build_params(
            **{
                "isAnyIssueType": is_any_issue_type,
                "isGlobalContext": is_global_context,
                "contextId": context_id,
                "startAt": start_at,
                "maxResults": max_results,
            }
        )
        resp = await self._client._request(
            "GET", f"/rest/api/3/field/{field_id}/context", params=params
        )
        return PageBeanCustomFieldContext.model_validate(resp.json())

    async def create_custom_field_context(
        self, field_id: str, body: CreateCustomFieldContext
    ) -> CreateCustomFieldContext:
        """Create custom field context"""
        resp = await self._client._request(
            "POST",
            f"/rest/api/3/field/{field_id}/context",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return CreateCustomFieldContext.model_validate(resp.json())

    async def get_default_values(
        self,
        field_id: str,
        *,
        context_id: list[str] | None = None,
        start_at: int | None = None,
        max_results: int | None = None,
    ) -> PageBeanCustomFieldContextDefaultValue:
        """Get custom field contexts default values"""
        params = self._client._build_params(
            **{"contextId": context_id, "startAt": start_at, "maxResults": max_results}
        )
        resp = await self._client._request(
            "GET", f"/rest/api/3/field/{field_id}/context/defaultValue", params=params
        )
        return PageBeanCustomFieldContextDefaultValue.model_validate(resp.json())

    async def set_default_values(
        self, field_id: str, body: CustomFieldContextDefaultValueUpdate
    ) -> None:
        """Set custom field contexts default values"""
        resp = await self._client._request(
            "PUT",
            f"/rest/api/3/field/{field_id}/context/defaultValue",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    async def get_issue_type_mappings_for_contexts(
        self,
        field_id: str,
        *,
        context_id: list[str] | None = None,
        start_at: int | None = None,
        max_results: int | None = None,
    ) -> PageBeanIssueTypeToContextMapping:
        """Get issue types for custom field context"""
        params = self._client._build_params(
            **{"contextId": context_id, "startAt": start_at, "maxResults": max_results}
        )
        resp = await self._client._request(
            "GET", f"/rest/api/3/field/{field_id}/context/issuetypemapping", params=params
        )
        return PageBeanIssueTypeToContextMapping.model_validate(resp.json())

    async def get_custom_field_contexts_for_projects_and_issue_types(
        self,
        field_id: str,
        body: ProjectIssueTypeMappings,
        *,
        start_at: int | None = None,
        max_results: int | None = None,
    ) -> PageBeanContextForProjectAndIssueType:
        """Get custom field contexts for projects and issue types"""
        params = self._client._build_params(**{"startAt": start_at, "maxResults": max_results})
        resp = await self._client._request(
            "POST",
            f"/rest/api/3/field/{field_id}/context/mapping",
            params=params,
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return PageBeanContextForProjectAndIssueType.model_validate(resp.json())

    async def get_project_context_mapping(
        self,
        field_id: str,
        *,
        context_id: list[str] | None = None,
        start_at: int | None = None,
        max_results: int | None = None,
    ) -> PageBeanCustomFieldContextProjectMapping:
        """Get project mappings for custom field context"""
        params = self._client._build_params(
            **{"contextId": context_id, "startAt": start_at, "maxResults": max_results}
        )
        resp = await self._client._request(
            "GET", f"/rest/api/3/field/{field_id}/context/projectmapping", params=params
        )
        return PageBeanCustomFieldContextProjectMapping.model_validate(resp.json())

    async def delete_custom_field_context(self, field_id: str, context_id: str) -> None:
        """Delete custom field context"""
        resp = await self._client._request(
            "DELETE", f"/rest/api/3/field/{field_id}/context/{context_id}"
        )
        return None

    async def update_custom_field_context(
        self, field_id: str, context_id: str, body: CustomFieldContextUpdateDetails
    ) -> None:
        """Update custom field context"""
        resp = await self._client._request(
            "PUT",
            f"/rest/api/3/field/{field_id}/context/{context_id}",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    async def add_issue_types_to_context(
        self, field_id: str, context_id: str, body: IssueTypeIds
    ) -> None:
        """Add issue types to context"""
        resp = await self._client._request(
            "PUT",
            f"/rest/api/3/field/{field_id}/context/{context_id}/issuetype",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    async def remove_issue_types_from_context(
        self, field_id: str, context_id: str, body: IssueTypeIds
    ) -> None:
        """Remove issue types from context"""
        resp = await self._client._request(
            "POST",
            f"/rest/api/3/field/{field_id}/context/{context_id}/issuetype/remove",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    async def assign_projects_to_custom_field_context(
        self, field_id: str, context_id: str, body: ProjectIds
    ) -> None:
        """Assign custom field context to projects"""
        resp = await self._client._request(
            "PUT",
            f"/rest/api/3/field/{field_id}/context/{context_id}/project",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    async def remove_custom_field_context_from_projects(
        self, field_id: str, context_id: str, body: ProjectIds
    ) -> None:
        """Remove custom field context from projects"""
        resp = await self._client._request(
            "POST",
            f"/rest/api/3/field/{field_id}/context/{context_id}/project/remove",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None
