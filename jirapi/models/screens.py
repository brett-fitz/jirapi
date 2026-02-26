"""Pydantic models for the screens domain."""

from __future__ import annotations

from typing import Annotated

from pydantic import AnyUrl, BaseModel, ConfigDict, Field


class IssueTypeScreenScheme(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    description: Annotated[
        str | None, Field(description="The description of the issue type screen scheme.")
    ] = None
    id: Annotated[str, Field(description="The ID of the issue type screen scheme.")]
    name: Annotated[str, Field(description="The name of the issue type screen scheme.")]


class IssueTypeScreenSchemeId(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    id: Annotated[str, Field(description="The ID of the issue type screen scheme.")]


class IssueTypeScreenSchemeItem(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    issue_type_id: Annotated[
        str,
        Field(
            alias="issueTypeId",
            description="The ID of the issue type or *default*. Only issue types used in classic projects are accepted. When creating an issue screen scheme, an entry for *default* must be provided and defines the mapping for all issue types without a screen scheme. Otherwise, a *default* entry can't be provided.",
        ),
    ]
    issue_type_screen_scheme_id: Annotated[
        str,
        Field(
            alias="issueTypeScreenSchemeId",
            description="The ID of the issue type screen scheme.",
        ),
    ]
    screen_scheme_id: Annotated[
        str, Field(alias="screenSchemeId", description="The ID of the screen scheme.")
    ]


class IssueTypeScreenSchemeMapping(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    issue_type_id: Annotated[
        str,
        Field(
            alias="issueTypeId",
            description="The ID of the issue type or *default*. Only issue types used in classic projects are accepted. An entry for *default* must be provided and defines the mapping for all issue types without a screen scheme.",
        ),
    ]
    screen_scheme_id: Annotated[
        str,
        Field(
            alias="screenSchemeId",
            description="The ID of the screen scheme. Only screen schemes used in classic projects are accepted.",
        ),
    ]


class IssueTypeScreenSchemeMappingDetails(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    issue_type_mappings: Annotated[
        list[IssueTypeScreenSchemeMapping],
        Field(
            alias="issueTypeMappings",
            description="The list of issue type to screen scheme mappings. A *default* entry cannot be specified because a default entry is added when an issue type screen scheme is created.",
        ),
    ]


class IssueTypeScreenSchemeProjectAssociation(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    issue_type_screen_scheme_id: Annotated[
        str | None,
        Field(
            alias="issueTypeScreenSchemeId",
            description="The ID of the issue type screen scheme.",
        ),
    ] = None
    project_id: Annotated[
        str | None, Field(alias="projectId", description="The ID of the project.")
    ] = None


class IssueTypeScreenSchemeUpdateDetails(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    description: Annotated[
        str | None,
        Field(
            description="The description of the issue type screen scheme. The maximum length is 255 characters."
        ),
    ] = None
    name: Annotated[
        str | None,
        Field(
            description="The name of the issue type screen scheme. The name must be unique. The maximum length is 255 characters."
        ),
    ] = None


class IssueTypeScreenSchemesProjects(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    issue_type_screen_scheme: Annotated[
        IssueTypeScreenScheme,
        Field(
            alias="issueTypeScreenScheme",
            description="Details of an issue type screen scheme.",
        ),
    ]
    project_ids: Annotated[
        list[str],
        Field(
            alias="projectIds",
            description="The IDs of the projects using the issue type screen scheme.",
        ),
    ]


class PageBeanIssueTypeScreenScheme(BaseModel):
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
        list[IssueTypeScreenScheme] | None, Field(description="The list of items.")
    ] = None


class PageBeanIssueTypeScreenSchemeItem(BaseModel):
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
        list[IssueTypeScreenSchemeItem] | None, Field(description="The list of items.")
    ] = None


class PageBeanIssueTypeScreenSchemesProjects(BaseModel):
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
        list[IssueTypeScreenSchemesProjects] | None, Field(description="The list of items.")
    ] = None


class ScreenDetails(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    description: Annotated[
        str | None,
        Field(description="The description of the screen. The maximum length is 255 characters."),
    ] = None
    name: Annotated[
        str,
        Field(
            description="The name of the screen. The name must be unique. The maximum length is 255 characters."
        ),
    ]


class ScreenSchemeId(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    id: Annotated[int, Field(description="The ID of the screen scheme.")]


class ScreenTypes(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    create: Annotated[int | None, Field(description="The ID of the create screen.")] = None
    default: Annotated[
        int,
        Field(description="The ID of the default screen. Required when creating a screen scheme."),
    ]
    edit: Annotated[int | None, Field(description="The ID of the edit screen.")] = None
    view: Annotated[int | None, Field(description="The ID of the view screen.")] = None


class ScreenableField(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    id: Annotated[str | None, Field(description="The ID of the screen tab field.")] = None
    name: Annotated[
        str | None,
        Field(
            description="The name of the screen tab field. Required on create and update. The maximum length is 255 characters."
        ),
    ] = None


class ScreenableTab(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    id: Annotated[int | None, Field(description="The ID of the screen tab.")] = None
    name: Annotated[
        str, Field(description="The name of the screen tab. The maximum length is 255 characters.")
    ]


class UpdateDefaultScreenScheme(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    screen_scheme_id: Annotated[
        str, Field(alias="screenSchemeId", description="The ID of the screen scheme.")
    ]


class UpdateScreenDetails(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    description: Annotated[
        str | None,
        Field(description="The description of the screen. The maximum length is 255 characters."),
    ] = None
    name: Annotated[
        str | None,
        Field(
            description="The name of the screen. The name must be unique. The maximum length is 255 characters."
        ),
    ] = None


class UpdateScreenTypes(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    create: Annotated[
        str | None,
        Field(
            description="The ID of the create screen. To remove the screen association, pass a null."
        ),
    ] = None
    default: Annotated[
        str | None,
        Field(
            description="The ID of the default screen. When specified, must include a screen ID as a default screen is required."
        ),
    ] = None
    edit: Annotated[
        str | None,
        Field(
            description="The ID of the edit screen. To remove the screen association, pass a null."
        ),
    ] = None
    view: Annotated[
        str | None,
        Field(
            description="The ID of the view screen. To remove the screen association, pass a null."
        ),
    ] = None


class IssueTypeScreenSchemeDetails(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    description: Annotated[
        str | None,
        Field(
            description="The description of the issue type screen scheme. The maximum length is 255 characters."
        ),
    ] = None
    issue_type_mappings: Annotated[
        list[IssueTypeScreenSchemeMapping],
        Field(
            alias="issueTypeMappings",
            description="The IDs of the screen schemes for the issue type IDs and *default*. A *default* entry is required to create an issue type screen scheme, it defines the mapping for all issue types without a screen scheme.",
        ),
    ]
    name: Annotated[
        str,
        Field(
            description="The name of the issue type screen scheme. The name must be unique. The maximum length is 255 characters."
        ),
    ]


class Screen(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    description: Annotated[str | None, Field(description="The description of the screen.")] = None
    id: Annotated[int | None, Field(description="The ID of the screen.")] = None
    name: Annotated[str | None, Field(description="The name of the screen.")] = None
    scope: Annotated[Scope | None, Field(description="The scope of the screen.")] = None


class ScreenScheme(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    description: Annotated[
        str | None, Field(description="The description of the screen scheme.")
    ] = None
    id: Annotated[int | None, Field(description="The ID of the screen scheme.")] = None
    issue_type_screen_schemes: Annotated[
        PageBeanIssueTypeScreenScheme | None,
        Field(
            alias="issueTypeScreenSchemes",
            description="Details of the issue type screen schemes associated with the screen scheme.",
        ),
    ] = None
    name: Annotated[str | None, Field(description="The name of the screen scheme.")] = None
    screens: Annotated[
        ScreenTypes | None,
        Field(description="The IDs of the screens for the screen types of the screen scheme."),
    ] = None


class ScreenSchemeDetails(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    description: Annotated[
        str | None,
        Field(
            description="The description of the screen scheme. The maximum length is 255 characters."
        ),
    ] = None
    name: Annotated[
        str,
        Field(
            description="The name of the screen scheme. The name must be unique. The maximum length is 255 characters."
        ),
    ]
    screens: Annotated[
        ScreenTypes,
        Field(
            description="The IDs of the screens for the screen types of the screen scheme. Only screens used in classic projects are accepted."
        ),
    ]


class ScreenWithTab(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    description: Annotated[str | None, Field(description="The description of the screen.")] = None
    id: Annotated[int | None, Field(description="The ID of the screen.")] = None
    name: Annotated[str | None, Field(description="The name of the screen.")] = None
    scope: Annotated[Scope | None, Field(description="The scope of the screen.")] = None
    tab: Annotated[ScreenableTab | None, Field(description="The tab for the screen.")] = None


class UpdateScreenSchemeDetails(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    description: Annotated[
        str | None,
        Field(
            description="The description of the screen scheme. The maximum length is 255 characters."
        ),
    ] = None
    name: Annotated[
        str | None,
        Field(
            description="The name of the screen scheme. The name must be unique. The maximum length is 255 characters."
        ),
    ] = None
    screens: Annotated[
        UpdateScreenTypes | None,
        Field(
            description="The IDs of the screens for the screen types of the screen scheme. Only screens used in classic projects are accepted."
        ),
    ] = None


class PageBeanScreen(BaseModel):
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
    values: Annotated[list[Screen] | None, Field(description="The list of items.")] = None


class PageBeanScreenScheme(BaseModel):
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
    values: Annotated[list[ScreenScheme] | None, Field(description="The list of items.")] = None


class PageBeanScreenWithTab(BaseModel):
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
    values: Annotated[list[ScreenWithTab] | None, Field(description="The list of items.")] = None


__all__ = [
    "IssueTypeScreenScheme",
    "IssueTypeScreenSchemeId",
    "IssueTypeScreenSchemeItem",
    "IssueTypeScreenSchemeMapping",
    "IssueTypeScreenSchemeMappingDetails",
    "IssueTypeScreenSchemeProjectAssociation",
    "IssueTypeScreenSchemeUpdateDetails",
    "IssueTypeScreenSchemesProjects",
    "PageBeanIssueTypeScreenScheme",
    "PageBeanIssueTypeScreenSchemeItem",
    "PageBeanIssueTypeScreenSchemesProjects",
    "ScreenDetails",
    "ScreenSchemeId",
    "ScreenTypes",
    "ScreenableField",
    "ScreenableTab",
    "UpdateDefaultScreenScheme",
    "UpdateScreenDetails",
    "UpdateScreenTypes",
    "IssueTypeScreenSchemeDetails",
    "Screen",
    "ScreenScheme",
    "ScreenSchemeDetails",
    "ScreenWithTab",
    "UpdateScreenSchemeDetails",
    "PageBeanScreen",
    "PageBeanScreenScheme",
    "PageBeanScreenWithTab",
]
