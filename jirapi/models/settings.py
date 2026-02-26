"""Pydantic models for the settings domain."""

from __future__ import annotations

from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field


class ApplicationProperty(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    allowed_values: Annotated[
        list[str] | None,
        Field(alias="allowedValues", description="The allowed values, if applicable."),
    ] = None
    default_value: Annotated[
        str | None,
        Field(
            alias="defaultValue",
            description="The default value of the application property.",
        ),
    ] = None
    desc: Annotated[
        str | None, Field(description="The description of the application property.")
    ] = None
    example: str | None = None
    id: Annotated[
        str | None,
        Field(description="The ID of the application property. The ID and key are the same."),
    ] = None
    key: Annotated[
        str | None,
        Field(description="The key of the application property. The ID and key are the same."),
    ] = None
    name: Annotated[str | None, Field(description="The name of the application property.")] = None
    type: Annotated[str | None, Field(description="The data type of the application property.")] = (
        None
    )
    value: Annotated[str | None, Field(description="The new value.")] = None


class Configuration(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    attachments_enabled: Annotated[
        bool | None,
        Field(
            alias="attachmentsEnabled",
            description="Whether the ability to add attachments to issues is enabled.",
        ),
    ] = None
    issue_linking_enabled: Annotated[
        bool | None,
        Field(
            alias="issueLinkingEnabled",
            description="Whether the ability to link issues is enabled.",
        ),
    ] = None
    sub_tasks_enabled: Annotated[
        bool | None,
        Field(
            alias="subTasksEnabled",
            description="Whether the ability to create subtasks for issues is enabled.",
        ),
    ] = None
    time_tracking_configuration: Annotated[
        TimeTrackingConfiguration | None,
        Field(
            alias="timeTrackingConfiguration",
            description="The configuration of time tracking.",
        ),
    ] = None
    time_tracking_enabled: Annotated[
        bool | None,
        Field(
            alias="timeTrackingEnabled",
            description="Whether the ability to track time is enabled. This property is deprecated.",
        ),
    ] = None
    unassigned_issues_allowed: Annotated[
        bool | None,
        Field(
            alias="unassignedIssuesAllowed",
            description="Whether the ability to create unassigned issues is enabled. See [Configuring Jira application options](https://confluence.atlassian.com/x/uYXKM) for details.",
        ),
    ] = None
    voting_enabled: Annotated[
        bool | None,
        Field(
            alias="votingEnabled",
            description="Whether the ability for users to vote on issues is enabled. See [Configuring Jira application options](https://confluence.atlassian.com/x/uYXKM) for details.",
        ),
    ] = None
    watching_enabled: Annotated[
        bool | None,
        Field(
            alias="watchingEnabled",
            description="Whether the ability for users to watch issues is enabled. See [Configuring Jira application options](https://confluence.atlassian.com/x/uYXKM) for details.",
        ),
    ] = None


__all__ = [
    "ApplicationProperty",
    "Configuration",
]
