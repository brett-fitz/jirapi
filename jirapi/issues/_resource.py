"""Resource classes for issues."""

from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING

from jirapi._resource import AsyncAPIResource, SyncAPIResource
from jirapi.models import (
    ArchivedIssuesFilterRequest,
    ArchiveIssueAsyncRequest,
    BulkChangelogRequest,
    BulkChangelogResponse,
    BulkEditGetFields,
    BulkFetchIssueRequest,
    BulkIssueResults,
    BulkOperationProgress,
    BulkRedactionRequest,
    BulkTransitionGetAvailableTransitions,
    ColumnItem,
    CreatedIssue,
    CreatedIssues,
    ExportArchivedIssuesTaskProgressResponse,
    Issue,
    IssueArchivalSyncRequest,
    IssueArchivalSyncResponse,
    IssueBulkDeletePayload,
    IssueBulkEditPayload,
    IssueBulkMovePayload,
    IssueBulkTransitionPayload,
    IssueBulkWatchOrUnwatchPayload,
    IssueChangelogIds,
    IssueEvent,
    IssueLimitReportResponse,
    IssueMatches,
    IssuePickerSuggestions,
    IssuesAndJQLQueries,
    IssuesUpdate,
    IssueUpdateDetails,
    IssueUpdateMetadata,
    JQLCountRequest,
    JQLCountResults,
    Notification,
    PageBeanChangelog,
    PageOfChangelogs,
    PageOfCreateMetaIssueTypes,
    PageOfCreateMetaIssueTypeWithField,
    RedactionJobStatusResponse,
    SearchAndReconcileRequest,
    SearchAndReconcileResults,
    SubmittedBulkOperation,
    Transitions,
    User,
)


if TYPE_CHECKING:
    from jirapi.issues.attachments import AsyncIssueAttachments, IssueAttachments
    from jirapi.issues.comment_properties import AsyncIssueCommentProperties, IssueCommentProperties
    from jirapi.issues.comments import AsyncIssueComments, IssueComments
    from jirapi.issues.links import AsyncIssueLinks, IssueLinks
    from jirapi.issues.properties import AsyncIssueProperties, IssueProperties
    from jirapi.issues.remote_links import AsyncIssueRemoteLinks, IssueRemoteLinks
    from jirapi.issues.votes import AsyncIssueVotes, IssueVotes
    from jirapi.issues.watchers import AsyncIssueWatchers, IssueWatchers
    from jirapi.issues.worklog_properties import AsyncIssueWorklogProperties, IssueWorklogProperties
    from jirapi.issues.worklogs import AsyncIssueWorklogs, IssueWorklogs


