"""Pydantic models for the priorities domain."""

from __future__ import annotations

from typing import Annotated

from pydantic import AnyUrl, BaseModel, ConfigDict, Field


class CreatePriorityDetails(BaseModel):
    model_config = ConfigDict(
        extra="allow",
    )
    avatar_id: Annotated[
        int | None,
        Field(
            alias="avatarId",
            description="The ID for the avatar for the priority. Either the iconUrl or avatarId must be defined, but not both. This parameter is nullable and will become mandatory once the iconUrl parameter is deprecated.",
        ),
    ] = None
    description: Annotated[
        str | None, Field(description="The description of the priority.", max_length=255)
    ] = None
    icon_url: Annotated[
        IconUrl | None,
        Field(
            alias="iconUrl",
            description="The URL of an icon for the priority. Accepted protocols are HTTP and HTTPS. Built in icons can also be used. Either the iconUrl or avatarId must be defined, but not both.",
        ),
    ] = None
    name: Annotated[
        str, Field(description="The name of the priority. Must be unique.", max_length=60)
    ]
    status_color: Annotated[
        str,
        Field(
            alias="statusColor",
            description="The status color of the priority in 3-digit or 6-digit hexadecimal format.",
        ),
    ]


class PriorityMapping(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    in_: Annotated[
        dict[str, int] | None,
        Field(
            alias="in",
            description='The mapping of priorities for issues being migrated **into** this priority scheme. Key is the old priority ID, value is the new priority ID (must exist in this priority scheme).\n\nE.g. The current priority scheme has priority ID `10001`. Issues with priority ID `10000` are being migrated into this priority scheme will need mapping to new priorities. The `in` mapping would be `{"10000": 10001}`.',
        ),
    ] = None
    out: Annotated[
        dict[str, int] | None,
        Field(
            description='The mapping of priorities for issues being migrated **out of** this priority scheme. Key is the old priority ID (must exist in this priority scheme), value is the new priority ID (must exist in the default priority scheme). Required for updating an existing priority scheme. Not used when creating a new priority scheme.\n\nE.g. The current priority scheme has priority ID `10001`. Issues with priority ID `10001` are being migrated out of this priority scheme will need mapping to new priorities. The `out` mapping would be `{"10001": 10000}`.'
        ),
    ] = None


class PrioritySchemeChangesWithoutMappings(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    ids: Annotated[list[int], Field(description="Affected entity ids.")]


class PriorityWithSequence(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    description: Annotated[
        str | None, Field(description="The description of the issue priority.")
    ] = None
    icon_url: Annotated[
        str | None,
        Field(alias="iconUrl", description="The URL of the icon for the issue priority."),
    ] = None
    id: Annotated[str | None, Field(description="The ID of the issue priority.")] = None
    is_default: Annotated[
        bool | None, Field(alias="isDefault", description="Whether this priority is the default.")
    ] = None
    name: Annotated[str | None, Field(description="The name of the issue priority.")] = None
    self: Annotated[str | None, Field(description="The URL of the issue priority.")] = None
    sequence: Annotated[str | None, Field(description="The sequence of the issue priority.")] = None
    status_color: Annotated[
        str | None,
        Field(
            alias="statusColor",
            description="The color used to indicate the issue priority.",
        ),
    ] = None


class ReorderIssuePriorities(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    after: Annotated[
        str | None,
        Field(description="The ID of the priority. Required if `position` isn't provided."),
    ] = None
    ids: Annotated[
        list[str],
        Field(
            description="The list of issue IDs to be reordered. Cannot contain duplicates nor after ID."
        ),
    ]
    position: Annotated[
        str | None,
        Field(
            description="The position for issue priorities to be moved to. Required if `after` isn't provided."
        ),
    ] = None


class SetDefaultPriorityRequest(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    id: Annotated[
        str,
        Field(
            description="The ID of the new default issue priority. Must be an existing ID or null. Setting this to null erases the default priority setting."
        ),
    ]


class TaskProgressBeanJsonNode(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    description: Annotated[str | None, Field(description="The description of the task.")] = None
    elapsed_runtime: Annotated[
        int,
        Field(
            alias="elapsedRuntime",
            description="The execution time of the task, in milliseconds.",
        ),
    ]
    finished: Annotated[
        int | None, Field(description="A timestamp recording when the task was finished.")
    ] = None
    id: Annotated[str, Field(description="The ID of the task.")]
    last_update: Annotated[
        int,
        Field(
            alias="lastUpdate",
            description="A timestamp recording when the task progress was last updated.",
        ),
    ]
    message: Annotated[
        str | None, Field(description="Information about the progress of the task.")
    ] = None
    progress: Annotated[
        int, Field(description="The progress of the task, as a percentage complete.")
    ]
    result: Annotated[JsonNode | None, Field(description="The result of the task execution.")] = (
        None
    )
    self: Annotated[AnyUrl, Field(description="The URL of the task.")]
    started: Annotated[
        int | None, Field(description="A timestamp recording when the task was started.")
    ] = None
    status: Annotated[Status3, Field(description="The status of the task.")]
    submitted: Annotated[
        int, Field(description="A timestamp recording when the task was submitted.")
    ]
    submitted_by: Annotated[
        int,
        Field(
            alias="submittedBy",
            description="The ID of the user who submitted the task.",
        ),
    ]


class UpdatePriorityDetails(BaseModel):
    model_config = ConfigDict(
        extra="allow",
    )
    avatar_id: Annotated[
        int | None,
        Field(
            alias="avatarId",
            description="The ID for the avatar for the priority. This parameter is nullable and both iconUrl and avatarId cannot be defined.",
        ),
    ] = None
    description: Annotated[
        str | None, Field(description="The description of the priority.", max_length=255)
    ] = None
    icon_url: Annotated[
        IconUrl | None,
        Field(
            alias="iconUrl",
            description="The URL of an icon for the priority. Accepted protocols are HTTP and HTTPS. Built in icons can also be used. Both iconUrl and avatarId cannot be defined.",
        ),
    ] = None
    name: Annotated[
        str | None, Field(description="The name of the priority. Must be unique.", max_length=60)
    ] = None
    status_color: Annotated[
        str | None,
        Field(
            alias="statusColor",
            description="The status color of the priority in 3-digit or 6-digit hexadecimal format.",
        ),
    ] = None


class CreatePrioritySchemeDetails(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    default_priority_id: Annotated[
        int,
        Field(
            alias="defaultPriorityId",
            description="The ID of the default priority for the priority scheme.",
        ),
    ]
    description: Annotated[
        str | None, Field(description="The description of the priority scheme.", max_length=4000)
    ] = None
    mappings: Annotated[
        PriorityMapping | None,
        Field(
            description="Instructions to migrate the priorities of issues.\n\n`in` mappings are used to migrate the priorities of issues to priorities used within the priority scheme.\n\n`out` mappings are used to migrate the priorities of issues to priorities not used within the priority scheme.\n\n *  When **priorities** are **added** to the new priority scheme, no mapping needs to be provided as the new priorities are not used by any issues.\n *  When **priorities** are **removed** from the new priority scheme, no mapping needs to be provided as the removed priorities are not used by any issues.\n *  When **projects** are **added** to the priority scheme, the priorities of issues in those projects might need to be migrated to new priorities used by the priority scheme. This can occur when the current scheme does not use all the priorities in the project(s)' priority scheme(s).\n    \n     *  An `in` mapping must be provided for each of these priorities.\n *  When **projects** are **removed** from the priority scheme, no mapping needs to be provided as the removed projects are not using the priorities of the new priority scheme.\n\nFor more information on `in` and `out` mappings, see the child properties documentation for the `PriorityMapping` object below."
        ),
    ] = None
    name: Annotated[
        str,
        Field(
            description="The name of the priority scheme. Must be unique.",
            max_length=255,
        ),
    ]
    priority_ids: Annotated[
        list[PriorityId],
        Field(
            alias="priorityIds",
            description="The IDs of priorities in the scheme.",
            max_length=300,
            min_length=1,
        ),
    ]
    project_ids: Annotated[
        list[int] | None,
        Field(
            alias="projectIds",
            description="The IDs of projects that will use the priority scheme.",
        ),
    ] = None


class PageBeanPriority(BaseModel):
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
    values: Annotated[list[Priority] | None, Field(description="The list of items.")] = None


class PageBeanPriorityWithSequence(BaseModel):
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
        list[PriorityWithSequence] | None, Field(description="The list of items.")
    ] = None


class PrioritySchemeId(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    id: Annotated[str | None, Field(description="The ID of the priority scheme.")] = None
    task: Annotated[
        TaskProgressBeanJsonNode | None, Field(description="The in-progress issue migration task.")
    ] = None


class PrioritySchemeWithPaginatedPrioritiesAndProjects(BaseModel):
    model_config = ConfigDict(
        extra="allow",
    )
    default: bool | None = None
    default_priority_id: Annotated[
        str | None,
        Field(
            alias="defaultPriorityId",
            description="The ID of the default issue priority.",
        ),
    ] = None
    description: Annotated[
        str | None, Field(description="The description of the priority scheme")
    ] = None
    id: Annotated[str, Field(description="The ID of the priority scheme.")]
    is_default: Annotated[bool | None, Field(alias="isDefault")] = None
    name: Annotated[str, Field(description="The name of the priority scheme")]
    priorities: Annotated[
        PageBeanPriorityWithSequence | None, Field(description="The paginated list of priorities.")
    ] = None
    projects: Annotated[
        PageBeanProjectDetails | None, Field(description="The paginated list of projects.")
    ] = None
    self: Annotated[str | None, Field(description="The URL of the priority scheme.")] = None


class PageBeanPrioritySchemeWithPaginatedPrioritiesAndProjects(BaseModel):
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
        list[PrioritySchemeWithPaginatedPrioritiesAndProjects] | None,
        Field(description="The list of items."),
    ] = None


__all__ = [
    "CreatePriorityDetails",
    "PriorityMapping",
    "PrioritySchemeChangesWithoutMappings",
    "PriorityWithSequence",
    "ReorderIssuePriorities",
    "SetDefaultPriorityRequest",
    "TaskProgressBeanJsonNode",
    "UpdatePriorityDetails",
    "CreatePrioritySchemeDetails",
    "PageBeanPriority",
    "PageBeanPriorityWithSequence",
    "PrioritySchemeId",
    "PrioritySchemeWithPaginatedPrioritiesAndProjects",
    "PageBeanPrioritySchemeWithPaginatedPrioritiesAndProjects",
]
