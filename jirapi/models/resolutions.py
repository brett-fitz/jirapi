"""Pydantic models for the resolutions domain."""

from __future__ import annotations

from typing import Annotated

from pydantic import AnyUrl, BaseModel, ConfigDict, Field


class CreateResolutionDetails(BaseModel):
    model_config = ConfigDict(
        extra="allow",
    )
    description: Annotated[
        str | None, Field(description="The description of the resolution.", max_length=255)
    ] = None
    name: Annotated[
        str,
        Field(
            description="The name of the resolution. Must be unique (case-insensitive).",
            max_length=60,
        ),
    ]


class ReorderIssueResolutionsRequest(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    after: Annotated[
        str | None,
        Field(description="The ID of the resolution. Required if `position` isn't provided."),
    ] = None
    ids: Annotated[
        list[str],
        Field(
            description="The list of resolution IDs to be reordered. Cannot contain duplicates nor after ID."
        ),
    ]
    position: Annotated[
        str | None,
        Field(
            description="The position for issue resolutions to be moved to. Required if `after` isn't provided."
        ),
    ] = None


class Resolution(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    description: Annotated[
        str | None, Field(description="The description of the issue resolution.")
    ] = None
    id: Annotated[str | None, Field(description="The ID of the issue resolution.")] = None
    name: Annotated[str | None, Field(description="The name of the issue resolution.")] = None
    self: Annotated[AnyUrl | None, Field(description="The URL of the issue resolution.")] = None


class ResolutionId(BaseModel):
    model_config = ConfigDict(
        extra="allow",
    )
    id: Annotated[str, Field(description="The ID of the issue resolution.")]


class SetDefaultResolutionRequest(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    id: Annotated[
        str,
        Field(
            description="The ID of the new default issue resolution. Must be an existing ID or null. Setting this to null erases the default resolution setting."
        ),
    ]


class UpdateResolutionDetails(BaseModel):
    model_config = ConfigDict(
        extra="allow",
    )
    description: Annotated[
        str | None, Field(description="The description of the resolution.", max_length=255)
    ] = None
    name: Annotated[
        str, Field(description="The name of the resolution. Must be unique.", max_length=60)
    ]


__all__ = [
    "CreateResolutionDetails",
    "ReorderIssueResolutionsRequest",
    "Resolution",
    "ResolutionId",
    "SetDefaultResolutionRequest",
    "UpdateResolutionDetails",
]
