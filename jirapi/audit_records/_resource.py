"""Resource classes for audit_records."""

from __future__ import annotations

from jirapi._resource import AsyncAPIResource, SyncAPIResource
from jirapi.models import AuditRecords as AuditRecordsModel


class AuditRecords(SyncAPIResource):
    """Synchronous resource for audit_records."""

    def get(
        self,
        *,
        offset: int | None = None,
        limit: int | None = None,
        filter_: str | None = None,
        from_: str | None = None,
        to: str | None = None,
    ) -> AuditRecordsModel:
        """Get audit records"""
        params = self._client._build_params(
            **{"offset": offset, "limit": limit, "filter": filter_, "from": from_, "to": to}
        )
        resp = self._client._request("GET", "/rest/api/3/auditing/record", params=params)
        return AuditRecordsModel.model_validate(resp.json())


class AsyncAuditRecords(AsyncAPIResource):
    """Asynchronous resource for audit_records."""

    async def get(
        self,
        *,
        offset: int | None = None,
        limit: int | None = None,
        filter_: str | None = None,
        from_: str | None = None,
        to: str | None = None,
    ) -> AuditRecordsModel:
        """Get audit records"""
        params = self._client._build_params(
            **{"offset": offset, "limit": limit, "filter": filter_, "from": from_, "to": to}
        )
        resp = await self._client._request("GET", "/rest/api/3/auditing/record", params=params)
        return AuditRecordsModel.model_validate(resp.json())
