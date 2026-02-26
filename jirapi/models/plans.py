"""Pydantic models for the plans domain."""

from __future__ import annotations

from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field


class AddAtlassianTeamRequest(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    capacity: Annotated[float | None, Field(description="The capacity for the Atlassian team.")] = (
        None
    )
    id: Annotated[str, Field(description="The Atlassian team ID.")]
    issue_source_id: Annotated[
        int | None,
        Field(
            alias="issueSourceId",
            description="The ID of the issue source for the Atlassian team.",
        ),
    ] = None
    planning_style: Annotated[
        PlanningStyle,
        Field(
            alias="planningStyle",
            description='The planning style for the Atlassian team. This must be "Scrum" or "Kanban".',
        ),
    ]
    sprint_length: Annotated[
        int | None,
        Field(
            alias="sprintLength",
            description="The sprint length for the Atlassian team.",
        ),
    ] = None


class CreateCrossProjectReleaseRequest(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    name: Annotated[str, Field(description="The cross-project release name.")]
    release_ids: Annotated[
        list[int] | None,
        Field(
            alias="releaseIds",
            description="The IDs of the releases to include in the cross-project release.",
        ),
    ] = None


class CreateCustomFieldRequest(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    custom_field_id: Annotated[
        int, Field(alias="customFieldId", description="The custom field ID.")
    ]
    filter: Annotated[
        bool | None,
        Field(description="Allows filtering issues based on their values for the custom field."),
    ] = None


class CreateDateFieldRequest(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    date_custom_field_id: Annotated[
        int | None,
        Field(
            alias="dateCustomFieldId",
            description='A date custom field ID. This is required if the type is "DateCustomField".',
        ),
    ] = None
    type: Annotated[
        Type,
        Field(
            description='The date field type. This must be "DueDate", "TargetStartDate", "TargetEndDate" or "DateCustomField".'
        ),
    ]


class CreateExclusionRulesRequest(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    issue_ids: Annotated[
        list[int] | None,
        Field(
            alias="issueIds",
            description="The IDs of the issues to exclude from the plan.",
        ),
    ] = None
    issue_type_ids: Annotated[
        list[int] | None,
        Field(
            alias="issueTypeIds",
            description="The IDs of the issue types to exclude from the plan.",
        ),
    ] = None
    number_of_days_to_show_completed_issues: Annotated[
        int | None,
        Field(
            alias="numberOfDaysToShowCompletedIssues",
            description="Issues completed this number of days ago will be excluded from the plan.",
        ),
    ] = None
    release_ids: Annotated[
        list[int] | None,
        Field(
            alias="releaseIds",
            description="The IDs of the releases to exclude from the plan.",
        ),
    ] = None
    work_status_category_ids: Annotated[
        list[int] | None,
        Field(
            alias="workStatusCategoryIds",
            description="The IDs of the work status categories to exclude from the plan.",
        ),
    ] = None
    work_status_ids: Annotated[
        list[int] | None,
        Field(
            alias="workStatusIds",
            description="The IDs of the work statuses to exclude from the plan.",
        ),
    ] = None


class CreateIssueSourceRequest(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    type: Annotated[
        Type1,
        Field(description='The issue source type. This must be "Board", "Project" or "Filter".'),
    ]
    value: Annotated[
        int,
        Field(
            description='The issue source value. This must be a board ID if the type is "Board", a project ID if the type is "Project" or a filter ID if the type is "Filter".'
        ),
    ]


class CreatePermissionHolderRequest(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    type: Annotated[
        Type2, Field(description='The permission holder type. This must be "Group" or "AccountId".')
    ]
    value: Annotated[
        str,
        Field(
            description='The permission holder value. This must be a group name if the type is "Group" or an account ID if the type is "AccountId".'
        ),
    ]


class CreatePermissionRequest(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    holder: Annotated[CreatePermissionHolderRequest, Field(description="The permission holder.")]
    type: Annotated[Type3, Field(description='The permission type. This must be "View" or "Edit".')]


class CreatePlanOnlyTeamRequest(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    capacity: Annotated[float | None, Field(description="The capacity for the plan-only team.")] = (
        None
    )
    issue_source_id: Annotated[
        int | None,
        Field(
            alias="issueSourceId",
            description="The ID of the issue source for the plan-only team.",
        ),
    ] = None
    member_account_ids: Annotated[
        list[str] | None,
        Field(
            alias="memberAccountIds",
            description="The account IDs of the plan-only team members.",
        ),
    ] = None
    name: Annotated[
        str, Field(description="The plan-only team name.", max_length=255, min_length=1)
    ]
    planning_style: Annotated[
        PlanningStyle,
        Field(
            alias="planningStyle",
            description='The planning style for the plan-only team. This must be "Scrum" or "Kanban".',
        ),
    ]
    sprint_length: Annotated[
        int | None,
        Field(
            alias="sprintLength",
            description="The sprint length for the plan-only team.",
        ),
    ] = None


class CreateSchedulingRequest(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    dependencies: Annotated[
        Dependencies | None,
        Field(
            description='The dependencies for the plan. This must be "Sequential" or "Concurrent".'
        ),
    ] = None
    end_date: Annotated[
        CreateDateFieldRequest | None,
        Field(alias="endDate", description="The end date field for the plan."),
    ] = None
    estimation: Annotated[
        Estimation,
        Field(
            description='The estimation unit for the plan. This must be "StoryPoints", "Days" or "Hours".'
        ),
    ]
    inferred_dates: Annotated[
        InferredDates | None,
        Field(
            alias="inferredDates",
            description='The inferred dates for the plan. This must be "None", "SprintDates" or "ReleaseDates".',
        ),
    ] = None
    start_date: Annotated[
        CreateDateFieldRequest | None,
        Field(alias="startDate", description="The start date field for the plan."),
    ] = None


class DuplicatePlanRequest(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    name: Annotated[str, Field(description="The plan name.")]


class GetAtlassianTeamResponse(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    capacity: Annotated[float | None, Field(description="The capacity for the Atlassian team.")] = (
        None
    )
    id: Annotated[str, Field(description="The Atlassian team ID.")]
    issue_source_id: Annotated[
        int | None,
        Field(
            alias="issueSourceId",
            description="The ID of the issue source for the Atlassian team.",
        ),
    ] = None
    planning_style: Annotated[
        PlanningStyle,
        Field(
            alias="planningStyle",
            description='The planning style for the Atlassian team. This is "Scrum" or "Kanban".',
        ),
    ]
    sprint_length: Annotated[
        int | None,
        Field(
            alias="sprintLength",
            description="The sprint length for the Atlassian team.",
        ),
    ] = None


class GetCrossProjectReleaseResponse(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    name: Annotated[str | None, Field(description="The cross-project release name.")] = None
    release_ids: Annotated[
        list[int] | None,
        Field(
            alias="releaseIds",
            description="The IDs of the releases included in the cross-project release.",
        ),
    ] = None


class GetCustomFieldResponse(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    custom_field_id: Annotated[
        int, Field(alias="customFieldId", description="The custom field ID.")
    ]
    filter: Annotated[
        bool | None,
        Field(description="Allows filtering issues based on their values for the custom field."),
    ] = None


class GetDateFieldResponse(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    date_custom_field_id: Annotated[
        int | None,
        Field(
            alias="dateCustomFieldId",
            description='A date custom field ID. This is returned if the type is "DateCustomField".',
        ),
    ] = None
    type: Annotated[
        Type6,
        Field(
            description='The date field type. This is "DueDate", "TargetStartDate", "TargetEndDate" or "DateCustomField".'
        ),
    ]


class GetExclusionRulesResponse(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    issue_ids: Annotated[
        list[int] | None,
        Field(
            alias="issueIds",
            description="The IDs of the issues excluded from the plan.",
        ),
    ] = None
    issue_type_ids: Annotated[
        list[int] | None,
        Field(
            alias="issueTypeIds",
            description="The IDs of the issue types excluded from the plan.",
        ),
    ] = None
    number_of_days_to_show_completed_issues: Annotated[
        int,
        Field(
            alias="numberOfDaysToShowCompletedIssues",
            description="Issues completed this number of days ago are excluded from the plan.",
        ),
    ]
    release_ids: Annotated[
        list[int] | None,
        Field(
            alias="releaseIds",
            description="The IDs of the releases excluded from the plan.",
        ),
    ] = None
    work_status_category_ids: Annotated[
        list[int] | None,
        Field(
            alias="workStatusCategoryIds",
            description="The IDs of the work status categories excluded from the plan.",
        ),
    ] = None
    work_status_ids: Annotated[
        list[int] | None,
        Field(
            alias="workStatusIds",
            description="The IDs of the work statuses excluded from the plan.",
        ),
    ] = None


class GetIssueSourceResponse(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    type: Annotated[
        Type7, Field(description='The issue source type. This is "Board", "Project" or "Filter".')
    ]
    value: Annotated[
        int,
        Field(
            description='The issue source value. This is a board ID if the type is "Board", a project ID if the type is "Project" or a filter ID if the type is "Filter".'
        ),
    ]


class GetPermissionHolderResponse(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    type: Annotated[
        Type8, Field(description='The permission holder type. This is "Group" or "AccountId".')
    ]
    value: Annotated[
        str,
        Field(
            description='The permission holder value. This is a group name if the type is "Group" or an account ID if the type is "AccountId".'
        ),
    ]


class GetPermissionResponse(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    holder: Annotated[GetPermissionHolderResponse, Field(description="The permission holder.")]
    type: Annotated[Type9, Field(description='The permission type. This is "View" or "Edit".')]


class GetPlanOnlyTeamResponse(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    capacity: Annotated[float | None, Field(description="The capacity for the plan-only team.")] = (
        None
    )
    id: Annotated[int, Field(description="The plan-only team ID.")]
    issue_source_id: Annotated[
        int | None,
        Field(
            alias="issueSourceId",
            description="The ID of the issue source for the plan-only team.",
        ),
    ] = None
    member_account_ids: Annotated[
        list[str] | None,
        Field(
            alias="memberAccountIds",
            description="The account IDs of the plan-only team members.",
        ),
    ] = None
    name: Annotated[str, Field(description="The plan-only team name.")]
    planning_style: Annotated[
        PlanningStyle,
        Field(
            alias="planningStyle",
            description='The planning style for the plan-only team. This is "Scrum" or "Kanban".',
        ),
    ]
    sprint_length: Annotated[
        int | None,
        Field(
            alias="sprintLength",
            description="The sprint length for the plan-only team.",
        ),
    ] = None


class GetPlanResponseForPage(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    id: Annotated[str, Field(description="The plan ID.")]
    issue_sources: Annotated[
        list[GetIssueSourceResponse] | None,
        Field(alias="issueSources", description="The issue sources included in the plan."),
    ] = None
    name: Annotated[str, Field(description="The plan name.")]
    scenario_id: Annotated[str, Field(alias="scenarioId", description="Default scenario ID.")]
    status: Annotated[
        Status1, Field(description='The plan status. This is "Active", "Trashed" or "Archived".')
    ]


class GetSchedulingResponse(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    dependencies: Annotated[
        Dependencies,
        Field(description='The dependencies for the plan. This is "Sequential" or "Concurrent".'),
    ]
    end_date: Annotated[
        GetDateFieldResponse, Field(alias="endDate", description="The end date field for the plan.")
    ]
    estimation: Annotated[
        Estimation,
        Field(
            description='The estimation unit for the plan. This is "StoryPoints", "Days" or "Hours".'
        ),
    ]
    inferred_dates: Annotated[
        InferredDates,
        Field(
            alias="inferredDates",
            description='The inferred dates for the plan. This is "None", "SprintDates" or "ReleaseDates".',
        ),
    ]
    start_date: Annotated[
        GetDateFieldResponse,
        Field(alias="startDate", description="The start date field for the plan."),
    ]


class GetTeamResponseForPage(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    id: Annotated[str, Field(description="The team ID.")]
    name: Annotated[
        str | None, Field(description='The team name. This is returned if the type is "PlanOnly".')
    ] = None
    type: Annotated[Type10, Field(description='The team type. This is "PlanOnly" or "Atlassian".')]


class PageWithCursorGetPlanResponseForPage(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    cursor: str | None = None
    last: bool | None = None
    next_page_cursor: Annotated[str | None, Field(alias="nextPageCursor")] = None
    size: int | None = None
    total: int | None = None
    values: list[GetPlanResponseForPage] | None = None


class PageWithCursorGetTeamResponseForPage(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    cursor: str | None = None
    last: bool | None = None
    next_page_cursor: Annotated[str | None, Field(alias="nextPageCursor")] = None
    size: int | None = None
    total: int | None = None
    values: list[GetTeamResponseForPage] | None = None


class CreatePlanRequest(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    cross_project_releases: Annotated[
        list[CreateCrossProjectReleaseRequest] | None,
        Field(
            alias="crossProjectReleases",
            description="The cross-project releases to include in the plan.",
        ),
    ] = None
    custom_fields: Annotated[
        list[CreateCustomFieldRequest] | None,
        Field(alias="customFields", description="The custom fields for the plan."),
    ] = None
    exclusion_rules: Annotated[
        CreateExclusionRulesRequest | None,
        Field(alias="exclusionRules", description="The exclusion rules for the plan."),
    ] = None
    issue_sources: Annotated[
        list[CreateIssueSourceRequest],
        Field(
            alias="issueSources",
            description="The issue sources to include in the plan.",
        ),
    ]
    lead_account_id: Annotated[
        str | None, Field(alias="leadAccountId", description="The account ID of the plan lead.")
    ] = None
    name: Annotated[str, Field(description="The plan name.", max_length=255, min_length=1)]
    permissions: Annotated[
        list[CreatePermissionRequest] | None, Field(description="The permissions for the plan.")
    ] = None
    scheduling: Annotated[
        CreateSchedulingRequest, Field(description="The scheduling settings for the plan.")
    ]


class GetPlanResponse(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    cross_project_releases: Annotated[
        list[GetCrossProjectReleaseResponse] | None,
        Field(
            alias="crossProjectReleases",
            description="The cross-project releases included in the plan.",
        ),
    ] = None
    custom_fields: Annotated[
        list[GetCustomFieldResponse] | None,
        Field(alias="customFields", description="The custom fields for the plan."),
    ] = None
    exclusion_rules: Annotated[
        GetExclusionRulesResponse | None,
        Field(alias="exclusionRules", description="The exclusion rules for the plan."),
    ] = None
    id: Annotated[int, Field(description="The plan ID.")]
    issue_sources: Annotated[
        list[GetIssueSourceResponse] | None,
        Field(alias="issueSources", description="The issue sources included in the plan."),
    ] = None
    last_saved: Annotated[
        str | None,
        Field(
            alias="lastSaved",
            description="The date when the plan was last saved in UTC.",
        ),
    ] = None
    lead_account_id: Annotated[
        str | None, Field(alias="leadAccountId", description="The account ID of the plan lead.")
    ] = None
    name: Annotated[str | None, Field(description="The plan name.")] = None
    permissions: Annotated[
        list[GetPermissionResponse] | None, Field(description="The permissions for the plan.")
    ] = None
    scheduling: Annotated[
        GetSchedulingResponse, Field(description="The scheduling settings for the plan.")
    ]
    status: Annotated[
        Status1, Field(description='The plan status. This is "Active", "Trashed" or "Archived".')
    ]


__all__ = [
    "AddAtlassianTeamRequest",
    "CreateCrossProjectReleaseRequest",
    "CreateCustomFieldRequest",
    "CreateDateFieldRequest",
    "CreateExclusionRulesRequest",
    "CreateIssueSourceRequest",
    "CreatePermissionHolderRequest",
    "CreatePermissionRequest",
    "CreatePlanOnlyTeamRequest",
    "CreateSchedulingRequest",
    "DuplicatePlanRequest",
    "GetAtlassianTeamResponse",
    "GetCrossProjectReleaseResponse",
    "GetCustomFieldResponse",
    "GetDateFieldResponse",
    "GetExclusionRulesResponse",
    "GetIssueSourceResponse",
    "GetPermissionHolderResponse",
    "GetPermissionResponse",
    "GetPlanOnlyTeamResponse",
    "GetPlanResponseForPage",
    "GetSchedulingResponse",
    "GetTeamResponseForPage",
    "PageWithCursorGetPlanResponseForPage",
    "PageWithCursorGetTeamResponseForPage",
    "CreatePlanRequest",
    "GetPlanResponse",
]
