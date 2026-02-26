"""Pydantic models for the license metrics domain."""

from __future__ import annotations

from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field


class LicenseMetric(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    key: Annotated[str | None, Field(description="The key of a specific license metric.")] = None
    value: Annotated[
        str | None,
        Field(
            description="The calculated value of a licence metric linked to the key. An example licence metric is the approximate number of user accounts."
        ),
    ] = None


class LicensedApplication(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    id: Annotated[str, Field(description="The ID of the application.")]
    plan: Annotated[Plan, Field(description="The licensing plan.")]


class License(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    applications: Annotated[
        list[LicensedApplication], Field(description="The applications under this license.")
    ]


__all__ = [
    "LicenseMetric",
    "LicensedApplication",
    "License",
]
