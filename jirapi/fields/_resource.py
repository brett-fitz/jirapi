"""Resource classes for fields."""

from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING

from jirapi._resource import AsyncAPIResource, SyncAPIResource
from jirapi.models import (
    CreateFieldAssociationSchemeRequest,
    CreateFieldAssociationSchemeResponse,
    CustomFieldDefinitionJson,
    DeleteFieldAssociationSchemeResponse,
    FieldDetails,
    FieldSchemeToFieldsResponse,
    FieldSchemeToProjectsResponse,
    GetFieldAssociationParametersResponse,
    GetFieldAssociationSchemeByIdResponse,
    MinimalFieldSchemeToFieldsResponse,
    PageBean2FieldAssociationSchemeFieldSearchResult,
    PageBean2FieldAssociationSchemeProjectSearchResult,
    PageBean2GetFieldAssociationSchemeResponse,
    PageBean2GetProjectsWithFieldSchemesResponse,
    PageBean2ProjectField,
    PageBeanField,
    UpdateCustomFieldDetails,
    UpdateFieldAssociationSchemeRequest,
    UpdateFieldAssociationSchemeResponse,
    UpdateFieldSchemeParametersResponse,
)


if TYPE_CHECKING:
    from jirapi.fields.custom_field_associations import (
        AsyncFieldCustomFieldAssociations,
        FieldCustomFieldAssociations,
    )
    from jirapi.fields.custom_field_config_apps import (
        AsyncFieldCustomFieldConfigApps,
        FieldCustomFieldConfigApps,
    )
    from jirapi.fields.custom_field_contexts import (
        AsyncFieldCustomFieldContexts,
        FieldCustomFieldContexts,
    )
    from jirapi.fields.custom_field_options import (
        AsyncFieldCustomFieldOptions,
        FieldCustomFieldOptions,
    )
    from jirapi.fields.custom_field_options_apps import (
        AsyncFieldCustomFieldOptionsApps,
        FieldCustomFieldOptionsApps,
    )
    from jirapi.fields.custom_field_values_apps import (
        AsyncFieldCustomFieldValuesApps,
        FieldCustomFieldValuesApps,
    )


