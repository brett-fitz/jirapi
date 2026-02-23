"""Resource classes for the Issue search API group."""

from __future__ import annotations

from jirapi._resource import AsyncAPIResource, SyncAPIResource
from jirapi.models import (
    IssueMatches,
    IssuePickerSuggestions,
    IssuesAndJQLQueries,
    JQLCountRequestBean,
    JQLCountResultsBean,
    SearchAndReconcileRequestBean,
    SearchAndReconcileResults,
)


class IssueSearch(SyncAPIResource):
    """Synchronous resource for the Issue search API group."""

    def get_issue_picker_resource(
        self,
        *,
        query: str | None = None,
        current_jql: str | None = None,
        current_issue_key: str | None = None,
        current_project_id: str | None = None,
        show_sub_tasks: bool | None = None,
        show_sub_task_parent: bool | None = None,
    ) -> IssuePickerSuggestions:
        """Get issue picker suggestions"""
        params = self._client._build_params(
            **{
                "query": query,
                "currentJQL": current_jql,
                "currentIssueKey": current_issue_key,
                "currentProjectId": current_project_id,
                "showSubTasks": show_sub_tasks,
                "showSubTaskParent": show_sub_task_parent,
            }
        )
        resp = self._client._request("GET", "/rest/api/3/issue/picker", params=params)
        return IssuePickerSuggestions.model_validate(resp.json())

    def match_issues(self, body: IssuesAndJQLQueries) -> IssueMatches:
        """Check issues against JQL"""
        resp = self._client._request(
            "POST", "/rest/api/3/jql/match", json=body.model_dump(by_alias=True, exclude_none=True)
        )
        return IssueMatches.model_validate(resp.json())

    def count_issues(self, body: JQLCountRequestBean) -> JQLCountResultsBean:
        """Count issues using JQL"""
        resp = self._client._request(
            "POST",
            "/rest/api/3/search/approximate-count",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return JQLCountResultsBean.model_validate(resp.json())

    def search_and_reconsile_issues_using_jql(
        self,
        *,
        jql: str | None = None,
        next_page_token: str | None = None,
        max_results: int | None = None,
        fields: list[str] | None = None,
        expand: str | None = None,
        properties: list[str] | None = None,
        fields_by_keys: bool | None = None,
        fail_fast: bool | None = None,
        reconcile_issues: list[str] | None = None,
    ) -> SearchAndReconcileResults:
        """Search for issues using JQL enhanced search (GET)"""
        params = self._client._build_params(
            **{
                "jql": jql,
                "nextPageToken": next_page_token,
                "maxResults": max_results,
                "fields": fields,
                "expand": expand,
                "properties": properties,
                "fieldsByKeys": fields_by_keys,
                "failFast": fail_fast,
                "reconcileIssues": reconcile_issues,
            }
        )
        resp = self._client._request("GET", "/rest/api/3/search/jql", params=params)
        return SearchAndReconcileResults.model_validate(resp.json())

    def search_and_reconsile_issues_using_jql_post(
        self, body: SearchAndReconcileRequestBean
    ) -> SearchAndReconcileResults:
        """Search for issues using JQL enhanced search (POST)"""
        resp = self._client._request(
            "POST", "/rest/api/3/search/jql", json=body.model_dump(by_alias=True, exclude_none=True)
        )
        return SearchAndReconcileResults.model_validate(resp.json())


class AsyncIssueSearch(AsyncAPIResource):
    """Asynchronous resource for the Issue search API group."""

    async def get_issue_picker_resource(
        self,
        *,
        query: str | None = None,
        current_jql: str | None = None,
        current_issue_key: str | None = None,
        current_project_id: str | None = None,
        show_sub_tasks: bool | None = None,
        show_sub_task_parent: bool | None = None,
    ) -> IssuePickerSuggestions:
        """Get issue picker suggestions"""
        params = self._client._build_params(
            **{
                "query": query,
                "currentJQL": current_jql,
                "currentIssueKey": current_issue_key,
                "currentProjectId": current_project_id,
                "showSubTasks": show_sub_tasks,
                "showSubTaskParent": show_sub_task_parent,
            }
        )
        resp = await self._client._request("GET", "/rest/api/3/issue/picker", params=params)
        return IssuePickerSuggestions.model_validate(resp.json())

    async def match_issues(self, body: IssuesAndJQLQueries) -> IssueMatches:
        """Check issues against JQL"""
        resp = await self._client._request(
            "POST", "/rest/api/3/jql/match", json=body.model_dump(by_alias=True, exclude_none=True)
        )
        return IssueMatches.model_validate(resp.json())

    async def count_issues(self, body: JQLCountRequestBean) -> JQLCountResultsBean:
        """Count issues using JQL"""
        resp = await self._client._request(
            "POST",
            "/rest/api/3/search/approximate-count",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return JQLCountResultsBean.model_validate(resp.json())

    async def search_and_reconsile_issues_using_jql(
        self,
        *,
        jql: str | None = None,
        next_page_token: str | None = None,
        max_results: int | None = None,
        fields: list[str] | None = None,
        expand: str | None = None,
        properties: list[str] | None = None,
        fields_by_keys: bool | None = None,
        fail_fast: bool | None = None,
        reconcile_issues: list[str] | None = None,
    ) -> SearchAndReconcileResults:
        """Search for issues using JQL enhanced search (GET)"""
        params = self._client._build_params(
            **{
                "jql": jql,
                "nextPageToken": next_page_token,
                "maxResults": max_results,
                "fields": fields,
                "expand": expand,
                "properties": properties,
                "fieldsByKeys": fields_by_keys,
                "failFast": fail_fast,
                "reconcileIssues": reconcile_issues,
            }
        )
        resp = await self._client._request("GET", "/rest/api/3/search/jql", params=params)
        return SearchAndReconcileResults.model_validate(resp.json())

    async def search_and_reconsile_issues_using_jql_post(
        self, body: SearchAndReconcileRequestBean
    ) -> SearchAndReconcileResults:
        """Search for issues using JQL enhanced search (POST)"""
        resp = await self._client._request(
            "POST", "/rest/api/3/search/jql", json=body.model_dump(by_alias=True, exclude_none=True)
        )
        return SearchAndReconcileResults.model_validate(resp.json())
