"""Pydantic models for the statuses domain."""

from __future__ import annotations

from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field


class StatusCreate(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    description: Annotated[str | None, Field(description="The description of the status.")] = None
    name: Annotated[str, Field(description="The name of the status.", max_length=255)]
    status_category: Annotated[
        StatusCategory4, Field(alias="statusCategory", description="The category of the status.")
    ]


class StatusProjectIssueTypeUsage(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    id: Annotated[str | None, Field(description="The issue type ID.")] = None


class StatusProjectIssueTypeUsagePage(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    next_page_token: Annotated[
        str | None,
        Field(
            alias="nextPageToken",
            description="Page token for the next page of issue type usages.",
        ),
    ] = None
    values: Annotated[
        list[StatusProjectIssueTypeUsage] | None, Field(description="The list of issue types.")
    ] = None


class StatusProjectUsage(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    id: Annotated[str | None, Field(description="The project ID.")] = None


class StatusProjectUsagePage(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    next_page_token: Annotated[
        str | None,
        Field(
            alias="nextPageToken",
            description="Page token for the next page of issue type usages.",
        ),
    ] = None
    values: Annotated[
        list[StatusProjectUsage] | None, Field(description="The list of projects.")
    ] = None


class StatusScope(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    project: ProjectId | None = None
    type: Annotated[
        Type28,
        Field(
            description="The scope of the status. `GLOBAL` for company-managed projects and `PROJECT` for team-managed projects."
        ),
    ]


class StatusUpdate(BaseModel):
    model_config = ConfigDict(
        extra="allow",
    )
    description: Annotated[str | None, Field(description="The description of the status.")] = None
    id: Annotated[str, Field(description="The ID of the status.")]
    name: Annotated[str, Field(description="The name of the status.")]
    status_category: Annotated[
        StatusCategory4, Field(alias="statusCategory", description="The category of the status.")
    ]


class StatusUpdateRequest(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    statuses: Annotated[
        list[StatusUpdate], Field(description="The list of statuses that will be updated.")
    ]


class StatusWorkflowUsageWorkflow(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    id: Annotated[str | None, Field(description="The workflow ID.")] = None


class JiraStatus(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    description: Annotated[str | None, Field(description="The description of the status.")] = None
    id: Annotated[str | None, Field(description="The ID of the status.")] = None
    name: Annotated[str | None, Field(description="The name of the status.")] = None
    scope: StatusScope | None = None
    status_category: Annotated[
        StatusCategory | None,
        Field(alias="statusCategory", description="The category of the status."),
    ] = None


class PageOfStatuses(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    is_last: Annotated[
        bool | None, Field(alias="isLast", description="Whether this is the last page.")
    ] = None
    max_results: Annotated[
        int | None,
        Field(
            alias="maxResults",
            description="The maximum number of items that could be returned.",
        ),
    ] = None
    next_page: Annotated[
        str | None,
        Field(alias="nextPage", description="The URL of the next page of results, if any."),
    ] = None
    self: Annotated[str | None, Field(description="The URL of this page.")] = None
    start_at: Annotated[
        int | None,
        Field(
            alias="startAt",
            description="The index of the first item returned on the page.",
        ),
    ] = None
    total: Annotated[int | None, Field(description="Number of items that satisfy the search.")] = (
        None
    )
    values: Annotated[list[JiraStatus] | None, Field(description="The list of items.")] = None


class StatusCreateRequest(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    scope: StatusScope
    statuses: Annotated[
        list[StatusCreate], Field(description="Details of the statuses being created.")
    ]


class StatusProjectIssueTypeUsageDTO(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    issue_types: Annotated[StatusProjectIssueTypeUsagePage | None, Field(alias="issueTypes")] = None
    project_id: Annotated[str | None, Field(alias="projectId", description="The project ID.")] = (
        None
    )
    status_id: Annotated[str | None, Field(alias="statusId", description="The status ID.")] = None


class StatusProjectUsageDTO(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    projects: StatusProjectUsagePage | None = None
    status_id: Annotated[str | None, Field(alias="statusId", description="The status ID.")] = None


class StatusWorkflowUsagePage(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    next_page_token: Annotated[
        str | None,
        Field(
            alias="nextPageToken",
            description="Page token for the next page of issue type usages.",
        ),
    ] = None
    values: Annotated[
        list[StatusWorkflowUsageWorkflow] | None, Field(description="The list of statuses.")
    ] = None


class StatusWorkflowUsageDTO(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    status_id: Annotated[str | None, Field(alias="statusId", description="The status ID.")] = None
    workflows: StatusWorkflowUsagePage | None = None


__all__ = [
    "StatusCreate",
    "StatusProjectIssueTypeUsage",
    "StatusProjectIssueTypeUsagePage",
    "StatusProjectUsage",
    "StatusProjectUsagePage",
    "StatusScope",
    "StatusUpdate",
    "StatusUpdateRequest",
    "StatusWorkflowUsageWorkflow",
    "JiraStatus",
    "PageOfStatuses",
    "StatusCreateRequest",
    "StatusProjectIssueTypeUsageDTO",
    "StatusProjectUsageDTO",
    "StatusWorkflowUsagePage",
    "StatusWorkflowUsageDTO",
]
