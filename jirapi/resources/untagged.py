"""Resource classes for the untagged API group."""

from __future__ import annotations

from jirapi._resource import AsyncAPIResource, SyncAPIResource
from jirapi.models import BulkWorklogKeyRequestBean, BulkWorklogKeyResponseBean


class Untagged(SyncAPIResource):
    """Synchronous resource for the untagged API group."""

    def get_worklogs_by_issue_id_and_worklog_id(
        self, body: BulkWorklogKeyRequestBean
    ) -> BulkWorklogKeyResponseBean:
        """Get worklogs by issue id and worklog id"""
        resp = self._client._request(
            "POST",
            "/rest/internal/api/latest/worklog/bulk",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return BulkWorklogKeyResponseBean.model_validate(resp.json())


class AsyncUntagged(AsyncAPIResource):
    """Asynchronous resource for the untagged API group."""

    async def get_worklogs_by_issue_id_and_worklog_id(
        self, body: BulkWorklogKeyRequestBean
    ) -> BulkWorklogKeyResponseBean:
        """Get worklogs by issue id and worklog id"""
        resp = await self._client._request(
            "POST",
            "/rest/internal/api/latest/worklog/bulk",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return BulkWorklogKeyResponseBean.model_validate(resp.json())
