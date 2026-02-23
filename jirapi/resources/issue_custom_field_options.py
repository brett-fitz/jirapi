"""Resource classes for the Issue custom field options API group."""

from __future__ import annotations

from jirapi._resource import AsyncAPIResource, SyncAPIResource
from jirapi.models import (
    BulkCustomFieldOptionCreateRequest,
    BulkCustomFieldOptionUpdateRequest,
    CustomFieldCreatedContextOptionsList,
    CustomFieldOption,
    CustomFieldUpdatedContextOptionsList,
    OrderOfCustomFieldOptions,
    PageBeanCustomFieldContextOption,
)


class IssueCustomFieldOptions(SyncAPIResource):
    """Synchronous resource for the Issue custom field options API group."""

    def get_custom_field_option(self, id_: str) -> CustomFieldOption:
        """Get custom field option"""
        resp = self._client._request("GET", f"/rest/api/3/customFieldOption/{id_}")
        return CustomFieldOption.model_validate(resp.json())

    def get_options_for_context(
        self,
        field_id: str,
        context_id: str,
        *,
        option_id: int | None = None,
        only_options: bool | None = None,
        start_at: int | None = None,
        max_results: int | None = None,
    ) -> PageBeanCustomFieldContextOption:
        """Get custom field options (context)"""
        params = self._client._build_params(
            **{
                "optionId": option_id,
                "onlyOptions": only_options,
                "startAt": start_at,
                "maxResults": max_results,
            }
        )
        resp = self._client._request(
            "GET", f"/rest/api/3/field/{field_id}/context/{context_id}/option", params=params
        )
        return PageBeanCustomFieldContextOption.model_validate(resp.json())

    def create_custom_field_option(
        self, field_id: str, context_id: str, body: BulkCustomFieldOptionCreateRequest
    ) -> CustomFieldCreatedContextOptionsList:
        """Create custom field options (context)"""
        resp = self._client._request(
            "POST",
            f"/rest/api/3/field/{field_id}/context/{context_id}/option",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return CustomFieldCreatedContextOptionsList.model_validate(resp.json())

    def update_custom_field_option(
        self, field_id: str, context_id: str, body: BulkCustomFieldOptionUpdateRequest
    ) -> CustomFieldUpdatedContextOptionsList:
        """Update custom field options (context)"""
        resp = self._client._request(
            "PUT",
            f"/rest/api/3/field/{field_id}/context/{context_id}/option",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return CustomFieldUpdatedContextOptionsList.model_validate(resp.json())

    def reorder_custom_field_options(
        self, field_id: str, context_id: str, body: OrderOfCustomFieldOptions
    ) -> None:
        """Reorder custom field options (context)"""
        resp = self._client._request(
            "PUT",
            f"/rest/api/3/field/{field_id}/context/{context_id}/option/move",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    def delete_custom_field_option(self, field_id: str, context_id: str, option_id: str) -> None:
        """Delete custom field options (context)"""
        resp = self._client._request(
            "DELETE", f"/rest/api/3/field/{field_id}/context/{context_id}/option/{option_id}"
        )
        return None

    def replace_custom_field_option(
        self,
        field_id: str,
        option_id: str,
        context_id: str,
        *,
        replace_with: int | None = None,
        jql: str | None = None,
    ) -> None:
        """Replace custom field options"""
        params = self._client._build_params(**{"replaceWith": replace_with, "jql": jql})
        resp = self._client._request(
            "DELETE",
            f"/rest/api/3/field/{field_id}/context/{context_id}/option/{option_id}/issue",
            params=params,
        )
        return None


class AsyncIssueCustomFieldOptions(AsyncAPIResource):
    """Asynchronous resource for the Issue custom field options API group."""

    async def get_custom_field_option(self, id_: str) -> CustomFieldOption:
        """Get custom field option"""
        resp = await self._client._request("GET", f"/rest/api/3/customFieldOption/{id_}")
        return CustomFieldOption.model_validate(resp.json())

    async def get_options_for_context(
        self,
        field_id: str,
        context_id: str,
        *,
        option_id: int | None = None,
        only_options: bool | None = None,
        start_at: int | None = None,
        max_results: int | None = None,
    ) -> PageBeanCustomFieldContextOption:
        """Get custom field options (context)"""
        params = self._client._build_params(
            **{
                "optionId": option_id,
                "onlyOptions": only_options,
                "startAt": start_at,
                "maxResults": max_results,
            }
        )
        resp = await self._client._request(
            "GET", f"/rest/api/3/field/{field_id}/context/{context_id}/option", params=params
        )
        return PageBeanCustomFieldContextOption.model_validate(resp.json())

    async def create_custom_field_option(
        self, field_id: str, context_id: str, body: BulkCustomFieldOptionCreateRequest
    ) -> CustomFieldCreatedContextOptionsList:
        """Create custom field options (context)"""
        resp = await self._client._request(
            "POST",
            f"/rest/api/3/field/{field_id}/context/{context_id}/option",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return CustomFieldCreatedContextOptionsList.model_validate(resp.json())

    async def update_custom_field_option(
        self, field_id: str, context_id: str, body: BulkCustomFieldOptionUpdateRequest
    ) -> CustomFieldUpdatedContextOptionsList:
        """Update custom field options (context)"""
        resp = await self._client._request(
            "PUT",
            f"/rest/api/3/field/{field_id}/context/{context_id}/option",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return CustomFieldUpdatedContextOptionsList.model_validate(resp.json())

    async def reorder_custom_field_options(
        self, field_id: str, context_id: str, body: OrderOfCustomFieldOptions
    ) -> None:
        """Reorder custom field options (context)"""
        resp = await self._client._request(
            "PUT",
            f"/rest/api/3/field/{field_id}/context/{context_id}/option/move",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    async def delete_custom_field_option(
        self, field_id: str, context_id: str, option_id: str
    ) -> None:
        """Delete custom field options (context)"""
        resp = await self._client._request(
            "DELETE", f"/rest/api/3/field/{field_id}/context/{context_id}/option/{option_id}"
        )
        return None

    async def replace_custom_field_option(
        self,
        field_id: str,
        option_id: str,
        context_id: str,
        *,
        replace_with: int | None = None,
        jql: str | None = None,
    ) -> None:
        """Replace custom field options"""
        params = self._client._build_params(**{"replaceWith": replace_with, "jql": jql})
        resp = await self._client._request(
            "DELETE",
            f"/rest/api/3/field/{field_id}/context/{context_id}/option/{option_id}/issue",
            params=params,
        )
        return None
