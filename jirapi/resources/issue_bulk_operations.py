"""Resource classes for the Issue bulk operations API group."""

from __future__ import annotations

from jirapi._resource import AsyncAPIResource, SyncAPIResource
from jirapi.models import (
    BulkEditGetFields,
    BulkOperationProgress,
    BulkTransitionGetAvailableTransitions,
    IssueBulkDeletePayload,
    IssueBulkEditPayload,
    IssueBulkMovePayload,
    IssueBulkTransitionPayload,
    IssueBulkWatchOrUnwatchPayload,
    SubmittedBulkOperation,
)


class IssueBulkOperations(SyncAPIResource):
    """Synchronous resource for the Issue bulk operations API group."""

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


class AsyncIssueBulkOperations(AsyncAPIResource):
    """Asynchronous resource for the Issue bulk operations API group."""

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
