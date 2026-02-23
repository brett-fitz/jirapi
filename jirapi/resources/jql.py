"""Resource classes for the JQL API group."""

from __future__ import annotations

from jirapi._resource import AsyncAPIResource, SyncAPIResource
from jirapi.models import (
    AutoCompleteSuggestions,
    ConvertedJQLQueries,
    JQLPersonalDataMigrationRequest,
    JqlQueriesToParse,
    JqlQueriesToSanitize,
    JQLReferenceData,
    ParsedJqlQueries,
    SanitizedJqlQueries,
    SearchAutoCompleteFilter,
)


class Jql(SyncAPIResource):
    """Synchronous resource for the JQL API group."""

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

    def parse_jql_queries(self, body: JqlQueriesToParse, *, validation: str) -> ParsedJqlQueries:
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

    def sanitise_jql_queries(self, body: JqlQueriesToSanitize) -> SanitizedJqlQueries:
        """Sanitize JQL queries"""
        resp = self._client._request(
            "POST",
            "/rest/api/3/jql/sanitize",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return SanitizedJqlQueries.model_validate(resp.json())


class AsyncJql(AsyncAPIResource):
    """Asynchronous resource for the JQL API group."""

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

    async def parse_jql_queries(
        self, body: JqlQueriesToParse, *, validation: str
    ) -> ParsedJqlQueries:
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

    async def sanitise_jql_queries(self, body: JqlQueriesToSanitize) -> SanitizedJqlQueries:
        """Sanitize JQL queries"""
        resp = await self._client._request(
            "POST",
            "/rest/api/3/jql/sanitize",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return SanitizedJqlQueries.model_validate(resp.json())
