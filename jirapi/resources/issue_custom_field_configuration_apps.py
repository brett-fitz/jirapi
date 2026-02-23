"""Resource classes for the Issue custom field configuration (apps) API group."""

from __future__ import annotations

from jirapi._resource import AsyncAPIResource, SyncAPIResource
from jirapi.models import (
    ConfigurationsListParameters,
    CustomFieldConfigurations,
    PageBeanBulkContextualConfiguration,
    PageBeanContextualConfiguration,
)


class IssueCustomFieldConfigurationApps(SyncAPIResource):
    """Synchronous resource for the Issue custom field configuration (apps) API group."""

    def get_custom_fields_configurations(
        self,
        body: ConfigurationsListParameters,
        *,
        id_: list[str] | None = None,
        field_context_id: list[str] | None = None,
        issue_id: int | None = None,
        project_key_or_id: str | None = None,
        issue_type_id: str | None = None,
        start_at: int | None = None,
        max_results: int | None = None,
    ) -> PageBeanBulkContextualConfiguration:
        """Bulk get custom field configurations"""
        params = self._client._build_params(
            **{
                "id": id_,
                "fieldContextId": field_context_id,
                "issueId": issue_id,
                "projectKeyOrId": project_key_or_id,
                "issueTypeId": issue_type_id,
                "startAt": start_at,
                "maxResults": max_results,
            }
        )
        resp = self._client._request(
            "POST",
            "/rest/api/3/app/field/context/configuration/list",
            params=params,
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return PageBeanBulkContextualConfiguration.model_validate(resp.json())

    def get_custom_field_configuration(
        self,
        field_id_or_key: str,
        *,
        id_: list[str] | None = None,
        field_context_id: list[str] | None = None,
        issue_id: int | None = None,
        project_key_or_id: str | None = None,
        issue_type_id: str | None = None,
        start_at: int | None = None,
        max_results: int | None = None,
    ) -> PageBeanContextualConfiguration:
        """Get custom field configurations"""
        params = self._client._build_params(
            **{
                "id": id_,
                "fieldContextId": field_context_id,
                "issueId": issue_id,
                "projectKeyOrId": project_key_or_id,
                "issueTypeId": issue_type_id,
                "startAt": start_at,
                "maxResults": max_results,
            }
        )
        resp = self._client._request(
            "GET", f"/rest/api/3/app/field/{field_id_or_key}/context/configuration", params=params
        )
        return PageBeanContextualConfiguration.model_validate(resp.json())

    def update_custom_field_configuration(
        self, field_id_or_key: str, body: CustomFieldConfigurations
    ) -> None:
        """Update custom field configurations"""
        resp = self._client._request(
            "PUT",
            f"/rest/api/3/app/field/{field_id_or_key}/context/configuration",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None


class AsyncIssueCustomFieldConfigurationApps(AsyncAPIResource):
    """Asynchronous resource for the Issue custom field configuration (apps) API group."""

    async def get_custom_fields_configurations(
        self,
        body: ConfigurationsListParameters,
        *,
        id_: list[str] | None = None,
        field_context_id: list[str] | None = None,
        issue_id: int | None = None,
        project_key_or_id: str | None = None,
        issue_type_id: str | None = None,
        start_at: int | None = None,
        max_results: int | None = None,
    ) -> PageBeanBulkContextualConfiguration:
        """Bulk get custom field configurations"""
        params = self._client._build_params(
            **{
                "id": id_,
                "fieldContextId": field_context_id,
                "issueId": issue_id,
                "projectKeyOrId": project_key_or_id,
                "issueTypeId": issue_type_id,
                "startAt": start_at,
                "maxResults": max_results,
            }
        )
        resp = await self._client._request(
            "POST",
            "/rest/api/3/app/field/context/configuration/list",
            params=params,
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return PageBeanBulkContextualConfiguration.model_validate(resp.json())

    async def get_custom_field_configuration(
        self,
        field_id_or_key: str,
        *,
        id_: list[str] | None = None,
        field_context_id: list[str] | None = None,
        issue_id: int | None = None,
        project_key_or_id: str | None = None,
        issue_type_id: str | None = None,
        start_at: int | None = None,
        max_results: int | None = None,
    ) -> PageBeanContextualConfiguration:
        """Get custom field configurations"""
        params = self._client._build_params(
            **{
                "id": id_,
                "fieldContextId": field_context_id,
                "issueId": issue_id,
                "projectKeyOrId": project_key_or_id,
                "issueTypeId": issue_type_id,
                "startAt": start_at,
                "maxResults": max_results,
            }
        )
        resp = await self._client._request(
            "GET", f"/rest/api/3/app/field/{field_id_or_key}/context/configuration", params=params
        )
        return PageBeanContextualConfiguration.model_validate(resp.json())

    async def update_custom_field_configuration(
        self, field_id_or_key: str, body: CustomFieldConfigurations
    ) -> None:
        """Update custom field configurations"""
        resp = await self._client._request(
            "PUT",
            f"/rest/api/3/app/field/{field_id_or_key}/context/configuration",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None
