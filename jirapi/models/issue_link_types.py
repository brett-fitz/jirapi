"""Pydantic models for the issue link types domain."""

from __future__ import annotations

from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field


class IssueLinkTypes(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    issue_link_types: Annotated[
        list[IssueLinkType] | None,
        Field(alias="issueLinkTypes", description="The issue link type bean."),
    ] = None


__all__ = [
    "IssueLinkTypes",
]
