"""Pydantic models for the avatars domain."""

from __future__ import annotations

from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field


class Avatars(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    custom: Annotated[list[Avatar] | None, Field(description="Custom avatars list.")] = None
    system: Annotated[list[Avatar] | None, Field(description="System avatars list.")] = None


class StreamingResponseBody(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )


class SystemAvatars(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    system: Annotated[list[Avatar] | None, Field(description="A list of avatar details.")] = None


__all__ = [
    "Avatars",
    "StreamingResponseBody",
    "SystemAvatars",
]
