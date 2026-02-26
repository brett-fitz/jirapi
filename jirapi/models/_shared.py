"""Shared Pydantic models, enums, and base types used across domains."""

from __future__ import annotations

from datetime import date as date_aliased
from enum import Enum, StrEnum
from typing import Annotated, Any
from uuid import UUID

from pydantic import AnyUrl, AwareDatetime, BaseModel, ConfigDict, Field, RootModel


class ActorInput(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    group: Annotated[
        list[str] | None,
        Field(
            description='The name of the group to add as a default actor. This parameter cannot be used with the `groupId` parameter. As a group\'s name can change,use of `groupId` is recommended. This parameter accepts a comma-separated list. For example, `"group":["project-admin", "jira-developers"]`.'
        ),
    ] = None
    group_id: Annotated[
        list[str] | None,
        Field(
            alias="groupId",
            description='The ID of the group to add as a default actor. This parameter cannot be used with the `group` parameter This parameter accepts a comma-separated list. For example, `"groupId":["77f6ab39-e755-4570-a6ae-2d7a8df0bcb8", "0c011f85-69ed-49c4-a801-3b18d0f771bc"]`.',
        ),
    ] = None
    user: Annotated[
        list[str] | None,
        Field(
            description='The account IDs of the users to add as default actors. This parameter accepts a comma-separated list. For example, `"user":["5b10a2844c20165700ede21g", "5b109f2e9729b51b54dc274d"]`.'
        ),
    ] = None


class PlanningStyle(StrEnum):
    scrum = "Scrum"
    kanban = "Kanban"


class AddField(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    field_id: Annotated[str, Field(alias="fieldId", description="The ID of the field to add.")]


class AddGroup(BaseModel):
    model_config = ConfigDict(
        extra="allow",
    )
    name: Annotated[str, Field(description="The name of the group.")]


class Visibility(StrEnum):
    public = "public"
    private = "private"


class Active(StrEnum):
    true = "true"
    false = "false"


class ConditionType(StrEnum):
    number = "number"
    percent = "percent"
    number_per_principal = "numberPerPrincipal"


class ExcludeEnum(StrEnum):
    assignee = "assignee"
    reporter = "reporter"


class AssociatedItem(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    id: Annotated[str | None, Field(description="The ID of the associated record.")] = None
    name: Annotated[str | None, Field(description="The name of the associated record.")] = None
    parent_id: Annotated[
        str | None, Field(alias="parentId", description="The ID of the associated parent record.")
    ] = None
    parent_name: Annotated[
        str | None,
        Field(alias="parentName", description="The name of the associated parent record."),
    ] = None
    type_name: Annotated[
        str | None, Field(alias="typeName", description="The type of the associated record.")
    ] = None


class RuleType(StrEnum):
    condition = "Condition"
    validator = "Validator"
    function = "Function"
    screen = "Screen"


class Avatar(BaseModel):
    model_config = ConfigDict(
        extra="allow",
    )
    file_name: Annotated[
        str | None,
        Field(
            alias="fileName",
            description="The file name of the avatar icon. Returned for system avatars.",
        ),
    ] = None
    id: Annotated[str, Field(description="The ID of the avatar.")]
    is_deletable: Annotated[
        bool | None, Field(alias="isDeletable", description="Whether the avatar can be deleted.")
    ] = None
    is_selected: Annotated[
        bool | None,
        Field(
            alias="isSelected",
            description="Whether the avatar is used in Jira. For example, shown as a project's avatar.",
        ),
    ] = None
    is_system_avatar: Annotated[
        bool | None,
        Field(alias="isSystemAvatar", description="Whether the avatar is a system avatar."),
    ] = None
    owner: Annotated[
        str | None,
        Field(
            description="The owner of the avatar. For a system avatar the owner is null (and nothing is returned). For non-system avatars this is the appropriate identifier, such as the ID for a project or the account ID for a user."
        ),
    ] = None
    urls: Annotated[
        dict[str, AnyUrl] | None, Field(description="The list of avatar icon URLs.")
    ] = None


class AvatarUrls(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    field_16x16: Annotated[
        AnyUrl | None, Field(alias="16x16", description="The URL of the item's 16x16 pixel avatar.")
    ] = None
    field_24x24: Annotated[
        AnyUrl | None, Field(alias="24x24", description="The URL of the item's 24x24 pixel avatar.")
    ] = None
    field_32x32: Annotated[
        AnyUrl | None, Field(alias="32x32", description="The URL of the item's 32x32 pixel avatar.")
    ] = None
    field_48x48: Annotated[
        AnyUrl | None, Field(alias="48x48", description="The URL of the item's 48x48 pixel avatar.")
    ] = None


class FeatureKey(StrEnum):
    estimation = "ESTIMATION"
    sprints = "SPRINTS"


class State(Enum):
    boolean_true = True
    boolean_false = False


class CardColorStrategy(StrEnum):
    issue_type = "ISSUE_TYPE"
    request_type = "REQUEST_TYPE"
    assignee = "ASSIGNEE"
    priority = "PRIORITY"
    none = "NONE"
    custom = "CUSTOM"


class BulkChangelogRequest(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    field_ids: Annotated[
        list[str] | None,
        Field(
            alias="fieldIds",
            description="List of field IDs to filter changelogs",
            max_length=10,
            min_length=0,
        ),
    ] = None
    issue_ids_or_keys: Annotated[
        list[str],
        Field(
            alias="issueIdsOrKeys",
            description="List of issue IDs/keys to fetch changelogs for",
            max_length=1000,
            min_length=1,
        ),
    ]
    max_results: Annotated[
        int,
        Field(
            alias="maxResults",
            description="The maximum number of items to return per page",
            ge=1,
            le=10000,
        ),
    ] = 1000
    next_page_token: Annotated[
        str | None, Field(alias="nextPageToken", description="The cursor for pagination")
    ] = None


class Action(StrEnum):
    change_owner = "changeOwner"
    change_permission = "changePermission"
    add_permission = "addPermission"
    remove_permission = "removePermission"


class BulkFetchIssueRequest(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    expand: Annotated[
        list[str] | None,
        Field(
            description="Use [expand](#expansion) to include additional information about issues in the response. Note that, unlike the majority of instances where `expand` is specified, `expand` is defined as a list of values. The expand options are:\n\n *  `renderedFields` Returns field values rendered in HTML format.\n *  `names` Returns the display name of each field.\n *  `schema` Returns the schema describing a field type.\n *  `transitions` Returns all possible transitions for the issue.\n *  `operations` Returns all possible operations for the issue.\n *  `editmeta` Returns information about how each field can be edited.\n *  `changelog` Returns a list of recent updates to an issue, sorted by date, starting from the most recent. This returns a maximum of 40 changelogs. If you require more, please refer to [Bulk fetch changelogs](#api-rest-api-3-changelog-bulkfetch-post).\n *  `versionedRepresentations` Instead of `fields`, returns `versionedRepresentations` a JSON array containing each version of a field's value, with the highest numbered item representing the most recent version."
        ),
    ] = None
    fields: Annotated[
        list[str] | None,
        Field(
            description="A list of fields to return for each issue, use it to retrieve a subset of fields. This parameter accepts a comma-separated list. Expand options include:\n\n *  `*all` Returns all fields.\n *  `*navigable` Returns navigable fields.\n *  Any issue field, prefixed with a minus to exclude.\n\nThe default is `*navigable`.\n\nExamples:\n\n *  `summary,comment` Returns the summary and comments fields only.\n *  `-description` Returns all navigable (default) fields except description.\n *  `*all,-comment` Returns all fields except comments.\n\nMultiple `fields` parameters can be included in a request.\n\nNote: All navigable fields are returned by default. This differs from [GET issue](#api-rest-api-3-issue-issueIdOrKey-get) where the default is all fields."
        ),
    ] = None
    fields_by_keys: Annotated[
        bool | None,
        Field(
            alias="fieldsByKeys",
            description="Reference fields by their key (rather than ID). The default is `false`.",
        ),
    ] = None
    issue_ids_or_keys: Annotated[
        list[str],
        Field(
            alias="issueIdsOrKeys",
            description="An array of issue IDs or issue keys to fetch. You can mix issue IDs and keys in the same query.",
        ),
    ]
    properties: Annotated[
        list[str] | None,
        Field(
            description="A list of issue property keys of issue properties to be included in the results. A maximum of 5 issue property keys can be specified."
        ),
    ] = None


class Status(StrEnum):
    enqueued = "ENQUEUED"
    running = "RUNNING"
    complete = "COMPLETE"
    failed = "FAILED"
    cancel_requested = "CANCEL_REQUESTED"
    cancelled = "CANCELLED"
    dead = "DEAD"


class ShowDaysInColumn(Enum):
    boolean_true = True
    boolean_false = False


class Mode(StrEnum):
    plan = "PLAN"
    work = "WORK"


class ChangedValue(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    changed_from: Annotated[
        str | None,
        Field(alias="changedFrom", description="The value of the field before the change."),
    ] = None
    changed_to: Annotated[
        str | None, Field(alias="changedTo", description="The value of the field after the change.")
    ] = None
    field_name: Annotated[
        str | None, Field(alias="fieldName", description="The name of the field changed.")
    ] = None


class ColumnItem(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    label: Annotated[str | None, Field(description="The issue navigator column label.")] = None
    value: Annotated[str | None, Field(description="The issue navigator column value.")] = None


class ColumnRequestBody(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    columns: list[str] | None = None


class ComponentJson(BaseModel):
    model_config = ConfigDict(
        extra="allow",
    )
    ari: str | None = None
    description: str | None = None
    id: str | None = None
    metadata: dict[str, str] | None = None
    name: str | None = None
    self: str | None = None


class AssigneeType(StrEnum):
    project_default = "PROJECT_DEFAULT"
    component_lead = "COMPONENT_LEAD"
    project_lead = "PROJECT_LEAD"
    unassigned = "UNASSIGNED"


class RealAssigneeType(StrEnum):
    project_default = "PROJECT_DEFAULT"
    component_lead = "COMPONENT_LEAD"
    project_lead = "PROJECT_LEAD"
    unassigned = "UNASSIGNED"


class Operator(StrEnum):
    and_ = "and"
    or_ = "or"
    not_ = "not"


class Operation(StrEnum):
    any = "ANY"
    all = "ALL"


class FieldType(StrEnum):
    string_issue_field = "StringIssueField"
    number_issue_field = "NumberIssueField"
    rich_text_issue_field = "RichTextIssueField"
    single_select_issue_field = "SingleSelectIssueField"
    multi_select_issue_field = "MultiSelectIssueField"
    text_issue_field = "TextIssueField"


class EntityType(StrEnum):
    issuefieldvalue = "issuefieldvalue"
    issue_comment = "issue-comment"
    issue_worklog = "issue-worklog"


class Type(StrEnum):
    due_date = "DueDate"
    target_start_date = "TargetStartDate"
    target_end_date = "TargetEndDate"
    date_custom_field = "DateCustomField"


class CreateFieldAssociationSchemeLinks(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    associations: str | None = None
    projects: str | None = None


class Type1(StrEnum):
    board = "Board"
    project = "Project"
    filter = "Filter"


class Type2(StrEnum):
    group = "Group"
    account_id = "AccountId"


class Type3(StrEnum):
    view = "View"
    edit = "Edit"


class IconUrl(StrEnum):
    field_images_icons_priorities_blocker_png = "/images/icons/priorities/blocker.png"
    field_images_icons_priorities_critical_png = "/images/icons/priorities/critical.png"
    field_images_icons_priorities_high_png = "/images/icons/priorities/high.png"
    field_images_icons_priorities_highest_png = "/images/icons/priorities/highest.png"
    field_images_icons_priorities_low_png = "/images/icons/priorities/low.png"
    field_images_icons_priorities_lowest_png = "/images/icons/priorities/lowest.png"
    field_images_icons_priorities_major_png = "/images/icons/priorities/major.png"
    field_images_icons_priorities_medium_png = "/images/icons/priorities/medium.png"
    field_images_icons_priorities_minor_png = "/images/icons/priorities/minor.png"
    field_images_icons_priorities_trivial_png = "/images/icons/priorities/trivial.png"
    field_images_icons_priorities_blocker_new_png = "/images/icons/priorities/blocker_new.png"
    field_images_icons_priorities_critical_new_png = "/images/icons/priorities/critical_new.png"
    field_images_icons_priorities_high_new_png = "/images/icons/priorities/high_new.png"
    field_images_icons_priorities_highest_new_png = "/images/icons/priorities/highest_new.png"
    field_images_icons_priorities_low_new_png = "/images/icons/priorities/low_new.png"
    field_images_icons_priorities_lowest_new_png = "/images/icons/priorities/lowest_new.png"
    field_images_icons_priorities_major_new_png = "/images/icons/priorities/major_new.png"
    field_images_icons_priorities_medium_new_png = "/images/icons/priorities/medium_new.png"
    field_images_icons_priorities_minor_new_png = "/images/icons/priorities/minor_new.png"
    field_images_icons_priorities_trivial_new_png = "/images/icons/priorities/trivial_new.png"


class PriorityId(RootModel[int]):
    root: Annotated[int, Field(max_length=300, min_length=1)]


class AssigneeType1(StrEnum):
    project_lead = "PROJECT_LEAD"
    unassigned = "UNASSIGNED"


class ProjectTemplateKey(StrEnum):
    com_pyxis_greenhopper_jira_gh_simplified_agility_kanban = (
        "com.pyxis.greenhopper.jira:gh-simplified-agility-kanban"
    )
    com_pyxis_greenhopper_jira_gh_simplified_agility_scrum = (
        "com.pyxis.greenhopper.jira:gh-simplified-agility-scrum"
    )
    com_pyxis_greenhopper_jira_gh_simplified_basic = (
        "com.pyxis.greenhopper.jira:gh-simplified-basic"
    )
    com_pyxis_greenhopper_jira_gh_simplified_kanban_classic = (
        "com.pyxis.greenhopper.jira:gh-simplified-kanban-classic"
    )
    com_pyxis_greenhopper_jira_gh_simplified_scrum_classic = (
        "com.pyxis.greenhopper.jira:gh-simplified-scrum-classic"
    )
    com_pyxis_greenhopper_jira_gh_cross_team_template = (
        "com.pyxis.greenhopper.jira:gh-cross-team-template"
    )
    com_pyxis_greenhopper_jira_gh_cross_team_planning_template = (
        "com.pyxis.greenhopper.jira:gh-cross-team-planning-template"
    )
    com_atlassian_servicedesk_simplified_it_service_management = (
        "com.atlassian.servicedesk:simplified-it-service-management"
    )
    com_atlassian_servicedesk_simplified_it_service_management_basic = (
        "com.atlassian.servicedesk:simplified-it-service-management-basic"
    )
    com_atlassian_servicedesk_simplified_it_service_management_operations = (
        "com.atlassian.servicedesk:simplified-it-service-management-operations"
    )
    com_atlassian_servicedesk_simplified_general_service_desk = (
        "com.atlassian.servicedesk:simplified-general-service-desk"
    )
    com_atlassian_servicedesk_simplified_internal_service_desk = (
        "com.atlassian.servicedesk:simplified-internal-service-desk"
    )
    com_atlassian_servicedesk_simplified_external_service_desk = (
        "com.atlassian.servicedesk:simplified-external-service-desk"
    )
    com_atlassian_servicedesk_simplified_hr_service_desk = (
        "com.atlassian.servicedesk:simplified-hr-service-desk"
    )
    com_atlassian_servicedesk_simplified_facilities_service_desk = (
        "com.atlassian.servicedesk:simplified-facilities-service-desk"
    )
    com_atlassian_servicedesk_simplified_legal_service_desk = (
        "com.atlassian.servicedesk:simplified-legal-service-desk"
    )
    com_atlassian_servicedesk_simplified_marketing_service_desk = (
        "com.atlassian.servicedesk:simplified-marketing-service-desk"
    )
    com_atlassian_servicedesk_simplified_finance_service_desk = (
        "com.atlassian.servicedesk:simplified-finance-service-desk"
    )
    com_atlassian_servicedesk_simplified_analytics_service_desk = (
        "com.atlassian.servicedesk:simplified-analytics-service-desk"
    )
    com_atlassian_servicedesk_simplified_design_service_desk = (
        "com.atlassian.servicedesk:simplified-design-service-desk"
    )
    com_atlassian_servicedesk_simplified_sales_service_desk = (
        "com.atlassian.servicedesk:simplified-sales-service-desk"
    )
    com_atlassian_servicedesk_simplified_halp_service_desk = (
        "com.atlassian.servicedesk:simplified-halp-service-desk"
    )
    com_atlassian_servicedesk_next_gen_it_service_desk = (
        "com.atlassian.servicedesk:next-gen-it-service-desk"
    )
    com_atlassian_servicedesk_next_gen_hr_service_desk = (
        "com.atlassian.servicedesk:next-gen-hr-service-desk"
    )
    com_atlassian_servicedesk_next_gen_legal_service_desk = (
        "com.atlassian.servicedesk:next-gen-legal-service-desk"
    )
    com_atlassian_servicedesk_next_gen_marketing_service_desk = (
        "com.atlassian.servicedesk:next-gen-marketing-service-desk"
    )
    com_atlassian_servicedesk_next_gen_facilities_service_desk = (
        "com.atlassian.servicedesk:next-gen-facilities-service-desk"
    )
    com_atlassian_servicedesk_next_gen_general_service_desk = (
        "com.atlassian.servicedesk:next-gen-general-service-desk"
    )
    com_atlassian_servicedesk_next_gen_analytics_service_desk = (
        "com.atlassian.servicedesk:next-gen-analytics-service-desk"
    )
    com_atlassian_servicedesk_next_gen_finance_service_desk = (
        "com.atlassian.servicedesk:next-gen-finance-service-desk"
    )
    com_atlassian_servicedesk_next_gen_design_service_desk = (
        "com.atlassian.servicedesk:next-gen-design-service-desk"
    )
    com_atlassian_servicedesk_next_gen_sales_service_desk = (
        "com.atlassian.servicedesk:next-gen-sales-service-desk"
    )
    com_atlassian_jira_core_project_templates_jira_core_simplified_content_management = (
        "com.atlassian.jira-core-project-templates:jira-core-simplified-content-management"
    )
    com_atlassian_jira_core_project_templates_jira_core_simplified_document_approval = (
        "com.atlassian.jira-core-project-templates:jira-core-simplified-document-approval"
    )
    com_atlassian_jira_core_project_templates_jira_core_simplified_lead_tracking = (
        "com.atlassian.jira-core-project-templates:jira-core-simplified-lead-tracking"
    )
    com_atlassian_jira_core_project_templates_jira_core_simplified_process_control = (
        "com.atlassian.jira-core-project-templates:jira-core-simplified-process-control"
    )
    com_atlassian_jira_core_project_templates_jira_core_simplified_procurement = (
        "com.atlassian.jira-core-project-templates:jira-core-simplified-procurement"
    )
    com_atlassian_jira_core_project_templates_jira_core_simplified_project_management = (
        "com.atlassian.jira-core-project-templates:jira-core-simplified-project-management"
    )
    com_atlassian_jira_core_project_templates_jira_core_simplified_recruitment = (
        "com.atlassian.jira-core-project-templates:jira-core-simplified-recruitment"
    )
    com_atlassian_jira_core_project_templates_jira_core_simplified_task_ = (
        "com.atlassian.jira-core-project-templates:jira-core-simplified-task-"
    )


class ProjectTypeKey(StrEnum):
    software = "software"
    service_desk = "service_desk"
    business = "business"


class Dependencies(StrEnum):
    sequential = "Sequential"
    concurrent = "Concurrent"


class Estimation(StrEnum):
    story_points = "StoryPoints"
    days = "Days"
    hours = "Hours"


class InferredDates(StrEnum):
    none = "None"
    sprint_dates = "SprintDates"
    release_dates = "ReleaseDates"


class CreateUpdateRoleRequest(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    description: Annotated[
        str | None,
        Field(
            description="A description of the project role. Required when fully updating a project role. Optional when creating or partially updating a project role."
        ),
    ] = None
    name: Annotated[
        str | None,
        Field(
            description="The name of the project role. Must be unique. Cannot begin or end with whitespace. The maximum length is 255 characters. Required when creating a project role. Optional when partially updating a project role."
        ),
    ] = None


class Operator1(StrEnum):
    and_ = "AND"
    or_ = "OR"


class Type4(StrEnum):
    global_ = "global"
    initial = "initial"
    directed = "directed"


class SearcherKey(StrEnum):
    com_atlassian_jira_plugin_system_customfieldtypes_cascadingselectsearcher = (
        "com.atlassian.jira.plugin.system.customfieldtypes:cascadingselectsearcher"
    )
    com_atlassian_jira_plugin_system_customfieldtypes_daterange = (
        "com.atlassian.jira.plugin.system.customfieldtypes:daterange"
    )
    com_atlassian_jira_plugin_system_customfieldtypes_datetimerange = (
        "com.atlassian.jira.plugin.system.customfieldtypes:datetimerange"
    )
    com_atlassian_jira_plugin_system_customfieldtypes_exactnumber = (
        "com.atlassian.jira.plugin.system.customfieldtypes:exactnumber"
    )
    com_atlassian_jira_plugin_system_customfieldtypes_exacttextsearcher = (
        "com.atlassian.jira.plugin.system.customfieldtypes:exacttextsearcher"
    )
    com_atlassian_jira_plugin_system_customfieldtypes_grouppickersearcher = (
        "com.atlassian.jira.plugin.system.customfieldtypes:grouppickersearcher"
    )
    com_atlassian_jira_plugin_system_customfieldtypes_labelsearcher = (
        "com.atlassian.jira.plugin.system.customfieldtypes:labelsearcher"
    )
    com_atlassian_jira_plugin_system_customfieldtypes_multiselectsearcher = (
        "com.atlassian.jira.plugin.system.customfieldtypes:multiselectsearcher"
    )
    com_atlassian_jira_plugin_system_customfieldtypes_numberrange = (
        "com.atlassian.jira.plugin.system.customfieldtypes:numberrange"
    )
    com_atlassian_jira_plugin_system_customfieldtypes_projectsearcher = (
        "com.atlassian.jira.plugin.system.customfieldtypes:projectsearcher"
    )
    com_atlassian_jira_plugin_system_customfieldtypes_textsearcher = (
        "com.atlassian.jira.plugin.system.customfieldtypes:textsearcher"
    )
    com_atlassian_jira_plugin_system_customfieldtypes_userpickergroupsearcher = (
        "com.atlassian.jira.plugin.system.customfieldtypes:userpickergroupsearcher"
    )
    com_atlassian_jira_plugin_system_customfieldtypes_versionsearcher = (
        "com.atlassian.jira.plugin.system.customfieldtypes:versionsearcher"
    )


class CustomFieldDefinitionJson(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    description: Annotated[
        str | None,
        Field(description="The description of the custom field, which is displayed in Jira."),
    ] = None
    name: Annotated[
        str,
        Field(
            description="The name of the custom field, which is displayed in Jira. This is not the unique identifier."
        ),
    ]
    searcher_key: Annotated[
        SearcherKey | None,
        Field(
            alias="searcherKey",
            description="The searcher defines the way the field is searched in Jira. For example, *com.atlassian.jira.plugin.system.customfieldtypes:grouppickersearcher*.  \nThe search UI (basic search and JQL search) will display different operations and values for the field, based on the field searcher. You must specify a searcher that is valid for the field type, as listed below (abbreviated values shown):\n\n *  `cascadingselect`: `cascadingselectsearcher`\n *  `datepicker`: `daterange`\n *  `datetime`: `datetimerange`\n *  `float`: `exactnumber` or `numberrange`\n *  `grouppicker`: `grouppickersearcher`\n *  `importid`: `exactnumber` or `numberrange`\n *  `labels`: `labelsearcher`\n *  `multicheckboxes`: `multiselectsearcher`\n *  `multigrouppicker`: `multiselectsearcher`\n *  `multiselect`: `multiselectsearcher`\n *  `multiuserpicker`: `userpickergroupsearcher`\n *  `multiversion`: `versionsearcher`\n *  `project`: `projectsearcher`\n *  `radiobuttons`: `multiselectsearcher`\n *  `readonlyfield`: `textsearcher`\n *  `select`: `multiselectsearcher`\n *  `textarea`: `textsearcher`\n *  `textfield`: `textsearcher`\n *  `url`: `exacttextsearcher`\n *  `userpicker`: `userpickergroupsearcher`\n *  `version`: `versionsearcher`\n\nIf no searcher is provided, the field isn't searchable. However, [Forge custom fields](https://developer.atlassian.com/platform/forge/manifest-reference/modules/#jira-custom-field-type--beta-) have a searcher set automatically, so are always searchable.",
        ),
    ] = None
    type: Annotated[
        str,
        Field(
            description="The type of the custom field. These built-in custom field types are available:\n\n *  `cascadingselect`: Enables values to be selected from two levels of select lists (value: `com.atlassian.jira.plugin.system.customfieldtypes:cascadingselect`)\n *  `datepicker`: Stores a date using a picker control (value: `com.atlassian.jira.plugin.system.customfieldtypes:datepicker`)\n *  `datetime`: Stores a date with a time component (value: `com.atlassian.jira.plugin.system.customfieldtypes:datetime`)\n *  `float`: Stores and validates a numeric (floating point) input (value: `com.atlassian.jira.plugin.system.customfieldtypes:float`)\n *  `grouppicker`: Stores a user group using a picker control (value: `com.atlassian.jira.plugin.system.customfieldtypes:grouppicker`)\n *  `importid`: A read-only field that stores the ID the issue had in the system it was imported from (value: `com.atlassian.jira.plugin.system.customfieldtypes:importid`)\n *  `labels`: Stores labels (value: `com.atlassian.jira.plugin.system.customfieldtypes:labels`)\n *  `multicheckboxes`: Stores multiple values using checkboxes (value: ``)\n *  `multigrouppicker`: Stores multiple user groups using a picker control (value: ``)\n *  `multiselect`: Stores multiple values using a select list (value: `com.atlassian.jira.plugin.system.customfieldtypes:multicheckboxes`)\n *  `multiuserpicker`: Stores multiple users using a picker control (value: `com.atlassian.jira.plugin.system.customfieldtypes:multigrouppicker`)\n *  `multiversion`: Stores multiple versions from the versions available in a project using a picker control (value: `com.atlassian.jira.plugin.system.customfieldtypes:multiversion`)\n *  `project`: Stores a project from a list of projects that the user is permitted to view (value: `com.atlassian.jira.plugin.system.customfieldtypes:project`)\n *  `radiobuttons`: Stores a value using radio buttons (value: `com.atlassian.jira.plugin.system.customfieldtypes:radiobuttons`)\n *  `readonlyfield`: Stores a read-only text value, which can only be populated via the API (value: `com.atlassian.jira.plugin.system.customfieldtypes:readonlyfield`)\n *  `select`: Stores a value from a configurable list of options (value: `com.atlassian.jira.plugin.system.customfieldtypes:select`)\n *  `textarea`: Stores a long text string using a multiline text area (value: `com.atlassian.jira.plugin.system.customfieldtypes:textarea`)\n *  `textfield`: Stores a text string using a single-line text box (value: `com.atlassian.jira.plugin.system.customfieldtypes:textfield`)\n *  `url`: Stores a URL (value: `com.atlassian.jira.plugin.system.customfieldtypes:url`)\n *  `userpicker`: Stores a user using a picker control (value: `com.atlassian.jira.plugin.system.customfieldtypes:userpicker`)\n *  `version`: Stores a version using a picker control (value: `com.atlassian.jira.plugin.system.customfieldtypes:version`)\n\nTo create a field based on a [Forge custom field type](https://developer.atlassian.com/platform/forge/manifest-reference/modules/#jira-custom-field-type--beta-), use the ID of the Forge custom field type as the value. For example, `ari:cloud:ecosystem::extension/e62f20a2-4b61-4dbe-bfb9-9a88b5e3ac84/548c5df1-24aa-4f7c-bbbb-3038d947cb05/static/my-cf-type-key`."
        ),
    ]


class OnConflict(StrEnum):
    fail = "FAIL"
    use = "USE"
    new = "NEW"


class Scope1(StrEnum):
    global_ = "GLOBAL"
    template = "TEMPLATE"
    project = "PROJECT"


class AccessLevel(StrEnum):
    open = "open"
    limited = "limited"
    private = "private"
    free = "free"


class AssigneeType2(StrEnum):
    project_default = "PROJECT_DEFAULT"
    component_lead = "COMPONENT_LEAD"
    project_lead = "PROJECT_LEAD"
    unassigned = "UNASSIGNED"


class Color(StrEnum):
    blue = "blue"
    red = "red"
    yellow = "yellow"
    green = "green"
    cyan = "cyan"
    purple = "purple"
    gray = "gray"
    white = "white"


class DataClassificationTag(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    color: Annotated[
        str | None, Field(description="The color of the data classification object.")
    ] = None
    description: Annotated[
        str | None, Field(description="The description of the data classification object.")
    ] = None
    guideline: Annotated[
        str | None, Field(description="The guideline of the data classification object.")
    ] = None
    guideline_adf: Annotated[
        str | None,
        Field(
            alias="guidelineADF",
            description="The guideline in ADF (Atlassian Document Format) for rich text rendering.",
        ),
    ] = None
    id: Annotated[str, Field(description="The ID of the data classification object.")]
    name: Annotated[
        str | None, Field(description="The name of the data classification object.")
    ] = None
    rank: Annotated[
        int | None, Field(description="The rank of the data classification object.")
    ] = None
    status: Annotated[str, Field(description="The status of the data classification object.")]


class Scope2(StrEnum):
    global_ = "GLOBAL"
    authenticated = "AUTHENTICATED"
    private = "PRIVATE"


class Value(StrEnum):
    new = "NEW"
    legacy = "LEGACY"


class DeleteAndReplaceVersion(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    custom_field_replacement_list: Annotated[
        list[CustomFieldReplacement] | None,
        Field(
            alias="customFieldReplacementList",
            description="An array of custom field IDs (`customFieldId`) and version IDs (`moveTo`) to update when the fields contain the deleted version.",
        ),
    ] = None
    move_affected_issues_to: Annotated[
        int | None,
        Field(
            alias="moveAffectedIssuesTo",
            description="The ID of the version to update `affectedVersion` to when the field contains the deleted version.",
        ),
    ] = None
    move_fix_issues_to: Annotated[
        int | None,
        Field(
            alias="moveFixIssuesTo",
            description="The ID of the version to update `fixVersion` to when the field contains the deleted version.",
        ),
    ] = None


class EntityProperty(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    key: Annotated[
        str | None, Field(description="The key of the property. Required on create and update.")
    ] = None
    value: Annotated[
        Any | None, Field(description="The value of the property. Required on create and update.")
    ] = None


class ErrorCollection(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
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
    status: int | None = None


class ErrorCollections(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )


class ErrorMessage(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    message: str | None = None


class NotificationType(StrEnum):
    current_assignee = "CurrentAssignee"
    reporter = "Reporter"
    current_user = "CurrentUser"
    project_lead = "ProjectLead"
    component_lead = "ComponentLead"
    user = "User"
    group = "Group"
    project_role = "ProjectRole"
    email_address = "EmailAddress"
    all_watchers = "AllWatchers"
    user_custom_field = "UserCustomField"
    group_custom_field = "GroupCustomField"


class ExpandPriorityScheme(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    id: Annotated[str | None, Field(description="The ID of the priority scheme.")] = None
    name: Annotated[str | None, Field(description="The name of the priority scheme.")] = None
    self: Annotated[str | None, Field(description="The URL of the priority scheme.")] = None


class ExpandPrioritySchemePage(BaseModel):
    model_config = ConfigDict(
        extra="allow",
    )
    max_results: Annotated[int | None, Field(alias="maxResults")] = None
    start_at: Annotated[int | None, Field(alias="startAt")] = None
    total: int | None = None


class FieldConfiguration(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    description: Annotated[str, Field(description="The description of the field configuration.")]
    id: Annotated[int, Field(description="The ID of the field configuration.")]
    is_default: Annotated[
        bool | None,
        Field(
            alias="isDefault",
            description="Whether the field configuration is the default.",
        ),
    ] = None
    name: Annotated[str, Field(description="The name of the field configuration.")]


class FieldConfigurationDetails(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    description: Annotated[
        str | None, Field(description="The description of the field configuration.", max_length=255)
    ] = None
    name: Annotated[
        str,
        Field(
            description="The name of the field configuration. Must be unique.",
            max_length=255,
        ),
    ]


class FieldConfigurationIssueTypeItem(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    field_configuration_id: Annotated[
        str,
        Field(
            alias="fieldConfigurationId",
            description="The ID of the field configuration.",
        ),
    ]
    field_configuration_scheme_id: Annotated[
        str,
        Field(
            alias="fieldConfigurationSchemeId",
            description="The ID of the field configuration scheme.",
        ),
    ]
    issue_type_id: Annotated[
        str,
        Field(
            alias="issueTypeId",
            description="The ID of the issue type or *default*. When set to *default* this field configuration issue type item applies to all issue types without a field configuration.",
        ),
    ]


class FieldConfigurationItem(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    description: Annotated[
        str | None,
        Field(description="The description of the field within the field configuration."),
    ] = None
    id: Annotated[str, Field(description="The ID of the field within the field configuration.")]
    is_hidden: Annotated[
        bool | None,
        Field(
            alias="isHidden",
            description="Whether the field is hidden in the field configuration.",
        ),
    ] = None
    is_required: Annotated[
        bool | None,
        Field(
            alias="isRequired",
            description="Whether the field is required in the field configuration.",
        ),
    ] = None
    renderer: Annotated[
        str | None,
        Field(description="The renderer type for the field within the field configuration."),
    ] = None


class FieldConfigurationItemsDetails(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    field_configuration_items: Annotated[
        list[FieldConfigurationItem],
        Field(
            alias="fieldConfigurationItems",
            description="Details of fields in a field configuration.",
        ),
    ]


class FieldConfigurationScheme(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    description: Annotated[
        str | None, Field(description="The description of the field configuration scheme.")
    ] = None
    id: Annotated[str, Field(description="The ID of the field configuration scheme.")]
    name: Annotated[str, Field(description="The name of the field configuration scheme.")]


class FieldConfigurationSchemeProjectAssociation(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    field_configuration_scheme_id: Annotated[
        str | None,
        Field(
            alias="fieldConfigurationSchemeId",
            description="The ID of the field configuration scheme. If the field configuration scheme ID is `null`, the operation assigns the default field configuration scheme.",
        ),
    ] = None
    project_id: Annotated[str, Field(alias="projectId", description="The ID of the project.")]


class FieldConfigurationSchemeProjects(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    field_configuration_scheme: Annotated[
        FieldConfigurationScheme | None, Field(alias="fieldConfigurationScheme")
    ] = None
    project_ids: Annotated[
        list[str],
        Field(
            alias="projectIds",
            description="The IDs of projects using the field configuration scheme.",
        ),
    ]


class FieldConfigurationToIssueTypeMapping(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    field_configuration_id: Annotated[
        str,
        Field(
            alias="fieldConfigurationId",
            description="The ID of the field configuration.",
        ),
    ]
    issue_type_id: Annotated[
        str,
        Field(
            alias="issueTypeId",
            description="The ID of the issue type or *default*. When set to *default* this field configuration issue type item applies to all issue types without a field configuration. An issue type can be included only once in a request.",
        ),
    ]


class Type5(StrEnum):
    tracked = "TRACKED"
    not_tracked = "NOT_TRACKED"
    no_information = "NO_INFORMATION"


class Auto(StrEnum):
    true = "true"
    false = "false"


class Deprecated(StrEnum):
    true = "true"
    false = "false"


class Orderable(StrEnum):
    true = "true"
    false = "false"


class Searchable(StrEnum):
    true = "true"
    false = "false"


class Operator2(StrEnum):
    field_ = "="
    field__ = "!="
    field__1 = ">"
    field__2 = "<"
    field___1 = ">="
    field___2 = "<="
    in_ = "in"
    not_in = "not in"
    field__3 = "~"
    field___3 = "~="
    is_ = "is"
    is_not = "is not"


class Operator3(StrEnum):
    was = "was"
    was_in = "was in"
    was_not_in = "was not in"
    was_not = "was not"


class ManagedBy(StrEnum):
    external = "EXTERNAL"
    admins = "ADMINS"
    team_members = "TEAM_MEMBERS"
    open = "OPEN"


class UsageType(StrEnum):
    userbase_group = "USERBASE_GROUP"
    team_collaboration = "TEAM_COLLABORATION"
    admin_oversight = "ADMIN_OVERSIGHT"


class IsList(StrEnum):
    true = "true"
    false = "false"


class SupportsListAndSingleValueOperators(StrEnum):
    true = "true"
    false = "false"


class Type6(StrEnum):
    due_date = "DueDate"
    target_start_date = "TargetStartDate"
    target_end_date = "TargetEndDate"
    date_custom_field = "DateCustomField"


class Type7(StrEnum):
    board = "Board"
    project = "Project"
    filter = "Filter"
    custom = "Custom"


class Type8(StrEnum):
    group = "Group"
    account_id = "AccountId"


class Type9(StrEnum):
    view = "View"
    edit = "Edit"


class Status1(StrEnum):
    active = "Active"
    trashed = "Trashed"
    archived = "Archived"


class Type10(StrEnum):
    plan_only = "PlanOnly"
    atlassian = "Atlassian"


class Attribute(StrEnum):
    not_selectable = "notSelectable"
    default_value = "defaultValue"


class GlobalScope(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    attributes: Annotated[
        list[Attribute] | None,
        Field(
            description="Defines the behavior of the option in the global context.If notSelectable is set, the option cannot be set as the field's value. This is useful for archiving an option that has previously been selected but shouldn't be used anymore.If defaultValue is set, the option is selected by default."
        ),
    ] = None


class Type11(StrEnum):
    admin = "ADMIN"
    single = "SINGLE"
    multiple = "MULTIPLE"


class GroupLabel(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    text: Annotated[str | None, Field(description="The group label name.")] = None
    title: Annotated[str | None, Field(description="The title of the group label.")] = None
    type: Annotated[Type11 | None, Field(description="The type of the group label.")] = None


class GroupName(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    group_id: Annotated[
        str | None,
        Field(
            alias="groupId",
            description="The ID of the group, which uniquely identifies the group across all Atlassian products. For example, *952d12c3-5b5b-4d04-bb32-44d383afc4b2*.",
        ),
    ] = None
    name: Annotated[str | None, Field(description="The name of group.")] = None
    self: Annotated[AnyUrl | None, Field(description="The URL for these group details.")] = None


class Id(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    id: Annotated[
        int,
        Field(
            description="The ID of the permission scheme to associate with the project. Use the [Get all permission schemes](#api-rest-api-3-permissionscheme-get) resource to get a list of permission scheme IDs."
        ),
    ]


class IdOrKey(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    id: Annotated[int | None, Field(description="The ID of the referenced item.")] = None
    key: Annotated[str | None, Field(description="The key of the referenced item.")] = None


class InputStreamSource(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    input_stream: Annotated[dict[str, Any] | None, Field(alias="inputStream")] = None


class MultiSelectFieldOption(StrEnum):
    add = "ADD"
    remove = "REMOVE"
    replace = "REPLACE"
    remove_all = "REMOVE_ALL"


class IssueCommentListRequest(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    ids: Annotated[
        list[int],
        Field(description="The list of comment IDs. A maximum of 1000 IDs can be specified."),
    ]


class SectionType(StrEnum):
    content = "content"
    primary_context = "primaryContext"
    secondary_context = "secondaryContext"


class IssueLayoutType(StrEnum):
    issue_view = "ISSUE_VIEW"
    issue_create = "ISSUE_CREATE"
    request_form = "REQUEST_FORM"


class IssueLimitReportResponse(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    issues_approaching_limit: Annotated[
        dict[str, dict[str, int]] | None,
        Field(
            alias="issuesApproachingLimit",
            description="A list of ids of issues approaching the limit and their field count",
        ),
    ] = None
    issues_breaching_limit: Annotated[
        dict[str, dict[str, int]] | None,
        Field(
            alias="issuesBreachingLimit",
            description="A list of ids of issues breaching the limit and their field count",
        ),
    ] = None
    limits: Annotated[
        dict[str, int] | None, Field(description="The fields and their defined limits")
    ] = None


class IssueLinkType(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    id: Annotated[
        str | None,
        Field(
            description="The ID of the issue link type and is used as follows:\n\n *  In the [ issueLink](#api-rest-api-3-issueLink-post) resource it is the type of issue link. Required on create when `name` isn't provided. Otherwise, read only.\n *  In the [ issueLinkType](#api-rest-api-3-issueLinkType-post) resource it is read only."
        ),
    ] = None
    inward: Annotated[
        str | None,
        Field(
            description="The description of the issue link type inward link and is used as follows:\n\n *  In the [ issueLink](#api-rest-api-3-issueLink-post) resource it is read only.\n *  In the [ issueLinkType](#api-rest-api-3-issueLinkType-post) resource it is required on create and optional on update. Otherwise, read only."
        ),
    ] = None
    name: Annotated[
        str | None,
        Field(
            description="The name of the issue link type and is used as follows:\n\n *  In the [ issueLink](#api-rest-api-3-issueLink-post) resource it is the type of issue link. Required on create when `id` isn't provided. Otherwise, read only.\n *  In the [ issueLinkType](#api-rest-api-3-issueLinkType-post) resource it is required on create and optional on update. Otherwise, read only."
        ),
    ] = None
    outward: Annotated[
        str | None,
        Field(
            description="The description of the issue link type outward link and is used as follows:\n\n *  In the [ issueLink](#api-rest-api-3-issueLink-post) resource it is read only.\n *  In the [ issueLinkType](#api-rest-api-3-issueLinkType-post) resource it is required on create and optional on update. Otherwise, read only."
        ),
    ] = None
    self: Annotated[
        AnyUrl | None, Field(description="The URL of the issue link type. Read only.")
    ] = None


class Type12(StrEnum):
    subtask = "subtask"
    standard = "standard"


class IssueTypeCreate(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    description: Annotated[str | None, Field(description="The description of the issue type.")] = (
        None
    )
    hierarchy_level: Annotated[
        int | None,
        Field(
            alias="hierarchyLevel",
            description="The hierarchy level of the issue type. Use:\n\n *  `-1` for Subtask.\n *  `0` for Base.\n\nDefaults to `0`.",
        ),
    ] = None
    name: Annotated[
        str,
        Field(
            description="The unique name for the issue type. The maximum length is 60 characters."
        ),
    ]
    type: Annotated[
        Type12 | None,
        Field(
            description="Deprecated. Use `hierarchyLevel` instead. See the [deprecation notice](https://community.developer.atlassian.com/t/deprecation-of-the-epic-link-parent-link-and-other-related-fields-in-rest-apis-and-webhooks/54048) for details.\n\nWhether the issue type is `subtype` or `standard`. Defaults to `standard`."
        ),
    ] = None


class IssueTypeIds(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    issue_type_ids: Annotated[
        list[str], Field(alias="issueTypeIds", description="The list of issue type IDs.")
    ]


class IssueTypeIdsToRemove(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    issue_type_ids: Annotated[
        list[str],
        Field(
            alias="issueTypeIds",
            description="The list of issue type IDs. Must contain unique values not longer than 255 characters and not be empty. Maximum of 100 IDs.",
        ),
    ]


class IssueTypeUpdate(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    avatar_id: Annotated[
        int | None,
        Field(
            alias="avatarId",
            description="The ID of an issue type avatar. This can be obtained be obtained from the following endpoints:\n\n *  [System issue type avatar IDs only](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-avatars/#api-rest-api-3-avatar-type-system-get)\n *  [System and custom issue type avatar IDs](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-avatars/#api-rest-api-3-universal-avatar-type-type-owner-entityid-get)",
        ),
    ] = None
    description: Annotated[str | None, Field(description="The description of the issue type.")] = (
        None
    )
    name: Annotated[
        str | None,
        Field(
            description="The unique name for the issue type. The maximum length is 60 characters."
        ),
    ] = None


class IssuesJqlMetaData(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    count: Annotated[
        int, Field(description="The number of issues that were loaded in this evaluation.")
    ]
    max_results: Annotated[
        int,
        Field(
            alias="maxResults",
            description="The maximum number of issues that could be loaded in this evaluation.",
        ),
    ]
    start_at: Annotated[int, Field(alias="startAt", description="The index of the first issue.")]
    total_count: Annotated[
        int,
        Field(
            alias="totalCount",
            description="The total number of issues the JQL returned.",
        ),
    ]
    validation_warnings: Annotated[
        list[str] | None,
        Field(
            alias="validationWarnings",
            description="Any warnings related to the JQL query. Present only if the validation mode was set to `warn`.",
        ),
    ] = None


class IssuesMeta(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    jql: IssuesJqlMetaData | None = None


class JExpEvaluateIssuesJqlMetaData(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    is_last: Annotated[
        bool | None,
        Field(
            alias="isLast",
            description="Indicates whether this is the last page of the paginated response.",
        ),
    ] = None
    next_page_token: Annotated[
        str,
        Field(
            alias="nextPageToken",
            description="Next Page token for the next page of issues.",
        ),
    ]


class JExpEvaluateIssuesMeta(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    jql: JExpEvaluateIssuesJqlMetaData | None = None


class JQLCountRequest(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    jql: Annotated[
        str | None,
        Field(
            description="A [JQL](https://confluence.atlassian.com/x/egORLQ) expression. For performance reasons, this parameter requires a bounded query. A bounded query is a query with a search restriction."
        ),
    ] = None


class JQLCountResults(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    count: Annotated[int | None, Field(description="Number of issues matching JQL query.")] = None


class Validation(StrEnum):
    strict = "strict"
    warn = "warn"
    none = "none"


class Type13(StrEnum):
    syntax = "syntax"
    type = "type"
    other = "other"


class JiraExpressionsComplexityValue(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    limit: Annotated[
        int,
        Field(
            description="The maximum allowed complexity. The evaluation will fail if this value is exceeded."
        ),
    ]
    value: Annotated[int, Field(description="The complexity value of the current expression.")]


class Color1(StrEnum):
    grey_lightest = "GREY_LIGHTEST"
    grey_lighter = "GREY_LIGHTER"
    grey = "GREY"
    grey_darker = "GREY_DARKER"
    grey_darkest = "GREY_DARKEST"
    purple_lightest = "PURPLE_LIGHTEST"
    purple_lighter = "PURPLE_LIGHTER"
    purple = "PURPLE"
    purple_darker = "PURPLE_DARKER"
    purple_darkest = "PURPLE_DARKEST"
    blue_lightest = "BLUE_LIGHTEST"
    blue_lighter = "BLUE_LIGHTER"
    blue = "BLUE"
    blue_darker = "BLUE_DARKER"
    blue_darkest = "BLUE_DARKEST"
    teal_lightest = "TEAL_LIGHTEST"
    teal_lighter = "TEAL_LIGHTER"
    teal = "TEAL"
    teal_darker = "TEAL_DARKER"
    teal_darkest = "TEAL_DARKEST"
    green_lightest = "GREEN_LIGHTEST"
    green_lighter = "GREEN_LIGHTER"
    green = "GREEN"
    green_darker = "GREEN_DARKER"
    green_darkest = "GREEN_DARKEST"
    lime_lightest = "LIME_LIGHTEST"
    lime_lighter = "LIME_LIGHTER"
    lime = "LIME"
    lime_darker = "LIME_DARKER"
    lime_darkest = "LIME_DARKEST"
    yellow_lightest = "YELLOW_LIGHTEST"
    yellow_lighter = "YELLOW_LIGHTER"
    yellow = "YELLOW"
    yellow_darker = "YELLOW_DARKER"
    yellow_darkest = "YELLOW_DARKEST"
    orange_lightest = "ORANGE_LIGHTEST"
    orange_lighter = "ORANGE_LIGHTER"
    orange = "ORANGE"
    orange_darker = "ORANGE_DARKER"
    orange_darkest = "ORANGE_DARKEST"
    red_lightest = "RED_LIGHTEST"
    red_lighter = "RED_LIGHTER"
    red = "RED"
    red_darker = "RED_DARKER"
    red_darkest = "RED_DARKEST"
    magenta_lightest = "MAGENTA_LIGHTEST"
    magenta_lighter = "MAGENTA_LIGHTER"
    magenta = "MAGENTA"
    magenta_darker = "MAGENTA_DARKER"
    magenta_darkest = "MAGENTA_DARKEST"


class BulkEditMultiSelectFieldOption(StrEnum):
    add = "ADD"
    remove = "REMOVE"
    replace = "REPLACE"
    remove_all = "REMOVE_ALL"


class StatusCategory(StrEnum):
    todo = "TODO"
    in_progress = "IN_PROGRESS"
    done = "DONE"


class JqlFunctionPrecomputation(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    arguments: Annotated[
        list[str] | None, Field(description="The list of arguments function was invoked with.")
    ] = None
    created: Annotated[
        AwareDatetime | None, Field(description="The timestamp of the precomputation creation.")
    ] = None
    error: Annotated[
        str | None, Field(description="The error message to be displayed to the user.")
    ] = None
    field: Annotated[
        str | None, Field(description="The field the function was executed against.")
    ] = None
    function_key: Annotated[
        str | None, Field(alias="functionKey", description="The function key.")
    ] = None
    function_name: Annotated[
        str | None, Field(alias="functionName", description="The name of the function.")
    ] = None
    id: Annotated[str | None, Field(description="The id of the precomputation.")] = None
    operator: Annotated[
        str | None, Field(description="The operator in context of which function was executed.")
    ] = None
    updated: Annotated[
        AwareDatetime | None, Field(description="The timestamp of the precomputation last update.")
    ] = None
    used: Annotated[
        AwareDatetime | None, Field(description="The timestamp of the precomputation last usage.")
    ] = None
    value: Annotated[
        str | None, Field(description="The JQL fragment stored as the precomputation.")
    ] = None


class JqlFunctionPrecomputationUpdate(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    error: Annotated[
        str | None,
        Field(
            description="The error message to be displayed to the user if the given function clause is no longer valid during recalculation of the precomputation."
        ),
    ] = None
    id: Annotated[str, Field(description="The id of the precomputation to update.")]
    value: Annotated[str | None, Field(description="The new value of the precomputation.")] = None


class JqlFunctionPrecomputationUpdateRequest(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    values: list[JqlFunctionPrecomputationUpdate] | None = None


class Query(RootModel[str]):
    root: Annotated[str, Field(min_length=1)]


class Operator4(StrEnum):
    before = "before"
    after = "after"
    from_ = "from"
    to = "to"
    on = "on"
    during = "during"
    by = "by"


class Type14(StrEnum):
    number = "number"
    string = "string"
    text = "text"
    date = "date"
    user = "user"


class Direction(StrEnum):
    asc = "asc"
    desc = "desc"


class NumberType(StrEnum):
    int = "INT"
    long = "LONG"
    big_integer = "BIG_INTEGER"
    float = "FLOAT"
    double = "DOUBLE"
    big_decimal = "BIG_DECIMAL"


class JsonNode(BaseModel):
    """Represents an arbitrary JSON value (Jackson JsonNode).

    The upstream schema defines fields (``float``, ``int``, ``type``, …) that
    shadow Python builtins and break annotation resolution.  This replacement
    uses ``extra="allow"`` to accept any JSON structure.
    """

    model_config = ConfigDict(
        extra="allow",
    )


class JsonType(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    configuration: Annotated[
        dict[str, Any] | None,
        Field(description="If the field is a custom field, the configuration of the field."),
    ] = None
    custom: Annotated[
        str | None, Field(description="If the field is a custom field, the URI of the field.")
    ] = None
    custom_id: Annotated[
        int | None,
        Field(
            alias="customId",
            description="If the field is a custom field, the custom ID of the field.",
        ),
    ] = None
    items: Annotated[
        str | None,
        Field(
            description="When the data type is an array, the name of the field items within the array."
        ),
    ] = None
    system: Annotated[
        str | None, Field(description="If the field is a system field, the name of the field.")
    ] = None
    type: Annotated[str, Field(description="The data type of the field.")]


class LegacyJackson1ListColumnItem(RootModel[list[ColumnItem]]):
    root: list[ColumnItem]


class Plan(StrEnum):
    unlicensed = "UNLICENSED"
    free = "FREE"
    paid = "PAID"


class ListWrapperCallbackApplicationRole(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )


class ListWrapperCallbackGroupName(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )


class Type15(StrEnum):
    adf = "adf"
    raw = "raw"


class Position(StrEnum):
    earlier = "Earlier"
    later = "Later"
    first = "First"
    last = "Last"


class MoveField(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    after: Annotated[
        AnyUrl | None,
        Field(
            description="The ID of the screen tab field after which to place the moved screen tab field. Required if `position` isn't provided."
        ),
    ] = None
    position: Annotated[
        Position | None,
        Field(
            description="The named position to which the screen tab field should be moved. Required if `after` isn't provided."
        ),
    ] = None


class NotificationEvent(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    description: Annotated[str | None, Field(description="The description of the event.")] = None
    id: Annotated[
        int | None,
        Field(
            description="The ID of the event. The event can be a [Jira system event](https://confluence.atlassian.com/x/8YdKLg#Creatinganotificationscheme-eventsEvents) or a [custom event](https://confluence.atlassian.com/x/AIlKLg)."
        ),
    ] = None
    name: Annotated[str | None, Field(description="The name of the event.")] = None
    template_event: Annotated[
        NotificationEvent | None,
        Field(
            alias="templateEvent",
            description="The template of the event. Only custom events configured by Jira administrators have template.",
        ),
    ] = None


class NotificationSchemeAndProjectMappingJson(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    notification_scheme_id: Annotated[str | None, Field(alias="notificationSchemeId")] = None
    project_id: Annotated[str | None, Field(alias="projectId")] = None


class OldToNewSecurityLevelMappings(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    new_level_id: Annotated[
        str,
        Field(
            alias="newLevelId",
            description="The new issue security level ID. Providing null will clear the assigned old level from issues.",
        ),
    ]
    old_level_id: Annotated[
        str,
        Field(
            alias="oldLevelId",
            description="The old issue security level ID. Providing null will remap all issues without any assigned levels.",
        ),
    ]


class OperationMessage(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    message: Annotated[
        str, Field(description="The human-readable message that describes the result.")
    ]
    status_code: Annotated[
        int, Field(alias="statusCode", description="The status code of the response.")
    ]


class Position1(StrEnum):
    first = "First"
    last = "Last"


class PageBean2ComponentJson(BaseModel):
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
    values: Annotated[list[ComponentJson] | None, Field(description="The list of items.")] = None


class PageBean2JqlFunctionPrecomputation(BaseModel):
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
        list[JqlFunctionPrecomputation] | None, Field(description="The list of items.")
    ] = None


class PageBeanFieldConfigurationDetails(BaseModel):
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
        list[FieldConfigurationDetails] | None, Field(description="The list of items.")
    ] = None


class PageBeanFieldConfigurationIssueTypeItem(BaseModel):
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
        list[FieldConfigurationIssueTypeItem] | None, Field(description="The list of items.")
    ] = None


class PageBeanFieldConfigurationItem(BaseModel):
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
        list[FieldConfigurationItem] | None, Field(description="The list of items.")
    ] = None


class PageBeanFieldConfigurationScheme(BaseModel):
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
        list[FieldConfigurationScheme] | None, Field(description="The list of items.")
    ] = None


class PageBeanFieldConfigurationSchemeProjects(BaseModel):
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
        list[FieldConfigurationSchemeProjects] | None, Field(description="The list of items.")
    ] = None


class PageBeanNotificationSchemeAndProjectMappingJson(BaseModel):
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
        list[NotificationSchemeAndProjectMappingJson] | None,
        Field(description="The list of items."),
    ] = None


class PermissionHolder(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    expand: Annotated[
        str | None,
        Field(
            description="Expand options that include additional permission holder details in the response."
        ),
    ] = None
    parameter: Annotated[
        str | None,
        Field(
            description="As a group's name can change, use of `value` is recommended. The identifier associated withthe `type` value that defines the holder of the permission."
        ),
    ] = None
    type: Annotated[str, Field(description="The type of permission holder.")]
    value: Annotated[
        str | None,
        Field(
            description="The identifier associated with the `type` value that defines the holder of the permission."
        ),
    ] = None


class PermissionsKeys(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    permissions: Annotated[list[str], Field(description="A list of permission keys.")]


class Priority(BaseModel):
    model_config = ConfigDict(
        extra="allow",
    )
    avatar_id: Annotated[
        int | None,
        Field(
            alias="avatarId",
            description="The avatarId of the avatar for the issue priority. This parameter is nullable and when set, this avatar references the universal avatar APIs.",
        ),
    ] = None
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
    schemes: Annotated[
        ExpandPrioritySchemePage | None,
        Field(description="Priority schemes associated with the issue priority."),
    ] = None
    self: Annotated[str | None, Field(description="The URL of the issue priority.")] = None
    status_color: Annotated[
        str | None,
        Field(
            alias="statusColor",
            description="The color used to indicate the issue priority.",
        ),
    ] = None


class PriorityId1(BaseModel):
    model_config = ConfigDict(
        extra="allow",
    )
    id: Annotated[str, Field(description="The ID of the issue priority.")]


class AssigneeType3(StrEnum):
    project_lead = "PROJECT_LEAD"
    unassigned = "UNASSIGNED"


class Style(StrEnum):
    classic = "classic"
    next_gen = "next-gen"


class RealType(StrEnum):
    business = "BUSINESS"
    software = "SOFTWARE"
    product_discovery = "PRODUCT_DISCOVERY"
    service_desk = "SERVICE_DESK"
    customer_service = "CUSTOMER_SERVICE"
    ops = "OPS"


class Type17(StrEnum):
    business = "BUSINESS"
    software = "SOFTWARE"
    product_discovery = "PRODUCT_DISCOVERY"
    service_desk = "SERVICE_DESK"
    customer_service = "CUSTOMER_SERVICE"
    ops = "OPS"


class ProjectCategory(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    description: Annotated[
        str | None, Field(description="The description of the project category.")
    ] = None
    id: Annotated[str | None, Field(description="The ID of the project category.")] = None
    name: Annotated[
        str | None,
        Field(
            description="The name of the project category. Required on create, optional on update."
        ),
    ] = None
    self: Annotated[AnyUrl | None, Field(description="The URL of the project category.")] = None


class AssigneeType4(StrEnum):
    project_default = "PROJECT_DEFAULT"
    component_lead = "COMPONENT_LEAD"
    project_lead = "PROJECT_LEAD"
    unassigned = "UNASSIGNED"


class Type18(StrEnum):
    id = "id"
    ref = "ref"


class State1(StrEnum):
    enabled = "ENABLED"
    disabled = "DISABLED"
    coming_soon = "COMING_SOON"


class ProjectField(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    description: str | None = None
    field_id: Annotated[str | None, Field(alias="fieldId")] = None
    is_required: Annotated[bool | None, Field(alias="isRequired")] = None
    project_id: Annotated[int | None, Field(alias="projectId")] = None
    work_type_id: Annotated[int | None, Field(alias="workTypeId")] = None


class ProjectId(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    id: Annotated[str, Field(description="The ID of the project.")]


class ProjectIdentifier(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    id: Annotated[int | None, Field(description="The ID of the project.")] = None
    key: Annotated[str | None, Field(description="The key of the project.")] = None


class ProjectInsight(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    last_issue_update_time: Annotated[
        AwareDatetime | None,
        Field(alias="lastIssueUpdateTime", description="The last issue update time."),
    ] = None
    total_issue_count: Annotated[
        int | None, Field(alias="totalIssueCount", description="Total issue count.")
    ] = None


class ProjectLandingPageInfo(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    attributes: dict[str, str] | None = None
    board_id: Annotated[int | None, Field(alias="boardId")] = None
    board_name: Annotated[str | None, Field(alias="boardName")] = None
    project_key: Annotated[str | None, Field(alias="projectKey")] = None
    project_type: Annotated[str | None, Field(alias="projectType")] = None
    queue_category: Annotated[str | None, Field(alias="queueCategory")] = None
    queue_id: Annotated[int | None, Field(alias="queueId")] = None
    queue_name: Annotated[str | None, Field(alias="queueName")] = None
    simple_board: Annotated[bool | None, Field(alias="simpleBoard")] = None
    simplified: bool | None = None
    url: str | None = None


class ProjectTypeKey3(StrEnum):
    software = "software"
    business = "business"
    service_desk = "service_desk"
    product_discovery = "product_discovery"


class ProjectPermissions(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    can_edit: Annotated[
        bool | None,
        Field(alias="canEdit", description="Whether the logged user can edit the project."),
    ] = None


class ProjectRoleActorsUpdate(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    categorised_actors: Annotated[
        dict[str, list[str]] | None,
        Field(
            alias="categorisedActors",
            description='The actors to add to the project role.\n\nAdd groups using:\n\n *  `atlassian-group-role-actor` and a list of group names.\n *  `atlassian-group-role-actor-id` and a list of group IDs.\n\nAs a group\'s name can change, use of `atlassian-group-role-actor-id` is recommended. For example, `"atlassian-group-role-actor-id":["eef79f81-0b89-4fca-a736-4be531a10869","77f6ab39-e755-4570-a6ae-2d7a8df0bcb8"]`.\n\nAdd users using `atlassian-user-role-actor` and a list of account IDs. For example, `"atlassian-user-role-actor":["12345678-9abc-def1-2345-6789abcdef12", "abcdef12-3456-789a-bcde-f123456789ab"]`.',
        ),
    ] = None
    id: Annotated[
        int | None,
        Field(
            description="The ID of the project role. Use [Get all project roles](#api-rest-api-3-role-get) to get a list of project role IDs."
        ),
    ] = None


class Type19(StrEnum):
    default = "DEFAULT"
    guest_role = "GUEST_ROLE"


class ProjectRoleGroup(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    display_name: Annotated[
        str | None, Field(alias="displayName", description="The display name of the group.")
    ] = None
    group_id: Annotated[str | None, Field(alias="groupId", description="The ID of the group.")] = (
        None
    )
    name: Annotated[
        str | None,
        Field(
            description="The name of the group. As a group's name can change, use of `groupId` is recommended to identify the group."
        ),
    ] = None


class ProjectRoleUser(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    account_id: Annotated[
        str | None,
        Field(
            alias="accountId",
            description="The account ID of the user, which uniquely identifies the user across all Atlassian products. For example, *5b10ac8d82e05b22cc7d4ef5*. Returns *unknown* if the record is deleted and corrupted, for example, as the result of a server import.",
            max_length=128,
        ),
    ] = None


class ProjectScope(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    attributes: Annotated[
        list[Attribute] | None,
        Field(
            description="Defines the behavior of the option in the project.If notSelectable is set, the option cannot be set as the field's value. This is useful for archiving an option that has previously been selected but shouldn't be used anymore.If defaultValue is set, the option is selected by default."
        ),
    ] = None
    id: Annotated[
        int | None,
        Field(description="The ID of the project that the option's behavior applies to."),
    ] = None


class ProjectTemplateKey1(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    key: str | None = None
    uuid: UUID | None = None


class Type20(StrEnum):
    live = "LIVE"
    snapshot = "SNAPSHOT"


class PropertyKey(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    key: Annotated[str | None, Field(description="The key of the property.")] = None
    self: Annotated[str | None, Field(description="The URL of the property.")] = None


class PropertyKeys(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    keys: Annotated[list[PropertyKey] | None, Field(description="Property key details.")] = None


class JobStatus(StrEnum):
    pending = "PENDING"
    in_progress = "IN_PROGRESS"
    completed = "COMPLETED"


class ResolutionJson(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    default: bool | None = None
    description: str | None = None
    icon_url: Annotated[str | None, Field(alias="iconUrl")] = None
    id: str | None = None
    name: str | None = None
    self: str | None = None


class RichText(BaseModel):
    empty: bool | None = None
    empty_adf: Annotated[bool | None, Field(alias="emptyAdf")] = None
    finalised: bool | None = None
    value_set: Annotated[bool | None, Field(alias="valueSet")] = None


class Type21(StrEnum):
    atlassian_group_role_actor = "atlassian-group-role-actor"
    atlassian_user_role_actor = "atlassian-user-role-actor"


class RoleActor(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    actor_group: Annotated[ProjectRoleGroup | None, Field(alias="actorGroup")] = None
    actor_user: Annotated[ProjectRoleUser | None, Field(alias="actorUser")] = None
    avatar_url: Annotated[
        AnyUrl | None, Field(alias="avatarUrl", description="The avatar of the role actor.")
    ] = None
    display_name: Annotated[
        str | None,
        Field(
            alias="displayName",
            description="The display name of the role actor. For users, depending on the user’s privacy setting, this may return an alternative value for the user's name.",
        ),
    ] = None
    id: Annotated[int | None, Field(description="The ID of the role actor.")] = None
    name: Annotated[
        str | None,
        Field(
            description="This property is no longer available and will be removed from the documentation soon. See the [deprecation notice](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-user-privacy-api-migration-guide/) for details."
        ),
    ] = None
    type: Annotated[Type21 | None, Field(description="The type of role actor.")] = None


class Type22(StrEnum):
    hidden = "HIDDEN"
    viewable = "VIEWABLE"
    editable = "EDITABLE"


class RuleConfiguration(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    disabled: Annotated[bool, Field(description="Whether the rule is disabled.")] = False
    tag: Annotated[
        str | None,
        Field(
            description="A tag used to filter rules in [Get workflow transition rule configurations](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-workflow-transition-rules/#api-rest-api-3-workflow-rule-config-get).",
            max_length=255,
        ),
    ] = None
    value: Annotated[
        str,
        Field(
            description="Configuration of the rule, as it is stored by the Connect or the Forge app on the rule configuration page."
        ),
    ]


class TemplateType(StrEnum):
    live = "LIVE"
    snapshot = "SNAPSHOT"


class Type23(StrEnum):
    project = "PROJECT"
    template = "TEMPLATE"


class Type24(StrEnum):
    global_ = "GLOBAL"
    project = "PROJECT"


class SearchAndReconcileRequest(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    expand: Annotated[
        str | None,
        Field(
            description='Use [expand](#expansion) to include additional information about issues in the response. Note that, unlike the majority of instances where `expand` is specified, `expand` is defined as a comma-delimited string of values. The expand options are:\n\n *  `renderedFields` Returns field values rendered in HTML format.\n *  `names` Returns the display name of each field.\n *  `schema` Returns the schema describing a field type.\n *  `transitions` Returns all possible transitions for the issue.\n *  `operations` Returns all possible operations for the issue.\n *  `editmeta` Returns information about how each field can be edited.\n *  `changelog` Returns a list of recent updates to an issue, sorted by date, starting from the most recent.\n *  `versionedRepresentations` Instead of `fields`, returns `versionedRepresentations` a JSON array containing each version of a field\'s value, with the highest numbered item representing the most recent version.\n\nExamples: `"names,changelog"` Returns the display name of each field as well as a list of recent updates to an issue.'
        ),
    ] = None
    fields: Annotated[
        list[str] | None,
        Field(
            description="A list of fields to return for each issue. Use it to retrieve a subset of fields. This parameter accepts a comma-separated list. Expand options include:\n\n *  `*all` Returns all fields.\n *  `*navigable` Returns navigable fields.\n *  `id` Returns only issue IDs.\n *  Any issue field, prefixed with a dash to exclude.\n\nThe default is `id`.\n\nExamples:\n\n *  `summary,comment` Returns the summary and comments fields only.\n *  `*all,-comment` Returns all fields except comments.\n\nMultiple `fields` parameters can be included in a request.\n\nNote: By default, this resource returns IDs only. This differs from [GET issue](#api-rest-api-3-issue-issueIdOrKey-get) where the default is all fields."
        ),
    ] = None
    fields_by_keys: Annotated[
        bool | None,
        Field(
            alias="fieldsByKeys",
            description="Reference fields by their key (rather than ID). The default is `false`.",
        ),
    ] = None
    jql: Annotated[
        str | None,
        Field(
            description="A [JQL](https://confluence.atlassian.com/x/egORLQ) expression. For performance reasons, this parameter requires a bounded query. A bounded query is a query with a search restriction.\n\n *  Example of an unbounded query: `order by key desc`.\n *  Example of a bounded query: `assignee = currentUser() order by key`.\n\nAdditionally, `orderBy` clause can contain a maximum of 7 fields."
        ),
    ] = None
    max_results: Annotated[
        int,
        Field(
            alias="maxResults",
            description="The maximum number of items to return per page. To manage page size, API may return fewer items per page where a large number of fields are requested. The greatest number of items returned per page is achieved when requesting `id` or `key` only. It returns max 5000 issues.",
        ),
    ] = 50
    next_page_token: Annotated[
        str | None,
        Field(
            alias="nextPageToken",
            description="The token for a page to fetch that is not the first page. The first page has a `nextPageToken` of `null`. Use the `nextPageToken` to fetch the next page of issues.",
        ),
    ] = None
    properties: Annotated[
        list[str] | None,
        Field(
            description="A list of up to 5 issue properties to include in the results. This parameter accepts a comma-separated list."
        ),
    ] = None
    reconcile_issues: Annotated[
        list[int] | None,
        Field(
            alias="reconcileIssues",
            description="Strong consistency issue ids to be reconciled with search results. Accepts max 50 ids. This list of ids should be consistent with each paginated request across different pages.",
        ),
    ] = None


class ValidateQuery(StrEnum):
    strict = "strict"
    warn = "warn"
    none = "none"
    true = "true"
    false = "false"


class SearchRequest(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    expand: Annotated[
        list[str] | None,
        Field(
            description="Use [expand](#expansion) to include additional information about issues in the response. Note that, unlike the majority of instances where `expand` is specified, `expand` is defined as a list of values. The expand options are:\n\n *  `renderedFields` Returns field values rendered in HTML format.\n *  `names` Returns the display name of each field.\n *  `schema` Returns the schema describing a field type.\n *  `transitions` Returns all possible transitions for the issue.\n *  `operations` Returns all possible operations for the issue.\n *  `editmeta` Returns information about how each field can be edited.\n *  `changelog` Returns a list of recent updates to an issue, sorted by date, starting from the most recent.\n *  `versionedRepresentations` Instead of `fields`, returns `versionedRepresentations` a JSON array containing each version of a field's value, with the highest numbered item representing the most recent version."
        ),
    ] = None
    fields: Annotated[
        list[str] | None,
        Field(
            description="A list of fields to return for each issue, use it to retrieve a subset of fields. This parameter accepts a comma-separated list. Expand options include:\n\n *  `*all` Returns all fields.\n *  `*navigable` Returns navigable fields.\n *  Any issue field, prefixed with a minus to exclude.\n\nThe default is `*navigable`.\n\nExamples:\n\n *  `summary,comment` Returns the summary and comments fields only.\n *  `-description` Returns all navigable (default) fields except description.\n *  `*all,-comment` Returns all fields except comments.\n\nMultiple `fields` parameters can be included in a request.\n\nNote: All navigable fields are returned by default. This differs from [GET issue](#api-rest-api-3-issue-issueIdOrKey-get) where the default is all fields."
        ),
    ] = None
    fields_by_keys: Annotated[
        bool | None,
        Field(
            alias="fieldsByKeys",
            description="Reference fields by their key (rather than ID). The default is `false`.",
        ),
    ] = None
    jql: Annotated[
        str | None,
        Field(description="A [JQL](https://confluence.atlassian.com/x/egORLQ) expression."),
    ] = None
    max_results: Annotated[
        int,
        Field(
            alias="maxResults",
            description="The maximum number of items to return per page.",
        ),
    ] = 50
    properties: Annotated[
        list[str] | None,
        Field(
            description="A list of up to 5 issue properties to include in the results. This parameter accepts a comma-separated list."
        ),
    ] = None
    start_at: Annotated[
        int | None,
        Field(
            alias="startAt",
            description="The index of the first item to return in the page of results (page offset). The base index is `0`.",
        ),
    ] = None
    validate_query: Annotated[
        ValidateQuery | None,
        Field(
            alias="validateQuery",
            description="Determines how to validate the JQL query and treat the validation results. Supported values:\n\n *  `strict` Returns a 400 response code if any errors are found, along with a list of all errors (and warnings).\n *  `warn` Returns all errors as warnings.\n *  `none` No validation is performed.\n *  `true` *Deprecated* A legacy synonym for `strict`.\n *  `false` *Deprecated* A legacy synonym for `warn`.\n\nThe default is `strict`.\n\nNote: If the JQL is not correctly formed a 400 response code is returned, regardless of the `validateQuery` value.",
        ),
    ] = None


class SecurityLevel(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    description: Annotated[
        str | None, Field(description="The description of the issue level security item.")
    ] = None
    id: Annotated[str | None, Field(description="The ID of the issue level security item.")] = None
    is_default: Annotated[
        bool | None,
        Field(
            alias="isDefault",
            description="Whether the issue level security item is the default.",
        ),
    ] = None
    issue_security_scheme_id: Annotated[
        str | None,
        Field(
            alias="issueSecuritySchemeId",
            description="The ID of the issue level security scheme.",
        ),
    ] = None
    name: Annotated[str | None, Field(description="The name of the issue level security item.")] = (
        None
    )
    self: Annotated[str | None, Field(description="The URL of the issue level security item.")] = (
        None
    )


class Type25(StrEnum):
    group = "group"
    reporter = "reporter"
    users = "users"


class IsDefault(Enum):
    boolean_true = True
    boolean_false = False


class SecurityScheme(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    default_security_level_id: Annotated[
        int | None,
        Field(
            alias="defaultSecurityLevelId",
            description="The ID of the default security level.",
        ),
    ] = None
    description: Annotated[
        str | None, Field(description="The description of the issue security scheme.")
    ] = None
    id: Annotated[int | None, Field(description="The ID of the issue security scheme.")] = None
    levels: list[SecurityLevel] | None = None
    name: Annotated[str | None, Field(description="The name of the issue security scheme.")] = None
    self: Annotated[str | None, Field(description="The URL of the issue security scheme.")] = None


class SecuritySchemeLevelMember(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    parameter: Annotated[
        str | None, Field(description="The value corresponding to the specified member type.")
    ] = None
    type: Annotated[
        str,
        Field(
            description="The issue security level member type, e.g `reporter`, `group`, `user`, `projectrole`, `applicationRole`."
        ),
    ]


class ServiceManagementNavigationInfo(BaseModel):
    queue_category: Annotated[str | None, Field(alias="queueCategory")] = None
    queue_id: Annotated[int | None, Field(alias="queueId")] = None
    queue_name: Annotated[str | None, Field(alias="queueName")] = None


class Type26(StrEnum):
    user = "user"
    group = "group"
    project = "project"
    project_role = "projectRole"
    global_ = "global"
    loggedin = "loggedin"
    authenticated = "authenticated"
    project_unknown = "project-unknown"


class Type27(StrEnum):
    user = "user"
    project = "project"
    group = "group"
    project_role = "projectRole"
    global_ = "global"
    authenticated = "authenticated"


class SharePermissionInput(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    account_id: Annotated[
        str | None,
        Field(
            alias="accountId",
            description="The user account ID that the filter is shared with. For a request, specify the `accountId` property for the user.",
        ),
    ] = None
    group_id: Annotated[
        str | None,
        Field(
            alias="groupId",
            description="The ID of the group, which uniquely identifies the group across all Atlassian products.For example, *952d12c3-5b5b-4d04-bb32-44d383afc4b2*. Cannot be provided with `groupname`.",
        ),
    ] = None
    groupname: Annotated[
        str | None,
        Field(
            description="The name of the group to share the filter with. Set `type` to `group`. Please note that the name of a group is mutable, to reliably identify a group use `groupId`."
        ),
    ] = None
    project_id: Annotated[
        str | None,
        Field(
            alias="projectId",
            description="The ID of the project to share the filter with. Set `type` to `project`.",
        ),
    ] = None
    project_role_id: Annotated[
        str | None,
        Field(
            alias="projectRoleId",
            description="The ID of the project role to share the filter with. Set `type` to `projectRole` and the `projectId` for the project that the role is in.",
        ),
    ] = None
    rights: Annotated[int | None, Field(description="The rights for the share permission.")] = None
    type: Annotated[
        Type27,
        Field(
            description="The type of the share permission.Specify the type as follows:\n\n *  `user` Share with a user.\n *  `group` Share with a group. Specify `groupname` as well.\n *  `project` Share with a project. Specify `projectId` as well.\n *  `projectRole` Share with a project role in a project. Specify `projectId` and `projectRoleId` as well.\n *  `global` Share globally, including anonymous users. If set, this type overrides all existing share permissions and must be deleted before any non-global share permissions is set.\n *  `authenticated` Share with all logged-in users. This shows as `loggedin` in the response. If set, this type overrides all existing share permissions and must be deleted before any non-global share permissions is set."
        ),
    ]


class SimpleApplicationProperty(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    id: Annotated[str | None, Field(description="The ID of the application property.")] = None
    value: Annotated[str | None, Field(description="The new value.")] = None


class SimpleLink(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    href: str | None = None
    icon_class: Annotated[str | None, Field(alias="iconClass")] = None
    id: str | None = None
    label: str | None = None
    style_class: Annotated[str | None, Field(alias="styleClass")] = None
    title: str | None = None
    weight: int | None = None


class SimpleListWrapperGroupName(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    callback: ListWrapperCallbackGroupName | None = None
    items: list[GroupName] | None = None
    max_results: Annotated[int | None, Field(alias="max-results")] = None
    paging_callback: Annotated[
        ListWrapperCallbackGroupName | None, Field(alias="pagingCallback")
    ] = None
    size: int | None = None


class SimplifiedHierarchyLevel(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    above_level_id: Annotated[
        int | None,
        Field(
            alias="aboveLevelId",
            description="The ID of the level above this one in the hierarchy. This property is deprecated, see [Change notice: Removing hierarchy level IDs from next-gen APIs](https://developer.atlassian.com/cloud/jira/platform/change-notice-removing-hierarchy-level-ids-from-next-gen-apis/).",
        ),
    ] = None
    below_level_id: Annotated[
        int | None,
        Field(
            alias="belowLevelId",
            description="The ID of the level below this one in the hierarchy. This property is deprecated, see [Change notice: Removing hierarchy level IDs from next-gen APIs](https://developer.atlassian.com/cloud/jira/platform/change-notice-removing-hierarchy-level-ids-from-next-gen-apis/).",
        ),
    ] = None
    external_uuid: Annotated[
        UUID | None,
        Field(
            alias="externalUuid",
            description="The external UUID of the hierarchy level. This property is deprecated, see [Change notice: Removing hierarchy level IDs from next-gen APIs](https://developer.atlassian.com/cloud/jira/platform/change-notice-removing-hierarchy-level-ids-from-next-gen-apis/).",
        ),
    ] = None
    hierarchy_level_number: Annotated[int | None, Field(alias="hierarchyLevelNumber")] = None
    id: Annotated[
        int | None,
        Field(
            description="The ID of the hierarchy level. This property is deprecated, see [Change notice: Removing hierarchy level IDs from next-gen APIs](https://developer.atlassian.com/cloud/jira/platform/change-notice-removing-hierarchy-level-ids-from-next-gen-apis/)."
        ),
    ] = None
    issue_type_ids: Annotated[
        list[int] | None,
        Field(
            alias="issueTypeIds",
            description="The issue types available in this hierarchy level.",
        ),
    ] = None
    level: Annotated[int | None, Field(description="The level of this item in the hierarchy.")] = (
        None
    )
    name: Annotated[str | None, Field(description="The name of this hierarchy level.")] = None
    project_configuration_id: Annotated[
        int | None,
        Field(
            alias="projectConfigurationId",
            description="The ID of the project configuration. This property is deprecated, see [Change oticen: Removing hierarchy level IDs from next-gen APIs](https://developer.atlassian.com/cloud/jira/platform/change-notice-removing-hierarchy-level-ids-from-next-gen-apis/).",
        ),
    ] = None


class SoftwareNavigationInfo(BaseModel):
    board_id: Annotated[int | None, Field(alias="boardId")] = None
    board_name: Annotated[str | None, Field(alias="boardName")] = None
    simple_board: Annotated[bool | None, Field(alias="simpleBoard")] = None
    total_boards_in_project: Annotated[int | None, Field(alias="totalBoardsInProject")] = None


class StatusModel(BaseModel):
    model_config = ConfigDict(
        extra="allow",
    )
    icon: Annotated[
        Icon | None,
        Field(
            description="Details of the icon representing the status. If not provided, no status icon displays in Jira."
        ),
    ] = None
    resolved: Annotated[
        bool | None,
        Field(
            description='Whether the item is resolved. If set to "true", the link to the issue is displayed in a strikethrough font, otherwise the link displays in normal font.'
        ),
    ] = None


class StatusCategory3(BaseModel):
    model_config = ConfigDict(
        extra="allow",
    )
    color_name: Annotated[
        str | None,
        Field(
            alias="colorName",
            description="The name of the color used to represent the status category.",
        ),
    ] = None
    id: Annotated[int | None, Field(description="The ID of the status category.")] = None
    key: Annotated[str | None, Field(description="The key of the status category.")] = None
    name: Annotated[str | None, Field(description="The name of the status category.")] = None
    self: Annotated[str | None, Field(description="The URL of the status category.")] = None


class StatusCategory4(StrEnum):
    todo = "TODO"
    in_progress = "IN_PROGRESS"
    done = "DONE"


class Category(StrEnum):
    todo = "TODO"
    in_progress = "IN_PROGRESS"
    done = "DONE"


class Type28(StrEnum):
    project = "PROJECT"
    global_ = "GLOBAL"


class StringList(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )


class SuggestedMappingsForPrioritiesRequest(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    add: Annotated[
        list[int] | None, Field(description="The ids of priorities being removed from the scheme.")
    ] = None
    remove: Annotated[
        list[int] | None, Field(description="The ids of priorities being removed from the scheme.")
    ] = None


class SuggestedMappingsForProjectsRequest(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    add: Annotated[
        list[int] | None, Field(description="The ids of projects being added to the scheme.")
    ] = None


class SuggestedMappingsRequest(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    max_results: Annotated[
        int | None,
        Field(
            alias="maxResults",
            description="The maximum number of results that could be on the page.",
        ),
    ] = None
    priorities: Annotated[
        SuggestedMappingsForPrioritiesRequest | None,
        Field(description="The priority changes in the scheme."),
    ] = None
    projects: Annotated[
        SuggestedMappingsForProjectsRequest | None,
        Field(description="The project changes in the scheme."),
    ] = None
    scheme_id: Annotated[
        int | None, Field(alias="schemeId", description="The id of the priority scheme.")
    ] = None
    start_at: Annotated[
        int | None,
        Field(
            alias="startAt",
            description="The index of the first item returned on the page.",
        ),
    ] = None


class SwimlaneStrategy(StrEnum):
    none = "none"
    custom = "custom"
    parent_child = "parentChild"
    assignee = "assignee"
    assignee_unassigned_first = "assigneeUnassignedFirst"
    epic = "epic"
    project = "project"
    issueparent = "issueparent"
    issuechildren = "issuechildren"
    request_type = "request_type"


class Status3(StrEnum):
    enqueued = "ENQUEUED"
    running = "RUNNING"
    complete = "COMPLETE"
    failed = "FAILED"
    cancel_requested = "CANCEL_REQUESTED"
    cancelled = "CANCELLED"
    dead = "DEAD"


class TaskProgressBeanObject(BaseModel):
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
    result: Annotated[Any | None, Field(description="The result of the task execution.")] = None
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


class DefaultUnit(StrEnum):
    minute = "minute"
    hour = "hour"
    day = "day"
    week = "week"


class TimeFormat(StrEnum):
    pretty = "pretty"
    days = "days"
    hours = "hours"


class TimeTrackingConfiguration(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    default_unit: Annotated[
        DefaultUnit,
        Field(
            alias="defaultUnit",
            description="The default unit of time applied to logged time.",
        ),
    ]
    time_format: Annotated[
        TimeFormat,
        Field(
            alias="timeFormat",
            description="The format that will appear on an issue's *Time Spent* field.",
        ),
    ]
    working_days_per_week: Annotated[
        float,
        Field(
            alias="workingDaysPerWeek",
            description="The number of days in a working week.",
        ),
    ]
    working_hours_per_day: Annotated[
        float,
        Field(
            alias="workingHoursPerDay",
            description="The number of hours in a working day.",
        ),
    ]


class Type29(StrEnum):
    global_ = "global"
    initial = "initial"
    directed = "directed"


class Type31(StrEnum):
    initial = "INITIAL"
    global_ = "GLOBAL"
    directed = "DIRECTED"


class ViewType(StrEnum):
    gic = "GIC"
    issue_view = "IssueView"
    issue_transition = "IssueTransition"
    jsm_request_create = "JSMRequestCreate"


class UpdateDefaultProjectClassification(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    id: Annotated[str, Field(description="The ID of the project classification.")]


class UpdateFieldAssociationSchemeLinks(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    associations: str | None = None
    projects: str | None = None


class UpdateFieldConfigurationSchemeDetails(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    description: Annotated[
        str | None,
        Field(
            description="The description of the field configuration scheme.",
            max_length=1024,
        ),
    ] = None
    name: Annotated[
        str,
        Field(
            description="The name of the field configuration scheme. The name must be unique.",
            max_length=255,
        ),
    ]


class UpdateIssueSecuritySchemeRequest(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    description: Annotated[
        str | None,
        Field(description="The description of the security scheme scheme.", max_length=255),
    ] = None
    name: Annotated[
        str | None,
        Field(
            description="The name of the security scheme scheme. Must be unique.",
            max_length=60,
        ),
    ] = None


class UpdatePrioritiesInSchemeRequest(BaseModel):
    model_config = ConfigDict(
        extra="allow",
    )
    add: Annotated[
        PrioritySchemeChangesWithoutMappings | None,
        Field(description="Priorities to add to a scheme"),
    ] = None
    remove: Annotated[
        PrioritySchemeChangesWithoutMappings | None,
        Field(description="Priorities to remove from a scheme"),
    ] = None


class AssigneeType5(StrEnum):
    project_lead = "PROJECT_LEAD"
    unassigned = "UNASSIGNED"


class UpdateProjectsInSchemeRequest(BaseModel):
    model_config = ConfigDict(
        extra="allow",
    )
    add: Annotated[
        PrioritySchemeChangesWithoutMappings | None,
        Field(description="Projects to add to a scheme"),
    ] = None
    remove: Annotated[
        PrioritySchemeChangesWithoutMappings | None,
        Field(description="Projects to remove from a scheme"),
    ] = None


class UpdateUserToGroup(BaseModel):
    model_config = ConfigDict(
        extra="allow",
    )
    account_id: Annotated[
        str | None,
        Field(
            alias="accountId",
            description="The account ID of the user, which uniquely identifies the user across all Atlassian products. For example, *5b10ac8d82e05b22cc7d4ef5*.",
            max_length=128,
        ),
    ] = None
    name: Annotated[
        str | None,
        Field(
            description="This property is no longer available. See the [deprecation notice](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-user-privacy-api-migration-guide/) for details."
        ),
    ] = None


class UpdatedProjectCategory(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    description: Annotated[str | None, Field(description="The name of the project category.")] = (
        None
    )
    id: Annotated[str | None, Field(description="The ID of the project category.")] = None
    name: Annotated[str | None, Field(description="The description of the project category.")] = (
        None
    )
    self: Annotated[str | None, Field(description="The URL of the project category.")] = None


class AccountType(StrEnum):
    atlassian = "atlassian"
    app = "app"
    customer = "customer"
    unknown = "unknown"


class UserAvatarUrls(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    field_16x16: Annotated[
        AnyUrl | None, Field(alias="16x16", description="The URL of the user's 16x16 pixel avatar.")
    ] = None
    field_24x24: Annotated[
        AnyUrl | None, Field(alias="24x24", description="The URL of the user's 24x24 pixel avatar.")
    ] = None
    field_32x32: Annotated[
        AnyUrl | None, Field(alias="32x32", description="The URL of the user's 32x32 pixel avatar.")
    ] = None
    field_48x48: Annotated[
        AnyUrl | None, Field(alias="48x48", description="The URL of the user's 48x48 pixel avatar.")
    ] = None


class UserDetails(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    account_id: Annotated[
        str | None,
        Field(
            alias="accountId",
            description="The account ID of the user, which uniquely identifies the user across all Atlassian products. For example, *5b10ac8d82e05b22cc7d4ef5*.",
            max_length=128,
        ),
    ] = None
    account_type: Annotated[
        str | None,
        Field(
            alias="accountType",
            description="The type of account represented by this user. This will be one of 'atlassian' (normal users), 'app' (application user) or 'customer' (Jira Service Desk customer user)",
        ),
    ] = None
    active: Annotated[bool | None, Field(description="Whether the user is active.")] = None
    avatar_urls: Annotated[
        AvatarUrls | None, Field(alias="avatarUrls", description="The avatars of the user.")
    ] = None
    display_name: Annotated[
        str | None,
        Field(
            alias="displayName",
            description="The display name of the user. Depending on the user’s privacy settings, this may return an alternative value.",
        ),
    ] = None
    email_address: Annotated[
        str | None,
        Field(
            alias="emailAddress",
            description="The email address of the user. Depending on the user’s privacy settings, this may be returned as null.",
        ),
    ] = None
    key: Annotated[
        str | None,
        Field(
            description="This property is no longer available and will be removed from the documentation soon. See the [deprecation notice](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-user-privacy-api-migration-guide/) for details."
        ),
    ] = None
    name: Annotated[
        str | None,
        Field(
            description="This property is no longer available and will be removed from the documentation soon. See the [deprecation notice](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-user-privacy-api-migration-guide/) for details."
        ),
    ] = None
    self: Annotated[str | None, Field(description="The URL of the user.")] = None
    time_zone: Annotated[
        str | None,
        Field(
            alias="timeZone",
            description="The time zone specified in the user's profile. Depending on the user’s privacy settings, this may be returned as null.",
        ),
    ] = None


class UserMigration(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    account_id: Annotated[str | None, Field(alias="accountId")] = None
    key: str | None = None
    username: str | None = None


class Type33(StrEnum):
    global_ = "GLOBAL"
    project = "PROJECT"


class Level(StrEnum):
    warning = "WARNING"
    error = "ERROR"


class VersionApprover(BaseModel):
    model_config = ConfigDict(
        extra="allow",
    )
    account_id: Annotated[
        str | None,
        Field(alias="accountId", description="The Atlassian account ID of the approver."),
    ] = None
    decline_reason: Annotated[
        str | None,
        Field(
            alias="declineReason",
            description="A description of why the user is declining the approval.",
        ),
    ] = None
    description: Annotated[
        str | None,
        Field(
            description="A description of what the user is approving within the specified version."
        ),
    ] = None
    status: Annotated[
        str | None,
        Field(
            description="The status of the approval, which can be *PENDING*, *APPROVED*, or *DECLINED*"
        ),
    ] = None


class VersionIssuesStatus(BaseModel):
    model_config = ConfigDict(
        extra="allow",
    )
    done: Annotated[int | None, Field(description="Count of issues with status *done*.")] = None
    in_progress: Annotated[
        int | None,
        Field(alias="inProgress", description="Count of issues with status *in progress*."),
    ] = None
    to_do: Annotated[
        int | None, Field(alias="toDo", description="Count of issues with status *to do*.")
    ] = None
    unmapped: Annotated[
        int | None,
        Field(
            description="Count of issues with a status other than *to do*, *in progress*, and *done*."
        ),
    ] = None


class Position3(StrEnum):
    earlier = "Earlier"
    later = "Later"
    first = "First"
    last = "Last"


class VersionMove(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    after: Annotated[
        AnyUrl | None,
        Field(
            description="The URL (self link) of the version after which to place the moved version. Cannot be used with `position`."
        ),
    ] = None
    position: Annotated[
        Position3 | None,
        Field(
            description="An absolute position in which to place the moved version. Cannot be used with `after`."
        ),
    ] = None


class Type34(StrEnum):
    group = "group"
    role = "role"


class VisibilityModel(BaseModel):
    model_config = ConfigDict(
        extra="allow",
    )
    identifier: Annotated[
        str | None,
        Field(
            description="The ID of the group or the name of the role that visibility of this item is restricted to."
        ),
    ] = None
    type: Annotated[
        Type34 | None,
        Field(description="Whether visibility of this item is restricted to a group or role."),
    ] = None
    value: Annotated[
        str | None,
        Field(
            description="The name of the group or role that visibility of this item is restricted to. Please note that the name of a group is mutable, to reliably identify a group use `identifier`."
        ),
    ] = None


class Event(StrEnum):
    jira_issue_created = "jira:issue_created"
    jira_issue_updated = "jira:issue_updated"
    jira_issue_deleted = "jira:issue_deleted"
    comment_created = "comment_created"
    comment_updated = "comment_updated"
    comment_deleted = "comment_deleted"
    issue_property_set = "issue_property_set"
    issue_property_deleted = "issue_property_deleted"
    sprint_created = "sprint_created"
    sprint_updated = "sprint_updated"
    sprint_closed = "sprint_closed"
    sprint_deleted = "sprint_deleted"
    sprint_started = "sprint_started"
    jira_version_released = "jira:version_released"
    jira_version_unreleased = "jira:version_unreleased"
    jira_version_created = "jira:version_created"
    jira_version_moved = "jira:version_moved"
    jira_version_updated = "jira:version_updated"
    jira_version_merged = "jira:version_merged"
    jira_version_deleted = "jira:version_deleted"


class WorkManagementNavigationInfo(BaseModel):
    board_name: Annotated[str | None, Field(alias="boardName")] = None


class EditorScope(StrEnum):
    project = "PROJECT"
    global_ = "GLOBAL"


class ProjectType1(StrEnum):
    software = "software"
    service_desk = "service_desk"
    product_discovery = "product_discovery"
    business = "business"
    unknown = "unknown"


class Operator5(StrEnum):
    and_ = "AND"
    or_ = "OR"


class WorkflowDocumentVersion(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    id: Annotated[str | None, Field(description="The version UUID.")] = None
    version_number: Annotated[
        int | None, Field(alias="versionNumber", description="The version number.")
    ] = None


class WorkflowId(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    draft: Annotated[bool, Field(description="Whether the workflow is in the draft state.")]
    name: Annotated[str, Field(description="The name of the workflow.")]


class Type35(StrEnum):
    project = "PROJECT"
    global_ = "GLOBAL"


class WorkflowTransition(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    id: Annotated[int, Field(description="The transition ID.")]
    name: Annotated[str, Field(description="The transition name.")]


class WorkflowTransitionProperty(BaseModel):
    model_config = ConfigDict(
        extra="allow",
    )
    id: Annotated[str | None, Field(description="The ID of the transition property.")] = None
    key: Annotated[
        str | None,
        Field(
            description="The key of the transition property. Also known as the name of the transition property."
        ),
    ] = None
    value: Annotated[str, Field(description="The value of the transition property.")]


class Type37(StrEnum):
    initial = "INITIAL"
    global_ = "GLOBAL"
    directed = "DIRECTED"


class Type38(StrEnum):
    rule = "RULE"
    status = "STATUS"
    status_layout = "STATUS_LAYOUT"
    status_property = "STATUS_PROPERTY"
    workflow = "WORKFLOW"
    transition = "TRANSITION"
    transition_property = "TRANSITION_PROPERTY"
    scope = "SCOPE"
    status_mapping = "STATUS_MAPPING"
    trigger = "TRIGGER"


class WorklogIdsRequest(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    ids: Annotated[list[int], Field(description="A list of worklog IDs.")]


class WorklogsMoveRequest(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    ids: Annotated[list[int] | None, Field(description="A list of worklog IDs.")] = None
    issue_id_or_key: Annotated[
        str | None,
        Field(
            alias="issueIdOrKey",
            description="The issue id or key of the destination issue",
        ),
    ] = None


class Type39(StrEnum):
    adf = "adf"
    raw = "raw"


class TargetClassification(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    classifications: Annotated[
        dict[str, list[str]],
        Field(
            description="An object with the key as the ID of the target classification and value with the list of the IDs of the current source classifications."
        ),
    ]
    issue_type: Annotated[
        str | None,
        Field(
            alias="issueType",
            description="ID of the source issueType to which issues present in `issueIdOrKeys` belongs.",
        ),
    ] = None
    project_key_or_id: Annotated[
        str | None,
        Field(
            alias="projectKeyOrId",
            description="ID or key of the source project to which issues present in `issueIdOrKeys` belongs.",
        ),
    ] = None


class TargetMandatoryFields(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    fields: Annotated[
        dict[str, Fields2 | Fields3], Field(description="Contains the value of mandatory fields")
    ]


class TargetStatus(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    statuses: Annotated[
        dict[str, list[str]],
        Field(
            description="An object with the key as the ID of the target status and value with the list of the IDs of the current source statuses."
        ),
    ]


class TargetToSourcesMapping(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    infer_classification_defaults: Annotated[
        bool,
        Field(
            alias="inferClassificationDefaults",
            description="If `true`, when issues are moved into this target group, they will adopt the target project's default classification, if they don't have a classification already. If they do have a classification, it will be kept the same even after the move. Leave `targetClassification` empty when using this.\n\nIf `false`, you must provide a `targetClassification` mapping for each classification associated with the selected issues.\n\n[Benefit from data classification](https://support.atlassian.com/security-and-access-policies/docs/what-is-data-classification/)",
        ),
    ]
    infer_field_defaults: Annotated[
        bool,
        Field(
            alias="inferFieldDefaults",
            description="If `true`, values from the source issues will be retained for the mandatory fields in the field configuration of the destination project. The `targetMandatoryFields` property shouldn't be defined.\n\nIf `false`, the user is required to set values for mandatory fields present in the field configuration of the destination project. Provide input by defining the `targetMandatoryFields` property",
        ),
    ]
    infer_status_defaults: Annotated[
        bool,
        Field(
            alias="inferStatusDefaults",
            description='If `true`, the statuses of issues being moved in this target group that are not present in the target workflow will be changed to the default status of the target workflow (see below). Leave `targetStatus` empty when using this.\n\nIf `false`, you must provide a `targetStatus` for each status not present in the target workflow.\n\nThe default status in a workflow is referred to as the "initial status". Each workflow has its own unique initial status. When an issue is created, it is automatically assigned to this initial status. Read more about configuring initial statuses: [Configure the initial status | Atlassian Support.](https://support.atlassian.com/jira-cloud-administration/docs/configure-the-initial-status/)',
        ),
    ]
    infer_subtask_type_default: Annotated[
        bool,
        Field(
            alias="inferSubtaskTypeDefault",
            description="When an issue is moved, its subtasks (if there are any) need to be moved with it. `inferSubtaskTypeDefault` helps with moving the subtasks by picking a random subtask type in the target project.\n\nIf `true`, subtasks will automatically move to the same project as their parent.\n\nWhen they move:\n\n *  Their `issueType` will be set to the default for subtasks in the target project.\n *  Values for mandatory fields will be retained from the source issues\n *  Specifying separate mapping for implicit subtasks won’t be allowed.\n\nIf `false`, you must manually move the subtasks. They will retain the parent which they had in the current project after being moved.",
        ),
    ]
    issue_ids_or_keys: Annotated[
        list[str] | None,
        Field(alias="issueIdsOrKeys", description="List of issue IDs or keys to be moved."),
    ] = None
    target_classification: Annotated[
        list[TargetClassification | None] | None,
        Field(
            alias="targetClassification",
            description='List of the objects containing classifications in the source issues and their new values which need to be set during the bulk move operation.\n\nIt is mandatory to provide source classification to target classification mapping when the source classification is invalid for the target project and issue type.\n\n *  **You should only define this property when `inferClassificationDefaults` is `false`.**\n *  **In order to provide mapping for issues which don\'t have a classification, use `"-1"`.**',
        ),
    ] = None
    target_mandatory_fields: Annotated[
        list[TargetMandatoryFields | None] | None,
        Field(
            alias="targetMandatoryFields",
            description="List of objects containing mandatory fields in the target field configuration and new values that need to be set during the bulk move operation.\n\nThe new values will only be applied if the field is mandatory in the target project and at least one issue from the source has that field empty, or if the field context is different in the target project (e.g. project-scoped version fields).\n\n**You should only define this property when `inferFieldDefaults` is `false`.**",
        ),
    ] = None
    target_status: Annotated[
        list[TargetStatus | None] | None,
        Field(
            alias="targetStatus",
            description="List of the objects containing statuses in the source workflow and their new values which need to be set during the bulk move operation.\n\nThe new values will only be applied if the source status is invalid for the target project and issue type.\n\nIt is mandatory to provide source status to target status mapping when the source status is invalid for the target project and issue type.\n\n**You should only define this property when `inferStatusDefaults` is `false`.**",
        ),
    ] = None


class AppWorkflowTransitionRule(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    configuration: RuleConfiguration
    id: Annotated[str, Field(description="The ID of the transition rule.")]
    key: Annotated[
        str,
        Field(
            description="The key of the rule, as defined in the Connect or the Forge app descriptor."
        ),
    ]
    transition: WorkflowTransition | None = None


class ApplicationRole(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    default_groups: Annotated[
        list[str] | None,
        Field(
            alias="defaultGroups",
            description="The groups that are granted default access for this application role. As a group's name can change, use of `defaultGroupsDetails` is recommended to identify a groups.",
        ),
    ] = None
    default_groups_details: Annotated[
        list[GroupName] | None,
        Field(
            alias="defaultGroupsDetails",
            description="The groups that are granted default access for this application role.",
        ),
    ] = None
    defined: Annotated[bool | None, Field(description="Deprecated.")] = None
    group_details: Annotated[
        list[GroupName] | None,
        Field(
            alias="groupDetails",
            description="The groups associated with the application role.",
        ),
    ] = None
    groups: Annotated[
        list[str] | None,
        Field(
            description="The groups associated with the application role. As a group's name can change, use of `groupDetails` is recommended to identify a groups."
        ),
    ] = None
    has_unlimited_seats: Annotated[bool | None, Field(alias="hasUnlimitedSeats")] = None
    key: Annotated[str | None, Field(description="The key of the application role.")] = None
    name: Annotated[str | None, Field(description="The display name of the application role.")] = (
        None
    )
    number_of_seats: Annotated[
        int | None,
        Field(
            alias="numberOfSeats",
            description="The maximum count of users on your license.",
        ),
    ] = None
    platform: Annotated[
        bool | None,
        Field(
            description="Indicates if the application role belongs to Jira platform (`jira-core`)."
        ),
    ] = None
    remaining_seats: Annotated[
        int | None,
        Field(
            alias="remainingSeats",
            description="The count of users remaining on your license.",
        ),
    ] = None
    selected_by_default: Annotated[
        bool | None,
        Field(
            alias="selectedByDefault",
            description="Determines whether this application role should be selected by default on user creation.",
        ),
    ] = None
    user_count: Annotated[
        int | None,
        Field(
            alias="userCount",
            description="The number of users counting against your license.",
        ),
    ] = None
    user_count_description: Annotated[
        str | None,
        Field(
            alias="userCountDescription",
            description="The [type of users](https://confluence.atlassian.com/x/lRW3Ng) being counted against your license.",
        ),
    ] = None


class AssociateFieldConfigurationsWithIssueTypesRequest(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    mappings: Annotated[
        list[FieldConfigurationToIssueTypeMapping],
        Field(description="Field configuration to issue type mappings."),
    ]


class AttachmentArchive(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    entries: list[AttachmentArchiveEntry] | None = None
    more_available: Annotated[bool | None, Field(alias="moreAvailable")] = None
    total_entry_count: Annotated[int | None, Field(alias="totalEntryCount")] = None
    total_number_of_entries_available: Annotated[
        int | None, Field(alias="totalNumberOfEntriesAvailable")
    ] = None


class AuditRecord(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    associated_items: Annotated[
        list[AssociatedItem] | None,
        Field(
            alias="associatedItems",
            description="The list of items associated with the changed record.",
        ),
    ] = None
    author_key: Annotated[
        str | None,
        Field(
            alias="authorKey",
            description="Deprecated, use `authorAccountId` instead. The key of the user who created the audit record.",
        ),
    ] = None
    category: Annotated[
        str | None,
        Field(
            description="The category of the audit record. For a list of these categories, see the help article [Auditing in Jira applications](https://confluence.atlassian.com/x/noXKM)."
        ),
    ] = None
    changed_values: Annotated[
        list[ChangedValue] | None,
        Field(
            alias="changedValues",
            description="The list of values changed in the record event.",
        ),
    ] = None
    created: Annotated[
        AwareDatetime | None,
        Field(description="The date and time on which the audit record was created."),
    ] = None
    description: Annotated[
        str | None, Field(description="The description of the audit record.")
    ] = None
    event_source: Annotated[
        str | None,
        Field(
            alias="eventSource",
            description="The event the audit record originated from.",
        ),
    ] = None
    id: Annotated[int | None, Field(description="The ID of the audit record.")] = None
    object_item: Annotated[AssociatedItem | None, Field(alias="objectItem")] = None
    remote_address: Annotated[
        str | None,
        Field(
            alias="remoteAddress",
            description="The URL of the computer where the creation of the audit record was initiated.",
        ),
    ] = None
    summary: Annotated[str | None, Field(description="The summary of the audit record.")] = None


class BulkPermissionsRequest(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    account_id: Annotated[
        str | None, Field(alias="accountId", description="The account ID of a user.")
    ] = None
    global_permissions: Annotated[
        list[str] | None,
        Field(alias="globalPermissions", description="Global permissions to look up."),
    ] = None
    project_permissions: Annotated[
        list[BulkProjectPermissions] | None,
        Field(
            alias="projectPermissions",
            description="Project permissions with associated projects and issues to look up.",
        ),
    ] = None


class BulkWorklogKeyRequest(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    requests: Annotated[
        list[WorklogCompositeKey] | None, Field(description="A list of issue and worklog ID pairs.")
    ] = None


class BulkWorklogKeyResponse(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    worklogs: Annotated[
        list[WorklogKeyResult] | None,
        Field(
            description="A list of successfully retrieved worklogs with their issue and worklog IDs."
        ),
    ] = None


class ConnectWorkflowTransitionRule(BaseModel):
    configuration: RuleConfiguration
    id: Annotated[str, Field(description="The ID of the transition rule.", examples=["123"])]
    key: Annotated[
        str,
        Field(
            description="The key of the rule, as defined in the Connect app descriptor.",
            examples=["WorkflowKey"],
        ),
    ]
    transition: WorkflowTransition | None = None


class DataClassificationLevels(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    classifications: Annotated[
        list[DataClassificationTag] | None, Field(description="The data classifications.")
    ] = None


class FieldModel(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    contexts_count: Annotated[
        int | None,
        Field(
            alias="contextsCount",
            description="Number of contexts where the field is used.",
        ),
    ] = None
    description: Annotated[str | None, Field(description="The description of the field.")] = None
    id: Annotated[str, Field(description="The ID of the field.")]
    is_locked: Annotated[
        bool | None, Field(alias="isLocked", description="Whether the field is locked.")
    ] = None
    is_unscreenable: Annotated[
        bool | None,
        Field(
            alias="isUnscreenable",
            description="Whether the field is shown on screen or not.",
        ),
    ] = None
    key: Annotated[str | None, Field(description="The key of the field.")] = None
    last_used: Annotated[FieldLastUsed | None, Field(alias="lastUsed")] = None
    name: Annotated[str, Field(description="The name of the field.")]
    projects_count: Annotated[
        int | None,
        Field(
            alias="projectsCount",
            description="Number of projects where the field is used.",
        ),
    ] = None
    schema_: Annotated[JsonType, Field(alias="schema")]
    screens_count: Annotated[
        int | None,
        Field(
            alias="screensCount",
            description="Number of screens where the field is used.",
        ),
    ] = None
    searcher_key: Annotated[
        str | None,
        Field(
            alias="searcherKey",
            description="The searcher key of the field. Returned for custom fields.",
        ),
    ] = None
    stable_id: Annotated[
        str | None, Field(alias="stableId", description="The stable ID of the field.")
    ] = None
    type_display_name: Annotated[
        str | None, Field(alias="typeDisplayName", description="The display name of the field type")
    ] = None


class FoundGroup(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    avatar_url: Annotated[
        str | None,
        Field(alias="avatarUrl", description="Avatar url for the group/team if present."),
    ] = None
    group_id: Annotated[
        str | None,
        Field(
            alias="groupId",
            description="The ID of the group, which uniquely identifies the group across all Atlassian products. For example, *952d12c3-5b5b-4d04-bb32-44d383afc4b2*.",
        ),
    ] = None
    html: Annotated[
        str | None,
        Field(
            description="The group name with the matched query string highlighted with the HTML bold tag."
        ),
    ] = None
    labels: list[GroupLabel] | None = None
    managed_by: Annotated[
        ManagedBy | None,
        Field(
            alias="managedBy",
            description="Describes who/how the team is managed. The possible values are  \n\\* external - when team is synced from an external directory like SCIM or HRIS, and team members cannot be modified.  \n\\* admins - when a team is managed by an admin (team members can only be modified by admins).  \n\\* team-members - managed by existing team members, new members need to be invited to join.  \n\\* open - anyone can join or modify this team.",
        ),
    ] = None
    name: Annotated[
        str | None,
        Field(
            description="The name of the group. The name of a group is mutable, to reliably identify a group use ``groupId`.`"
        ),
    ] = None
    usage_type: Annotated[
        UsageType | None,
        Field(
            alias="usageType",
            description="Describes the type of group. The possible values are  \n\\* team-collaboration - A platform team managed in people directory.  \n\\* userbase-group - a group of users created in adminhub.  \n\\* admin-oversight - currently unused.",
        ),
    ] = None


class FoundGroups(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    groups: list[FoundGroup] | None = None
    header: Annotated[
        str | None,
        Field(
            description="Header text indicating the number of groups in the response and the total number of groups found in the search."
        ),
    ] = None
    total: Annotated[
        int | None, Field(description="The total number of groups found in the search.")
    ] = None


class Hierarchy(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    base_level_id: Annotated[
        int | None,
        Field(
            alias="baseLevelId",
            description="The ID of the base level. This property is deprecated, see [Change notice: Removing hierarchy level IDs from next-gen APIs](https://developer.atlassian.com/cloud/jira/platform/change-notice-removing-hierarchy-level-ids-from-next-gen-apis/).",
        ),
    ] = None
    levels: Annotated[
        list[SimplifiedHierarchyLevel] | None,
        Field(description="Details about the hierarchy level."),
    ] = None


class IssueFieldOptionScope(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    global_: Annotated[
        GlobalScope | None,
        Field(
            alias="global",
            description="Defines the behavior of the option within the global context. If this property is set, even if set to an empty object, then the option is available in all projects.",
        ),
    ] = None
    projects: Annotated[list[int] | None, Field(description="DEPRECATED")] = None
    projects2: Annotated[
        list[ProjectScope] | None,
        Field(
            description="Defines the projects in which the option is available and the behavior of the option within each project. Specify one object per project. The behavior of the option in a project context overrides the behavior in the global context."
        ),
    ] = None


class JiraExpressionEvalContext(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    board: Annotated[
        int | None,
        Field(
            description="The ID of the board that is available under the `board` variable when evaluating the expression."
        ),
    ] = None
    custom: Annotated[
        list[CustomContextVariable1 | CustomContextVariable2 | CustomContextVariable3] | None,
        Field(
            description="Custom context variables and their types. These variable types are available for use in a custom context:\n\n *  `user`: A [user](https://developer.atlassian.com/cloud/jira/platform/jira-expressions-type-reference#user) specified as an Atlassian account ID.\n *  `issue`: An [issue](https://developer.atlassian.com/cloud/jira/platform/jira-expressions-type-reference#issue) specified by ID or key. All the fields of the issue object are available in the Jira expression.\n *  `json`: A JSON object containing custom content.\n *  `list`: A JSON list of `user`, `issue`, or `json` variable types."
        ),
    ] = None
    customer_request: Annotated[
        int | None,
        Field(
            alias="customerRequest",
            description="The ID of the customer request that is available under the `customerRequest` variable when evaluating the expression. This is the same as the ID of the underlying Jira issue, but the customer request context variable will have a different type.",
        ),
    ] = None
    issue: Annotated[
        IdOrKey | None,
        Field(
            description="The issue that is available under the `issue` variable when evaluating the expression."
        ),
    ] = None
    issues: Annotated[
        JexpIssues | None,
        Field(
            description="The collection of issues that is available under the `issues` variable when evaluating the expression."
        ),
    ] = None
    project: Annotated[
        IdOrKey | None,
        Field(
            description="The project that is available under the `project` variable when evaluating the expression."
        ),
    ] = None
    service_desk: Annotated[
        int | None,
        Field(
            alias="serviceDesk",
            description="The ID of the service desk that is available under the `serviceDesk` variable when evaluating the expression.",
        ),
    ] = None
    sprint: Annotated[
        int | None,
        Field(
            description="The ID of the sprint that is available under the `sprint` variable when evaluating the expression."
        ),
    ] = None


class JiraExpressionEvalRequest(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    context: Annotated[
        JiraExpressionEvalContext | None,
        Field(description="The context in which the Jira expression is evaluated."),
    ] = None
    expression: Annotated[
        str,
        Field(
            description="The Jira expression to evaluate.",
            examples=[
                "{ key: issue.key, type: issue.issueType.name, links: issue.links.map(link => link.linkedIssue.id) }"
            ],
        ),
    ]


class JiraExpressionEvaluateContext(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    board: Annotated[
        int | None,
        Field(
            description="The ID of the board that is available under the `board` variable when evaluating the expression."
        ),
    ] = None
    custom: Annotated[
        list[CustomContextVariable1 | CustomContextVariable2 | CustomContextVariable3] | None,
        Field(
            description="Custom context variables and their types. These variable types are available for use in a custom context:\n\n *  `user`: A [user](https://developer.atlassian.com/cloud/jira/platform/jira-expressions-type-reference#user) specified as an Atlassian account ID.\n *  `issue`: An [issue](https://developer.atlassian.com/cloud/jira/platform/jira-expressions-type-reference#issue) specified by ID or key. All the fields of the issue object are available in the Jira expression.\n *  `json`: A JSON object containing custom content.\n *  `list`: A JSON list of `user`, `issue`, or `json` variable types."
        ),
    ] = None
    customer_request: Annotated[
        int | None,
        Field(
            alias="customerRequest",
            description="The ID of the customer request that is available under the `customerRequest` variable when evaluating the expression. This is the same as the ID of the underlying Jira issue, but the customer request context variable will have a different type.",
        ),
    ] = None
    issue: Annotated[
        IdOrKey | None,
        Field(
            description="The issue that is available under the `issue` variable when evaluating the expression."
        ),
    ] = None
    issues: Annotated[
        JexpEvaluateCtxIssues | None,
        Field(
            description="The collection of issues that is available under the `issues` variable when evaluating the expression."
        ),
    ] = None
    project: Annotated[
        IdOrKey | None,
        Field(
            description="The project that is available under the `project` variable when evaluating the expression."
        ),
    ] = None
    service_desk: Annotated[
        int | None,
        Field(
            alias="serviceDesk",
            description="The ID of the service desk that is available under the `serviceDesk` variable when evaluating the expression.",
        ),
    ] = None
    sprint: Annotated[
        int | None,
        Field(
            description="The ID of the sprint that is available under the `sprint` variable when evaluating the expression."
        ),
    ] = None


class JiraExpressionEvaluateRequest(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    context: Annotated[
        JiraExpressionEvaluateContext | None,
        Field(description="The context in which the Jira expression is evaluated."),
    ] = None
    expression: Annotated[
        str,
        Field(
            description="The Jira expression to evaluate.",
            examples=[
                "{ key: issue.key, type: issue.issueType.name, links: issue.links.map(link => link.linkedIssue.id) }"
            ],
        ),
    ]


class JiraExpressionsComplexity(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    beans: Annotated[
        JiraExpressionsComplexityValue,
        Field(description="The number of Jira REST API beans returned in the response."),
    ]
    expensive_operations: Annotated[
        JiraExpressionsComplexityValue,
        Field(
            alias="expensiveOperations",
            description="The number of expensive operations executed while evaluating the expression. Expensive operations are those that load additional data, such as entity properties, comments, or custom fields.",
        ),
    ]
    primitive_values: Annotated[
        JiraExpressionsComplexityValue,
        Field(
            alias="primitiveValues",
            description="The number of primitive values returned in the response.",
        ),
    ]
    steps: Annotated[
        JiraExpressionsComplexityValue,
        Field(
            description="The number of steps it took to evaluate the expression, where a step is a high-level operation performed by the expression. A step is an operation such as arithmetic, accessing a property, accessing a context variable, or calling a function."
        ),
    ]


class LegacyJackson1ListUserMigration(RootModel[list[UserMigration]]):
    root: list[UserMigration]


class PageBean2ProjectField(BaseModel):
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
    values: Annotated[list[ProjectField] | None, Field(description="The list of items.")] = None


class PageBeanResolutionJson(BaseModel):
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
    values: Annotated[list[ResolutionJson] | None, Field(description="The list of items.")] = None


class PaginatedResponseComment(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    max_results: Annotated[int | None, Field(alias="maxResults")] = None
    results: list[Comment] | None = None
    start_at: Annotated[int | None, Field(alias="startAt")] = None
    total: int | None = None


class PaginatedResponseFieldCreateMetadata(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    max_results: Annotated[int | None, Field(alias="maxResults")] = None
    results: list[FieldCreateMetadata] | None = None
    start_at: Annotated[int | None, Field(alias="startAt")] = None
    total: int | None = None


class PermissionGrant(BaseModel):
    model_config = ConfigDict(
        extra="allow",
    )
    holder: Annotated[
        PermissionHolder | None,
        Field(
            description="The user or group being granted the permission. It consists of a `type`, a type-dependent `parameter` and a type-dependent `value`. See [Holder object](../api-group-permission-schemes/#holder-object) in *Get all permission schemes* for more information."
        ),
    ] = None
    id: Annotated[int | None, Field(description="The ID of the permission granted details.")] = None
    permission: Annotated[
        str | None,
        Field(
            description="The permission to grant. This permission can be one of the built-in permissions or a custom permission added by an app. See [Built-in permissions](../api-group-permission-schemes/#built-in-permissions) in *Get all permission schemes* for more information about the built-in permissions. See the [project permission](https://developer.atlassian.com/cloud/jira/platform/modules/project-permission/) and [global permission](https://developer.atlassian.com/cloud/jira/platform/modules/global-permission/) module documentation for more information about custom permissions."
        ),
    ] = None
    self: Annotated[
        AnyUrl | None, Field(description="The URL of the permission granted details.")
    ] = None


class ProjectDetails(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    avatar_urls: Annotated[
        AvatarUrls | None,
        Field(alias="avatarUrls", description="The URLs of the project's avatars."),
    ] = None
    id: Annotated[str | None, Field(description="The ID of the project.")] = None
    key: Annotated[str | None, Field(description="The key of the project.")] = None
    name: Annotated[str | None, Field(description="The name of the project.")] = None
    project_category: Annotated[
        UpdatedProjectCategory | None,
        Field(alias="projectCategory", description="The category the project belongs to."),
    ] = None
    project_type_key: Annotated[
        ProjectTypeKey | None,
        Field(
            alias="projectTypeKey",
            description="The [project type](https://confluence.atlassian.com/x/GwiiLQ#Jiraapplicationsoverview-Productfeaturesandprojecttypes) of the project.",
        ),
    ] = None
    self: Annotated[str | None, Field(description="The URL of the project details.")] = None
    simplified: Annotated[
        bool | None, Field(description="Whether or not the project is simplified.")
    ] = None


class Scope(BaseModel):
    model_config = ConfigDict(
        extra="allow",
    )
    project: Annotated[
        ProjectDetails | None, Field(description="The project the item has scope in.")
    ] = None
    type: Annotated[Type23 | None, Field(description="The type of scope.")] = None


class SecuritySchemeLevel(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    description: Annotated[
        str | None,
        Field(
            description="The description of the issue security scheme level.",
            max_length=4000,
        ),
    ] = None
    is_default: Annotated[
        bool | None,
        Field(
            alias="isDefault",
            description="Specifies whether the level is the default level. False by default.",
        ),
    ] = None
    members: Annotated[
        list[SecuritySchemeLevelMember] | None,
        Field(
            description="The list of level members which should be added to the issue security scheme level."
        ),
    ] = None
    name: Annotated[
        str,
        Field(
            description="The name of the issue security scheme level. Must be unique.",
            max_length=255,
        ),
    ]


class SimpleListWrapperApplicationRole(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    callback: ListWrapperCallbackApplicationRole | None = None
    items: list[ApplicationRole] | None = None
    max_results: Annotated[int | None, Field(alias="max-results")] = None
    paging_callback: Annotated[
        ListWrapperCallbackApplicationRole | None, Field(alias="pagingCallback")
    ] = None
    size: int | None = None


class StatusDetails(BaseModel):
    model_config = ConfigDict(
        extra="allow",
    )
    description: Annotated[str | None, Field(description="The description of the status.")] = None
    icon_url: Annotated[
        str | None,
        Field(
            alias="iconUrl",
            description="The URL of the icon used to represent the status.",
        ),
    ] = None
    id: Annotated[str | None, Field(description="The ID of the status.")] = None
    name: Annotated[str | None, Field(description="The name of the status.")] = None
    scope: Annotated[Scope | None, Field(description="The scope of the field.")] = None
    self: Annotated[str | None, Field(description="The URL of the status.")] = None
    status_category: Annotated[
        StatusCategory3 | None,
        Field(alias="statusCategory", description="The category assigned to the status."),
    ] = None


class UpdatePrioritySchemeRequest(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    default_priority_id: Annotated[
        int | None,
        Field(alias="defaultPriorityId", description="The default priority of the scheme."),
    ] = None
    description: Annotated[
        str | None, Field(description="The description of the priority scheme.", max_length=4000)
    ] = None
    mappings: Annotated[
        PriorityMapping | None,
        Field(
            description="Instructions to migrate the priorities of issues.\n\n`in` mappings are used to migrate the priorities of issues to priorities used within the priority scheme.\n\n`out` mappings are used to migrate the priorities of issues to priorities not used within the priority scheme.\n\n *  When **priorities** are **added** to the priority scheme, no mapping needs to be provided as the new priorities are not used by any issues.\n *  When **priorities** are **removed** from the priority scheme, issues that are using those priorities must be migrated to new priorities used by the priority scheme.\n    \n     *  An `in` mapping must be provided for each of these priorities.\n *  When **projects** are **added** to the priority scheme, the priorities of issues in those projects might need to be migrated to new priorities used by the priority scheme. This can occur when the current scheme does not use all the priorities in the project(s)' priority scheme(s).\n    \n     *  An `in` mapping must be provided for each of these priorities.\n *  When **projects** are **removed** from the priority scheme, the priorities of issues in those projects might need to be migrated to new priorities within the **Default Priority Scheme** that are not used by the priority scheme. This can occur when the **Default Priority Scheme** does not use all the priorities within the current scheme.\n    \n     *  An `out` mapping must be provided for each of these priorities.\n\nFor more information on `in` and `out` mappings, see the child properties documentation for the `PriorityMapping` object below."
        ),
    ] = None
    name: Annotated[
        str | None,
        Field(
            description="The name of the priority scheme. Must be unique.",
            max_length=255,
        ),
    ] = None
    priorities: Annotated[
        UpdatePrioritiesInSchemeRequest | None, Field(description="The priorities in the scheme.")
    ] = None
    projects: Annotated[
        UpdateProjectsInSchemeRequest | None, Field(description="The projects in the scheme.")
    ] = None


class User(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    account_id: Annotated[
        str | None,
        Field(
            alias="accountId",
            description="The account ID of the user, which uniquely identifies the user across all Atlassian products. For example, *5b10ac8d82e05b22cc7d4ef5*. Required in requests.",
            max_length=128,
        ),
    ] = None
    account_type: Annotated[
        AccountType | None,
        Field(
            alias="accountType",
            description="The user account type. Can take the following values:\n\n *  `atlassian` regular Atlassian user account\n *  `app` system account used for Connect applications and OAuth to represent external systems\n *  `customer` Jira Service Desk account representing an external service desk",
        ),
    ] = None
    active: Annotated[bool | None, Field(description="Whether the user is active.")] = None
    app_type: Annotated[
        str | None,
        Field(
            alias="appType",
            description="The app type of the user account when accountType is 'app'. Can take the following values:\n\n *  `service` Service Account\n *  `agent` Rovo Agent Account\n *  `unknown` Unknown app type",
        ),
    ] = None
    application_roles: Annotated[
        SimpleListWrapperApplicationRole | None,
        Field(
            alias="applicationRoles",
            description="The application roles the user is assigned to.",
        ),
    ] = None
    avatar_urls: Annotated[
        AvatarUrls | None, Field(alias="avatarUrls", description="The avatars of the user.")
    ] = None
    display_name: Annotated[
        str | None,
        Field(
            alias="displayName",
            description="The display name of the user. Depending on the user’s privacy setting, this may return an alternative value.",
        ),
    ] = None
    email_address: Annotated[
        str | None,
        Field(
            alias="emailAddress",
            description="The email address of the user. Depending on the user’s privacy setting, this may be returned as null.",
        ),
    ] = None
    expand: Annotated[
        str | None,
        Field(description="Expand options that include additional user details in the response."),
    ] = None
    groups: Annotated[
        SimpleListWrapperGroupName | None, Field(description="The groups that the user belongs to.")
    ] = None
    guest: Annotated[bool | None, Field(description="Whether the user is a guest.")] = None
    key: Annotated[
        str | None,
        Field(
            description="This property is no longer available and will be removed from the documentation soon. See the [deprecation notice](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-user-privacy-api-migration-guide/) for details."
        ),
    ] = None
    locale: Annotated[
        str | None,
        Field(
            description="The locale of the user. Depending on the user’s privacy setting, this may be returned as null."
        ),
    ] = None
    name: Annotated[
        str | None,
        Field(
            description="This property is no longer available and will be removed from the documentation soon. See the [deprecation notice](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-user-privacy-api-migration-guide/) for details."
        ),
    ] = None
    self: Annotated[AnyUrl | None, Field(description="The URL of the user.")] = None
    time_zone: Annotated[
        str | None,
        Field(
            alias="timeZone",
            description="The time zone specified in the user's profile. If the user's time zone is not visible to the current user (due to user's profile setting), or if a time zone has not been set, the instance's default time zone will be returned.",
        ),
    ] = None


class Version(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    approvers: Annotated[
        list[VersionApprover] | None,
        Field(
            description="If the expand option `approvers` is used, returns a list containing the approvers for this version."
        ),
    ] = None
    archived: Annotated[
        bool | None,
        Field(
            description="Indicates that the version is archived. Optional when creating or updating a version."
        ),
    ] = None
    description: Annotated[
        str | None,
        Field(
            description="The description of the version. Optional when creating or updating a version. The maximum size is 16,384 bytes."
        ),
    ] = None
    driver: Annotated[
        str | None,
        Field(
            description="If the expand option `driver` is used, returns the Atlassian account ID of the driver."
        ),
    ] = None
    expand: Annotated[
        str | None,
        Field(
            description="Use [expand](em>#expansion) to include additional information about version in the response. This parameter accepts a comma-separated list. Expand options include:\n\n *  `operations` Returns the list of operations available for this version.\n *  `issuesstatus` Returns the count of issues in this version for each of the status categories *to do*, *in progress*, *done*, and *unmapped*. The *unmapped* property contains a count of issues with a status other than *to do*, *in progress*, and *done*.\n *  `driver` Returns the Atlassian account ID of the version driver.\n *  `approvers` Returns a list containing approvers for this version.\n\nOptional for create and update."
        ),
    ] = None
    id: Annotated[str | None, Field(description="The ID of the version.")] = None
    issues_status_for_fix_version: Annotated[
        VersionIssuesStatus | None,
        Field(
            alias="issuesStatusForFixVersion",
            description="If the expand option `issuesstatus` is used, returns the count of issues in this version for each of the status categories *to do*, *in progress*, *done*, and *unmapped*. The *unmapped* property contains a count of issues with a status other than *to do*, *in progress*, and *done*.",
        ),
    ] = None
    move_unfixed_issues_to: Annotated[
        AnyUrl | None,
        Field(
            alias="moveUnfixedIssuesTo",
            description="The URL of the self link to the version to which all unfixed issues are moved when a version is released. Not applicable when creating a version. Optional when updating a version.",
        ),
    ] = None
    name: Annotated[
        str | None,
        Field(
            description="The unique name of the version. Required when creating a version. Optional when updating a version. The maximum length is 255 characters."
        ),
    ] = None
    operations: Annotated[
        list[SimpleLink] | None,
        Field(
            description="If the expand option `operations` is used, returns the list of operations available for this version."
        ),
    ] = None
    overdue: Annotated[bool | None, Field(description="Indicates that the version is overdue.")] = (
        None
    )
    project: Annotated[str | None, Field(description="Deprecated. Use `projectId`.")] = None
    project_id: Annotated[
        int | None,
        Field(
            alias="projectId",
            description="The ID of the project to which this version is attached. Required when creating a version. Not applicable when updating a version.",
        ),
    ] = None
    release_date: Annotated[
        date_aliased | None,
        Field(
            alias="releaseDate",
            description="The release date of the version. Expressed in ISO 8601 format (yyyy-mm-dd). Optional when creating or updating a version.",
        ),
    ] = None
    released: Annotated[
        bool | None,
        Field(
            description="Indicates that the version is released. If the version is released a request to release again is ignored. Not applicable when creating a version. Optional when updating a version."
        ),
    ] = None
    self: Annotated[AnyUrl | None, Field(description="The URL of the version.")] = None
    start_date: Annotated[
        date_aliased | None,
        Field(
            alias="startDate",
            description="The start date of the version. Expressed in ISO 8601 format (yyyy-mm-dd). Optional when creating or updating a version.",
        ),
    ] = None
    user_release_date: Annotated[
        str | None,
        Field(
            alias="userReleaseDate",
            description="The date on which work on this version is expected to finish, expressed in the instance's *Day/Month/Year Format* date format.",
        ),
    ] = None
    user_start_date: Annotated[
        str | None,
        Field(
            alias="userStartDate",
            description="The date on which work on this version is expected to start, expressed in the instance's *Day/Month/Year Format* date format.",
        ),
    ] = None


class WorkflowSchemeProjectSwitch(BaseModel):
    model_config = ConfigDict(
        extra="allow",
    )
    mappings_by_issue_type_override: Annotated[
        list[MappingsByIssueTypeOverride] | None,
        Field(
            alias="mappingsByIssueTypeOverride",
            description="The mappings for migrating issues from old statuses to new statuses when switching from one workflow scheme to another. This field is required if any statuses in the current project's workflows would no longer exist in the target workflow scheme. Each mapping defines how to update issues from an old status to the corresponding new status in the issue’s new workflow.",
        ),
    ] = None
    project_id: Annotated[
        str | None,
        Field(
            alias="projectId",
            description="The ID of the project to switch the workflow scheme for",
            examples=["10001"],
        ),
    ] = None
    target_scheme_id: Annotated[
        str | None,
        Field(
            alias="targetSchemeId",
            description="The ID of the target workflow scheme to switch to",
            examples=["10002"],
        ),
    ] = None


class WorkflowTransitionRules(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    conditions: Annotated[
        list[AppWorkflowTransitionRule] | None,
        Field(description="The list of conditions within the workflow."),
    ] = None
    post_functions: Annotated[
        list[AppWorkflowTransitionRule] | None,
        Field(
            alias="postFunctions",
            description="The list of post functions within the workflow.",
        ),
    ] = None
    validators: Annotated[
        list[AppWorkflowTransitionRule] | None,
        Field(description="The list of validators within the workflow."),
    ] = None
    workflow_id: Annotated[WorkflowId, Field(alias="workflowId")]


class WorkflowUpdateValidateRequest(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    payload: WorkflowUpdateRequest
    validation_options: Annotated[
        ValidationOptionsForUpdate | None, Field(alias="validationOptions")
    ] = None


class AddSecuritySchemeLevelsRequest(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    levels: Annotated[
        list[SecuritySchemeLevel] | None,
        Field(
            description="The list of scheme levels which should be added to the security scheme."
        ),
    ] = None


class FieldDetails(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    clause_names: Annotated[
        list[str] | None,
        Field(
            alias="clauseNames",
            description="The names that can be used to reference the field in an advanced search. For more information, see [Advanced searching - fields reference](https://confluence.atlassian.com/x/gwORLQ).",
        ),
    ] = None
    custom: Annotated[bool | None, Field(description="Whether the field is a custom field.")] = None
    id: Annotated[str | None, Field(description="The ID of the field.")] = None
    key: Annotated[str | None, Field(description="The key of the field.")] = None
    name: Annotated[str | None, Field(description="The name of the field.")] = None
    navigable: Annotated[
        bool | None,
        Field(description="Whether the field can be used as a column on the issue navigator."),
    ] = None
    orderable: Annotated[
        bool | None,
        Field(description="Whether the content of the field can be used to order lists."),
    ] = None
    schema_: Annotated[
        JsonType | None, Field(alias="schema", description="The data schema for the field.")
    ] = None
    scope: Annotated[Scope | None, Field(description="The scope of the field.")] = None
    searchable: Annotated[
        bool | None, Field(description="Whether the content of the field can be searched.")
    ] = None


class IssueFieldOptionCreate(BaseModel):
    model_config = ConfigDict(
        extra="allow",
    )
    config: IssueFieldOptionConfiguration | None = None
    properties: Annotated[
        dict[str, Any] | None,
        Field(
            description="The properties of the option as arbitrary key-value pairs. These properties can be searched using JQL, if the extractions (see https://developer.atlassian.com/cloud/jira/platform/modules/issue-field-option-property-index/) are defined in the descriptor for the issue field module."
        ),
    ] = None
    value: Annotated[str, Field(description="The option's name, which is displayed in Jira.")]


class IssueTypeDetails(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    avatar_id: Annotated[
        int | None, Field(alias="avatarId", description="The ID of the issue type's avatar.")
    ] = None
    description: Annotated[str | None, Field(description="The description of the issue type.")] = (
        None
    )
    entity_id: Annotated[
        UUID | None, Field(alias="entityId", description="Unique ID for next-gen projects.")
    ] = None
    hierarchy_level: Annotated[
        int | None, Field(alias="hierarchyLevel", description="Hierarchy level of the issue type.")
    ] = None
    icon_url: Annotated[
        str | None, Field(alias="iconUrl", description="The URL of the issue type's avatar.")
    ] = None
    id: Annotated[str | None, Field(description="The ID of the issue type.")] = None
    name: Annotated[str | None, Field(description="The name of the issue type.")] = None
    scope: Annotated[
        Scope | None,
        Field(description="Details of the next-gen projects the issue type is available in."),
    ] = None
    self: Annotated[str | None, Field(description="The URL of these issue type details.")] = None
    subtask: Annotated[
        bool | None, Field(description="Whether this issue type is used to create subtasks.")
    ] = None


class IssuesUpdate(BaseModel):
    model_config = ConfigDict(
        extra="allow",
    )
    issue_updates: Annotated[list[IssueUpdateDetails] | None, Field(alias="issueUpdates")] = None


class JExpEvaluateMetaData(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    complexity: Annotated[
        JiraExpressionsComplexity | None,
        Field(
            description="Contains information about the expression complexity. For example, the number of steps it took to evaluate the expression."
        ),
    ] = None
    issues: Annotated[
        JExpEvaluateIssuesMeta | None,
        Field(
            description="Contains information about the `issues` variable in the context. For example, is the issues were loaded with JQL, information about the page will be included here."
        ),
    ] = None


class JiraExpressionEvaluationMetaData(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    complexity: Annotated[
        JiraExpressionsComplexity | None,
        Field(
            description="Contains information about the expression complexity. For example, the number of steps it took to evaluate the expression."
        ),
    ] = None
    issues: Annotated[
        IssuesMeta | None,
        Field(
            description="Contains information about the `issues` variable in the context. For example, is the issues were loaded with JQL, information about the page will be included here."
        ),
    ] = None


class LegacyJackson1ListVersion(RootModel[list[Version]]):
    root: list[Version]


class PageBeanProjectDetails(BaseModel):
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
    values: Annotated[list[ProjectDetails] | None, Field(description="The list of items.")] = None


class PaginatedResponseIssueTypeIssueCreateMetadata(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    max_results: Annotated[int | None, Field(alias="maxResults")] = None
    results: list[IssueTypeIssueCreateMetadata] | None = None
    start_at: Annotated[int | None, Field(alias="startAt")] = None
    total: int | None = None


class PermissionScheme(BaseModel):
    model_config = ConfigDict(
        extra="allow",
    )
    description: Annotated[
        str | None, Field(description="A description for the permission scheme.")
    ] = None
    expand: Annotated[
        str | None, Field(description="The expand options available for the permission scheme.")
    ] = None
    id: Annotated[int | None, Field(description="The ID of the permission scheme.")] = None
    name: Annotated[str, Field(description="The name of the permission scheme. Must be unique.")]
    permissions: Annotated[
        list[PermissionGrant] | None,
        Field(
            description="The permission scheme to create or update. See [About permission schemes and grants](../api-group-permission-schemes/#about-permission-schemes-and-grants) for more information."
        ),
    ] = None
    scope: Annotated[Scope | None, Field(description="The scope of the permission scheme.")] = None
    self: Annotated[AnyUrl | None, Field(description="The URL of the permission scheme.")] = None


class ProjectComponent(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    ari: Annotated[
        str | None,
        Field(
            description="Compass component's ID. Can't be updated. Not required for creating a Project Component."
        ),
    ] = None
    assignee: Annotated[
        User | None,
        Field(
            description="The details of the user associated with `assigneeType`, if any. See `realAssignee` for details of the user assigned to issues created with this component."
        ),
    ] = None
    assignee_type: Annotated[
        AssigneeType4 | None,
        Field(
            alias="assigneeType",
            description="The nominal user type used to determine the assignee for issues created with this component. See `realAssigneeType` for details on how the type of the user, and hence the user, assigned to issues is determined. Can take the following values:\n\n *  `PROJECT_LEAD` the assignee to any issues created with this component is nominally the lead for the project the component is in.\n *  `COMPONENT_LEAD` the assignee to any issues created with this component is nominally the lead for the component.\n *  `UNASSIGNED` an assignee is not set for issues created with this component.\n *  `PROJECT_DEFAULT` the assignee to any issues created with this component is nominally the default assignee for the project that the component is in.\n\nDefault value: `PROJECT_DEFAULT`.  \nOptional when creating or updating a component.",
        ),
    ] = None
    description: Annotated[
        str | None,
        Field(
            description="The description for the component. Optional when creating or updating a component."
        ),
    ] = None
    id: Annotated[str | None, Field(description="The unique identifier for the component.")] = None
    is_assignee_type_valid: Annotated[
        bool | None,
        Field(
            alias="isAssigneeTypeValid",
            description="Whether a user is associated with `assigneeType`. For example, if the `assigneeType` is set to `COMPONENT_LEAD` but the component lead is not set, then `false` is returned.",
        ),
    ] = None
    lead: Annotated[
        User | None, Field(description="The user details for the component's lead user.")
    ] = None
    lead_account_id: Annotated[
        str | None,
        Field(
            alias="leadAccountId",
            description="The accountId of the component's lead user. The accountId uniquely identifies the user across all Atlassian products. For example, *5b10ac8d82e05b22cc7d4ef5*.",
            max_length=128,
        ),
    ] = None
    lead_user_name: Annotated[
        str | None,
        Field(
            alias="leadUserName",
            description="This property is no longer available and will be removed from the documentation soon. See the [deprecation notice](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-user-privacy-api-migration-guide/) for details.",
        ),
    ] = None
    metadata: Annotated[
        dict[str, str] | None,
        Field(
            description="Compass component's metadata. Can't be updated. Not required for creating a Project Component."
        ),
    ] = None
    name: Annotated[
        str | None,
        Field(
            description="The unique name for the component in the project. Required when creating a component. Optional when updating a component. The maximum length is 255 characters."
        ),
    ] = None
    project: Annotated[
        str | None,
        Field(
            description="The key of the project the component is assigned to. Required when creating a component. Can't be updated."
        ),
    ] = None
    project_id: Annotated[
        int | None,
        Field(
            alias="projectId",
            description="The ID of the project the component is assigned to.",
        ),
    ] = None
    real_assignee: Annotated[
        User | None,
        Field(
            alias="realAssignee",
            description="The user assigned to issues created with this component, when `assigneeType` does not identify a valid assignee.",
        ),
    ] = None
    real_assignee_type: Annotated[
        RealAssigneeType | None,
        Field(
            alias="realAssigneeType",
            description="The type of the assignee that is assigned to issues created with this component, when an assignee cannot be set from the `assigneeType`. For example, `assigneeType` is set to `COMPONENT_LEAD` but no component lead is set. This property is set to one of the following values:\n\n *  `PROJECT_LEAD` when `assigneeType` is `PROJECT_LEAD` and the project lead has permission to be assigned issues in the project that the component is in.\n *  `COMPONENT_LEAD` when `assignee`Type is `COMPONENT_LEAD` and the component lead has permission to be assigned issues in the project that the component is in.\n *  `UNASSIGNED` when `assigneeType` is `UNASSIGNED` and Jira is configured to allow unassigned issues.\n *  `PROJECT_DEFAULT` when none of the preceding cases are true.",
        ),
    ] = None
    self: Annotated[AnyUrl | None, Field(description="The URL of the component.")] = None


class ProjectRole(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    actors: Annotated[
        list[RoleActor] | None, Field(description="The list of users who act in this role.")
    ] = None
    admin: Annotated[
        bool | None, Field(description="Whether this role is the admin role for the project.")
    ] = None
    current_user_role: Annotated[
        bool | None,
        Field(
            alias="currentUserRole",
            description="Whether the calling user is part of this role.",
        ),
    ] = None
    default: Annotated[
        bool | None, Field(description="Whether this role is the default role for the project")
    ] = None
    description: Annotated[
        str | None, Field(description="The description of the project role.")
    ] = None
    id: Annotated[int | None, Field(description="The ID of the project role.")] = None
    name: Annotated[str | None, Field(description="The name of the project role.")] = None
    role_configurable: Annotated[
        bool | None,
        Field(
            alias="roleConfigurable",
            description="Whether the roles are configurable for this project.",
        ),
    ] = None
    scope: Annotated[
        Scope | None,
        Field(
            description="The scope of the role. Indicated for roles associated with [next-gen projects](https://confluence.atlassian.com/x/loMyO)."
        ),
    ] = None
    self: Annotated[AnyUrl | None, Field(description="The URL the project role details.")] = None
    translated_name: Annotated[
        str | None,
        Field(
            alias="translatedName",
            description="The translated name of the project role.",
        ),
    ] = None


class UpdatePrioritySchemeResponse(BaseModel):
    model_config = ConfigDict(
        extra="allow",
    )
    priority_scheme: Annotated[
        PrioritySchemeWithPaginatedPrioritiesAndProjects | None, Field(alias="priorityScheme")
    ] = None
    task: Annotated[
        TaskProgressBeanJsonNode | None, Field(description="The in-progress issue migration task.")
    ] = None


class BulkChangelogResponse(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    issue_change_logs: Annotated[
        list[IssueChangeLog] | None,
        Field(alias="issueChangeLogs", description="The list of issues changelogs."),
    ] = None
    next_page_token: Annotated[
        str | None,
        Field(
            alias="nextPageToken",
            description="Continuation token to fetch the next page. If this result represents the last or the only page, this token will be null.",
        ),
    ] = None


class EventNotification(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    email_address: Annotated[
        str | None, Field(alias="emailAddress", description="The email address.")
    ] = None
    expand: Annotated[
        str | None,
        Field(
            description="Expand options that include additional event notification details in the response."
        ),
    ] = None
    field: Annotated[FieldDetails | None, Field(description="The custom user or group field.")] = (
        None
    )
    group: Annotated[GroupName | None, Field(description="The specified group.")] = None
    id: Annotated[int | None, Field(description="The ID of the notification.")] = None
    notification_type: Annotated[
        NotificationType | None,
        Field(
            alias="notificationType",
            description="Identifies the recipients of the notification.",
        ),
    ] = None
    parameter: Annotated[
        str | None,
        Field(
            description="As a group's name can change, use of `recipient` is recommended. The identifier associated with the `notificationType` value that defines the receiver of the notification, where the receiver isn't implied by `notificationType` value. So, when `notificationType` is:\n\n *  `User` The `parameter` is the user account ID.\n *  `Group` The `parameter` is the group name.\n *  `ProjectRole` The `parameter` is the project role ID.\n *  `UserCustomField` The `parameter` is the ID of the custom field.\n *  `GroupCustomField` The `parameter` is the ID of the custom field."
        ),
    ] = None
    project_role: Annotated[
        ProjectRole | None, Field(alias="projectRole", description="The specified project role.")
    ] = None
    recipient: Annotated[
        str | None,
        Field(
            description="The identifier associated with the `notificationType` value that defines the receiver of the notification, where the receiver isn't implied by the `notificationType` value. So, when `notificationType` is:\n\n *  `User`, `recipient` is the user account ID.\n *  `Group`, `recipient` is the group ID.\n *  `ProjectRole`, `recipient` is the project role ID.\n *  `UserCustomField`, `recipient` is the ID of the custom field.\n *  `GroupCustomField`, `recipient` is the ID of the custom field."
        ),
    ] = None
    user: Annotated[UserDetails | None, Field(description="The specified user.")] = None


class Issue(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    changelog: Annotated[
        PageOfChangelogs | None,
        Field(description="Details of changelogs associated with the issue."),
    ] = None
    editmeta: Annotated[
        IssueUpdateMetadata | None,
        Field(description="The metadata for the fields on the issue that can be amended."),
    ] = None
    expand: Annotated[
        str | None,
        Field(description="Expand options that include additional issue details in the response."),
    ] = None
    fields: dict[str, Any] | None = None
    fields_to_include: Annotated[IncludedFields | None, Field(alias="fieldsToInclude")] = None
    id: Annotated[str | None, Field(description="The ID of the issue.")] = None
    key: Annotated[str | None, Field(description="The key of the issue.")] = None
    names: Annotated[
        dict[str, str] | None,
        Field(description="The ID and name of each field present on the issue."),
    ] = None
    operations: Annotated[
        Operations | None, Field(description="The operations that can be performed on the issue.")
    ] = None
    properties: Annotated[
        dict[str, Any] | None,
        Field(description="Details of the issue properties identified in the request."),
    ] = None
    rendered_fields: Annotated[
        dict[str, Any] | None,
        Field(
            alias="renderedFields",
            description="The rendered value of each field present on the issue.",
        ),
    ] = None
    schema_: Annotated[
        dict[str, JsonType] | None,
        Field(
            alias="schema",
            description="The schema describing each field present on the issue.",
        ),
    ] = None
    self: Annotated[AnyUrl | None, Field(description="The URL of the issue details.")] = None
    transitions: Annotated[
        list[IssueTransition] | None,
        Field(description="The transitions that can be performed on the issue."),
    ] = None
    versioned_representations: Annotated[
        dict[str, dict[str, Any]] | None,
        Field(
            alias="versionedRepresentations",
            description="The versions of each field on the issue.",
        ),
    ] = None


class JExpEvaluateJiraExpressionResult(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    meta: Annotated[
        JExpEvaluateMetaData | None,
        Field(
            description="Contains various characteristics of the performed expression evaluation."
        ),
    ] = None
    value: Annotated[
        Any,
        Field(
            description="The value of the evaluated expression. It may be a primitive JSON value or a Jira REST API object. (Some expressions do not produce any meaningful results—for example, an expression that returns a lambda function—if that's the case a simple string representation is returned. These string representations should not be relied upon and may change without notice.)"
        ),
    ]


class LegacyJackson1ListProjectComponent(RootModel[list[ProjectComponent]]):
    root: list[ProjectComponent]


class NotificationSchemeEvent(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    event: NotificationEvent | None = None
    notifications: list[EventNotification] | None = None


class Project(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    archived: Annotated[bool | None, Field(description="Whether the project is archived.")] = None
    archived_by: Annotated[
        User | None, Field(alias="archivedBy", description="The user who archived the project.")
    ] = None
    archived_date: Annotated[
        AwareDatetime | None,
        Field(alias="archivedDate", description="The date when the project was archived."),
    ] = None
    assignee_type: Annotated[
        AssigneeType3 | None,
        Field(
            alias="assigneeType",
            description="The default assignee when creating issues for this project.",
        ),
    ] = None
    avatar_urls: Annotated[
        AvatarUrls | None,
        Field(alias="avatarUrls", description="The URLs of the project's avatars."),
    ] = None
    components: Annotated[
        list[ProjectComponent] | None,
        Field(description="List of the components contained in the project."),
    ] = None
    deleted: Annotated[
        bool | None, Field(description="Whether the project is marked as deleted.")
    ] = None
    deleted_by: Annotated[
        User | None,
        Field(alias="deletedBy", description="The user who marked the project as deleted."),
    ] = None
    deleted_date: Annotated[
        AwareDatetime | None,
        Field(
            alias="deletedDate",
            description="The date when the project was marked as deleted.",
        ),
    ] = None
    description: Annotated[str | None, Field(description="A brief description of the project.")] = (
        None
    )
    email: Annotated[
        str | None, Field(description="An email address associated with the project.")
    ] = None
    expand: Annotated[
        str | None,
        Field(
            description="Expand options that include additional project details in the response."
        ),
    ] = None
    favourite: Annotated[
        bool | None, Field(description="Whether the project is selected as a favorite.")
    ] = None
    id: Annotated[str | None, Field(description="The ID of the project.")] = None
    insight: Annotated[ProjectInsight | None, Field(description="Insights about the project.")] = (
        None
    )
    is_private: Annotated[
        bool | None,
        Field(
            alias="isPrivate",
            description="Whether the project is private from the user's perspective. This means the user can't see the project or any associated issues.",
        ),
    ] = None
    issue_type_hierarchy: Annotated[
        Hierarchy | None,
        Field(
            alias="issueTypeHierarchy",
            description="The issue type hierarchy for the project.",
        ),
    ] = None
    issue_types: Annotated[
        list[IssueTypeDetails] | None,
        Field(
            alias="issueTypes",
            description="List of the issue types available in the project.",
        ),
    ] = None
    key: Annotated[str | None, Field(description="The key of the project.")] = None
    landing_page_info: Annotated[
        ProjectLandingPageInfo | None,
        Field(alias="landingPageInfo", description="The project landing page info."),
    ] = None
    lead: Annotated[User | None, Field(description="The username of the project lead.")] = None
    name: Annotated[str | None, Field(description="The name of the project.")] = None
    permissions: Annotated[
        ProjectPermissions | None, Field(description="User permissions on the project")
    ] = None
    project_category: Annotated[
        ProjectCategory | None,
        Field(alias="projectCategory", description="The category the project belongs to."),
    ] = None
    project_type_key: Annotated[
        ProjectTypeKey | None,
        Field(
            alias="projectTypeKey",
            description="The [project type](https://confluence.atlassian.com/x/GwiiLQ#Jiraapplicationsoverview-Productfeaturesandprojecttypes) of the project.",
        ),
    ] = None
    properties: Annotated[dict[str, Any] | None, Field(description="Map of project properties")] = (
        None
    )
    retention_till_date: Annotated[
        AwareDatetime | None,
        Field(
            alias="retentionTillDate",
            description="The date when the project is deleted permanently.",
        ),
    ] = None
    roles: Annotated[
        dict[str, AnyUrl] | None,
        Field(
            description="The name and self URL for each role defined in the project. For more information, see [Create project role](#api-rest-api-3-role-post)."
        ),
    ] = None
    self: Annotated[AnyUrl | None, Field(description="The URL of the project details.")] = None
    simplified: Annotated[bool | None, Field(description="Whether the project is simplified.")] = (
        None
    )
    style: Annotated[Style | None, Field(description="The type of the project.")] = None
    url: Annotated[
        str | None,
        Field(
            description="A link to information about this project, such as project documentation."
        ),
    ] = None
    uuid: Annotated[UUID | None, Field(description="Unique ID for next-gen projects.")] = None
    versions: Annotated[
        list[Version] | None,
        Field(
            description="The versions defined in the project. For more information, see [Create version](#api-rest-api-3-version-post)."
        ),
    ] = None


class SharePermission(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    group: Annotated[
        GroupName | None,
        Field(
            description="The group that the filter is shared with. For a request, specify the `groupId` or `name` property for the group. As a group's name can change, use of `groupId` is recommended."
        ),
    ] = None
    id: Annotated[
        int | None, Field(description="The unique identifier of the share permission.")
    ] = None
    project: Annotated[
        Project | None,
        Field(
            description="The project that the filter is shared with. This is similar to the project object returned by [Get project](#api-rest-api-3-project-projectIdOrKey-get) but it contains a subset of the properties, which are: `self`, `id`, `key`, `assigneeType`, `name`, `roles`, `avatarUrls`, `projectType`, `simplified`.  \nFor a request, specify the `id` for the project."
        ),
    ] = None
    role: Annotated[
        ProjectRole | None,
        Field(
            description="The project role that the filter is shared with.  \nFor a request, specify the `id` for the role. You must also specify the `project` object and `id` for the project that the role is in."
        ),
    ] = None
    type: Annotated[
        Type26,
        Field(
            description="The type of share permission:\n\n *  `user` Shared with a user.\n *  `group` Shared with a group. If set in a request, then specify `sharePermission.group` as well.\n *  `project` Shared with a project. If set in a request, then specify `sharePermission.project` as well.\n *  `projectRole` Share with a project role in a project. This value is not returned in responses. It is used in requests, where it needs to be specify with `projectId` and `projectRoleId`.\n *  `global` Shared globally. If set in a request, no other `sharePermission` properties need to be specified.\n *  `loggedin` Shared with all logged-in users. Note: This value is set in a request by specifying `authenticated` as the `type`.\n *  `project-unknown` Shared with a project that the user does not have access to. Cannot be set in a request."
        ),
    ]
    user: Annotated[
        User | None,
        Field(
            description="The user account ID that the filter is shared with. For a request, specify the `accountId` property for the user."
        ),
    ] = None


class LegacyJackson1ListProject(RootModel[list[Project]]):
    root: list[Project]


class LinkIssueRequestJson(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    comment: Comment | None = None
    inward_issue: Annotated[LinkedIssue, Field(alias="inwardIssue")]
    outward_issue: Annotated[LinkedIssue, Field(alias="outwardIssue")]
    type: IssueLinkType


class NotificationScheme(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    description: Annotated[
        str | None, Field(description="The description of the notification scheme.")
    ] = None
    expand: Annotated[
        str | None,
        Field(
            description="Expand options that include additional notification scheme details in the response."
        ),
    ] = None
    id: Annotated[int | None, Field(description="The ID of the notification scheme.")] = None
    name: Annotated[str | None, Field(description="The name of the notification scheme.")] = None
    notification_scheme_events: Annotated[
        list[NotificationSchemeEvent] | None,
        Field(
            alias="notificationSchemeEvents",
            description="The notification events and associated recipients.",
        ),
    ] = None
    projects: Annotated[
        list[int] | None,
        Field(description="The list of project IDs associated with the notification scheme."),
    ] = None
    scope: Annotated[Scope | None, Field(description="The scope of the notification scheme.")] = (
        None
    )
    self: str | None = None


class PageBeanProject(BaseModel):
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
    values: Annotated[list[Project] | None, Field(description="The list of items.")] = None


__all__ = [
    "ActorInput",
    "PlanningStyle",
    "AddField",
    "AddGroup",
    "Visibility",
    "Active",
    "ConditionType",
    "ExcludeEnum",
    "AssociatedItem",
    "RuleType",
    "Avatar",
    "AvatarUrls",
    "FeatureKey",
    "State",
    "CardColorStrategy",
    "BulkChangelogRequest",
    "Action",
    "BulkFetchIssueRequest",
    "Status",
    "ShowDaysInColumn",
    "Mode",
    "ChangedValue",
    "ColumnItem",
    "ColumnRequestBody",
    "ComponentJson",
    "AssigneeType",
    "RealAssigneeType",
    "Operator",
    "Operation",
    "FieldType",
    "EntityType",
    "Type",
    "CreateFieldAssociationSchemeLinks",
    "Type1",
    "Type2",
    "Type3",
    "IconUrl",
    "PriorityId",
    "AssigneeType1",
    "ProjectTemplateKey",
    "ProjectTypeKey",
    "Dependencies",
    "Estimation",
    "InferredDates",
    "CreateUpdateRoleRequest",
    "Operator1",
    "Type4",
    "SearcherKey",
    "CustomFieldDefinitionJson",
    "OnConflict",
    "Scope1",
    "AccessLevel",
    "AssigneeType2",
    "Color",
    "DataClassificationTag",
    "Scope2",
    "Value",
    "DeleteAndReplaceVersion",
    "EntityProperty",
    "ErrorCollection",
    "ErrorCollections",
    "ErrorMessage",
    "NotificationType",
    "ExpandPriorityScheme",
    "ExpandPrioritySchemePage",
    "FieldConfiguration",
    "FieldConfigurationDetails",
    "FieldConfigurationIssueTypeItem",
    "FieldConfigurationItem",
    "FieldConfigurationItemsDetails",
    "FieldConfigurationScheme",
    "FieldConfigurationSchemeProjectAssociation",
    "FieldConfigurationSchemeProjects",
    "FieldConfigurationToIssueTypeMapping",
    "Type5",
    "Auto",
    "Deprecated",
    "Orderable",
    "Searchable",
    "Operator2",
    "Operator3",
    "ManagedBy",
    "UsageType",
    "IsList",
    "SupportsListAndSingleValueOperators",
    "Type6",
    "Type7",
    "Type8",
    "Type9",
    "Status1",
    "Type10",
    "Attribute",
    "GlobalScope",
    "Type11",
    "GroupLabel",
    "GroupName",
    "Id",
    "IdOrKey",
    "InputStreamSource",
    "MultiSelectFieldOption",
    "IssueCommentListRequest",
    "SectionType",
    "IssueLayoutType",
    "IssueLimitReportResponse",
    "IssueLinkType",
    "Type12",
    "IssueTypeCreate",
    "IssueTypeIds",
    "IssueTypeIdsToRemove",
    "IssueTypeUpdate",
    "IssuesJqlMetaData",
    "IssuesMeta",
    "JExpEvaluateIssuesJqlMetaData",
    "JExpEvaluateIssuesMeta",
    "JQLCountRequest",
    "JQLCountResults",
    "Validation",
    "Type13",
    "JiraExpressionsComplexityValue",
    "Color1",
    "BulkEditMultiSelectFieldOption",
    "StatusCategory",
    "JqlFunctionPrecomputation",
    "JqlFunctionPrecomputationUpdate",
    "JqlFunctionPrecomputationUpdateRequest",
    "Query",
    "Operator4",
    "Type14",
    "Direction",
    "NumberType",
    "JsonNode",
    "JsonType",
    "LegacyJackson1ListColumnItem",
    "Plan",
    "ListWrapperCallbackApplicationRole",
    "ListWrapperCallbackGroupName",
    "Type15",
    "Position",
    "MoveField",
    "NotificationEvent",
    "NotificationSchemeAndProjectMappingJson",
    "OldToNewSecurityLevelMappings",
    "OperationMessage",
    "Position1",
    "PageBean2ComponentJson",
    "PageBean2JqlFunctionPrecomputation",
    "PageBeanFieldConfigurationDetails",
    "PageBeanFieldConfigurationIssueTypeItem",
    "PageBeanFieldConfigurationItem",
    "PageBeanFieldConfigurationScheme",
    "PageBeanFieldConfigurationSchemeProjects",
    "PageBeanNotificationSchemeAndProjectMappingJson",
    "PermissionHolder",
    "PermissionsKeys",
    "Priority",
    "PriorityId1",
    "AssigneeType3",
    "Style",
    "RealType",
    "Type17",
    "ProjectCategory",
    "AssigneeType4",
    "Type18",
    "State1",
    "ProjectField",
    "ProjectId",
    "ProjectIdentifier",
    "ProjectInsight",
    "ProjectLandingPageInfo",
    "ProjectTypeKey3",
    "ProjectPermissions",
    "ProjectRoleActorsUpdate",
    "Type19",
    "ProjectRoleGroup",
    "ProjectRoleUser",
    "ProjectScope",
    "ProjectTemplateKey1",
    "Type20",
    "PropertyKey",
    "PropertyKeys",
    "JobStatus",
    "ResolutionJson",
    "RichText",
    "Type21",
    "RoleActor",
    "Type22",
    "RuleConfiguration",
    "TemplateType",
    "Type23",
    "Type24",
    "SearchAndReconcileRequest",
    "ValidateQuery",
    "SearchRequest",
    "SecurityLevel",
    "Type25",
    "IsDefault",
    "SecurityScheme",
    "SecuritySchemeLevelMember",
    "ServiceManagementNavigationInfo",
    "Type26",
    "Type27",
    "SharePermissionInput",
    "SimpleApplicationProperty",
    "SimpleLink",
    "SimpleListWrapperGroupName",
    "SimplifiedHierarchyLevel",
    "SoftwareNavigationInfo",
    "StatusModel",
    "StatusCategory3",
    "StatusCategory4",
    "Category",
    "Type28",
    "StringList",
    "SuggestedMappingsForPrioritiesRequest",
    "SuggestedMappingsForProjectsRequest",
    "SuggestedMappingsRequest",
    "SwimlaneStrategy",
    "Status3",
    "TaskProgressBeanObject",
    "DefaultUnit",
    "TimeFormat",
    "TimeTrackingConfiguration",
    "Type29",
    "Type31",
    "ViewType",
    "UpdateDefaultProjectClassification",
    "UpdateFieldAssociationSchemeLinks",
    "UpdateFieldConfigurationSchemeDetails",
    "UpdateIssueSecuritySchemeRequest",
    "UpdatePrioritiesInSchemeRequest",
    "AssigneeType5",
    "UpdateProjectsInSchemeRequest",
    "UpdateUserToGroup",
    "UpdatedProjectCategory",
    "AccountType",
    "UserAvatarUrls",
    "UserDetails",
    "UserMigration",
    "Type33",
    "Level",
    "VersionApprover",
    "VersionIssuesStatus",
    "Position3",
    "VersionMove",
    "Type34",
    "VisibilityModel",
    "Event",
    "WorkManagementNavigationInfo",
    "EditorScope",
    "ProjectType1",
    "Operator5",
    "WorkflowDocumentVersion",
    "WorkflowId",
    "Type35",
    "WorkflowTransition",
    "WorkflowTransitionProperty",
    "Type37",
    "Type38",
    "WorklogIdsRequest",
    "WorklogsMoveRequest",
    "Type39",
    "TargetClassification",
    "TargetMandatoryFields",
    "TargetStatus",
    "TargetToSourcesMapping",
    "AppWorkflowTransitionRule",
    "ApplicationRole",
    "AssociateFieldConfigurationsWithIssueTypesRequest",
    "AttachmentArchive",
    "AuditRecord",
    "BulkPermissionsRequest",
    "BulkWorklogKeyRequest",
    "BulkWorklogKeyResponse",
    "ConnectWorkflowTransitionRule",
    "DataClassificationLevels",
    "FieldModel",
    "FoundGroup",
    "FoundGroups",
    "Hierarchy",
    "IssueFieldOptionScope",
    "JiraExpressionEvalContext",
    "JiraExpressionEvalRequest",
    "JiraExpressionEvaluateContext",
    "JiraExpressionEvaluateRequest",
    "JiraExpressionsComplexity",
    "LegacyJackson1ListUserMigration",
    "PageBean2ProjectField",
    "PageBeanResolutionJson",
    "PaginatedResponseComment",
    "PaginatedResponseFieldCreateMetadata",
    "PermissionGrant",
    "ProjectDetails",
    "Scope",
    "SecuritySchemeLevel",
    "SimpleListWrapperApplicationRole",
    "StatusDetails",
    "UpdatePrioritySchemeRequest",
    "User",
    "Version",
    "WorkflowSchemeProjectSwitch",
    "WorkflowTransitionRules",
    "WorkflowUpdateValidateRequest",
    "AddSecuritySchemeLevelsRequest",
    "FieldDetails",
    "IssueFieldOptionCreate",
    "IssueTypeDetails",
    "IssuesUpdate",
    "JExpEvaluateMetaData",
    "JiraExpressionEvaluationMetaData",
    "LegacyJackson1ListVersion",
    "PageBeanProjectDetails",
    "PaginatedResponseIssueTypeIssueCreateMetadata",
    "PermissionScheme",
    "ProjectComponent",
    "ProjectRole",
    "UpdatePrioritySchemeResponse",
    "BulkChangelogResponse",
    "EventNotification",
    "Issue",
    "JExpEvaluateJiraExpressionResult",
    "LegacyJackson1ListProjectComponent",
    "NotificationSchemeEvent",
    "Project",
    "SharePermission",
    "LegacyJackson1ListProject",
    "LinkIssueRequestJson",
    "NotificationScheme",
    "PageBeanProject",
]
