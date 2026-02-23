"""Resource classes for the Issue fields API group."""

from __future__ import annotations

from jirapi._resource import AsyncAPIResource, SyncAPIResource
from jirapi.models import (
    CustomFieldDefinitionJsonBean,
    FieldDetails,
    PageBean2ProjectFieldBean,
    PageBeanField,
    UpdateCustomFieldDetails,
)


class IssueFields(SyncAPIResource):
    """Synchronous resource for the Issue fields API group."""

    def get_fields(self) -> FieldDetails:
        """Get fields"""
        resp = self._client._request("GET", "/rest/api/3/field")
        return FieldDetails.model_validate(resp.json())

    def create_custom_field(self, body: CustomFieldDefinitionJsonBean) -> FieldDetails:
        """Create custom field"""
        resp = self._client._request(
            "POST", "/rest/api/3/field", json=body.model_dump(by_alias=True, exclude_none=True)
        )
        return FieldDetails.model_validate(resp.json())

    def get_fields_paginated(
        self,
        *,
        start_at: int | None = None,
        max_results: int | None = None,
        type_: list[str] | None = None,
        id_: list[str] | None = None,
        query: str | None = None,
        order_by: str | None = None,
        expand: str | None = None,
        project_ids: list[str] | None = None,
    ) -> PageBeanField:
        """Get fields paginated"""
        params = self._client._build_params(
            **{
                "startAt": start_at,
                "maxResults": max_results,
                "type": type_,
                "id": id_,
                "query": query,
                "orderBy": order_by,
                "expand": expand,
                "projectIds": project_ids,
            }
        )
        resp = self._client._request("GET", "/rest/api/3/field/search", params=params)
        return PageBeanField.model_validate(resp.json())

    def get_trashed_fields_paginated(
        self,
        *,
        start_at: int | None = None,
        max_results: int | None = None,
        id_: list[str] | None = None,
        query: str | None = None,
        expand: str | None = None,
        order_by: str | None = None,
    ) -> PageBeanField:
        """Get fields in trash paginated"""
        params = self._client._build_params(
            **{
                "startAt": start_at,
                "maxResults": max_results,
                "id": id_,
                "query": query,
                "expand": expand,
                "orderBy": order_by,
            }
        )
        resp = self._client._request("GET", "/rest/api/3/field/search/trashed", params=params)
        return PageBeanField.model_validate(resp.json())

    def update_custom_field(self, field_id: str, body: UpdateCustomFieldDetails) -> None:
        """Update custom field"""
        resp = self._client._request(
            "PUT",
            f"/rest/api/3/field/{field_id}",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    def delete_custom_field(self, id_: str) -> None:
        """Delete custom field"""
        resp = self._client._request("DELETE", f"/rest/api/3/field/{id_}")
        return None

    def restore_custom_field(self, id_: str) -> None:
        """Restore custom field from trash"""
        resp = self._client._request("POST", f"/rest/api/3/field/{id_}/restore")
        return None

    def trash_custom_field(self, id_: str) -> None:
        """Move custom field to trash"""
        resp = self._client._request("POST", f"/rest/api/3/field/{id_}/trash")
        return None

    def get_project_fields(
        self,
        *,
        start_at: int | None = None,
        max_results: int | None = None,
        project_id: list[str],
        work_type_id: list[str],
        field_id: list[str] | None = None,
    ) -> PageBean2ProjectFieldBean:
        """Get fields for projects"""
        params = self._client._build_params(
            **{
                "startAt": start_at,
                "maxResults": max_results,
                "projectId": project_id,
                "workTypeId": work_type_id,
                "fieldId": field_id,
            }
        )
        resp = self._client._request("GET", "/rest/api/3/projects/fields", params=params)
        return PageBean2ProjectFieldBean.model_validate(resp.json())


class AsyncIssueFields(AsyncAPIResource):
    """Asynchronous resource for the Issue fields API group."""

    async def get_fields(self) -> FieldDetails:
        """Get fields"""
        resp = await self._client._request("GET", "/rest/api/3/field")
        return FieldDetails.model_validate(resp.json())

    async def create_custom_field(self, body: CustomFieldDefinitionJsonBean) -> FieldDetails:
        """Create custom field"""
        resp = await self._client._request(
            "POST", "/rest/api/3/field", json=body.model_dump(by_alias=True, exclude_none=True)
        )
        return FieldDetails.model_validate(resp.json())

    async def get_fields_paginated(
        self,
        *,
        start_at: int | None = None,
        max_results: int | None = None,
        type_: list[str] | None = None,
        id_: list[str] | None = None,
        query: str | None = None,
        order_by: str | None = None,
        expand: str | None = None,
        project_ids: list[str] | None = None,
    ) -> PageBeanField:
        """Get fields paginated"""
        params = self._client._build_params(
            **{
                "startAt": start_at,
                "maxResults": max_results,
                "type": type_,
                "id": id_,
                "query": query,
                "orderBy": order_by,
                "expand": expand,
                "projectIds": project_ids,
            }
        )
        resp = await self._client._request("GET", "/rest/api/3/field/search", params=params)
        return PageBeanField.model_validate(resp.json())

    async def get_trashed_fields_paginated(
        self,
        *,
        start_at: int | None = None,
        max_results: int | None = None,
        id_: list[str] | None = None,
        query: str | None = None,
        expand: str | None = None,
        order_by: str | None = None,
    ) -> PageBeanField:
        """Get fields in trash paginated"""
        params = self._client._build_params(
            **{
                "startAt": start_at,
                "maxResults": max_results,
                "id": id_,
                "query": query,
                "expand": expand,
                "orderBy": order_by,
            }
        )
        resp = await self._client._request("GET", "/rest/api/3/field/search/trashed", params=params)
        return PageBeanField.model_validate(resp.json())

    async def update_custom_field(self, field_id: str, body: UpdateCustomFieldDetails) -> None:
        """Update custom field"""
        resp = await self._client._request(
            "PUT",
            f"/rest/api/3/field/{field_id}",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    async def delete_custom_field(self, id_: str) -> None:
        """Delete custom field"""
        resp = await self._client._request("DELETE", f"/rest/api/3/field/{id_}")
        return None

    async def restore_custom_field(self, id_: str) -> None:
        """Restore custom field from trash"""
        resp = await self._client._request("POST", f"/rest/api/3/field/{id_}/restore")
        return None

    async def trash_custom_field(self, id_: str) -> None:
        """Move custom field to trash"""
        resp = await self._client._request("POST", f"/rest/api/3/field/{id_}/trash")
        return None

    async def get_project_fields(
        self,
        *,
        start_at: int | None = None,
        max_results: int | None = None,
        project_id: list[str],
        work_type_id: list[str],
        field_id: list[str] | None = None,
    ) -> PageBean2ProjectFieldBean:
        """Get fields for projects"""
        params = self._client._build_params(
            **{
                "startAt": start_at,
                "maxResults": max_results,
                "projectId": project_id,
                "workTypeId": work_type_id,
                "fieldId": field_id,
            }
        )
        resp = await self._client._request("GET", "/rest/api/3/projects/fields", params=params)
        return PageBean2ProjectFieldBean.model_validate(resp.json())