class Fields(SyncAPIResource):
    """Synchronous resource for fields."""

    @cached_property
    def custom_field_associations(self) -> FieldCustomFieldAssociations:
        from jirapi.fields.custom_field_associations import FieldCustomFieldAssociations

        return FieldCustomFieldAssociations(self._client)

    @cached_property
    def custom_field_config_apps(self) -> FieldCustomFieldConfigApps:
        from jirapi.fields.custom_field_config_apps import FieldCustomFieldConfigApps

        return FieldCustomFieldConfigApps(self._client)

    @cached_property
    def custom_field_contexts(self) -> FieldCustomFieldContexts:
        from jirapi.fields.custom_field_contexts import FieldCustomFieldContexts

        return FieldCustomFieldContexts(self._client)

    @cached_property
    def custom_field_options(self) -> FieldCustomFieldOptions:
        from jirapi.fields.custom_field_options import FieldCustomFieldOptions

        return FieldCustomFieldOptions(self._client)

    @cached_property
    def custom_field_options_apps(self) -> FieldCustomFieldOptionsApps:
        from jirapi.fields.custom_field_options_apps import FieldCustomFieldOptionsApps

        return FieldCustomFieldOptionsApps(self._client)

    @cached_property
    def custom_field_values_apps(self) -> FieldCustomFieldValuesApps:
        from jirapi.fields.custom_field_values_apps import FieldCustomFieldValuesApps

        return FieldCustomFieldValuesApps(self._client)

    def list_schemes(
        self,
        *,
        project_id: list[str] | None = None,
        query: str | None = None,
        start_at: int | None = None,
        max_results: int | None = None,
    ) -> PageBean2GetFieldAssociationSchemeResponse:
        """Get field schemes"""
        params = self._client._build_params(
            **{
                "projectId": project_id,
                "query": query,
                "startAt": start_at,
                "maxResults": max_results,
            }
        )
        resp = self._client._request("GET", "/rest/api/3/config/fieldschemes", params=params)
        return PageBean2GetFieldAssociationSchemeResponse.model_validate(resp.json())

    def create_scheme(
        self, body: CreateFieldAssociationSchemeRequest
    ) -> CreateFieldAssociationSchemeResponse:
        """Create field scheme"""
        resp = self._client._request(
            "POST",
            "/rest/api/3/config/fieldschemes",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return CreateFieldAssociationSchemeResponse.model_validate(resp.json())

    def remove_fields_from_schemes(self) -> MinimalFieldSchemeToFieldsResponse:
        """Remove fields associated with field schemes"""
        resp = self._client._request("DELETE", "/rest/api/3/config/fieldschemes/fields")
        return MinimalFieldSchemeToFieldsResponse.model_validate(resp.json())

    def update_fields_in_schemes(self) -> FieldSchemeToFieldsResponse:
        """Update fields associated with field schemes"""
        resp = self._client._request("PUT", "/rest/api/3/config/fieldschemes/fields")
        return FieldSchemeToFieldsResponse.model_validate(resp.json())

    def remove_scheme_item_params(self) -> None:
        """Remove field parameters"""
        self._client._request("DELETE", "/rest/api/3/config/fieldschemes/fields/parameters")
        return None

    def update_scheme_item_params(self) -> UpdateFieldSchemeParametersResponse:
        """Update field parameters"""
        resp = self._client._request("PUT", "/rest/api/3/config/fieldschemes/fields/parameters")
        return UpdateFieldSchemeParametersResponse.model_validate(resp.json())

    def get_projects_with_schemes(
        self, *, start_at: int | None = None, max_results: int | None = None, project_id: list[str]
    ) -> PageBean2GetProjectsWithFieldSchemesResponse:
        """Get projects with field schemes"""
        params = self._client._build_params(
            **{"startAt": start_at, "maxResults": max_results, "projectId": project_id}
        )
        resp = self._client._request(
            "GET", "/rest/api/3/config/fieldschemes/projects", params=params
        )
        return PageBean2GetProjectsWithFieldSchemesResponse.model_validate(resp.json())

    def associate_projects_to_schemes(self) -> FieldSchemeToProjectsResponse:
        """Associate projects to field schemes"""
        resp = self._client._request("PUT", "/rest/api/3/config/fieldschemes/projects")
        return FieldSchemeToProjectsResponse.model_validate(resp.json())

    def delete_scheme(self, id_: str) -> DeleteFieldAssociationSchemeResponse:
        """Delete a field scheme"""
        resp = self._client._request("DELETE", f"/rest/api/3/config/fieldschemes/{id_}")
        return DeleteFieldAssociationSchemeResponse.model_validate(resp.json())

    def get_scheme(self, id_: str) -> GetFieldAssociationSchemeByIdResponse:
        """Get field scheme"""
        resp = self._client._request("GET", f"/rest/api/3/config/fieldschemes/{id_}")
        return GetFieldAssociationSchemeByIdResponse.model_validate(resp.json())

    def update_scheme(
        self, id_: str, body: UpdateFieldAssociationSchemeRequest
    ) -> UpdateFieldAssociationSchemeResponse:
        """Update field scheme"""
        resp = self._client._request(
            "PUT",
            f"/rest/api/3/config/fieldschemes/{id_}",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return UpdateFieldAssociationSchemeResponse.model_validate(resp.json())

    def clone_scheme(
        self, id_: str, body: CreateFieldAssociationSchemeRequest
    ) -> CreateFieldAssociationSchemeResponse:
        """Clone field scheme"""
        resp = self._client._request(
            "POST",
            f"/rest/api/3/config/fieldschemes/{id_}/clone",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return CreateFieldAssociationSchemeResponse.model_validate(resp.json())

    def search_scheme_fields(
        self,
        id_: str,
        *,
        start_at: int | None = None,
        max_results: int | None = None,
        field_id: list[str] | None = None,
    ) -> PageBean2FieldAssociationSchemeFieldSearchResult:
        """Search field scheme fields"""
        params = self._client._build_params(
            **{"startAt": start_at, "maxResults": max_results, "fieldId": field_id}
        )
        resp = self._client._request(
            "GET", f"/rest/api/3/config/fieldschemes/{id_}/fields", params=params
        )
        return PageBean2FieldAssociationSchemeFieldSearchResult.model_validate(resp.json())

    def get_scheme_item_params(
        self, id_: str, field_id: str
    ) -> GetFieldAssociationParametersResponse:
        """Get field parameters"""
        resp = self._client._request(
            "GET", f"/rest/api/3/config/fieldschemes/{id_}/fields/{field_id}/parameters"
        )
        return GetFieldAssociationParametersResponse.model_validate(resp.json())

    def search_scheme_projects(
        self,
        id_: str,
        *,
        start_at: int | None = None,
        max_results: int | None = None,
        project_id: list[str] | None = None,
    ) -> PageBean2FieldAssociationSchemeProjectSearchResult:
        """Search field scheme projects"""
        params = self._client._build_params(
            **{"startAt": start_at, "maxResults": max_results, "projectId": project_id}
        )
        resp = self._client._request(
            "GET", f"/rest/api/3/config/fieldschemes/{id_}/projects", params=params
        )
        return PageBean2FieldAssociationSchemeProjectSearchResult.model_validate(resp.json())

    def list(self) -> FieldDetails:
        """Get fields"""
        resp = self._client._request("GET", "/rest/api/3/field")
        return FieldDetails.model_validate(resp.json())

    def create_custom(self, body: CustomFieldDefinitionJson) -> FieldDetails:
        """Create custom field"""
        resp = self._client._request(
            "POST", "/rest/api/3/field", json=body.model_dump(by_alias=True, exclude_none=True)
        )
        return FieldDetails.model_validate(resp.json())

    def list_paginated(
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

    def list_trashed(
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

    def update_custom(self, field_id: str, body: UpdateCustomFieldDetails) -> None:
        """Update custom field"""
        self._client._request(
            "PUT",
            f"/rest/api/3/field/{field_id}",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    def delete_custom(self, id_: str) -> None:
        """Delete custom field"""
        self._client._request("DELETE", f"/rest/api/3/field/{id_}")
        return None

    def restore_custom(self, id_: str) -> None:
        """Restore custom field from trash"""
        self._client._request("POST", f"/rest/api/3/field/{id_}/restore")
        return None

    def trash_custom(self, id_: str) -> None:
        """Move custom field to trash"""
        self._client._request("POST", f"/rest/api/3/field/{id_}/trash")
        return None

    def get_project(
        self,
        *,
        start_at: int | None = None,
        max_results: int | None = None,
        project_id: list[str],
        work_type_id: list[str],
        field_id: list[str] | None = None,
    ) -> PageBean2ProjectField:
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
        return PageBean2ProjectField.model_validate(resp.json())


class AsyncFields(AsyncAPIResource):
    """Asynchronous resource for fields."""

    @cached_property
    def custom_field_associations(self) -> AsyncFieldCustomFieldAssociations:
        from jirapi.fields.custom_field_associations import AsyncFieldCustomFieldAssociations

        return AsyncFieldCustomFieldAssociations(self._client)

    @cached_property
    def custom_field_config_apps(self) -> AsyncFieldCustomFieldConfigApps:
        from jirapi.fields.custom_field_config_apps import AsyncFieldCustomFieldConfigApps

        return AsyncFieldCustomFieldConfigApps(self._client)

    @cached_property
    def custom_field_contexts(self) -> AsyncFieldCustomFieldContexts:
        from jirapi.fields.custom_field_contexts import AsyncFieldCustomFieldContexts

        return AsyncFieldCustomFieldContexts(self._client)

    @cached_property
    def custom_field_options(self) -> AsyncFieldCustomFieldOptions:
        from jirapi.fields.custom_field_options import AsyncFieldCustomFieldOptions

        return AsyncFieldCustomFieldOptions(self._client)

    @cached_property
    def custom_field_options_apps(self) -> AsyncFieldCustomFieldOptionsApps:
        from jirapi.fields.custom_field_options_apps import AsyncFieldCustomFieldOptionsApps

        return AsyncFieldCustomFieldOptionsApps(self._client)

    @cached_property
    def custom_field_values_apps(self) -> AsyncFieldCustomFieldValuesApps:
        from jirapi.fields.custom_field_values_apps import AsyncFieldCustomFieldValuesApps

        return AsyncFieldCustomFieldValuesApps(self._client)

    async def list_schemes(
        self,
        *,
        project_id: list[str] | None = None,
        query: str | None = None,
        start_at: int | None = None,
        max_results: int | None = None,
    ) -> PageBean2GetFieldAssociationSchemeResponse:
        """Get field schemes"""
        params = self._client._build_params(
            **{
                "projectId": project_id,
                "query": query,
                "startAt": start_at,
                "maxResults": max_results,
            }
        )
        resp = await self._client._request("GET", "/rest/api/3/config/fieldschemes", params=params)
        return PageBean2GetFieldAssociationSchemeResponse.model_validate(resp.json())

    async def create_scheme(
        self, body: CreateFieldAssociationSchemeRequest
    ) -> CreateFieldAssociationSchemeResponse:
        """Create field scheme"""
        resp = await self._client._request(
            "POST",
            "/rest/api/3/config/fieldschemes",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return CreateFieldAssociationSchemeResponse.model_validate(resp.json())

    async def remove_fields_from_schemes(self) -> MinimalFieldSchemeToFieldsResponse:
        """Remove fields associated with field schemes"""
        resp = await self._client._request("DELETE", "/rest/api/3/config/fieldschemes/fields")
        return MinimalFieldSchemeToFieldsResponse.model_validate(resp.json())

    async def update_fields_in_schemes(self) -> FieldSchemeToFieldsResponse:
        """Update fields associated with field schemes"""
        resp = await self._client._request("PUT", "/rest/api/3/config/fieldschemes/fields")
        return FieldSchemeToFieldsResponse.model_validate(resp.json())

    async def remove_scheme_item_params(self) -> None:
        """Remove field parameters"""
        await self._client._request("DELETE", "/rest/api/3/config/fieldschemes/fields/parameters")
        return None

    async def update_scheme_item_params(self) -> UpdateFieldSchemeParametersResponse:
        """Update field parameters"""
        resp = await self._client._request(
            "PUT", "/rest/api/3/config/fieldschemes/fields/parameters"
        )
        return UpdateFieldSchemeParametersResponse.model_validate(resp.json())

    async def get_projects_with_schemes(
        self, *, start_at: int | None = None, max_results: int | None = None, project_id: list[str]
    ) -> PageBean2GetProjectsWithFieldSchemesResponse:
        """Get projects with field schemes"""
        params = self._client._build_params(
            **{"startAt": start_at, "maxResults": max_results, "projectId": project_id}
        )
        resp = await self._client._request(
            "GET", "/rest/api/3/config/fieldschemes/projects", params=params
        )
        return PageBean2GetProjectsWithFieldSchemesResponse.model_validate(resp.json())

    async def associate_projects_to_schemes(self) -> FieldSchemeToProjectsResponse:
        """Associate projects to field schemes"""
        resp = await self._client._request("PUT", "/rest/api/3/config/fieldschemes/projects")
        return FieldSchemeToProjectsResponse.model_validate(resp.json())

    async def delete_scheme(self, id_: str) -> DeleteFieldAssociationSchemeResponse:
        """Delete a field scheme"""
        resp = await self._client._request("DELETE", f"/rest/api/3/config/fieldschemes/{id_}")
        return DeleteFieldAssociationSchemeResponse.model_validate(resp.json())

    async def get_scheme(self, id_: str) -> GetFieldAssociationSchemeByIdResponse:
        """Get field scheme"""
        resp = await self._client._request("GET", f"/rest/api/3/config/fieldschemes/{id_}")
        return GetFieldAssociationSchemeByIdResponse.model_validate(resp.json())

    async def update_scheme(
        self, id_: str, body: UpdateFieldAssociationSchemeRequest
    ) -> UpdateFieldAssociationSchemeResponse:
        """Update field scheme"""
        resp = await self._client._request(
            "PUT",
            f"/rest/api/3/config/fieldschemes/{id_}",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return UpdateFieldAssociationSchemeResponse.model_validate(resp.json())

    async def clone_scheme(
        self, id_: str, body: CreateFieldAssociationSchemeRequest
    ) -> CreateFieldAssociationSchemeResponse:
        """Clone field scheme"""
        resp = await self._client._request(
            "POST",
            f"/rest/api/3/config/fieldschemes/{id_}/clone",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return CreateFieldAssociationSchemeResponse.model_validate(resp.json())

    async def search_scheme_fields(
        self,
        id_: str,
        *,
        start_at: int | None = None,
        max_results: int | None = None,
        field_id: list[str] | None = None,
    ) -> PageBean2FieldAssociationSchemeFieldSearchResult:
        """Search field scheme fields"""
        params = self._client._build_params(
            **{"startAt": start_at, "maxResults": max_results, "fieldId": field_id}
        )
        resp = await self._client._request(
            "GET", f"/rest/api/3/config/fieldschemes/{id_}/fields", params=params
        )
        return PageBean2FieldAssociationSchemeFieldSearchResult.model_validate(resp.json())

    async def get_scheme_item_params(
        self, id_: str, field_id: str
    ) -> GetFieldAssociationParametersResponse:
        """Get field parameters"""
        resp = await self._client._request(
            "GET", f"/rest/api/3/config/fieldschemes/{id_}/fields/{field_id}/parameters"
        )
        return GetFieldAssociationParametersResponse.model_validate(resp.json())

    async def search_scheme_projects(
        self,
        id_: str,
        *,
        start_at: int | None = None,
        max_results: int | None = None,
        project_id: list[str] | None = None,
    ) -> PageBean2FieldAssociationSchemeProjectSearchResult:
        """Search field scheme projects"""
        params = self._client._build_params(
            **{"startAt": start_at, "maxResults": max_results, "projectId": project_id}
        )
        resp = await self._client._request(
            "GET", f"/rest/api/3/config/fieldschemes/{id_}/projects", params=params
        )
        return PageBean2FieldAssociationSchemeProjectSearchResult.model_validate(resp.json())

    async def list(self) -> FieldDetails:
        """Get fields"""
        resp = await self._client._request("GET", "/rest/api/3/field")
        return FieldDetails.model_validate(resp.json())

    async def create_custom(self, body: CustomFieldDefinitionJson) -> FieldDetails:
        """Create custom field"""
        resp = await self._client._request(
            "POST", "/rest/api/3/field", json=body.model_dump(by_alias=True, exclude_none=True)
        )
        return FieldDetails.model_validate(resp.json())

    async def list_paginated(
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

    async def list_trashed(
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

    async def update_custom(self, field_id: str, body: UpdateCustomFieldDetails) -> None:
        """Update custom field"""
        await self._client._request(
            "PUT",
            f"/rest/api/3/field/{field_id}",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    async def delete_custom(self, id_: str) -> None:
        """Delete custom field"""
        await self._client._request("DELETE", f"/rest/api/3/field/{id_}")
        return None

    async def restore_custom(self, id_: str) -> None:
        """Restore custom field from trash"""
        await self._client._request("POST", f"/rest/api/3/field/{id_}/restore")
        return None

    async def trash_custom(self, id_: str) -> None:
        """Move custom field to trash"""
        await self._client._request("POST", f"/rest/api/3/field/{id_}/trash")
        return None

    async def get_project(
        self,
        *,
        start_at: int | None = None,
        max_results: int | None = None,
        project_id: list[str],
        work_type_id: list[str],
        field_id: list[str] | None = None,
    ) -> PageBean2ProjectField:
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
        return PageBean2ProjectField.model_validate(resp.json())
