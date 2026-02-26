"""Pydantic models for the security schemes domain."""

from __future__ import annotations

from typing import Annotated

from pydantic import AnyUrl, BaseModel, ConfigDict, Field


class DefaultLevelValue(BaseModel):
    model_config = ConfigDict(
        extra="allow",
    )
    default_level_id: Annotated[
        str,
        Field(
            alias="defaultLevelId",
            description="The ID of the issue security level to set as default for the specified scheme. Providing null will reset the default level.",
        ),
    ]
    issue_security_scheme_id: Annotated[
        str,
        Field(
            alias="issueSecuritySchemeId",
            description="The ID of the issue security scheme to set default level for.",
        ),
    ]


class IssueSecuritySchemeToProjectMapping(BaseModel):
    model_config = ConfigDict(
        extra="allow",
    )
    issue_security_scheme_id: Annotated[str | None, Field(alias="issueSecuritySchemeId")] = None
    project_id: Annotated[str | None, Field(alias="projectId")] = None


class PageBeanIssueSecuritySchemeToProjectMapping(BaseModel):
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
        list[IssueSecuritySchemeToProjectMapping] | None, Field(description="The list of items.")
    ] = None


class SecurityLevelMember(BaseModel):
    model_config = ConfigDict(
        extra="allow",
    )
    holder: Annotated[
        PermissionHolder,
        Field(
            description="The user or group being granted the permission. It consists of a `type` and a type-dependent `parameter`. See [Holder object](../api-group-permission-schemes/#holder-object) in *Get all permission schemes* for more information."
        ),
    ]
    id: Annotated[str, Field(description="The ID of the issue security level member.")]
    issue_security_level_id: Annotated[
        str,
        Field(
            alias="issueSecurityLevelId",
            description="The ID of the issue security level.",
        ),
    ]
    issue_security_scheme_id: Annotated[
        str,
        Field(
            alias="issueSecuritySchemeId",
            description="The ID of the issue security scheme.",
        ),
    ]
    managed: bool | None = None


class SecuritySchemeId(BaseModel):
    model_config = ConfigDict(
        extra="allow",
    )
    id: Annotated[str, Field(description="The ID of the issue security scheme.")]


class SecuritySchemeMembersRequest(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    members: Annotated[
        list[SecuritySchemeLevelMember] | None,
        Field(
            description="The list of level members which should be added to the issue security scheme level."
        ),
    ] = None


class SecuritySchemeWithProjects(BaseModel):
    model_config = ConfigDict(
        extra="allow",
    )
    default_level: Annotated[
        int | None,
        Field(
            alias="defaultLevel",
            description="The default level ID of the issue security scheme.",
        ),
    ] = None
    description: Annotated[
        str | None, Field(description="The description of the issue security scheme.")
    ] = None
    id: Annotated[int, Field(description="The ID of the issue security scheme.")]
    name: Annotated[str, Field(description="The name of the issue security scheme.")]
    project_ids: Annotated[
        list[int] | None,
        Field(
            alias="projectIds",
            description="The list of project IDs associated with the issue security scheme.",
        ),
    ] = None
    self: Annotated[str, Field(description="The URL of the issue security scheme.")]


class SecuritySchemes(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    issue_security_schemes: Annotated[
        list[SecurityScheme] | None,
        Field(alias="issueSecuritySchemes", description="List of security schemes."),
    ] = None


class SetDefaultLevelsRequest(BaseModel):
    model_config = ConfigDict(
        extra="allow",
    )
    default_values: Annotated[
        list[DefaultLevelValue],
        Field(
            alias="defaultValues",
            description="List of objects with issue security scheme ID and new default level ID.",
            max_length=1000,
        ),
    ]


class UpdateIssueSecurityLevelDetails(BaseModel):
    model_config = ConfigDict(
        extra="allow",
    )
    description: Annotated[
        str | None,
        Field(
            description="The description of the issue security scheme level.",
            max_length=255,
        ),
    ] = None
    name: Annotated[
        str | None,
        Field(
            description="The name of the issue security scheme level. Must be unique.",
            max_length=60,
        ),
    ] = None


class AssociateSecuritySchemeWithProjectDetails(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    old_to_new_security_level_mappings: Annotated[
        list[OldToNewSecurityLevelMappings] | None,
        Field(
            alias="oldToNewSecurityLevelMappings",
            description="The list of scheme levels which should be remapped to new levels of the issue security scheme.",
        ),
    ] = None
    project_id: Annotated[str, Field(alias="projectId", description="The ID of the project.")]
    scheme_id: Annotated[
        str,
        Field(
            alias="schemeId",
            description="The ID of the issue security scheme. Providing null will clear the association with the issue security scheme.",
        ),
    ]


class IssueSecurityLevelMember(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    holder: Annotated[
        PermissionHolder,
        Field(
            description="The user or group being granted the permission. It consists of a `type` and a type-dependent `parameter`. See [Holder object](../api-group-permission-schemes/#holder-object) in *Get all permission schemes* for more information."
        ),
    ]
    id: Annotated[int, Field(description="The ID of the issue security level member.")]
    issue_security_level_id: Annotated[
        int,
        Field(
            alias="issueSecurityLevelId",
            description="The ID of the issue security level.",
        ),
    ]


class PageBeanIssueSecurityLevelMember(BaseModel):
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
        list[IssueSecurityLevelMember] | None, Field(description="The list of items.")
    ] = None


class PageBeanSecurityLevel(BaseModel):
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
    values: Annotated[list[SecurityLevel] | None, Field(description="The list of items.")] = None


class PageBeanSecurityLevelMember(BaseModel):
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
    values: Annotated[list[SecurityLevelMember] | None, Field(description="The list of items.")] = (
        None
    )


class PageBeanSecuritySchemeWithProjects(BaseModel):
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
        list[SecuritySchemeWithProjects] | None, Field(description="The list of items.")
    ] = None


class CreateIssueSecuritySchemeDetails(BaseModel):
    model_config = ConfigDict(
        extra="allow",
    )
    description: Annotated[
        str | None,
        Field(description="The description of the issue security scheme.", max_length=255),
    ] = None
    levels: Annotated[
        list[SecuritySchemeLevel] | None,
        Field(
            description="The list of scheme levels which should be added to the security scheme."
        ),
    ] = None
    name: Annotated[
        str,
        Field(
            description="The name of the issue security scheme. Must be unique (case-insensitive).",
            max_length=60,
        ),
    ]


__all__ = [
    "DefaultLevelValue",
    "IssueSecuritySchemeToProjectMapping",
    "PageBeanIssueSecuritySchemeToProjectMapping",
    "SecurityLevelMember",
    "SecuritySchemeId",
    "SecuritySchemeMembersRequest",
    "SecuritySchemeWithProjects",
    "SecuritySchemes",
    "SetDefaultLevelsRequest",
    "UpdateIssueSecurityLevelDetails",
    "AssociateSecuritySchemeWithProjectDetails",
    "IssueSecurityLevelMember",
    "PageBeanIssueSecurityLevelMember",
    "PageBeanSecurityLevel",
    "PageBeanSecurityLevelMember",
    "PageBeanSecuritySchemeWithProjects",
    "CreateIssueSecuritySchemeDetails",
]
