"""Pydantic models for the app data policies domain."""

from __future__ import annotations

from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field


class ProjectDataPolicy(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    any_content_blocked: Annotated[
        bool | None,
        Field(
            alias="anyContentBlocked",
            description="Whether the project contains any content inaccessible to the requesting application.",
        ),
    ] = None


class ProjectWithDataPolicy(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    data_policy: Annotated[
        ProjectDataPolicy | None, Field(alias="dataPolicy", description="Data policy.")
    ] = None
    id: Annotated[int | None, Field(description="The project ID.")] = None


class WorkspaceDataPolicy(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    any_content_blocked: Annotated[
        bool | None,
        Field(
            alias="anyContentBlocked",
            description="Whether the workspace contains any content inaccessible to the requesting application.",
        ),
    ] = None


class ProjectDataPolicies(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    project_data_policies: Annotated[
        list[ProjectWithDataPolicy] | None,
        Field(
            alias="projectDataPolicies",
            description="List of projects with data policies.",
        ),
    ] = None


__all__ = [
    "ProjectDataPolicy",
    "ProjectWithDataPolicy",
    "WorkspaceDataPolicy",
    "ProjectDataPolicies",
]
