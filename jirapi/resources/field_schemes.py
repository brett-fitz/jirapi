"""Resource classes for the Field schemes API group."""

from __future__ import annotations

from jirapi._resource import AsyncAPIResource, SyncAPIResource
from jirapi.models import (
    CreateFieldAssociationSchemeRequest,
    CreateFieldAssociationSchemeResponse,
    DeleteFieldAssociationSchemeResponse,
    FieldSchemeToFieldsResponse,
    FieldSchemeToProjectsResponse,
    GetFieldAssociationParametersResponse,
    GetFieldAssociationSchemeByIdResponse,
    MinimalFieldSchemeToFieldsResponse,
    PageBean2FieldAssociationSchemeFieldSearchResult,
    PageBean2FieldAssociationSchemeProjectSearchResult,
    PageBean2GetFieldAssociationSchemeResponse,
    PageBean2GetProjectsWithFieldSchemesResponse,
    UpdateFieldAssociationSchemeRequest,
    UpdateFieldAssociationSchemeResponse,
    UpdateFieldSchemeParametersResponse,
)


class FieldSchemes(SyncAPIResource):
    """Synchronous resource for the Field schemes API group."""

    def get_field_association_schemes(
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

    def create_field_association_scheme(
        self, body: CreateFieldAssociationSchemeRequest
    ) -> CreateFieldAssociationSchemeResponse:
        """Create field scheme"""
        resp = self._client._request(
            "POST",
            "/rest/api/3/config/fieldschemes",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return CreateFieldAssociationSchemeResponse.model_validate(resp.json())

    def remove_fields_associated_with_schemes(self) -> MinimalFieldSchemeToFieldsResponse:
        """Remove fields associated with field schemes"""
        resp = self._client._request("DELETE", "/rest/api/3/config/fieldschemes/fields")
        return MinimalFieldSchemeToFieldsResponse.model_validate(resp.json())

    def update_fields_associated_with_schemes(self) -> FieldSchemeToFieldsResponse:
        """Update fields associated with field schemes"""
        resp = self._client._request("PUT", "/rest/api/3/config/fieldschemes/fields")
        return FieldSchemeToFieldsResponse.model_validate(resp.json())

    def remove_field_association_scheme_item_parameters(self) -> None:
        """Remove field parameters"""
        resp = self._client._request("DELETE", "/rest/api/3/config/fieldschemes/fields/parameters")
        return None

    def update_field_association_scheme_item_parameters(
        self,
    ) -> UpdateFieldSchemeParametersResponse:
        """Update field parameters"""
        resp = self._client._request("PUT", "/rest/api/3/config/fieldschemes/fields/parameters")
        return UpdateFieldSchemeParametersResponse.model_validate(resp.json())

    def get_projects_with_field_schemes(
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

    def associate_projects_to_field_association_schemes(self) -> FieldSchemeToProjectsResponse:
        """Associate projects to field schemes"""
        resp = self._client._request("PUT", "/rest/api/3/config/fieldschemes/projects")
        return FieldSchemeToProjectsResponse.model_validate(resp.json())

    def delete_field_association_scheme(self, id_: str) -> DeleteFieldAssociationSchemeResponse:
        """Delete a field scheme"""
        resp = self._client._request("DELETE", f"/rest/api/3/config/fieldschemes/{id_}")
        return DeleteFieldAssociationSchemeResponse.model_validate(resp.json())

    def get_field_association_scheme_by_id(self, id_: str) -> GetFieldAssociationSchemeByIdResponse:
        """Get field scheme"""
        resp = self._client._request("GET", f"/rest/api/3/config/fieldschemes/{id_}")
        return GetFieldAssociationSchemeByIdResponse.model_validate(resp.json())

    def update_field_association_scheme(
        self, id_: str, body: UpdateFieldAssociationSchemeRequest
    ) -> UpdateFieldAssociationSchemeResponse:
        """Update field scheme"""
        resp = self._client._request(
            "PUT",
            f"/rest/api/3/config/fieldschemes/{id_}",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return UpdateFieldAssociationSchemeResponse.model_validate(resp.json())

    def clone_field_association_scheme(
        self, id_: str, body: CreateFieldAssociationSchemeRequest
    ) -> CreateFieldAssociationSchemeResponse:
        """Clone field scheme"""
        resp = self._client._request(
            "POST",
            f"/rest/api/3/config/fieldschemes/{id_}/clone",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return CreateFieldAssociationSchemeResponse.model_validate(resp.json())

    def search_field_association_scheme_fields(
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

    def get_field_association_scheme_item_parameters(
        self, id_: str, field_id: str
    ) -> GetFieldAssociationParametersResponse:
        """Get field parameters"""
        resp = self._client._request(
            "GET", f"/rest/api/3/config/fieldschemes/{id_}/fields/{field_id}/parameters"
        )
        return GetFieldAssociationParametersResponse.model_validate(resp.json())

    def search_field_association_scheme_projects(
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


class AsyncFieldSchemes(AsyncAPIResource):
    """Asynchronous resource for the Field schemes API group."""

    async def get_field_association_schemes(
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

    async def create_field_association_scheme(
        self, body: CreateFieldAssociationSchemeRequest
    ) -> CreateFieldAssociationSchemeResponse:
        """Create field scheme"""
        resp = await self._client._request(
            "POST",
            "/rest/api/3/config/fieldschemes",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return CreateFieldAssociationSchemeResponse.model_validate(resp.json())

    async def remove_fields_associated_with_schemes(self) -> MinimalFieldSchemeToFieldsResponse:
        """Remove fields associated with field schemes"""
        resp = await self._client._request("DELETE", "/rest/api/3/config/fieldschemes/fields")
        return MinimalFieldSchemeToFieldsResponse.model_validate(resp.json())

    async def update_fields_associated_with_schemes(self) -> FieldSchemeToFieldsResponse:
        """Update fields associated with field schemes"""
        resp = await self._client._request("PUT", "/rest/api/3/config/fieldschemes/fields")
        return FieldSchemeToFieldsResponse.model_validate(resp.json())

    async def remove_field_association_scheme_item_parameters(self) -> None:
        """Remove field parameters"""
        resp = await self._client._request(
            "DELETE", "/rest/api/3/config/fieldschemes/fields/parameters"
        )
        return None

    async def update_field_association_scheme_item_parameters(
        self,
    ) -> UpdateFieldSchemeParametersResponse:
        """Update field parameters"""
        resp = await self._client._request(
            "PUT", "/rest/api/3/config/fieldschemes/fields/parameters"
        )
        return UpdateFieldSchemeParametersResponse.model_validate(resp.json())

    async def get_projects_with_field_schemes(
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

    async def associate_projects_to_field_association_schemes(
        self,
    ) -> FieldSchemeToProjectsResponse:
        """Associate projects to field schemes"""
        resp = await self._client._request("PUT", "/rest/api/3/config/fieldschemes/projects")
        return FieldSchemeToProjectsResponse.model_validate(resp.json())

    async def delete_field_association_scheme(
        self, id_: str
    ) -> DeleteFieldAssociationSchemeResponse:
        """Delete a field scheme"""
        resp = await self._client._request("DELETE", f"/rest/api/3/config/fieldschemes/{id_}")
        return DeleteFieldAssociationSchemeResponse.model_validate(resp.json())

    async def get_field_association_scheme_by_id(
        self, id_: str
    ) -> GetFieldAssociationSchemeByIdResponse:
        """Get field scheme"""
        resp = await self._client._request("GET", f"/rest/api/3/config/fieldschemes/{id_}")
        return GetFieldAssociationSchemeByIdResponse.model_validate(resp.json())

    async def update_field_association_scheme(
        self, id_: str, body: UpdateFieldAssociationSchemeRequest
    ) -> UpdateFieldAssociationSchemeResponse:
        """Update field scheme"""
        resp = await self._client._request(
            "PUT",
            f"/rest/api/3/config/fieldschemes/{id_}",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return UpdateFieldAssociationSchemeResponse.model_validate(resp.json())

    async def clone_field_association_scheme(
        self, id_: str, body: CreateFieldAssociationSchemeRequest
    ) -> CreateFieldAssociationSchemeResponse:
        """Clone field scheme"""
        resp = await self._client._request(
            "POST",
            f"/rest/api/3/config/fieldschemes/{id_}/clone",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return CreateFieldAssociationSchemeResponse.model_validate(resp.json())

    async def search_field_association_scheme_fields(
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

    async def get_field_association_scheme_item_parameters(
        self, id_: str, field_id: str
    ) -> GetFieldAssociationParametersResponse:
        """Get field parameters"""
        resp = await self._client._request(
            "GET", f"/rest/api/3/config/fieldschemes/{id_}/fields/{field_id}/parameters"
        )
        return GetFieldAssociationParametersResponse.model_validate(resp.json())

    async def search_field_association_scheme_projects(
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
