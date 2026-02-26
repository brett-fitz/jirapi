"""Resource classes for jql."""

from __future__ import annotations

from jirapi._resource import AsyncAPIResource, SyncAPIResource
from jirapi.models import (
    AutoCompleteSuggestions,
    ConvertedJQLQueries,
    JqlFunctionPrecomputationGetByIdRequest,
    JqlFunctionPrecomputationGetByIdResponse,
    JqlFunctionPrecomputationUpdateRequest,
    JqlFunctionPrecomputationUpdateResponse,
    JQLPersonalDataMigrationRequest,
    JqlQueriesToParse,
    JqlQueriesToSanitize,
    JQLReferenceData,
    PageBean2JqlFunctionPrecomputation,
    ParsedJqlQueries,
    SanitizedJqlQueries,
    SearchAutoCompleteFilter,
)


class Jql(SyncAPIResource):
    """Synchronous resource for jql."""

    def get_auto_complete(self) -> JQLReferenceData:
        """Get field reference data (GET)"""
        resp = self._client._request("GET", "/rest/api/3/jql/autocompletedata")
        return JQLReferenceData.model_validate(resp.json())

    def get_auto_complete_post(self, body: SearchAutoCompleteFilter) -> JQLReferenceData:
        """Get field reference data (POST)"""
        resp = self._client._request(
            "POST",
            "/rest/api/3/jql/autocompletedata",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return JQLReferenceData.model_validate(resp.json())

    def get_field_auto_complete_for_query_string(
        self,
        *,
        field_name: str | None = None,
        field_value: str | None = None,
        predicate_name: str | None = None,
        predicate_value: str | None = None,
    ) -> AutoCompleteSuggestions:
        """Get field auto complete suggestions"""
        params = self._client._build_params(
            **{
                "fieldName": field_name,
                "fieldValue": field_value,
                "predicateName": predicate_name,
                "predicateValue": predicate_value,
            }
        )
        resp = self._client._request(
            "GET", "/rest/api/3/jql/autocompletedata/suggestions", params=params
        )
        return AutoCompleteSuggestions.model_validate(resp.json())

    def get_precomputations(
        self,
        *,
        function_key: list[str] | None = None,
        start_at: int | None = None,
        max_results: int | None = None,
        order_by: str | None = None,
    ) -> PageBean2JqlFunctionPrecomputation:
        """Get precomputations (apps)"""
        params = self._client._build_params(
            **{
                "functionKey": function_key,
                "startAt": start_at,
                "maxResults": max_results,
                "orderBy": order_by,
            }
        )
        resp = self._client._request("GET", "/rest/api/3/jql/function/computation", params=params)
        return PageBean2JqlFunctionPrecomputation.model_validate(resp.json())

    def update_precomputations(
        self,
        body: JqlFunctionPrecomputationUpdateRequest,
        *,
        skip_not_found_precomputations: bool | None = None,
    ) -> JqlFunctionPrecomputationUpdateResponse:
        """Update precomputations (apps)"""
        params = self._client._build_params(
            **{"skipNotFoundPrecomputations": skip_not_found_precomputations}
        )
        resp = self._client._request(
            "POST",
            "/rest/api/3/jql/function/computation",
            params=params,
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return JqlFunctionPrecomputationUpdateResponse.model_validate(resp.json())

    def get_precomputations_by_id(
        self, body: JqlFunctionPrecomputationGetByIdRequest, *, order_by: str | None = None
    ) -> JqlFunctionPrecomputationGetByIdResponse:
        """Get precomputations by ID (apps)"""
        params = self._client._build_params(**{"orderBy": order_by})
        resp = self._client._request(
            "POST",
            "/rest/api/3/jql/function/computation/search",
            params=params,
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return JqlFunctionPrecomputationGetByIdResponse.model_validate(resp.json())

    def parse_queries(self, body: JqlQueriesToParse, *, validation: str) -> ParsedJqlQueries:
        """Parse JQL query"""
        params = self._client._build_params(**{"validation": validation})
        resp = self._client._request(
            "POST",
            "/rest/api/3/jql/parse",
            params=params,
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return ParsedJqlQueries.model_validate(resp.json())

    def migrate_queries(self, body: JQLPersonalDataMigrationRequest) -> ConvertedJQLQueries:
        """Convert user identifiers to account IDs in JQL queries"""
        resp = self._client._request(
            "POST",
            "/rest/api/3/jql/pdcleaner",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return ConvertedJQLQueries.model_validate(resp.json())

    def sanitise_queries(self, body: JqlQueriesToSanitize) -> SanitizedJqlQueries:
        """Sanitize JQL queries"""
        resp = self._client._request(
            "POST",
            "/rest/api/3/jql/sanitize",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return SanitizedJqlQueries.model_validate(resp.json())


class AsyncJql(AsyncAPIResource):
    """Asynchronous resource for jql."""

    async def get_auto_complete(self) -> JQLReferenceData:
        """Get field reference data (GET)"""
        resp = await self._client._request("GET", "/rest/api/3/jql/autocompletedata")
        return JQLReferenceData.model_validate(resp.json())

    async def get_auto_complete_post(self, body: SearchAutoCompleteFilter) -> JQLReferenceData:
        """Get field reference data (POST)"""
        resp = await self._client._request(
            "POST",
            "/rest/api/3/jql/autocompletedata",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return JQLReferenceData.model_validate(resp.json())

    async def get_field_auto_complete_for_query_string(
        self,
        *,
        field_name: str | None = None,
        field_value: str | None = None,
        predicate_name: str | None = None,
        predicate_value: str | None = None,
    ) -> AutoCompleteSuggestions:
        """Get field auto complete suggestions"""
        params = self._client._build_params(
            **{
                "fieldName": field_name,
                "fieldValue": field_value,
                "predicateName": predicate_name,
                "predicateValue": predicate_value,
            }
        )
        resp = await self._client._request(
            "GET", "/rest/api/3/jql/autocompletedata/suggestions", params=params
        )
        return AutoCompleteSuggestions.model_validate(resp.json())

    async def get_precomputations(
        self,
        *,
        function_key: list[str] | None = None,
        start_at: int | None = None,
        max_results: int | None = None,
        order_by: str | None = None,
    ) -> PageBean2JqlFunctionPrecomputation:
        """Get precomputations (apps)"""
        params = self._client._build_params(
            **{
                "functionKey": function_key,
                "startAt": start_at,
                "maxResults": max_results,
                "orderBy": order_by,
            }
        )
        resp = await self._client._request(
            "GET", "/rest/api/3/jql/function/computation", params=params
        )
        return PageBean2JqlFunctionPrecomputation.model_validate(resp.json())

    async def update_precomputations(
        self,
        body: JqlFunctionPrecomputationUpdateRequest,
        *,
        skip_not_found_precomputations: bool | None = None,
    ) -> JqlFunctionPrecomputationUpdateResponse:
        """Update precomputations (apps)"""
        params = self._client._build_params(
            **{"skipNotFoundPrecomputations": skip_not_found_precomputations}
        )
        resp = await self._client._request(
            "POST",
            "/rest/api/3/jql/function/computation",
            params=params,
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return JqlFunctionPrecomputationUpdateResponse.model_validate(resp.json())

    async def get_precomputations_by_id(
        self, body: JqlFunctionPrecomputationGetByIdRequest, *, order_by: str | None = None
    ) -> JqlFunctionPrecomputationGetByIdResponse:
        """Get precomputations by ID (apps)"""
        params = self._client._build_params(**{"orderBy": order_by})
        resp = await self._client._request(
            "POST",
            "/rest/api/3/jql/function/computation/search",
            params=params,
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return JqlFunctionPrecomputationGetByIdResponse.model_validate(resp.json())

    async def parse_queries(self, body: JqlQueriesToParse, *, validation: str) -> ParsedJqlQueries:
        """Parse JQL query"""
        params = self._client._build_params(**{"validation": validation})
        resp = await self._client._request(
            "POST",
            "/rest/api/3/jql/parse",
            params=params,
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return ParsedJqlQueries.model_validate(resp.json())

    async def migrate_queries(self, body: JQLPersonalDataMigrationRequest) -> ConvertedJQLQueries:
        """Convert user identifiers to account IDs in JQL queries"""
        resp = await self._client._request(
            "POST",
            "/rest/api/3/jql/pdcleaner",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return ConvertedJQLQueries.model_validate(resp.json())

    async def sanitise_queries(self, body: JqlQueriesToSanitize) -> SanitizedJqlQueries:
        """Sanitize JQL queries"""
        resp = await self._client._request(
            "POST",
            "/rest/api/3/jql/sanitize",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return SanitizedJqlQueries.model_validate(resp.json())
