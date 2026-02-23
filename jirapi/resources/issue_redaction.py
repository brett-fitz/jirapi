"""Resource classes for the Issue redaction API group."""

from __future__ import annotations

from jirapi._resource import AsyncAPIResource, SyncAPIResource
from jirapi.models import BulkRedactionRequest, RedactionJobStatusResponse


class IssueRedaction(SyncAPIResource):
    """Synchronous resource for the Issue redaction API group."""

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


class AsyncIssueRedaction(AsyncAPIResource):
    """Asynchronous resource for the Issue redaction API group."""

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
