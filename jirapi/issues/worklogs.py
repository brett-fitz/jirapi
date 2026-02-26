"""Resource classes for issues.worklogs."""

from __future__ import annotations

from jirapi._resource import AsyncAPIResource, SyncAPIResource
from jirapi.models import (
    BulkWorklogKeyRequest,
    BulkWorklogKeyResponse,
    ChangedWorklogs,
    PageOfWorklogs,
    Worklog,
    WorklogIdsRequest,
    WorklogsMoveRequest,
)


class IssueWorklogs(SyncAPIResource):
    """Synchronous resource for issues.worklogs."""

    def bulk_delete(
        self,
        issue_id_or_key: str,
        body: WorklogIdsRequest,
        *,
        adjust_estimate: str | None = None,
        override_editable_flag: bool | None = None,
    ) -> None:
        """Bulk delete worklogs"""
        params = self._client._build_params(
            **{"adjustEstimate": adjust_estimate, "overrideEditableFlag": override_editable_flag}
        )
        self._client._request(
            "DELETE",
            f"/rest/api/3/issue/{issue_id_or_key}/worklog",
            params=params,
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    def list(
        self,
        issue_id_or_key: str,
        *,
        start_at: int | None = None,
        max_results: int | None = None,
        started_after: int | None = None,
        started_before: int | None = None,
        expand: str | None = None,
    ) -> PageOfWorklogs:
        """Get issue worklogs"""
        params = self._client._build_params(
            **{
                "startAt": start_at,
                "maxResults": max_results,
                "startedAfter": started_after,
                "startedBefore": started_before,
                "expand": expand,
            }
        )
        resp = self._client._request(
            "GET", f"/rest/api/3/issue/{issue_id_or_key}/worklog", params=params
        )
        return PageOfWorklogs.model_validate(resp.json())

    def add(
        self,
        issue_id_or_key: str,
        body: Worklog,
        *,
        notify_users: bool | None = None,
        adjust_estimate: str | None = None,
        new_estimate: str | None = None,
        reduce_by: str | None = None,
        expand: str | None = None,
        override_editable_flag: bool | None = None,
    ) -> Worklog:
        """Add worklog"""
        params = self._client._build_params(
            **{
                "notifyUsers": notify_users,
                "adjustEstimate": adjust_estimate,
                "newEstimate": new_estimate,
                "reduceBy": reduce_by,
                "expand": expand,
                "overrideEditableFlag": override_editable_flag,
            }
        )
        resp = self._client._request(
            "POST",
            f"/rest/api/3/issue/{issue_id_or_key}/worklog",
            params=params,
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return Worklog.model_validate(resp.json())

    def bulk_move(
        self,
        issue_id_or_key: str,
        body: WorklogsMoveRequest,
        *,
        adjust_estimate: str | None = None,
        override_editable_flag: bool | None = None,
    ) -> None:
        """Bulk move worklogs"""
        params = self._client._build_params(
            **{"adjustEstimate": adjust_estimate, "overrideEditableFlag": override_editable_flag}
        )
        self._client._request(
            "POST",
            f"/rest/api/3/issue/{issue_id_or_key}/worklog/move",
            params=params,
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    def delete(
        self,
        issue_id_or_key: str,
        id_: str,
        *,
        notify_users: bool | None = None,
        adjust_estimate: str | None = None,
        new_estimate: str | None = None,
        increase_by: str | None = None,
        override_editable_flag: bool | None = None,
    ) -> None:
        """Delete worklog"""
        params = self._client._build_params(
            **{
                "notifyUsers": notify_users,
                "adjustEstimate": adjust_estimate,
                "newEstimate": new_estimate,
                "increaseBy": increase_by,
                "overrideEditableFlag": override_editable_flag,
            }
        )
        self._client._request(
            "DELETE", f"/rest/api/3/issue/{issue_id_or_key}/worklog/{id_}", params=params
        )
        return None

    def get(self, issue_id_or_key: str, id_: str, *, expand: str | None = None) -> Worklog:
        """Get worklog"""
        params = self._client._build_params(**{"expand": expand})
        resp = self._client._request(
            "GET", f"/rest/api/3/issue/{issue_id_or_key}/worklog/{id_}", params=params
        )
        return Worklog.model_validate(resp.json())

    def update(
        self,
        issue_id_or_key: str,
        id_: str,
        body: Worklog,
        *,
        notify_users: bool | None = None,
        adjust_estimate: str | None = None,
        new_estimate: str | None = None,
        expand: str | None = None,
        override_editable_flag: bool | None = None,
    ) -> Worklog:
        """Update worklog"""
        params = self._client._build_params(
            **{
                "notifyUsers": notify_users,
                "adjustEstimate": adjust_estimate,
                "newEstimate": new_estimate,
                "expand": expand,
                "overrideEditableFlag": override_editable_flag,
            }
        )
        resp = self._client._request(
            "PUT",
            f"/rest/api/3/issue/{issue_id_or_key}/worklog/{id_}",
            params=params,
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return Worklog.model_validate(resp.json())

    def get_deleted_ids(self, *, since: int | None = None) -> ChangedWorklogs:
        """Get IDs of deleted worklogs"""
        params = self._client._build_params(**{"since": since})
        resp = self._client._request("GET", "/rest/api/3/worklog/deleted", params=params)
        return ChangedWorklogs.model_validate(resp.json())

    def get_by_ids(self, body: WorklogIdsRequest, *, expand: str | None = None) -> Worklog:
        """Get worklogs"""
        params = self._client._build_params(**{"expand": expand})
        resp = self._client._request(
            "POST",
            "/rest/api/3/worklog/list",
            params=params,
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return Worklog.model_validate(resp.json())

    def get_modified_ids(
        self, *, since: int | None = None, expand: str | None = None
    ) -> ChangedWorklogs:
        """Get IDs of updated worklogs"""
        params = self._client._build_params(**{"since": since, "expand": expand})
        resp = self._client._request("GET", "/rest/api/3/worklog/updated", params=params)
        return ChangedWorklogs.model_validate(resp.json())

    def get_by_ids_legacy(self, body: BulkWorklogKeyRequest) -> BulkWorklogKeyResponse:
        """Get worklogs by issue id and worklog id"""
        resp = self._client._request(
            "POST",
            "/rest/internal/api/latest/worklog/bulk",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return BulkWorklogKeyResponse.model_validate(resp.json())


class AsyncIssueWorklogs(AsyncAPIResource):
    """Asynchronous resource for issues.worklogs."""

    async def bulk_delete(
        self,
        issue_id_or_key: str,
        body: WorklogIdsRequest,
        *,
        adjust_estimate: str | None = None,
        override_editable_flag: bool | None = None,
    ) -> None:
        """Bulk delete worklogs"""
        params = self._client._build_params(
            **{"adjustEstimate": adjust_estimate, "overrideEditableFlag": override_editable_flag}
        )
        await self._client._request(
            "DELETE",
            f"/rest/api/3/issue/{issue_id_or_key}/worklog",
            params=params,
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    async def list(
        self,
        issue_id_or_key: str,
        *,
        start_at: int | None = None,
        max_results: int | None = None,
        started_after: int | None = None,
        started_before: int | None = None,
        expand: str | None = None,
    ) -> PageOfWorklogs:
        """Get issue worklogs"""
        params = self._client._build_params(
            **{
                "startAt": start_at,
                "maxResults": max_results,
                "startedAfter": started_after,
                "startedBefore": started_before,
                "expand": expand,
            }
        )
        resp = await self._client._request(
            "GET", f"/rest/api/3/issue/{issue_id_or_key}/worklog", params=params
        )
        return PageOfWorklogs.model_validate(resp.json())

    async def add(
        self,
        issue_id_or_key: str,
        body: Worklog,
        *,
        notify_users: bool | None = None,
        adjust_estimate: str | None = None,
        new_estimate: str | None = None,
        reduce_by: str | None = None,
        expand: str | None = None,
        override_editable_flag: bool | None = None,
    ) -> Worklog:
        """Add worklog"""
        params = self._client._build_params(
            **{
                "notifyUsers": notify_users,
                "adjustEstimate": adjust_estimate,
                "newEstimate": new_estimate,
                "reduceBy": reduce_by,
                "expand": expand,
                "overrideEditableFlag": override_editable_flag,
            }
        )
        resp = await self._client._request(
            "POST",
            f"/rest/api/3/issue/{issue_id_or_key}/worklog",
            params=params,
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return Worklog.model_validate(resp.json())

    async def bulk_move(
        self,
        issue_id_or_key: str,
        body: WorklogsMoveRequest,
        *,
        adjust_estimate: str | None = None,
        override_editable_flag: bool | None = None,
    ) -> None:
        """Bulk move worklogs"""
        params = self._client._build_params(
            **{"adjustEstimate": adjust_estimate, "overrideEditableFlag": override_editable_flag}
        )
        await self._client._request(
            "POST",
            f"/rest/api/3/issue/{issue_id_or_key}/worklog/move",
            params=params,
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    async def delete(
        self,
        issue_id_or_key: str,
        id_: str,
        *,
        notify_users: bool | None = None,
        adjust_estimate: str | None = None,
        new_estimate: str | None = None,
        increase_by: str | None = None,
        override_editable_flag: bool | None = None,
    ) -> None:
        """Delete worklog"""
        params = self._client._build_params(
            **{
                "notifyUsers": notify_users,
                "adjustEstimate": adjust_estimate,
                "newEstimate": new_estimate,
                "increaseBy": increase_by,
                "overrideEditableFlag": override_editable_flag,
            }
        )
        await self._client._request(
            "DELETE", f"/rest/api/3/issue/{issue_id_or_key}/worklog/{id_}", params=params
        )
        return None

    async def get(self, issue_id_or_key: str, id_: str, *, expand: str | None = None) -> Worklog:
        """Get worklog"""
        params = self._client._build_params(**{"expand": expand})
        resp = await self._client._request(
            "GET", f"/rest/api/3/issue/{issue_id_or_key}/worklog/{id_}", params=params
        )
        return Worklog.model_validate(resp.json())

    async def update(
        self,
        issue_id_or_key: str,
        id_: str,
        body: Worklog,
        *,
        notify_users: bool | None = None,
        adjust_estimate: str | None = None,
        new_estimate: str | None = None,
        expand: str | None = None,
        override_editable_flag: bool | None = None,
    ) -> Worklog:
        """Update worklog"""
        params = self._client._build_params(
            **{
                "notifyUsers": notify_users,
                "adjustEstimate": adjust_estimate,
                "newEstimate": new_estimate,
                "expand": expand,
                "overrideEditableFlag": override_editable_flag,
            }
        )
        resp = await self._client._request(
            "PUT",
            f"/rest/api/3/issue/{issue_id_or_key}/worklog/{id_}",
            params=params,
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return Worklog.model_validate(resp.json())

    async def get_deleted_ids(self, *, since: int | None = None) -> ChangedWorklogs:
        """Get IDs of deleted worklogs"""
        params = self._client._build_params(**{"since": since})
        resp = await self._client._request("GET", "/rest/api/3/worklog/deleted", params=params)
        return ChangedWorklogs.model_validate(resp.json())

    async def get_by_ids(self, body: WorklogIdsRequest, *, expand: str | None = None) -> Worklog:
        """Get worklogs"""
        params = self._client._build_params(**{"expand": expand})
        resp = await self._client._request(
            "POST",
            "/rest/api/3/worklog/list",
            params=params,
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return Worklog.model_validate(resp.json())

    async def get_modified_ids(
        self, *, since: int | None = None, expand: str | None = None
    ) -> ChangedWorklogs:
        """Get IDs of updated worklogs"""
        params = self._client._build_params(**{"since": since, "expand": expand})
        resp = await self._client._request("GET", "/rest/api/3/worklog/updated", params=params)
        return ChangedWorklogs.model_validate(resp.json())

    async def get_by_ids_legacy(self, body: BulkWorklogKeyRequest) -> BulkWorklogKeyResponse:
        """Get worklogs by issue id and worklog id"""
        resp = await self._client._request(
            "POST",
            "/rest/internal/api/latest/worklog/bulk",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return BulkWorklogKeyResponse.model_validate(resp.json())
