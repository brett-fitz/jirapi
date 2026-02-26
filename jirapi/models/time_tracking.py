"""Pydantic models for the time tracking domain."""

from __future__ import annotations

from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field


class TimeTrackingProvider(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    key: Annotated[
        str, Field(description="The key for the time tracking provider. For example, *JIRA*.")
    ]
    name: Annotated[
        str | None,
        Field(
            description="The name of the time tracking provider. For example, *JIRA provided time tracking*."
        ),
    ] = None
    url: Annotated[
        str | None,
        Field(
            description="The URL of the configuration page for the time tracking provider app. For example, */example/config/url*. This property is only returned if the `adminPageKey` property is set in the module descriptor of the time tracking provider app."
        ),
    ] = None


__all__ = [
    "TimeTrackingProvider",
]
