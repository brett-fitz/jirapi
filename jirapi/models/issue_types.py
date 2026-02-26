"""Pydantic models for the issue types domain."""

from __future__ import annotations

from typing import Annotated

from pydantic import AnyUrl, BaseModel, ConfigDict, Field


class IssueTypeScheme(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    default_issue_type_id: Annotated[
        str | None,
        Field(
            alias="defaultIssueTypeId",
            description="The ID of the default issue type of the issue type scheme.",
        ),
    ] = None
    description: Annotated[
        str | None, Field(description="The description of the issue type scheme.")
    ] = None
    id: Annotated[str, Field(description="The ID of the issue type scheme.")]
    is_default: Annotated[
        bool | None,
        Field(
            alias="isDefault",
            description="Whether the issue type scheme is the default.",
        ),
    ] = None
    name: Annotated[str, Field(description="The name of the issue type scheme.")]


class IssueTypeSchemeDetails(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    default_issue_type_id: Annotated[
        str | None,
        Field(
            alias="defaultIssueTypeId",
            description="The ID of the default issue type of the issue type scheme. This ID must be included in `issueTypeIds`.",
        ),
    ] = None
    description: Annotated[
        str | None,
        Field(
            description="The description of the issue type scheme. The maximum length is 4000 characters."
        ),
    ] = None
    issue_type_ids: Annotated[
        list[str],
        Field(
            alias="issueTypeIds",
            description="The list of issue types IDs of the issue type scheme. At least one standard issue type ID is required.",
        ),
    ]
    name: Annotated[
        str,
        Field(
            description="The name of the issue type scheme. The name must be unique. The maximum length is 255 characters."
        ),
    ]


class IssueTypeSchemeID(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    issue_type_scheme_id: Annotated[
        str, Field(alias="issueTypeSchemeId", description="The ID of the issue type scheme.")
    ]


class IssueTypeSchemeMapping(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    issue_type_id: Annotated[
        str, Field(alias="issueTypeId", description="The ID of the issue type.")
    ]
    issue_type_scheme_id: Annotated[
        str, Field(alias="issueTypeSchemeId", description="The ID of the issue type scheme.")
    ]


class IssueTypeSchemeProjectAssociation(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    issue_type_scheme_id: Annotated[
        str, Field(alias="issueTypeSchemeId", description="The ID of the issue type scheme.")
    ]
    project_id: Annotated[str, Field(alias="projectId", description="The ID of the project.")]


class IssueTypeSchemeProjects(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    issue_type_scheme: Annotated[
        IssueTypeScheme,
        Field(alias="issueTypeScheme", description="Details of an issue type scheme."),
    ]
    project_ids: Annotated[
        list[str],
        Field(
            alias="projectIds",
            description="The IDs of the projects using the issue type scheme.",
        ),
    ]


class IssueTypeSchemeUpdateDetails(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    default_issue_type_id: Annotated[
        str | None,
        Field(
            alias="defaultIssueTypeId",
            description="The ID of the default issue type of the issue type scheme.",
        ),
    ] = None
    description: Annotated[
        str | None,
        Field(
            description="The description of the issue type scheme. The maximum length is 4000 characters."
        ),
    ] = None
    name: Annotated[
        str | None,
        Field(
            description="The name of the issue type scheme. The name must be unique. The maximum length is 255 characters."
        ),
    ] = None


class OrderOfIssueTypes(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    after: Annotated[
        str | None,
        Field(
            description="The ID of the issue type to place the moved issue types after. Required if `position` isn't provided."
        ),
    ] = None
    issue_type_ids: Annotated[
        list[str],
        Field(
            alias="issueTypeIds",
            description="A list of the issue type IDs to move. The order of the issue type IDs in the list is the order they are given after the move.",
        ),
    ]
    position: Annotated[
        Position1 | None,
        Field(
            description="The position the issue types should be moved to. Required if `after` isn't provided."
        ),
    ] = None


class PageBeanIssueTypeScheme(BaseModel):
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
    values: Annotated[list[IssueTypeScheme] | None, Field(description="The list of items.")] = None


class PageBeanIssueTypeSchemeMapping(BaseModel):
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
        list[IssueTypeSchemeMapping] | None, Field(description="The list of items.")
    ] = None


class PageBeanIssueTypeSchemeProjects(BaseModel):
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
        list[IssueTypeSchemeProjects] | None, Field(description="The list of items.")
    ] = None


__all__ = [
    "IssueTypeScheme",
    "IssueTypeSchemeDetails",
    "IssueTypeSchemeID",
    "IssueTypeSchemeMapping",
    "IssueTypeSchemeProjectAssociation",
    "IssueTypeSchemeProjects",
    "IssueTypeSchemeUpdateDetails",
    "OrderOfIssueTypes",
    "PageBeanIssueTypeScheme",
    "PageBeanIssueTypeSchemeMapping",
    "PageBeanIssueTypeSchemeProjects",
]
