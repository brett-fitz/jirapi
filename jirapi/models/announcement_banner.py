"""Pydantic models for the announcement banner domain."""

from __future__ import annotations

from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field


class AnnouncementBannerConfiguration(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    hash_id: Annotated[
        str | None,
        Field(
            alias="hashId",
            description="Hash of the banner data. The client detects updates by comparing hash IDs.",
        ),
    ] = None
    is_dismissible: Annotated[
        bool | None,
        Field(
            alias="isDismissible",
            description="Flag indicating if the announcement banner can be dismissed by the user.",
        ),
    ] = None
    is_enabled: Annotated[
        bool | None,
        Field(
            alias="isEnabled",
            description="Flag indicating if the announcement banner is enabled or not.",
        ),
    ] = None
    message: Annotated[str | None, Field(description="The text on the announcement banner.")] = None
    visibility: Annotated[
        Visibility | None, Field(description="Visibility of the announcement banner.")
    ] = None


class AnnouncementBannerConfigurationUpdate(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    is_dismissible: Annotated[
        bool | None,
        Field(
            alias="isDismissible",
            description="Flag indicating if the announcement banner can be dismissed by the user.",
        ),
    ] = None
    is_enabled: Annotated[
        bool | None,
        Field(
            alias="isEnabled",
            description="Flag indicating if the announcement banner is enabled or not.",
        ),
    ] = None
    message: Annotated[str | None, Field(description="The text on the announcement banner.")] = None
    visibility: Annotated[
        str | None,
        Field(description="Visibility of the announcement banner. Can be public or private."),
    ] = None


__all__ = [
    "AnnouncementBannerConfiguration",
    "AnnouncementBannerConfigurationUpdate",
]
