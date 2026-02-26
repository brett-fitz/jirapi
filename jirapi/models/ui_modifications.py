"""Pydantic models for the ui modifications domain."""

from __future__ import annotations

from typing import Annotated, Any

from pydantic import AnyUrl, BaseModel, ConfigDict, Field


class DetailedErrorCollection(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    details: Annotated[
        dict[str, Any] | None,
        Field(description="Map of objects representing additional details for an error"),
    ] = None
    error_messages: Annotated[
        list[str] | None,
        Field(
            alias="errorMessages",
            description="The list of error messages produced by this operation. For example, \"input parameter 'key' must be provided\"",
        ),
    ] = None
    errors: Annotated[
        dict[str, str] | None,
        Field(
            description='The list of errors by parameter returned by the operation. For example,"projectKey": "Project keys must start with an uppercase letter, followed by one or more uppercase alphanumeric characters."'
        ),
    ] = None


class UiModificationContextDetails(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    id: Annotated[str | None, Field(description="The ID of the UI modification context.")] = None
    is_available: Annotated[
        bool | None,
        Field(
            alias="isAvailable",
            description="Whether a context is available. For example, when a project is deleted the context becomes unavailable.",
        ),
    ] = None
    issue_type_id: Annotated[
        str | None,
        Field(
            alias="issueTypeId",
            description="The issue type ID of the context. Null is treated as a wildcard, meaning the UI modification will be applied to all issue types. Each UI modification context can have a maximum of one wildcard.",
        ),
    ] = None
    portal_id: Annotated[
        str | None,
        Field(
            alias="portalId",
            description="The portal ID of the context. Only required for Jira Service Management request create portal view (`JSMRequestCreate`).",
        ),
    ] = None
    project_id: Annotated[
        str | None,
        Field(
            alias="projectId",
            description="The project ID of the context. Null is treated as a wildcard, meaning the UI modification will be applied to all projects. Each UI modification context can have a maximum of one wildcard.",
        ),
    ] = None
    request_type_id: Annotated[
        str | None,
        Field(
            alias="requestTypeId",
            description="The request type ID of the context. Only required for Jira Service Management request create portal view (`JSMRequestCreate`).",
        ),
    ] = None
    view_type: Annotated[
        ViewType | None,
        Field(
            alias="viewType",
            description="The view type of the context.  \nSupported values:\n\n *  `GIC` \\- Jira global issue create\n *  `IssueView` \\- Jira issue view\n *  `IssueTransition` \\- Jira issue transition\n *  `JSMRequestCreate` \\- Jira Service Management request create portal view\n\nFor Jira view types (`GIC`, `IssueView`, `IssueTransition`), null is treated as a wildcard, meaning the UI modification will be applied to all view types. Each Jira context can have a maximum of one wildcard.  \n  \nWildcards are not applicable for JSM contexts.",
        ),
    ] = None


class UiModificationDetails(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    contexts: Annotated[
        list[UiModificationContextDetails] | None,
        Field(
            description="List of contexts of the UI modification. The maximum number of contexts is 1000."
        ),
    ] = None
    data: Annotated[
        str | None,
        Field(
            description="The data of the UI modification. The maximum size of the data is 50000 characters."
        ),
    ] = None
    description: Annotated[
        str | None,
        Field(
            description="The description of the UI modification. The maximum length is 255 characters."
        ),
    ] = None
    id: Annotated[str, Field(description="The ID of the UI modification.")]
    name: Annotated[
        str,
        Field(description="The name of the UI modification. The maximum length is 255 characters."),
    ]
    self: Annotated[str, Field(description="The URL of the UI modification.")]


class UiModificationIdentifiers(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    id: Annotated[str, Field(description="The ID of the UI modification.")]
    self: Annotated[str, Field(description="The URL of the UI modification.")]


class UpdateUiModificationDetails(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    contexts: Annotated[
        list[UiModificationContextDetails] | None,
        Field(
            description="List of contexts of the UI modification. The maximum number of contexts is 1000. If provided, replaces all existing contexts."
        ),
    ] = None
    data: Annotated[
        str | None,
        Field(
            description="The data of the UI modification. The maximum size of the data is 50000 characters."
        ),
    ] = None
    description: Annotated[
        str | None,
        Field(
            description="The description of the UI modification. The maximum length is 255 characters."
        ),
    ] = None
    name: Annotated[
        str | None,
        Field(description="The name of the UI modification. The maximum length is 255 characters."),
    ] = None


class CreateUiModificationDetails(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    contexts: Annotated[
        list[UiModificationContextDetails] | None,
        Field(
            description="List of contexts of the UI modification. The maximum number of contexts is 1000."
        ),
    ] = None
    data: Annotated[
        str | None,
        Field(
            description="The data of the UI modification. The maximum size of the data is 50000 characters."
        ),
    ] = None
    description: Annotated[
        str | None,
        Field(
            description="The description of the UI modification. The maximum length is 255 characters."
        ),
    ] = None
    name: Annotated[
        str,
        Field(description="The name of the UI modification. The maximum length is 255 characters."),
    ]


class PageBeanUiModificationDetails(BaseModel):
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
        AnyUrl | None,
        Field(
            alias="nextPage",
            description="If there is another page of results, the URL of the next page.",
        ),
    ] = None
    self: Annotated[AnyUrl | None, Field(description="The URL of the page.")] = None
    start_at: Annotated[
        int | None, Field(alias="startAt", description="The index of the first item returned.")
    ] = None
    total: Annotated[int | None, Field(description="The number of items returned.")] = None
    values: Annotated[
        list[UiModificationDetails] | None, Field(description="The list of items.")
    ] = None


__all__ = [
    "DetailedErrorCollection",
    "UiModificationContextDetails",
    "UiModificationDetails",
    "UiModificationIdentifiers",
    "UpdateUiModificationDetails",
    "CreateUiModificationDetails",
    "PageBeanUiModificationDetails",
]
