"""Pydantic models for the audit records domain."""

from __future__ import annotations

from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field


class AuditRecords(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    limit: Annotated[
        int | None,
        Field(
            description="The requested or default limit on the number of audit items to be returned."
        ),
    ] = None
    offset: Annotated[
        int | None,
        Field(description="The number of audit items skipped before the first item in this list."),
    ] = None
    records: Annotated[list[AuditRecord] | None, Field(description="The list of audit items.")] = (
        None
    )
    total: Annotated[int | None, Field(description="The total number of audit items returned.")] = (
        None
    )


__all__ = [
    "AuditRecords",
]
