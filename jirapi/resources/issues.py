"""Resource classes for the Issues API group."""

from __future__ import annotations

from jirapi._resource import AsyncAPIResource, SyncAPIResource
from jirapi.models import (
    ArchivedIssuesFilterRequest,
    ArchiveIssueAsyncRequest,
    BulkChangelogRequestBean,
    BulkChangelogResponseBean,
    BulkFetchIssueRequestBean,
    BulkIssueResults,
    CreatedIssue,
    CreatedIssues,
    ExportArchivedIssuesTaskProgressResponse,
    IssueArchivalSyncRequest,
    IssueArchivalSyncResponse,
    IssueBean,
    IssueChangelogIds,
    IssueEvent,
    IssueLimitReportResponseBean,
    IssuesUpdateBean,
    IssueUpdateDetails,
    IssueUpdateMetadata,
    Notification,
    PageBeanChangelog,
    PageOfChangelogs,
    PageOfCreateMetaIssueTypes,
    PageOfCreateMetaIssueTypeWithField,
    Transitions,
    User,
)


class Issues(SyncAPIResource):
    """Synchronous resource for the Issues API group."""

    def get_bulk_changelogs(self, body: BulkChangelogRequestBean) -> BulkChangelogResponseBean:
        """Bulk fetch changelogs"""
        resp = self._client._request(
            "POST",
            "/rest/api/3/changelog/bulkfetch",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return BulkChangelogResponseBean.model_validate(resp.json())

    def get_events(self) -> IssueEvent:
        """Get events"""
        resp = self._client._request("GET", "/rest/api/3/events")
        return IssueEvent.model_validate(resp.json())

    def create_issue(
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

    def archive_issues_async(self, body: ArchiveIssueAsyncRequest) -> str:
        """Archive issue(s) by JQL"""
        resp = self._client._request(
            "POST",
            "/rest/api/3/issue/archive",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return resp.json()

    def archive_issues(self, body: IssueArchivalSyncRequest) -> IssueArchivalSyncResponse:
        """Archive issue(s) by issue ID/key"""
        resp = self._client._request(
            "PUT",
            "/rest/api/3/issue/archive",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return IssueArchivalSyncResponse.model_validate(resp.json())

    def create_issues(self, body: IssuesUpdateBean) -> CreatedIssues:
        """Bulk create issue"""
        resp = self._client._request(
            "POST", "/rest/api/3/issue/bulk", json=body.model_dump(by_alias=True, exclude_none=True)
        )
        return CreatedIssues.model_validate(resp.json())

    def bulk_fetch_issues(self, body: BulkFetchIssueRequestBean) -> BulkIssueResults:
        """Bulk fetch issues"""
        resp = self._client._request(
            "POST",
            "/rest/api/3/issue/bulkfetch",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return BulkIssueResults.model_validate(resp.json())

    def get_create_issue_meta_issue_types(
        self, project_id_or_key: str, *, start_at: int | None = None, max_results: int | None = None
    ) -> PageOfCreateMetaIssueTypes:
        """Get create metadata issue types for a project"""
        params = self._client._build_params(**{"startAt": start_at, "maxResults": max_results})
        resp = self._client._request(
            "GET", f"/rest/api/3/issue/createmeta/{project_id_or_key}/issuetypes", params=params
        )
        return PageOfCreateMetaIssueTypes.model_validate(resp.json())

    def get_create_issue_meta_issue_type_id(
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

    def get_issue_limit_report(
        self, *, is_returning_keys: bool | None = None
    ) -> IssueLimitReportResponseBean:
        """Get issue limit report"""
        params = self._client._build_params(**{"isReturningKeys": is_returning_keys})
        resp = self._client._request("GET", "/rest/api/3/issue/limit/report", params=params)
        return IssueLimitReportResponseBean.model_validate(resp.json())

    def unarchive_issues(self, body: IssueArchivalSyncRequest) -> IssueArchivalSyncResponse:
        """Unarchive issue(s) by issue keys/ID"""
        resp = self._client._request(
            "PUT",
            "/rest/api/3/issue/unarchive",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return IssueArchivalSyncResponse.model_validate(resp.json())

    def delete_issue(self, issue_id_or_key: str, *, delete_subtasks: str | None = None) -> None:
        """Delete issue"""
        params = self._client._build_params(**{"deleteSubtasks": delete_subtasks})
        self._client._request("DELETE", f"/rest/api/3/issue/{issue_id_or_key}", params=params)
        return None

    def get_issue(
        self,
        issue_id_or_key: str,
        *,
        fields: list[str] | None = None,
        fields_by_keys: bool | None = None,
        expand: str | None = None,
        properties: list[str] | None = None,
        update_history: bool | None = None,
        fail_fast: bool | None = None,
    ) -> IssueBean:
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
        return IssueBean.model_validate(resp.json())

    def edit_issue(
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

    def assign_issue(self, issue_id_or_key: str, body: User) -> None:
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

    def get_edit_issue_meta(
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

    def do_transition(self, issue_id_or_key: str, body: IssueUpdateDetails) -> None:
        """Transition issue"""
        self._client._request(
            "POST",
            f"/rest/api/3/issue/{issue_id_or_key}/transitions",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    def export_archived_issues(
        self, body: ArchivedIssuesFilterRequest
    ) -> ExportArchivedIssuesTaskProgressResponse:
        """Export archived issue(s)"""
        resp = self._client._request(
            "PUT",
            "/rest/api/3/issues/archive/export",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return ExportArchivedIssuesTaskProgressResponse.model_validate(resp.json())


class AsyncIssues(AsyncAPIResource):
    """Asynchronous resource for the Issues API group."""

    async def get_bulk_changelogs(
        self, body: BulkChangelogRequestBean
    ) -> BulkChangelogResponseBean:
        """Bulk fetch changelogs"""
        resp = await self._client._request(
            "POST",
            "/rest/api/3/changelog/bulkfetch",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return BulkChangelogResponseBean.model_validate(resp.json())

    async def get_events(self) -> IssueEvent:
        """Get events"""
        resp = await self._client._request("GET", "/rest/api/3/events")
        return IssueEvent.model_validate(resp.json())

    async def create_issue(
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

    async def archive_issues_async(self, body: ArchiveIssueAsyncRequest) -> str:
        """Archive issue(s) by JQL"""
        resp = await self._client._request(
            "POST",
            "/rest/api/3/issue/archive",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return resp.json()

    async def archive_issues(self, body: IssueArchivalSyncRequest) -> IssueArchivalSyncResponse:
        """Archive issue(s) by issue ID/key"""
        resp = await self._client._request(
            "PUT",
            "/rest/api/3/issue/archive",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return IssueArchivalSyncResponse.model_validate(resp.json())

    async def create_issues(self, body: IssuesUpdateBean) -> CreatedIssues:
        """Bulk create issue"""
        resp = await self._client._request(
            "POST", "/rest/api/3/issue/bulk", json=body.model_dump(by_alias=True, exclude_none=True)
        )
        return CreatedIssues.model_validate(resp.json())

    async def bulk_fetch_issues(self, body: BulkFetchIssueRequestBean) -> BulkIssueResults:
        """Bulk fetch issues"""
        resp = await self._client._request(
            "POST",
            "/rest/api/3/issue/bulkfetch",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return BulkIssueResults.model_validate(resp.json())

    async def get_create_issue_meta_issue_types(
        self, project_id_or_key: str, *, start_at: int | None = None, max_results: int | None = None
    ) -> PageOfCreateMetaIssueTypes:
        """Get create metadata issue types for a project"""
        params = self._client._build_params(**{"startAt": start_at, "maxResults": max_results})
        resp = await self._client._request(
            "GET", f"/rest/api/3/issue/createmeta/{project_id_or_key}/issuetypes", params=params
        )
        return PageOfCreateMetaIssueTypes.model_validate(resp.json())

    async def get_create_issue_meta_issue_type_id(
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

    async def get_issue_limit_report(
        self, *, is_returning_keys: bool | None = None
    ) -> IssueLimitReportResponseBean:
        """Get issue limit report"""
        params = self._client._build_params(**{"isReturningKeys": is_returning_keys})
        resp = await self._client._request("GET", "/rest/api/3/issue/limit/report", params=params)
        return IssueLimitReportResponseBean.model_validate(resp.json())

    async def unarchive_issues(self, body: IssueArchivalSyncRequest) -> IssueArchivalSyncResponse:
        """Unarchive issue(s) by issue keys/ID"""
        resp = await self._client._request(
            "PUT",
            "/rest/api/3/issue/unarchive",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return IssueArchivalSyncResponse.model_validate(resp.json())

    async def delete_issue(
        self, issue_id_or_key: str, *, delete_subtasks: str | None = None
    ) -> None:
        """Delete issue"""
        params = self._client._build_params(**{"deleteSubtasks": delete_subtasks})
        await self._client._request("DELETE", f"/rest/api/3/issue/{issue_id_or_key}", params=params)
        return None

    async def get_issue(
        self,
        issue_id_or_key: str,
        *,
        fields: list[str] | None = None,
        fields_by_keys: bool | None = None,
        expand: str | None = None,
        properties: list[str] | None = None,
        update_history: bool | None = None,
        fail_fast: bool | None = None,
    ) -> IssueBean:
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
        return IssueBean.model_validate(resp.json())

    async def edit_issue(
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

    async def assign_issue(self, issue_id_or_key: str, body: User) -> None:
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

    async def get_edit_issue_meta(
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

    async def do_transition(self, issue_id_or_key: str, body: IssueUpdateDetails) -> None:
        """Transition issue"""
        await self._client._request(
            "POST",
            f"/rest/api/3/issue/{issue_id_or_key}/transitions",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    async def export_archived_issues(
        self, body: ArchivedIssuesFilterRequest
    ) -> ExportArchivedIssuesTaskProgressResponse:
        """Export archived issue(s)"""
        resp = await self._client._request(
            "PUT",
            "/rest/api/3/issues/archive/export",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return ExportArchivedIssuesTaskProgressResponse.model_validate(resp.json())