class Issues(SyncAPIResource):
    """Synchronous resource for issues."""

    @cached_property
    def attachments(self) -> IssueAttachments:
        from jirapi.issues.attachments import IssueAttachments

        return IssueAttachments(self._client)

    @cached_property
    def comment_properties(self) -> IssueCommentProperties:
        from jirapi.issues.comment_properties import IssueCommentProperties

        return IssueCommentProperties(self._client)

    @cached_property
    def comments(self) -> IssueComments:
        from jirapi.issues.comments import IssueComments

        return IssueComments(self._client)

    @cached_property
    def links(self) -> IssueLinks:
        from jirapi.issues.links import IssueLinks

        return IssueLinks(self._client)

    @cached_property
    def properties(self) -> IssueProperties:
        from jirapi.issues.properties import IssueProperties

        return IssueProperties(self._client)

    @cached_property
    def remote_links(self) -> IssueRemoteLinks:
        from jirapi.issues.remote_links import IssueRemoteLinks

        return IssueRemoteLinks(self._client)

    @cached_property
    def votes(self) -> IssueVotes:
        from jirapi.issues.votes import IssueVotes

        return IssueVotes(self._client)

    @cached_property
    def watchers(self) -> IssueWatchers:
        from jirapi.issues.watchers import IssueWatchers

        return IssueWatchers(self._client)

    @cached_property
    def worklog_properties(self) -> IssueWorklogProperties:
        from jirapi.issues.worklog_properties import IssueWorklogProperties

        return IssueWorklogProperties(self._client)

    @cached_property
    def worklogs(self) -> IssueWorklogs:
        from jirapi.issues.worklogs import IssueWorklogs

        return IssueWorklogs(self._client)

    def submit_bulk_delete(self, body: IssueBulkDeletePayload) -> SubmittedBulkOperation:
        """Bulk delete issues"""
        resp = self._client._request(
            "POST",
            "/rest/api/3/bulk/issues/delete",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return SubmittedBulkOperation.model_validate(resp.json())

    def get_bulk_editable_fields(
        self,
        *,
        issue_ids_or_keys: str,
        search_text: str | None = None,
        ending_before: str | None = None,
        starting_after: str | None = None,
    ) -> BulkEditGetFields:
        """Get bulk editable fields"""
        params = self._client._build_params(
            **{
                "issueIdsOrKeys": issue_ids_or_keys,
                "searchText": search_text,
                "endingBefore": ending_before,
                "startingAfter": starting_after,
            }
        )
        resp = self._client._request("GET", "/rest/api/3/bulk/issues/fields", params=params)
        return BulkEditGetFields.model_validate(resp.json())

    def submit_bulk_edit(self, body: IssueBulkEditPayload) -> SubmittedBulkOperation:
        """Bulk edit issues"""
        resp = self._client._request(
            "POST",
            "/rest/api/3/bulk/issues/fields",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return SubmittedBulkOperation.model_validate(resp.json())

    def submit_bulk_move(self, body: IssueBulkMovePayload) -> SubmittedBulkOperation:
        """Bulk move issues"""
        resp = self._client._request(
            "POST",
            "/rest/api/3/bulk/issues/move",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return SubmittedBulkOperation.model_validate(resp.json())

    def get_available_transitions(
        self,
        *,
        issue_ids_or_keys: str,
        ending_before: str | None = None,
        starting_after: str | None = None,
    ) -> BulkTransitionGetAvailableTransitions:
        """Get available transitions"""
        params = self._client._build_params(
            **{
                "issueIdsOrKeys": issue_ids_or_keys,
                "endingBefore": ending_before,
                "startingAfter": starting_after,
            }
        )
        resp = self._client._request("GET", "/rest/api/3/bulk/issues/transition", params=params)
        return BulkTransitionGetAvailableTransitions.model_validate(resp.json())

    def submit_bulk_transition(self, body: IssueBulkTransitionPayload) -> SubmittedBulkOperation:
        """Bulk transition issue statuses"""
        resp = self._client._request(
            "POST",
            "/rest/api/3/bulk/issues/transition",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return SubmittedBulkOperation.model_validate(resp.json())

    def submit_bulk_unwatch(self, body: IssueBulkWatchOrUnwatchPayload) -> SubmittedBulkOperation:
        """Bulk unwatch issues"""
        resp = self._client._request(
            "POST",
            "/rest/api/3/bulk/issues/unwatch",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return SubmittedBulkOperation.model_validate(resp.json())

    def submit_bulk_watch(self, body: IssueBulkWatchOrUnwatchPayload) -> SubmittedBulkOperation:
        """Bulk watch issues"""
        resp = self._client._request(
            "POST",
            "/rest/api/3/bulk/issues/watch",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return SubmittedBulkOperation.model_validate(resp.json())

    def get_bulk_operation_progress(self, task_id: str) -> BulkOperationProgress:
        """Get bulk issue operation progress"""
        resp = self._client._request("GET", f"/rest/api/3/bulk/queue/{task_id}")
        return BulkOperationProgress.model_validate(resp.json())

    def get_bulk_changelogs(self, body: BulkChangelogRequest) -> BulkChangelogResponse:
        """Bulk fetch changelogs"""
        resp = self._client._request(
            "POST",
            "/rest/api/3/changelog/bulkfetch",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return BulkChangelogResponse.model_validate(resp.json())

    def get_events(self) -> IssueEvent:
        """Get events"""
        resp = self._client._request("GET", "/rest/api/3/events")
        return IssueEvent.model_validate(resp.json())

    def create(
        self, body: IssueUpdateDetails, *, update_history: bool | None = None
    ) -> CreatedIssue:
        """Create issue"""
        params = self._client._build_params(**{"updateHistory": update_history})
        resp = self._client._request(
            "POST",
            "/rest/api/3/issue",
            params=params,
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return CreatedIssue.model_validate(resp.json())

    def archive_async(self, body: ArchiveIssueAsyncRequest) -> str:
        """Archive issue(s) by JQL"""
        resp = self._client._request(
            "POST",
            "/rest/api/3/issue/archive",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return resp.json()

    def archive(self, body: IssueArchivalSyncRequest) -> IssueArchivalSyncResponse:
        """Archive issue(s) by issue ID/key"""
        resp = self._client._request(
            "PUT",
            "/rest/api/3/issue/archive",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return IssueArchivalSyncResponse.model_validate(resp.json())

    def create_bulk(self, body: IssuesUpdate) -> CreatedIssues:
        """Bulk create issue"""
        resp = self._client._request(
            "POST", "/rest/api/3/issue/bulk", json=body.model_dump(by_alias=True, exclude_none=True)
        )
        return CreatedIssues.model_validate(resp.json())

    def bulk_fetch(self, body: BulkFetchIssueRequest) -> BulkIssueResults:
        """Bulk fetch issues"""
        resp = self._client._request(
            "POST",
            "/rest/api/3/issue/bulkfetch",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return BulkIssueResults.model_validate(resp.json())

    def get_create_meta_types(
        self, project_id_or_key: str, *, start_at: int | None = None, max_results: int | None = None
    ) -> PageOfCreateMetaIssueTypes:
        """Get create metadata issue types for a project"""
        params = self._client._build_params(**{"startAt": start_at, "maxResults": max_results})
        resp = self._client._request(
            "GET", f"/rest/api/3/issue/createmeta/{project_id_or_key}/issuetypes", params=params
        )
        return PageOfCreateMetaIssueTypes.model_validate(resp.json())

    def get_create_meta_type_id(
        self,
        project_id_or_key: str,
        issue_type_id: str,
        *,
        start_at: int | None = None,
        max_results: int | None = None,
    ) -> PageOfCreateMetaIssueTypeWithField:
        """Get create field metadata for a project and issue type id"""
        params = self._client._build_params(**{"startAt": start_at, "maxResults": max_results})
        resp = self._client._request(
            "GET",
            f"/rest/api/3/issue/createmeta/{project_id_or_key}/issuetypes/{issue_type_id}",
            params=params,
        )
        return PageOfCreateMetaIssueTypeWithField.model_validate(resp.json())

    def get_limit_report(
        self, *, is_returning_keys: bool | None = None
    ) -> IssueLimitReportResponse:
        """Get issue limit report"""
        params = self._client._build_params(**{"isReturningKeys": is_returning_keys})
        resp = self._client._request("GET", "/rest/api/3/issue/limit/report", params=params)
        return IssueLimitReportResponse.model_validate(resp.json())

    def picker_suggestions(
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

    def unarchive(self, body: IssueArchivalSyncRequest) -> IssueArchivalSyncResponse:
        """Unarchive issue(s) by issue keys/ID"""
        resp = self._client._request(
            "PUT",
            "/rest/api/3/issue/unarchive",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return IssueArchivalSyncResponse.model_validate(resp.json())

    def delete(self, issue_id_or_key: str, *, delete_subtasks: str | None = None) -> None:
        """Delete issue"""
        params = self._client._build_params(**{"deleteSubtasks": delete_subtasks})
        self._client._request("DELETE", f"/rest/api/3/issue/{issue_id_or_key}", params=params)
        return None

    def get(
        self,
        issue_id_or_key: str,
        *,
        fields: list[str] | None = None,
        fields_by_keys: bool | None = None,
        expand: str | None = None,
        properties: list[str] | None = None,
        update_history: bool | None = None,
        fail_fast: bool | None = None,
    ) -> Issue:
        """Get issue"""
        params = self._client._build_params(
            **{
                "fields": fields,
                "fieldsByKeys": fields_by_keys,
                "expand": expand,
                "properties": properties,
                "updateHistory": update_history,
                "failFast": fail_fast,
            }
        )
        resp = self._client._request("GET", f"/rest/api/3/issue/{issue_id_or_key}", params=params)
        return Issue.model_validate(resp.json())

    def edit(
        self,
        issue_id_or_key: str,
        body: IssueUpdateDetails,
        *,
        notify_users: bool | None = None,
        override_screen_security: bool | None = None,
        override_editable_flag: bool | None = None,
        return_issue: bool | None = None,
        expand: str | None = None,
    ) -> None:
        """Edit issue"""
        params = self._client._build_params(
            **{
                "notifyUsers": notify_users,
                "overrideScreenSecurity": override_screen_security,
                "overrideEditableFlag": override_editable_flag,
                "returnIssue": return_issue,
                "expand": expand,
            }
        )
        self._client._request(
            "PUT",
            f"/rest/api/3/issue/{issue_id_or_key}",
            params=params,
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    def assign(self, issue_id_or_key: str, body: User) -> None:
        """Assign issue"""
        self._client._request(
            "PUT",
            f"/rest/api/3/issue/{issue_id_or_key}/assignee",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    def get_change_logs(
        self, issue_id_or_key: str, *, start_at: int | None = None, max_results: int | None = None
    ) -> PageBeanChangelog:
        """Get changelogs"""
        params = self._client._build_params(**{"startAt": start_at, "maxResults": max_results})
        resp = self._client._request(
            "GET", f"/rest/api/3/issue/{issue_id_or_key}/changelog", params=params
        )
        return PageBeanChangelog.model_validate(resp.json())

    def get_change_logs_by_ids(
        self, issue_id_or_key: str, body: IssueChangelogIds
    ) -> PageOfChangelogs:
        """Get changelogs by IDs"""
        resp = self._client._request(
            "POST",
            f"/rest/api/3/issue/{issue_id_or_key}/changelog/list",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return PageOfChangelogs.model_validate(resp.json())

    def get_edit_meta(
        self,
        issue_id_or_key: str,
        *,
        override_screen_security: bool | None = None,
        override_editable_flag: bool | None = None,
    ) -> IssueUpdateMetadata:
        """Get edit issue metadata"""
        params = self._client._build_params(
            **{
                "overrideScreenSecurity": override_screen_security,
                "overrideEditableFlag": override_editable_flag,
            }
        )
        resp = self._client._request(
            "GET", f"/rest/api/3/issue/{issue_id_or_key}/editmeta", params=params
        )
        return IssueUpdateMetadata.model_validate(resp.json())

    def notify(self, issue_id_or_key: str, body: Notification) -> None:
        """Send notification for issue"""
        self._client._request(
            "POST",
            f"/rest/api/3/issue/{issue_id_or_key}/notify",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    def get_transitions(
        self,
        issue_id_or_key: str,
        *,
        expand: str | None = None,
        transition_id: str | None = None,
        skip_remote_only_condition: bool | None = None,
        include_unavailable_transitions: bool | None = None,
        sort_by_ops_bar_and_status: bool | None = None,
    ) -> Transitions:
        """Get transitions"""
        params = self._client._build_params(
            **{
                "expand": expand,
                "transitionId": transition_id,
                "skipRemoteOnlyCondition": skip_remote_only_condition,
                "includeUnavailableTransitions": include_unavailable_transitions,
                "sortByOpsBarAndStatus": sort_by_ops_bar_and_status,
            }
        )
        resp = self._client._request(
            "GET", f"/rest/api/3/issue/{issue_id_or_key}/transitions", params=params
        )
        return Transitions.model_validate(resp.json())

    def transition(self, issue_id_or_key: str, body: IssueUpdateDetails) -> None:
        """Transition issue"""
        self._client._request(
            "POST",
            f"/rest/api/3/issue/{issue_id_or_key}/transitions",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    def export_archived(
        self, body: ArchivedIssuesFilterRequest
    ) -> ExportArchivedIssuesTaskProgressResponse:
        """Export archived issue(s)"""
        resp = self._client._request(
            "PUT",
            "/rest/api/3/issues/archive/export",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return ExportArchivedIssuesTaskProgressResponse.model_validate(resp.json())

    def match(self, body: IssuesAndJQLQueries) -> IssueMatches:
        """Check issues against JQL"""
        resp = self._client._request(
            "POST", "/rest/api/3/jql/match", json=body.model_dump(by_alias=True, exclude_none=True)
        )
        return IssueMatches.model_validate(resp.json())

    def redact(self, body: BulkRedactionRequest) -> str:
        """Redact"""
        resp = self._client._request(
            "POST", "/rest/api/3/redact", json=body.model_dump(by_alias=True, exclude_none=True)
        )
        return resp.json()

    def get_redaction_status(self, job_id: str) -> RedactionJobStatusResponse:
        """Get redaction status"""
        resp = self._client._request("GET", f"/rest/api/3/redact/status/{job_id}")
        return RedactionJobStatusResponse.model_validate(resp.json())

    def count(self, body: JQLCountRequest) -> JQLCountResults:
        """Count issues using JQL"""
        resp = self._client._request(
            "POST",
            "/rest/api/3/search/approximate-count",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return JQLCountResults.model_validate(resp.json())

    def search(
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

    def search_post(self, body: SearchAndReconcileRequest) -> SearchAndReconcileResults:
        """Search for issues using JQL enhanced search (POST)"""
        resp = self._client._request(
            "POST", "/rest/api/3/search/jql", json=body.model_dump(by_alias=True, exclude_none=True)
        )
        return SearchAndReconcileResults.model_validate(resp.json())

    def get_navigator_default_columns(self) -> ColumnItem:
        """Get issue navigator default columns"""
        resp = self._client._request("GET", "/rest/api/3/settings/columns")
        return ColumnItem.model_validate(resp.json())

    def set_navigator_default_columns(self) -> None:
        """Set issue navigator default columns"""
        self._client._request("PUT", "/rest/api/3/settings/columns")
        return None


class AsyncIssues(AsyncAPIResource):
    """Asynchronous resource for issues."""

    @cached_property
    def attachments(self) -> AsyncIssueAttachments:
        from jirapi.issues.attachments import AsyncIssueAttachments

        return AsyncIssueAttachments(self._client)

    @cached_property
    def comment_properties(self) -> AsyncIssueCommentProperties:
        from jirapi.issues.comment_properties import AsyncIssueCommentProperties

        return AsyncIssueCommentProperties(self._client)

    @cached_property
    def comments(self) -> AsyncIssueComments:
        from jirapi.issues.comments import AsyncIssueComments

        return AsyncIssueComments(self._client)

    @cached_property
    def links(self) -> AsyncIssueLinks:
        from jirapi.issues.links import AsyncIssueLinks

        return AsyncIssueLinks(self._client)

    @cached_property
    def properties(self) -> AsyncIssueProperties:
        from jirapi.issues.properties import AsyncIssueProperties

        return AsyncIssueProperties(self._client)

    @cached_property
    def remote_links(self) -> AsyncIssueRemoteLinks:
        from jirapi.issues.remote_links import AsyncIssueRemoteLinks

        return AsyncIssueRemoteLinks(self._client)

    @cached_property
    def votes(self) -> AsyncIssueVotes:
        from jirapi.issues.votes import AsyncIssueVotes

        return AsyncIssueVotes(self._client)

    @cached_property
    def watchers(self) -> AsyncIssueWatchers:
        from jirapi.issues.watchers import AsyncIssueWatchers

        return AsyncIssueWatchers(self._client)

    @cached_property
    def worklog_properties(self) -> AsyncIssueWorklogProperties:
        from jirapi.issues.worklog_properties import AsyncIssueWorklogProperties

        return AsyncIssueWorklogProperties(self._client)

    @cached_property
    def worklogs(self) -> AsyncIssueWorklogs:
        from jirapi.issues.worklogs import AsyncIssueWorklogs

        return AsyncIssueWorklogs(self._client)

    async def submit_bulk_delete(self, body: IssueBulkDeletePayload) -> SubmittedBulkOperation:
        """Bulk delete issues"""
        resp = await self._client._request(
            "POST",
            "/rest/api/3/bulk/issues/delete",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return SubmittedBulkOperation.model_validate(resp.json())

    async def get_bulk_editable_fields(
        self,
        *,
        issue_ids_or_keys: str,
        search_text: str | None = None,
        ending_before: str | None = None,
        starting_after: str | None = None,
    ) -> BulkEditGetFields:
        """Get bulk editable fields"""
        params = self._client._build_params(
            **{
                "issueIdsOrKeys": issue_ids_or_keys,
                "searchText": search_text,
                "endingBefore": ending_before,
                "startingAfter": starting_after,
            }
        )
        resp = await self._client._request("GET", "/rest/api/3/bulk/issues/fields", params=params)
        return BulkEditGetFields.model_validate(resp.json())

    async def submit_bulk_edit(self, body: IssueBulkEditPayload) -> SubmittedBulkOperation:
        """Bulk edit issues"""
        resp = await self._client._request(
            "POST",
            "/rest/api/3/bulk/issues/fields",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return SubmittedBulkOperation.model_validate(resp.json())

    async def submit_bulk_move(self, body: IssueBulkMovePayload) -> SubmittedBulkOperation:
        """Bulk move issues"""
        resp = await self._client._request(
            "POST",
            "/rest/api/3/bulk/issues/move",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return SubmittedBulkOperation.model_validate(resp.json())

    async def get_available_transitions(
        self,
        *,
        issue_ids_or_keys: str,
        ending_before: str | None = None,
        starting_after: str | None = None,
    ) -> BulkTransitionGetAvailableTransitions:
        """Get available transitions"""
        params = self._client._build_params(
            **{
                "issueIdsOrKeys": issue_ids_or_keys,
                "endingBefore": ending_before,
                "startingAfter": starting_after,
            }
        )
        resp = await self._client._request(
            "GET", "/rest/api/3/bulk/issues/transition", params=params
        )
        return BulkTransitionGetAvailableTransitions.model_validate(resp.json())

    async def submit_bulk_transition(
        self, body: IssueBulkTransitionPayload
    ) -> SubmittedBulkOperation:
        """Bulk transition issue statuses"""
        resp = await self._client._request(
            "POST",
            "/rest/api/3/bulk/issues/transition",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return SubmittedBulkOperation.model_validate(resp.json())

    async def submit_bulk_unwatch(
        self, body: IssueBulkWatchOrUnwatchPayload
    ) -> SubmittedBulkOperation:
        """Bulk unwatch issues"""
        resp = await self._client._request(
            "POST",
            "/rest/api/3/bulk/issues/unwatch",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return SubmittedBulkOperation.model_validate(resp.json())

    async def submit_bulk_watch(
        self, body: IssueBulkWatchOrUnwatchPayload
    ) -> SubmittedBulkOperation:
        """Bulk watch issues"""
        resp = await self._client._request(
            "POST",
            "/rest/api/3/bulk/issues/watch",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return SubmittedBulkOperation.model_validate(resp.json())

    async def get_bulk_operation_progress(self, task_id: str) -> BulkOperationProgress:
        """Get bulk issue operation progress"""
        resp = await self._client._request("GET", f"/rest/api/3/bulk/queue/{task_id}")
        return BulkOperationProgress.model_validate(resp.json())

    async def get_bulk_changelogs(self, body: BulkChangelogRequest) -> BulkChangelogResponse:
        """Bulk fetch changelogs"""
        resp = await self._client._request(
            "POST",
            "/rest/api/3/changelog/bulkfetch",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return BulkChangelogResponse.model_validate(resp.json())

    async def get_events(self) -> IssueEvent:
        """Get events"""
        resp = await self._client._request("GET", "/rest/api/3/events")
        return IssueEvent.model_validate(resp.json())

    async def create(
        self, body: IssueUpdateDetails, *, update_history: bool | None = None
    ) -> CreatedIssue:
        """Create issue"""
        params = self._client._build_params(**{"updateHistory": update_history})
        resp = await self._client._request(
            "POST",
            "/rest/api/3/issue",
            params=params,
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return CreatedIssue.model_validate(resp.json())

    async def archive_async(self, body: ArchiveIssueAsyncRequest) -> str:
        """Archive issue(s) by JQL"""
        resp = await self._client._request(
            "POST",
            "/rest/api/3/issue/archive",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return resp.json()

    async def archive(self, body: IssueArchivalSyncRequest) -> IssueArchivalSyncResponse:
        """Archive issue(s) by issue ID/key"""
        resp = await self._client._request(
            "PUT",
            "/rest/api/3/issue/archive",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return IssueArchivalSyncResponse.model_validate(resp.json())

    async def create_bulk(self, body: IssuesUpdate) -> CreatedIssues:
        """Bulk create issue"""
        resp = await self._client._request(
            "POST", "/rest/api/3/issue/bulk", json=body.model_dump(by_alias=True, exclude_none=True)
        )
        return CreatedIssues.model_validate(resp.json())

    async def bulk_fetch(self, body: BulkFetchIssueRequest) -> BulkIssueResults:
        """Bulk fetch issues"""
        resp = await self._client._request(
            "POST",
            "/rest/api/3/issue/bulkfetch",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return BulkIssueResults.model_validate(resp.json())

    async def get_create_meta_types(
        self, project_id_or_key: str, *, start_at: int | None = None, max_results: int | None = None
    ) -> PageOfCreateMetaIssueTypes:
        """Get create metadata issue types for a project"""
        params = self._client._build_params(**{"startAt": start_at, "maxResults": max_results})
        resp = await self._client._request(
            "GET", f"/rest/api/3/issue/createmeta/{project_id_or_key}/issuetypes", params=params
        )
        return PageOfCreateMetaIssueTypes.model_validate(resp.json())

    async def get_create_meta_type_id(
        self,
        project_id_or_key: str,
        issue_type_id: str,
        *,
        start_at: int | None = None,
        max_results: int | None = None,
    ) -> PageOfCreateMetaIssueTypeWithField:
        """Get create field metadata for a project and issue type id"""
        params = self._client._build_params(**{"startAt": start_at, "maxResults": max_results})
        resp = await self._client._request(
            "GET",
            f"/rest/api/3/issue/createmeta/{project_id_or_key}/issuetypes/{issue_type_id}",
            params=params,
        )
        return PageOfCreateMetaIssueTypeWithField.model_validate(resp.json())

    async def get_limit_report(
        self, *, is_returning_keys: bool | None = None
    ) -> IssueLimitReportResponse:
        """Get issue limit report"""
        params = self._client._build_params(**{"isReturningKeys": is_returning_keys})
        resp = await self._client._request("GET", "/rest/api/3/issue/limit/report", params=params)
        return IssueLimitReportResponse.model_validate(resp.json())

    async def picker_suggestions(
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

    async def unarchive(self, body: IssueArchivalSyncRequest) -> IssueArchivalSyncResponse:
        """Unarchive issue(s) by issue keys/ID"""
        resp = await self._client._request(
            "PUT",
            "/rest/api/3/issue/unarchive",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return IssueArchivalSyncResponse.model_validate(resp.json())

    async def delete(self, issue_id_or_key: str, *, delete_subtasks: str | None = None) -> None:
        """Delete issue"""
        params = self._client._build_params(**{"deleteSubtasks": delete_subtasks})
        await self._client._request("DELETE", f"/rest/api/3/issue/{issue_id_or_key}", params=params)
        return None

    async def get(
        self,
        issue_id_or_key: str,
        *,
        fields: list[str] | None = None,
        fields_by_keys: bool | None = None,
        expand: str | None = None,
        properties: list[str] | None = None,
        update_history: bool | None = None,
        fail_fast: bool | None = None,
    ) -> Issue:
        """Get issue"""
        params = self._client._build_params(
            **{
                "fields": fields,
                "fieldsByKeys": fields_by_keys,
                "expand": expand,
                "properties": properties,
                "updateHistory": update_history,
                "failFast": fail_fast,
            }
        )
        resp = await self._client._request(
            "GET", f"/rest/api/3/issue/{issue_id_or_key}", params=params
        )
        return Issue.model_validate(resp.json())

    async def edit(
        self,
        issue_id_or_key: str,
        body: IssueUpdateDetails,
        *,
        notify_users: bool | None = None,
        override_screen_security: bool | None = None,
        override_editable_flag: bool | None = None,
        return_issue: bool | None = None,
        expand: str | None = None,
    ) -> None:
        """Edit issue"""
        params = self._client._build_params(
            **{
                "notifyUsers": notify_users,
                "overrideScreenSecurity": override_screen_security,
                "overrideEditableFlag": override_editable_flag,
                "returnIssue": return_issue,
                "expand": expand,
            }
        )
        await self._client._request(
            "PUT",
            f"/rest/api/3/issue/{issue_id_or_key}",
            params=params,
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    async def assign(self, issue_id_or_key: str, body: User) -> None:
        """Assign issue"""
        await self._client._request(
            "PUT",
            f"/rest/api/3/issue/{issue_id_or_key}/assignee",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    async def get_change_logs(
        self, issue_id_or_key: str, *, start_at: int | None = None, max_results: int | None = None
    ) -> PageBeanChangelog:
        """Get changelogs"""
        params = self._client._build_params(**{"startAt": start_at, "maxResults": max_results})
        resp = await self._client._request(
            "GET", f"/rest/api/3/issue/{issue_id_or_key}/changelog", params=params
        )
        return PageBeanChangelog.model_validate(resp.json())

    async def get_change_logs_by_ids(
        self, issue_id_or_key: str, body: IssueChangelogIds
    ) -> PageOfChangelogs:
        """Get changelogs by IDs"""
        resp = await self._client._request(
            "POST",
            f"/rest/api/3/issue/{issue_id_or_key}/changelog/list",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return PageOfChangelogs.model_validate(resp.json())

    async def get_edit_meta(
        self,
        issue_id_or_key: str,
        *,
        override_screen_security: bool | None = None,
        override_editable_flag: bool | None = None,
    ) -> IssueUpdateMetadata:
        """Get edit issue metadata"""
        params = self._client._build_params(
            **{
                "overrideScreenSecurity": override_screen_security,
                "overrideEditableFlag": override_editable_flag,
            }
        )
        resp = await self._client._request(
            "GET", f"/rest/api/3/issue/{issue_id_or_key}/editmeta", params=params
        )
        return IssueUpdateMetadata.model_validate(resp.json())

    async def notify(self, issue_id_or_key: str, body: Notification) -> None:
        """Send notification for issue"""
        await self._client._request(
            "POST",
            f"/rest/api/3/issue/{issue_id_or_key}/notify",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    async def get_transitions(
        self,
        issue_id_or_key: str,
        *,
        expand: str | None = None,
        transition_id: str | None = None,
        skip_remote_only_condition: bool | None = None,
        include_unavailable_transitions: bool | None = None,
        sort_by_ops_bar_and_status: bool | None = None,
    ) -> Transitions:
        """Get transitions"""
        params = self._client._build_params(
            **{
                "expand": expand,
                "transitionId": transition_id,
                "skipRemoteOnlyCondition": skip_remote_only_condition,
                "includeUnavailableTransitions": include_unavailable_transitions,
                "sortByOpsBarAndStatus": sort_by_ops_bar_and_status,
            }
        )
        resp = await self._client._request(
            "GET", f"/rest/api/3/issue/{issue_id_or_key}/transitions", params=params
        )
        return Transitions.model_validate(resp.json())

    async def transition(self, issue_id_or_key: str, body: IssueUpdateDetails) -> None:
        """Transition issue"""
        await self._client._request(
            "POST",
            f"/rest/api/3/issue/{issue_id_or_key}/transitions",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    async def export_archived(
        self, body: ArchivedIssuesFilterRequest
    ) -> ExportArchivedIssuesTaskProgressResponse:
        """Export archived issue(s)"""
        resp = await self._client._request(
            "PUT",
            "/rest/api/3/issues/archive/export",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return ExportArchivedIssuesTaskProgressResponse.model_validate(resp.json())

    async def match(self, body: IssuesAndJQLQueries) -> IssueMatches:
        """Check issues against JQL"""
        resp = await self._client._request(
            "POST", "/rest/api/3/jql/match", json=body.model_dump(by_alias=True, exclude_none=True)
        )
        return IssueMatches.model_validate(resp.json())

    async def redact(self, body: BulkRedactionRequest) -> str:
        """Redact"""
        resp = await self._client._request(
            "POST", "/rest/api/3/redact", json=body.model_dump(by_alias=True, exclude_none=True)
        )
        return resp.json()

    async def get_redaction_status(self, job_id: str) -> RedactionJobStatusResponse:
        """Get redaction status"""
        resp = await self._client._request("GET", f"/rest/api/3/redact/status/{job_id}")
        return RedactionJobStatusResponse.model_validate(resp.json())

    async def count(self, body: JQLCountRequest) -> JQLCountResults:
        """Count issues using JQL"""
        resp = await self._client._request(
            "POST",
            "/rest/api/3/search/approximate-count",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return JQLCountResults.model_validate(resp.json())

    async def search(
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

    async def search_post(self, body: SearchAndReconcileRequest) -> SearchAndReconcileResults:
        """Search for issues using JQL enhanced search (POST)"""
        resp = await self._client._request(
            "POST", "/rest/api/3/search/jql", json=body.model_dump(by_alias=True, exclude_none=True)
        )
        return SearchAndReconcileResults.model_validate(resp.json())

    async def get_navigator_default_columns(self) -> ColumnItem:
        """Get issue navigator default columns"""
        resp = await self._client._request("GET", "/rest/api/3/settings/columns")
        return ColumnItem.model_validate(resp.json())

    async def set_navigator_default_columns(self) -> None:
        """Set issue navigator default columns"""
        await self._client._request("PUT", "/rest/api/3/settings/columns")
        return None
