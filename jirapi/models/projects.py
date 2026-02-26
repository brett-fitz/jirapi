"""Pydantic models for the projects domain."""

from __future__ import annotations

from typing import Annotated, Any, Literal
from uuid import UUID

from pydantic import AnyUrl, BaseModel, ConfigDict, Field, RootModel

from jirapi.models._shared import OnConflict, ShowDaysInColumn


class ActorsMap(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    group: Annotated[
        list[str] | None,
        Field(
            description="The name of the group to add. This parameter cannot be used with the `groupId` parameter. As a group's name can change, use of `groupId` is recommended."
        ),
    ] = None
    group_id: Annotated[
        list[str] | None,
        Field(
            alias="groupId",
            description="The ID of the group to add. This parameter cannot be used with the `group` parameter.",
        ),
    ] = None
    user: Annotated[
        list[str] | None, Field(description="The user account ID of the user to add.")
    ] = None


class BoardFeaturePayload(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    feature_key: Annotated[
        FeatureKey | None, Field(alias="featureKey", description="The key of the feature")
    ] = None
    state: Annotated[
        State | None, Field(description="Whether the feature should be turned on or off")
    ] = None


class CardLayout(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    show_days_in_column: Annotated[
        ShowDaysInColumn,
        Field(alias="showDaysInColumn", description="Whether to show days in column"),
    ] = ShowDaysInColumn.boolean_false


class CardLayoutField(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    field_id: Annotated[str | None, Field(alias="fieldId")] = None
    id: int | None = None
    mode: Mode | None = None
    position: int | None = None


class ComponentIssuesCount(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    issue_count: Annotated[
        int | None,
        Field(
            alias="issueCount",
            description="The count of issues assigned to a component.",
        ),
    ] = None
    self: Annotated[
        AnyUrl | None, Field(description="The URL for this count of issues for a component.")
    ] = None


class CreateProjectDetails(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    assignee_type: Annotated[
        AssigneeType1 | None,
        Field(
            alias="assigneeType",
            description="The default assignee when creating issues for this project.",
        ),
    ] = None
    avatar_id: Annotated[
        int | None,
        Field(alias="avatarId", description="An integer value for the project's avatar."),
    ] = None
    category_id: Annotated[
        int | None,
        Field(
            alias="categoryId",
            description="The ID of the project's category. A complete list of category IDs is found using the [Get all project categories](#api-rest-api-3-projectCategory-get) operation.",
        ),
    ] = None
    description: Annotated[str | None, Field(description="A brief description of the project.")] = (
        None
    )
    field_configuration_scheme: Annotated[
        int | None,
        Field(
            alias="fieldConfigurationScheme",
            description="The ID of the field configuration scheme for the project. Use the [Get all field configuration schemes](#api-rest-api-3-fieldconfigurationscheme-get) operation to get a list of field configuration scheme IDs. If you specify the field configuration scheme you cannot specify the project template key.",
        ),
    ] = None
    issue_security_scheme: Annotated[
        int | None,
        Field(
            alias="issueSecurityScheme",
            description="The ID of the issue security scheme for the project, which enables you to control who can and cannot view issues. Use the [Get issue security schemes](#api-rest-api-3-issuesecurityschemes-get) resource to get all issue security scheme IDs.",
        ),
    ] = None
    issue_type_scheme: Annotated[
        int | None,
        Field(
            alias="issueTypeScheme",
            description="The ID of the issue type scheme for the project. Use the [Get all issue type schemes](#api-rest-api-3-issuetypescheme-get) operation to get a list of issue type scheme IDs. If you specify the issue type scheme you cannot specify the project template key.",
        ),
    ] = None
    issue_type_screen_scheme: Annotated[
        int | None,
        Field(
            alias="issueTypeScreenScheme",
            description="The ID of the issue type screen scheme for the project. Use the [Get all issue type screen schemes](#api-rest-api-3-issuetypescreenscheme-get) operation to get a list of issue type screen scheme IDs. If you specify the issue type screen scheme you cannot specify the project template key.",
        ),
    ] = None
    key: Annotated[
        str,
        Field(
            description="Project keys must be unique and start with an uppercase letter followed by one or more uppercase alphanumeric characters. The maximum length is 10 characters."
        ),
    ]
    lead: Annotated[
        str | None,
        Field(
            description="This parameter is deprecated because of privacy changes. Use `leadAccountId` instead. See the [migration guide](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-user-privacy-api-migration-guide/) for details. The user name of the project lead. Either `lead` or `leadAccountId` must be set when creating a project. Cannot be provided with `leadAccountId`."
        ),
    ] = None
    lead_account_id: Annotated[
        str | None,
        Field(
            alias="leadAccountId",
            description="The account ID of the project lead. Either `lead` or `leadAccountId` must be set when creating a project. Cannot be provided with `lead`.",
            max_length=128,
        ),
    ] = None
    name: Annotated[str, Field(description="The name of the project.")]
    notification_scheme: Annotated[
        int | None,
        Field(
            alias="notificationScheme",
            description="The ID of the notification scheme for the project. Use the [Get notification schemes](#api-rest-api-3-notificationscheme-get) resource to get a list of notification scheme IDs.",
        ),
    ] = None
    permission_scheme: Annotated[
        int | None,
        Field(
            alias="permissionScheme",
            description="The ID of the permission scheme for the project. Use the [Get all permission schemes](#api-rest-api-3-permissionscheme-get) resource to see a list of all permission scheme IDs.",
        ),
    ] = None
    project_template_key: Annotated[
        ProjectTemplateKey | None,
        Field(
            alias="projectTemplateKey",
            description="A predefined configuration for a project. The type of the `projectTemplateKey` must match with the type of the `projectTypeKey`.",
        ),
    ] = None
    project_type_key: Annotated[
        ProjectTypeKey | None,
        Field(
            alias="projectTypeKey",
            description="The [project type](https://confluence.atlassian.com/x/GwiiLQ#Jiraapplicationsoverview-Productfeaturesandprojecttypes), which defines the application-specific feature set. If you don't specify the project template you have to specify the project type.",
        ),
    ] = None
    url: Annotated[
        str | None,
        Field(
            description="A link to information about this project, such as project documentation"
        ),
    ] = None
    workflow_scheme: Annotated[
        int | None,
        Field(
            alias="workflowScheme",
            description="The ID of the workflow scheme for the project. Use the [Get all workflow schemes](#api-rest-api-3-workflowscheme-get) operation to get a list of workflow scheme IDs. If you specify the workflow scheme you cannot specify the project template key.",
        ),
    ] = None


class CustomFieldReplacement(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    custom_field_id: Annotated[
        int | None,
        Field(
            alias="customFieldId",
            description="The ID of the custom field in which to replace the version number.",
        ),
    ] = None
    move_to: Annotated[
        int | None,
        Field(
            alias="moveTo",
            description="The version number to use as a replacement for the deleted version.",
        ),
    ] = None


class CustomTemplateOptions(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    enable_screen_delegated_admin_support: Annotated[
        bool | None,
        Field(
            alias="enableScreenDelegatedAdminSupport",
            description="Enable screen delegated admin support for the template. This means screen and associated schemes will be copied rather than referenced.",
        ),
    ] = None
    enable_workflow_delegated_admin_support: Annotated[
        bool | None,
        Field(
            alias="enableWorkflowDelegatedAdminSupport",
            description="Enable workflow delegated admin support for the template. This means workflows and workflow schemes will be copied rather than referenced.",
        ),
    ] = None


class CustomTemplatesProjectDetails(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    access_level: Annotated[
        AccessLevel | None,
        Field(
            alias="accessLevel",
            description="The access level of the project. Only used by team-managed project",
            examples=["private"],
        ),
    ] = None
    additional_properties: Annotated[
        dict[str, str] | None,
        Field(
            alias="additionalProperties",
            description="Additional properties of the project",
        ),
    ] = None
    assignee_type: Annotated[
        AssigneeType2 | None,
        Field(
            alias="assigneeType",
            description="The default assignee when creating issues in the project",
            examples=["PROJECT_LEAD"],
        ),
    ] = None
    avatar_id: Annotated[
        int | None,
        Field(
            alias="avatarId",
            description="The ID of the project's avatar. Use the \\[Get project avatars\\](\\#api-rest-api-3-project-projectIdOrKey-avatar-get) operation to list the available avatars in a project.",
            examples=[10200],
        ),
    ] = None
    category_id: Annotated[
        int | None,
        Field(
            alias="categoryId",
            description="The ID of the project's category. A complete list of category IDs is found using the [Get all project categories](#api-rest-api-3-projectCategory-get) operation.",
        ),
    ] = None
    description: Annotated[
        str | None,
        Field(
            description="Brief description of the project",
            examples=["This is a project for Foo Bar"],
        ),
    ] = None
    enable_components: Annotated[
        bool,
        Field(
            alias="enableComponents",
            description="Whether components are enabled for the project. Only used by company-managed project",
            examples=[False],
        ),
    ] = False
    key: Annotated[
        str | None,
        Field(
            description="Project keys must be unique and start with an uppercase letter followed by one or more uppercase alphanumeric characters. The maximum length is 10 characters.",
            examples=["PRJ"],
        ),
    ] = None
    language: Annotated[
        str | None, Field(description="The default language for the project", examples=["en"])
    ] = None
    lead_account_id: Annotated[
        str | None,
        Field(
            alias="leadAccountId",
            description="The account ID of the project lead. Either `lead` or `leadAccountId` must be set when creating a project. Cannot be provided with `lead`.",
            examples=["1234567890"],
        ),
    ] = None
    name: Annotated[
        str | None, Field(description="Name of the project", examples=["Project Foo Bar"])
    ] = None
    url: Annotated[
        str | None,
        Field(
            description="A link to information about this project, such as project documentation",
            examples=["https://www.example.com"],
        ),
    ] = None


class EditTemplateRequest(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    template_description: Annotated[
        str | None,
        Field(
            alias="templateDescription",
            description="The description of the template",
            max_length=150,
        ),
    ] = None
    template_generation_options: Annotated[
        CustomTemplateOptions | None, Field(alias="templateGenerationOptions")
    ] = None
    template_key: Annotated[
        str | None, Field(alias="templateKey", description="The unique identifier of the template")
    ] = None
    template_name: Annotated[
        str | None,
        Field(alias="templateName", description="The name of the template", max_length=50),
    ] = None


class IssueTypeInfo(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    avatar_id: Annotated[
        int | None, Field(alias="avatarId", description="The avatar of the issue type.")
    ] = None
    id: Annotated[int | None, Field(description="The ID of the issue type.")] = None
    name: Annotated[str | None, Field(description="The name of the issue type.")] = None


class NonWorkingDay(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    id: int | None = None
    iso8601_date: Annotated[str | None, Field(alias="iso8601Date")] = None


class NotificationSchemeEventIDPayload(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    id: Annotated[
        str | None,
        Field(
            description="The event ID to use for reference in the payload",
            examples=["1"],
        ),
    ] = None


class NotificationSchemeNotificationDetailsPayload(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    notification_type: Annotated[
        str | None, Field(alias="notificationType", description="The type of notification.")
    ] = None
    parameter: Annotated[
        str | None,
        Field(
            description="The parameter of the notification, should be eiither null if not required, or PCRI."
        ),
    ] = None


class ProjectArchetype(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    real_type: Annotated[RealType | None, Field(alias="realType")] = None
    style: Style | None = None
    type: Type17 | None = None


class ProjectAvatars(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    custom: Annotated[
        list[Avatar] | None,
        Field(description="List of avatars added to Jira. These avatars may be deleted."),
    ] = None
    system: Annotated[
        list[Avatar] | None,
        Field(description="List of avatars included with Jira. These avatars cannot be deleted."),
    ] = None


class ProjectCreateResourceIdentifier(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    an_id: Annotated[bool | None, Field(alias="anID")] = None
    areference: bool | None = None
    entity_id: Annotated[str | None, Field(alias="entityId")] = None
    entity_type: Annotated[str | None, Field(alias="entityType")] = None
    id: str | None = None
    type: Type18 | None = None


class ProjectEmailAddress(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    email_address: Annotated[
        str | None, Field(alias="emailAddress", description="The email address.")
    ] = None
    email_address_status: Annotated[
        list[str] | None,
        Field(
            alias="emailAddressStatus",
            description="When using a custom domain, the status of the email address.",
        ),
    ] = None


class ProjectFeature(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    feature: Annotated[str | None, Field(description="The key of the feature.")] = None
    image_uri: Annotated[
        str | None,
        Field(alias="imageUri", description="URI for the image representing the feature."),
    ] = None
    localised_description: Annotated[
        str | None,
        Field(
            alias="localisedDescription",
            description="Localized display description for the feature.",
        ),
    ] = None
    localised_name: Annotated[
        str | None,
        Field(alias="localisedName", description="Localized display name for the feature."),
    ] = None
    prerequisites: Annotated[
        list[str] | None,
        Field(description="List of keys of the features required to enable the feature."),
    ] = None
    project_id: Annotated[
        int | None, Field(alias="projectId", description="The ID of the project.")
    ] = None
    state: Annotated[
        State1 | None,
        Field(
            description="The state of the feature. When updating the state of a feature, only ENABLED and DISABLED are supported. Responses can contain all values"
        ),
    ] = None
    toggle_locked: Annotated[
        bool | None,
        Field(
            alias="toggleLocked",
            description="Whether the state of the feature can be updated.",
        ),
    ] = None


class ProjectFeatureState(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    state: Annotated[State1 | None, Field(description="The feature state.")] = None


class ProjectIdentifiers(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    id: Annotated[int, Field(description="The ID of the created project.")]
    key: Annotated[str, Field(description="The key of the created project.")]
    self: Annotated[AnyUrl, Field(description="The URL of the created project.")]


class ProjectIssueTypesHierarchyLevel(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    entity_id: Annotated[
        UUID | None,
        Field(
            alias="entityId",
            description="The ID of the issue type hierarchy level. This property is deprecated, see [Change notice: Removing hierarchy level IDs from next-gen APIs](https://developer.atlassian.com/cloud/jira/platform/change-notice-removing-hierarchy-level-ids-from-next-gen-apis/).",
        ),
    ] = None
    issue_types: Annotated[
        list[IssueTypeInfo] | None,
        Field(
            alias="issueTypes",
            description="The list of issue types in the hierarchy level.",
        ),
    ] = None
    level: Annotated[
        int | None, Field(description="The level of the issue type hierarchy level.")
    ] = None
    name: Annotated[
        str | None, Field(description="The name of the issue type hierarchy level.")
    ] = None


class ProjectPayload(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    field_layout_scheme_id: Annotated[
        ProjectCreateResourceIdentifier | None, Field(alias="fieldLayoutSchemeId")
    ] = None
    issue_security_scheme_id: Annotated[
        ProjectCreateResourceIdentifier | None, Field(alias="issueSecuritySchemeId")
    ] = None
    issue_type_scheme_id: Annotated[
        ProjectCreateResourceIdentifier | None, Field(alias="issueTypeSchemeId")
    ] = None
    issue_type_screen_scheme_id: Annotated[
        ProjectCreateResourceIdentifier | None, Field(alias="issueTypeScreenSchemeId")
    ] = None
    notification_scheme_id: Annotated[
        ProjectCreateResourceIdentifier | None, Field(alias="notificationSchemeId")
    ] = None
    pcri: ProjectCreateResourceIdentifier | None = None
    permission_scheme_id: Annotated[
        ProjectCreateResourceIdentifier | None, Field(alias="permissionSchemeId")
    ] = None
    project_type_key: Annotated[
        ProjectTypeKey3 | None,
        Field(
            alias="projectTypeKey",
            description="The [project type](https://confluence.atlassian.com/x/GwiiLQ#Jiraapplicationsoverview-Productfeaturesandprojecttypes), which defines the application-specific feature set. If you don't specify the project template you have to specify the project type.",
            examples=["software"],
        ),
    ] = None
    workflow_scheme_id: Annotated[
        ProjectCreateResourceIdentifier | None, Field(alias="workflowSchemeId")
    ] = None


class ProjectTemplateModel(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    archetype: ProjectArchetype | None = None
    default_board_view: Annotated[str | None, Field(alias="defaultBoardView")] = None
    description: str | None = None
    live_template_project_id_reference: Annotated[
        int | None, Field(alias="liveTemplateProjectIdReference")
    ] = None
    name: str | None = None
    project_template_key: Annotated[
        ProjectTemplateKey1 | None, Field(alias="projectTemplateKey")
    ] = None
    snapshot_template: Annotated[dict[str, Any] | None, Field(alias="snapshotTemplate")] = None
    template_generation_options: Annotated[
        CustomTemplateOptions | None, Field(alias="templateGenerationOptions")
    ] = None
    type: Type20 | None = None


class ProjectType(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    color: Annotated[str | None, Field(description="The color of the project type.")] = None
    description_i18n_key: Annotated[
        str | None,
        Field(
            alias="descriptionI18nKey",
            description="The key of the project type's description.",
        ),
    ] = None
    formatted_key: Annotated[
        str | None,
        Field(alias="formattedKey", description="The formatted key of the project type."),
    ] = None
    icon: Annotated[str | None, Field(description="The icon of the project type.")] = None
    key: Annotated[str | None, Field(description="The key of the project type.")] = None


class QuickFilterPayload(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    description: Annotated[str | None, Field(description="The description of the quick filter")] = (
        None
    )
    jql_query: Annotated[
        str | None, Field(alias="jqlQuery", description="The jql query for the quick filter")
    ] = None
    name: Annotated[str | None, Field(description="The name of the quick filter")] = None


class RolePayload(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    default_actors: Annotated[
        list[ProjectCreateResourceIdentifier] | None,
        Field(
            alias="defaultActors",
            description="The default actors for the role. By adding default actors, the role will be added to any future projects created",
            examples=["[pcri:user:id:1234]"],
        ),
    ] = None
    description: Annotated[str | None, Field(description="The description of the role")] = None
    name: Annotated[str | None, Field(description="The name of the role")] = None
    on_conflict: Annotated[
        OnConflict,
        Field(
            alias="onConflict",
            description="The strategy to use when there is a conflict with an existing project role. FAIL - Fail execution, this always needs to be unique; USE - Use the existing entity and ignore new entity parameters",
        ),
    ] = OnConflict.use
    pcri: ProjectCreateResourceIdentifier | None = None
    type: Annotated[
        Type22 | None,
        Field(
            description="The type of the role. Only used by project-scoped project",
            examples=["EDITABLE"],
        ),
    ] = None


class RolesCapabilityPayload(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    role_to_project_actors: Annotated[
        dict[str, list[ProjectCreateResourceIdentifier]] | None,
        Field(
            alias="roleToProjectActors",
            description="A map of role PCRI (can be ID or REF) to a list of user or group PCRI IDs to associate with the role and project.",
        ),
    ] = None
    roles: Annotated[
        list[RolePayload] | None, Field(description="The list of roles to create.")
    ] = None


class RulePayload(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    parameters: Annotated[
        dict[str, str] | None, Field(description="The parameters of the rule")
    ] = None
    rule_key: Annotated[
        str | None,
        Field(
            alias="ruleKey",
            description="The key of the rule. See https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-workflows/\\#api-rest-api-3-workflows-capabilities-get",
            examples=["system:update-field"],
        ),
    ] = None


class SaveProjectTemplateRequest(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    project_id: Annotated[
        int | None, Field(alias="projectId", description="The ID of the target project")
    ] = None
    template_generation_options: Annotated[
        CustomTemplateOptions | None, Field(alias="templateGenerationOptions")
    ] = None
    template_type: Annotated[
        TemplateType | None,
        Field(
            alias="templateType",
            description="The type of the template: LIVE | SNAPSHOT",
        ),
    ] = None


class SaveTemplateRequest(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    template_description: Annotated[
        str | None,
        Field(
            alias="templateDescription",
            description="The description of the template",
            max_length=150,
        ),
    ] = None
    template_from_project_request: Annotated[
        SaveProjectTemplateRequest | None, Field(alias="templateFromProjectRequest")
    ] = None
    template_name: Annotated[
        str | None,
        Field(alias="templateName", description="The name of the template", max_length=50),
    ] = None


class SaveTemplateResponse(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    project_template_key: Annotated[
        ProjectTemplateKey1 | None, Field(alias="projectTemplateKey")
    ] = None


class ScopePayload(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    type: Annotated[
        Type24 | None,
        Field(
            description="The type of the scope. Use `GLOBAL` or empty for company-managed project, and `PROJECT` for team-managed project"
        ),
    ] = None


class ScreenSchemePayload(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    default_screen: Annotated[
        ProjectCreateResourceIdentifier | None, Field(alias="defaultScreen")
    ] = None
    description: Annotated[
        str | None,
        Field(
            description="The description of the screen scheme",
            examples=["This is a screen scheme"],
        ),
    ] = None
    name: Annotated[
        str | None,
        Field(description="The name of the screen scheme", examples=["My Screen Scheme"]),
    ] = None
    pcri: ProjectCreateResourceIdentifier | None = None
    screens: Annotated[
        dict[str, ProjectCreateResourceIdentifier] | None,
        Field(
            description="Similar to the field layout scheme those mappings allow users to set different screens for different operations: default - always there, applied to all operations that don't have an explicit mapping `create`, `view`, `edit` - specific operations that are available and users can assign a different screen for each one of them https://support.atlassian.com/jira-cloud-administration/docs/manage-screen-schemes/\\#Associating-a-screen-with-an-issue-operation"
        ),
    ] = None


class SecurityLevelMemberPayload(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    parameter: Annotated[
        str | None,
        Field(
            description='Defines the value associated with the type. For reporter this would be \\{"null"\\}; for users this would be the names of specific users); for group this would be group names like \\{"administrators", "jira-administrators", "jira-users"\\}'
        ),
    ] = None
    type: Annotated[Type25 | None, Field(description="The type of the security level member")] = (
        None
    )


class SecurityLevelPayload(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    description: Annotated[
        str | None,
        Field(
            description="The description of the security level",
            examples=["Newly created issue security level"],
        ),
    ] = None
    is_default: Annotated[
        IsDefault | None,
        Field(
            alias="isDefault",
            description="Whether the security level is default for the security scheme",
        ),
    ] = None
    name: Annotated[
        str | None,
        Field(
            description="The name of the security level",
            examples=["New Security Level"],
        ),
    ] = None
    security_level_members: Annotated[
        list[SecurityLevelMemberPayload] | None,
        Field(
            alias="securityLevelMembers",
            description="The members of the security level",
        ),
    ] = None


class SecuritySchemePayload(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    description: Annotated[
        str | None,
        Field(
            description="The description of the security scheme",
            examples=["Newly created issue security scheme"],
        ),
    ] = None
    name: Annotated[
        str | None,
        Field(
            description="The name of the security scheme",
            examples=["New Security Scheme"],
        ),
    ] = None
    pcri: ProjectCreateResourceIdentifier | None = None
    security_levels: Annotated[
        list[SecurityLevelPayload] | None,
        Field(
            alias="securityLevels",
            description="The security levels for the security scheme",
        ),
    ] = None


class StatusPayload(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    description: Annotated[str | None, Field(description="The description of the status")] = None
    name: Annotated[str | None, Field(description="The name of the status")] = None
    on_conflict: Annotated[
        OnConflict | None,
        Field(
            alias="onConflict",
            description="The conflict strategy for the status already exists. FAIL - Fail execution, this always needs to be unique; USE - Use the existing entity and ignore new entity parameters; NEW - Create a new entity",
        ),
    ] = None
    pcri: ProjectCreateResourceIdentifier | None = None
    status_category: Annotated[
        StatusCategory4 | None,
        Field(
            alias="statusCategory",
            description="The status category of the status. The value is case-sensitive.",
        ),
    ] = None


class SwimlanePayload(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    description: Annotated[str | None, Field(description="The description of the quick filter")] = (
        None
    )
    jql_query: Annotated[
        str | None, Field(alias="jqlQuery", description="The jql query for the quick filter")
    ] = None
    name: Annotated[str | None, Field(description="The name of the quick filter")] = None


class SwimlanesPayload(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    custom_swimlanes: Annotated[
        list[SwimlanePayload] | None,
        Field(alias="customSwimlanes", description="The custom swimlane definitions."),
    ] = None
    default_custom_swimlane_name: Annotated[
        str | None,
        Field(
            alias="defaultCustomSwimlaneName",
            description="The name of the custom swimlane to use for work items that don't match any other swimlanes.",
        ),
    ] = None
    swimlane_strategy: Annotated[
        SwimlaneStrategy | None,
        Field(alias="swimlaneStrategy", description="The swimlane strategy for the board."),
    ] = None


class TabPayload(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    fields: Annotated[
        list[ProjectCreateResourceIdentifier] | None,
        Field(
            description="The list of resource identifier of the field associated to the tab. See https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-screen-tab-fields/\\#api-rest-api-3-screens-screenid-tabs-tabid-fields-post"
        ),
    ] = None
    name: Annotated[str | None, Field(description="The name of the tab")] = None


class ToLayoutPayload(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    port: Annotated[
        int | None,
        Field(
            description="Defines where the transition line will be connected to a status. Port 0 to 7 are acceptable values.",
            examples=[1],
        ),
    ] = None
    status: ProjectCreateResourceIdentifier | None = None


class UpdateProjectDetails(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    assignee_type: Annotated[
        AssigneeType5 | None,
        Field(
            alias="assigneeType",
            description="The default assignee when creating issues for this project.",
        ),
    ] = None
    avatar_id: Annotated[
        int | None,
        Field(alias="avatarId", description="An integer value for the project's avatar."),
    ] = None
    category_id: Annotated[
        int | None,
        Field(
            alias="categoryId",
            description="The ID of the project's category. A complete list of category IDs is found using the [Get all project categories](#api-rest-api-3-projectCategory-get) operation. To remove the project category from the project, set the value to `-1.`",
        ),
    ] = None
    description: Annotated[str | None, Field(description="A brief description of the project.")] = (
        None
    )
    issue_security_scheme: Annotated[
        int | None,
        Field(
            alias="issueSecurityScheme",
            description="The ID of the issue security scheme for the project, which enables you to control who can and cannot view issues. Use the [Get issue security schemes](#api-rest-api-3-issuesecurityschemes-get) resource to get all issue security scheme IDs.",
        ),
    ] = None
    key: Annotated[
        str | None,
        Field(
            description="Project keys must be unique and start with an uppercase letter followed by one or more uppercase alphanumeric characters. The maximum length is 10 characters."
        ),
    ] = None
    lead: Annotated[
        str | None,
        Field(
            description="This parameter is deprecated because of privacy changes. Use `leadAccountId` instead. See the [migration guide](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-user-privacy-api-migration-guide/) for details. The user name of the project lead. Cannot be provided with `leadAccountId`."
        ),
    ] = None
    lead_account_id: Annotated[
        str | None,
        Field(
            alias="leadAccountId",
            description="The account ID of the project lead. Cannot be provided with `lead`.",
            max_length=128,
        ),
    ] = None
    name: Annotated[str | None, Field(description="The name of the project.")] = None
    notification_scheme: Annotated[
        int | None,
        Field(
            alias="notificationScheme",
            description="The ID of the notification scheme for the project. Use the [Get notification schemes](#api-rest-api-3-notificationscheme-get) resource to get a list of notification scheme IDs.",
        ),
    ] = None
    permission_scheme: Annotated[
        int | None,
        Field(
            alias="permissionScheme",
            description="The ID of the permission scheme for the project. Use the [Get all permission schemes](#api-rest-api-3-permissionscheme-get) resource to see a list of all permission scheme IDs.",
        ),
    ] = None
    released_project_keys: Annotated[
        list[str] | None,
        Field(
            alias="releasedProjectKeys",
            description="Previous project keys to be released from the current project. Released keys must belong to the current project and not contain the current project key",
        ),
    ] = None
    url: Annotated[
        str | None,
        Field(
            description="A link to information about this project, such as project documentation"
        ),
    ] = None


class VersionRelatedWork(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    category: Annotated[str, Field(description="The category of the related work")]
    issue_id: Annotated[
        int | None,
        Field(
            alias="issueId",
            description="The ID of the issue associated with the related work (if there is one). Cannot be updated via the Rest API.",
        ),
    ] = None
    related_work_id: Annotated[
        str | None,
        Field(
            alias="relatedWorkId",
            description="The id of the related work. For the native release note related work item, this will be null, and Rest API does not support updating it.",
        ),
    ] = None
    title: Annotated[str | None, Field(description="The title of the related work")] = None
    url: Annotated[
        AnyUrl | None,
        Field(
            description="The URL of the related work. Will be null for the native release note related work item, but is otherwise required."
        ),
    ] = None


class VersionUnresolvedIssuesCount(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    issues_count: Annotated[
        int | None, Field(alias="issuesCount", description="Count of issues.")
    ] = None
    issues_unresolved_count: Annotated[
        int | None, Field(alias="issuesUnresolvedCount", description="Count of unresolved issues.")
    ] = None
    self: Annotated[AnyUrl | None, Field(description="The URL of these count details.")] = None


class VersionUsageInCustomField(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    custom_field_id: Annotated[
        int | None, Field(alias="customFieldId", description="The ID of the custom field.")
    ] = None
    field_name: Annotated[
        str | None, Field(alias="fieldName", description="The name of the custom field.")
    ] = None
    issue_count_with_version_in_custom_field: Annotated[
        int | None,
        Field(
            alias="issueCountWithVersionInCustomField",
            description="Count of the issues where the custom field contains the version.",
        ),
    ] = None


class WorkflowSchemePayload(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    default_workflow: Annotated[
        ProjectCreateResourceIdentifier | None, Field(alias="defaultWorkflow")
    ] = None
    description: Annotated[
        str | None, Field(description="The description of the workflow scheme")
    ] = None
    explicit_mappings: Annotated[
        dict[str, ProjectCreateResourceIdentifier] | None,
        Field(
            alias="explicitMappings",
            description="Association between issuetypes and workflows",
        ),
    ] = None
    name: Annotated[str | None, Field(description="The name of the workflow scheme")] = None
    pcri: ProjectCreateResourceIdentifier | None = None


class WorkflowStatusLayoutPayload(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    x: Annotated[
        float | None, Field(description="The x coordinate of the status.", examples=[1])
    ] = None
    y: Annotated[
        float | None, Field(description="The y coordinate of the status.", examples=[2])
    ] = None


class WorkflowStatusPayload(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    layout: WorkflowStatusLayoutPayload | None = None
    pcri: ProjectCreateResourceIdentifier | None = None
    properties: Annotated[
        dict[str, str] | None, Field(description="The properties of the workflow status.")
    ] = None


class WorkingDaysConfig(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    friday: bool | None = None
    id: int | None = None
    monday: bool | None = None
    non_working_days: Annotated[list[NonWorkingDay] | None, Field(alias="nonWorkingDays")] = None
    saturday: bool | None = None
    sunday: bool | None = None
    thursday: bool | None = None
    timezone_id: Annotated[str | None, Field(alias="timezoneId")] = None
    tuesday: bool | None = None
    wednesday: bool | None = None


class BoardColumnPayload(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    maximum_issue_constraint: Annotated[
        int | None,
        Field(
            alias="maximumIssueConstraint",
            description="The maximum issue constraint for the column",
        ),
    ] = None
    minimum_issue_constraint: Annotated[
        int | None,
        Field(
            alias="minimumIssueConstraint",
            description="The minimum issue constraint for the column",
        ),
    ] = None
    name: Annotated[str | None, Field(description="The name of the column", examples=["TODO"])] = (
        None
    )
    status_ids: Annotated[
        list[ProjectCreateResourceIdentifier] | None,
        Field(
            alias="statusIds",
            description="The status IDs for the column",
            examples=["pcri:status:ref:done"],
        ),
    ] = None


class BoardPayload(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    board_filter_jql: Annotated[
        str | None,
        Field(
            alias="boardFilterJQL",
            description="Takes in a JQL string to create a new filter. If no value is provided, it'll default to a JQL filter for the project creating",
            examples=["project = 'My Project'"],
        ),
    ] = None
    card_color_strategy: Annotated[
        CardColorStrategy | None,
        Field(alias="cardColorStrategy", description="Card color settings of the board"),
    ] = None
    card_layout: Annotated[CardLayout | None, Field(alias="cardLayout")] = None
    card_layouts: Annotated[
        list[CardLayoutField] | None,
        Field(alias="cardLayouts", description="Card layout settings of the board"),
    ] = None
    columns: Annotated[
        list[BoardColumnPayload] | None, Field(description="The columns of the board")
    ] = None
    features: Annotated[
        list[BoardFeaturePayload] | None, Field(description="Feature settings for the board")
    ] = None
    name: Annotated[str | None, Field(description="The name of the board")] = None
    pcri: ProjectCreateResourceIdentifier | None = None
    quick_filters: Annotated[
        list[QuickFilterPayload] | None,
        Field(alias="quickFilters", description="The quick filters for the board."),
    ] = None
    supports_sprint: Annotated[
        bool,
        Field(
            alias="supportsSprint",
            description="Whether sprints are supported on the board",
        ),
    ] = True
    swimlanes: SwimlanesPayload | None = None
    working_days_config: Annotated[WorkingDaysConfig | None, Field(alias="workingDaysConfig")] = (
        None
    )


class BoardsPayload(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    boards: Annotated[
        list[BoardPayload] | None,
        Field(description="The boards to be associated with the project."),
    ] = None


class ConditionGroupPayload(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    condition_group: Annotated[
        list[ConditionGroupPayload] | None,
        Field(
            alias="conditionGroup",
            description="The nested conditions of the condition group.",
        ),
    ] = None
    conditions: Annotated[
        list[RulePayload] | None, Field(description="The rules for this condition.")
    ] = None
    operation: Annotated[
        Operation | None,
        Field(
            description="Determines how the conditions in the group are evaluated. Accepts either `ANY` or `ALL`. If `ANY` is used, at least one condition in the group must be true for the group to evaluate to true. If `ALL` is used, all conditions in the group must be true for the group to evaluate to true."
        ),
    ] = None


class ContainerForProjectFeatures(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    features: Annotated[list[ProjectFeature] | None, Field(description="The project features.")] = (
        None
    )


class CustomFieldPayload(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    cf_type: Annotated[
        str | None,
        Field(
            alias="cfType",
            description="The type of the custom field",
            examples=[
                "See https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-fields/#api-rest-api-3-field-post `type` for values"
            ],
        ),
    ] = None
    description: Annotated[
        str | None,
        Field(
            description="The description of the custom field",
            examples=["This is a custom field"],
        ),
    ] = None
    name: Annotated[
        str | None, Field(description="The name of the custom field", examples=["My Custom Field"])
    ] = None
    on_conflict: Annotated[
        OnConflict | None,
        Field(
            alias="onConflict",
            description="The strategy to use when there is a conflict with an existing custom field. FAIL - Fail execution, this always needs to be unique; USE - Use the existing entity and ignore new entity parameters",
        ),
    ] = None
    pcri: ProjectCreateResourceIdentifier | None = None
    scope: Annotated[
        Scope1 | None,
        Field(
            description="Allows an overwrite to declare the new Custom Field to be created as a GLOBAL-scoped field. Leave this as empty or null to use the project's default scope."
        ),
    ] = None
    searcher_key: Annotated[
        str | None,
        Field(
            alias="searcherKey",
            description="The searcher key of the custom field",
            examples=[
                "See https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-fields/#api-rest-api-3-field-post `searcherKey` for values"
            ],
        ),
    ] = None


class FieldLayoutConfiguration(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    field: Annotated[bool | None, Field(description="Whether to show the field")] = None
    pcri: ProjectCreateResourceIdentifier | None = None
    required: Annotated[bool | None, Field(description="Whether the field is required")] = None


class FieldLayoutPayload(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    configuration: Annotated[
        list[FieldLayoutConfiguration] | None,
        Field(
            description="The field layout configuration. See https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-field-configurations/\\#api-rest-api-3-fieldconfiguration-post"
        ),
    ] = None
    description: Annotated[
        str | None,
        Field(
            description="The description of the field layout",
            examples=["This is a field layout"],
        ),
    ] = None
    name: Annotated[
        str | None, Field(description="The name of the field layout", examples=["My Field Layout"])
    ] = None
    pcri: ProjectCreateResourceIdentifier | None = None


class FieldLayoutSchemePayload(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    default_field_layout: Annotated[
        ProjectCreateResourceIdentifier | None, Field(alias="defaultFieldLayout")
    ] = None
    description: Annotated[
        str | None,
        Field(
            description="The description of the field layout scheme",
            examples=["This is a field layout scheme"],
        ),
    ] = None
    explicit_mappings: Annotated[
        dict[str, ProjectCreateResourceIdentifier] | None,
        Field(
            alias="explicitMappings",
            description='There is a default configuration "fieldlayout" that is applied to all issue types using this scheme that don\'t have an explicit mapping users can create (or re-use existing) configurations for other issue types and map them to this scheme',
        ),
    ] = None
    name: Annotated[
        str | None,
        Field(
            description="The name of the field layout scheme",
            examples=["My Field Layout Scheme"],
        ),
    ] = None
    pcri: ProjectCreateResourceIdentifier | None = None


class FromLayoutPayload(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    from_port: Annotated[
        int | None,
        Field(
            alias="fromPort",
            description="The port that the transition can be made from",
        ),
    ] = None
    status: ProjectCreateResourceIdentifier | None = None
    to_port_override: Annotated[
        int | None,
        Field(alias="toPortOverride", description="The port that the transition goes to"),
    ] = None


class IssueLayoutItemPayload(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    item_key: Annotated[ProjectCreateResourceIdentifier | None, Field(alias="itemKey")] = None
    properties: Annotated[
        dict[str, Any] | None,
        Field(
            description="Additional properties for this item. This field is only used when the type is FIELD."
        ),
    ] = None
    section_type: Annotated[
        SectionType | None, Field(alias="sectionType", description="The item section type")
    ] = None
    type: Annotated[
        Literal["FIELD"] | None, Field(description="The item type. Currently only support FIELD")
    ] = None


class IssueLayoutPayload(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    container_id: Annotated[ProjectCreateResourceIdentifier | None, Field(alias="containerId")] = (
        None
    )
    issue_layout_type: Annotated[
        IssueLayoutType | None, Field(alias="issueLayoutType", description="The issue layout type")
    ] = None
    items: Annotated[
        list[IssueLayoutItemPayload] | None,
        Field(description="The configuration of items in the issue layout"),
    ] = None
    pcri: ProjectCreateResourceIdentifier | None = None


class IssueTypeHierarchyPayload(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    hierarchy_level: Annotated[
        int | None,
        Field(
            alias="hierarchyLevel",
            description="The hierarchy level of the issue type. 0, 1, 2, 3 .. n; Negative values for subtasks",
        ),
    ] = None
    name: Annotated[str | None, Field(description="The name of the issue type")] = None
    on_conflict: Annotated[
        OnConflict | None,
        Field(
            alias="onConflict",
            description="The conflict strategy to use when the issue type already exists. FAIL - Fail execution, this always needs to be unique; USE - Use the existing entity and ignore new entity parameters",
        ),
    ] = None
    pcri: ProjectCreateResourceIdentifier | None = None


class IssueTypePayload(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    avatar_id: Annotated[
        int | None,
        Field(
            alias="avatarId",
            description="The avatar ID of the issue type. Go to https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-avatars/\\#api-rest-api-3-avatar-type-system-get to choose an avatarId existing in Jira",
        ),
    ] = None
    description: Annotated[str | None, Field(description="The description of the issue type")] = (
        None
    )
    hierarchy_level: Annotated[
        int | None,
        Field(
            alias="hierarchyLevel",
            description="The hierarchy level of the issue type. 0, 1, 2, 3 .. n; Negative values for subtasks",
        ),
    ] = None
    name: Annotated[str | None, Field(description="The name of the issue type")] = None
    on_conflict: Annotated[
        OnConflict | None,
        Field(
            alias="onConflict",
            description="The conflict strategy to use when the issue type already exists. FAIL - Fail execution, this always needs to be unique; USE - Use the existing entity and ignore new entity parameters",
        ),
    ] = None
    pcri: ProjectCreateResourceIdentifier | None = None


class IssueTypeSchemePayload(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    default_issue_type_id: Annotated[
        ProjectCreateResourceIdentifier | None, Field(alias="defaultIssueTypeId")
    ] = None
    description: Annotated[
        str | None, Field(description="The description of the issue type scheme")
    ] = None
    issue_type_ids: Annotated[
        list[ProjectCreateResourceIdentifier] | None,
        Field(
            alias="issueTypeIds",
            description="The issue type IDs for the issue type scheme",
            examples=["pcri:issueType:id:10001"],
        ),
    ] = None
    name: Annotated[str | None, Field(description="The name of the issue type scheme")] = None
    pcri: ProjectCreateResourceIdentifier | None = None


class IssueTypeScreenSchemePayload(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    default_screen_scheme: Annotated[
        ProjectCreateResourceIdentifier | None, Field(alias="defaultScreenScheme")
    ] = None
    description: Annotated[
        str | None,
        Field(
            description="The description of the issue type screen scheme",
            examples=["This is an issue type screen scheme"],
        ),
    ] = None
    explicit_mappings: Annotated[
        dict[str, ProjectCreateResourceIdentifier] | None,
        Field(
            alias="explicitMappings",
            description="The IDs of the screen schemes for the issue type IDs and default. A default entry is required to create an issue type screen scheme, it defines the mapping for all issue types without a screen scheme.",
        ),
    ] = None
    name: Annotated[
        str | None,
        Field(
            description="The name of the issue type screen scheme",
            examples=["My Issue Type Screen Scheme"],
        ),
    ] = None
    pcri: ProjectCreateResourceIdentifier | None = None


class LegacyJackson1ListProjectType(RootModel[list[ProjectType]]):
    root: list[ProjectType]


class NotificationSchemeEventPayload(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    event: NotificationSchemeEventIDPayload | None = None
    notifications: Annotated[
        list[NotificationSchemeNotificationDetailsPayload] | None,
        Field(description="The configuration for notification recipents"),
    ] = None


class NotificationSchemePayload(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    description: Annotated[
        str | None, Field(description="The description of the notification scheme")
    ] = None
    name: Annotated[str | None, Field(description="The name of the notification scheme")] = None
    notification_scheme_events: Annotated[
        list[NotificationSchemeEventPayload] | None,
        Field(
            alias="notificationSchemeEvents",
            description="The events and notifications for the notification scheme",
        ),
    ] = None
    on_conflict: Annotated[
        OnConflict | None,
        Field(
            alias="onConflict",
            description="The strategy to use when there is a conflict with an existing entity",
        ),
    ] = None
    pcri: ProjectCreateResourceIdentifier | None = None


class PermissionGrantDTO(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    application_access: Annotated[list[str] | None, Field(alias="applicationAccess")] = None
    group_custom_fields: Annotated[
        list[ProjectCreateResourceIdentifier] | None, Field(alias="groupCustomFields")
    ] = None
    groups: list[ProjectCreateResourceIdentifier] | None = None
    permission_keys: Annotated[list[str] | None, Field(alias="permissionKeys")] = None
    project_roles: Annotated[
        list[ProjectCreateResourceIdentifier] | None, Field(alias="projectRoles")
    ] = None
    special_grants: Annotated[list[str] | None, Field(alias="specialGrants")] = None
    user_custom_fields: Annotated[
        list[ProjectCreateResourceIdentifier] | None, Field(alias="userCustomFields")
    ] = None
    users: list[ProjectCreateResourceIdentifier] | None = None


class PermissionPayloadDTO(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    add_addon_role: Annotated[
        bool | None,
        Field(
            alias="addAddonRole",
            description="Configuration to generate addon role. Default is false if null. Only applies to GLOBAL-scoped permission scheme",
        ),
    ] = None
    description: Annotated[
        str | None, Field(description="The description of the permission scheme")
    ] = None
    grants: Annotated[
        list[PermissionGrantDTO] | None, Field(description="List of permission grants")
    ] = None
    name: Annotated[str | None, Field(description="The name of the permission scheme")] = None
    on_conflict: Annotated[
        OnConflict,
        Field(
            alias="onConflict",
            description="The strategy to use when there is a conflict with an existing permission scheme. FAIL - Fail execution, this always needs to be unique; USE - Use the existing entity and ignore new entity parameters; NEW - If the entity exist, try and create a new one with a different name",
        ),
    ] = OnConflict.fail
    pcri: ProjectCreateResourceIdentifier | None = None


class ProjectIssueSecurityLevels(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    levels: Annotated[list[SecurityLevel], Field(description="Issue level security items list.")]


class ProjectIssueTypeHierarchy(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    hierarchy: Annotated[
        list[ProjectIssueTypesHierarchyLevel] | None,
        Field(description="Details of an issue type hierarchy level."),
    ] = None
    project_id: Annotated[
        int | None, Field(alias="projectId", description="The ID of the project.")
    ] = None


class ScreenPayload(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    description: Annotated[
        str | None,
        Field(description="The description of the screen", examples=["This is a screen"]),
    ] = None
    name: Annotated[
        str | None, Field(description="The name of the screen", examples=["My Screen"])
    ] = None
    pcri: ProjectCreateResourceIdentifier | None = None
    tabs: Annotated[
        list[TabPayload] | None,
        Field(
            description="The tabs of the screen. See https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-screen-tab-fields/\\#api-rest-api-3-screens-screenid-tabs-tabid-fields-post"
        ),
    ] = None


class TransitionPayload(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    actions: Annotated[
        list[RulePayload] | None,
        Field(description="The actions that are performed when the transition is made"),
    ] = None
    conditions: ConditionGroupPayload | None = None
    custom_issue_event_id: Annotated[
        str | None,
        Field(
            alias="customIssueEventId",
            description="Mechanism in Jira for triggering certain actions, like notifications, automations, etc. Unless a custom notification scheme is configure, it's better not to provide any value here",
        ),
    ] = None
    description: Annotated[str | None, Field(description="The description of the transition")] = (
        None
    )
    from_: Annotated[
        list[FromLayoutPayload] | None,
        Field(
            alias="from",
            description="The statuses that the transition can be made from",
        ),
    ] = None
    id: Annotated[int | None, Field(description="The id of the transition")] = None
    name: Annotated[str | None, Field(description="The name of the transition")] = None
    properties: Annotated[
        dict[str, str] | None, Field(description="The properties of the transition")
    ] = None
    to: ToLayoutPayload | None = None
    transition_screen: Annotated[RulePayload | None, Field(alias="transitionScreen")] = None
    triggers: Annotated[
        list[RulePayload] | None,
        Field(description="The triggers that are performed when the transition is made"),
    ] = None
    type: Annotated[Type29 | None, Field(description="The type of the transition")] = None
    validators: Annotated[
        list[RulePayload] | None,
        Field(description="The validators that are performed when the transition is made"),
    ] = None


class VersionIssueCounts(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    custom_field_usage: Annotated[
        list[VersionUsageInCustomField] | None,
        Field(
            alias="customFieldUsage",
            description="List of custom fields using the version.",
        ),
    ] = None
    issue_count_with_custom_fields_showing_version: Annotated[
        int | None,
        Field(
            alias="issueCountWithCustomFieldsShowingVersion",
            description="Count of issues where a version custom field is set to the version.",
        ),
    ] = None
    issues_affected_count: Annotated[
        int | None,
        Field(
            alias="issuesAffectedCount",
            description="Count of issues where the `affectedVersion` is set to the version.",
        ),
    ] = None
    issues_fixed_count: Annotated[
        int | None,
        Field(
            alias="issuesFixedCount",
            description="Count of issues where the `fixVersion` is set to the version.",
        ),
    ] = None
    self: Annotated[AnyUrl | None, Field(description="The URL of these count details.")] = None


class WorkflowPayload(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    description: Annotated[
        str | None,
        Field(
            description="The description of the workflow",
            examples=["a software workflow"],
        ),
    ] = None
    looped_transition_container_layout: Annotated[
        WorkflowStatusLayoutPayload | None, Field(alias="loopedTransitionContainerLayout")
    ] = None
    name: Annotated[
        str | None,
        Field(
            description="The name of the workflow",
            examples=["Software Simplified Workflow"],
        ),
    ] = None
    on_conflict: Annotated[
        OnConflict,
        Field(
            alias="onConflict",
            description="The strategy to use if there is a conflict with another workflow",
        ),
    ] = OnConflict.new
    pcri: ProjectCreateResourceIdentifier | None = None
    start_point_layout: Annotated[
        WorkflowStatusLayoutPayload | None, Field(alias="startPointLayout")
    ] = None
    statuses: Annotated[
        list[WorkflowStatusPayload] | None,
        Field(description="The statuses to be used in the workflow"),
    ] = None
    transitions: Annotated[
        list[TransitionPayload] | None, Field(description="The transitions for the workflow")
    ] = None


class ComponentWithIssueCount(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    assignee: Annotated[
        User | None,
        Field(
            description="The details of the user associated with `assigneeType`, if any. See `realAssignee` for details of the user assigned to issues created with this component."
        ),
    ] = None
    assignee_type: Annotated[
        AssigneeType | None,
        Field(
            alias="assigneeType",
            description="The nominal user type used to determine the assignee for issues created with this component. See `realAssigneeType` for details on how the type of the user, and hence the user, assigned to issues is determined. Takes the following values:\n\n *  `PROJECT_LEAD` the assignee to any issues created with this component is nominally the lead for the project the component is in.\n *  `COMPONENT_LEAD` the assignee to any issues created with this component is nominally the lead for the component.\n *  `UNASSIGNED` an assignee is not set for issues created with this component.\n *  `PROJECT_DEFAULT` the assignee to any issues created with this component is nominally the default assignee for the project that the component is in.",
        ),
    ] = None
    description: Annotated[str | None, Field(description="The description for the component.")] = (
        None
    )
    id: Annotated[str | None, Field(description="The unique identifier for the component.")] = None
    is_assignee_type_valid: Annotated[
        bool | None,
        Field(
            alias="isAssigneeTypeValid",
            description="Whether a user is associated with `assigneeType`. For example, if the `assigneeType` is set to `COMPONENT_LEAD` but the component lead is not set, then `false` is returned.",
        ),
    ] = None
    issue_count: Annotated[
        int | None, Field(alias="issueCount", description="Count of issues for the component.")
    ] = None
    lead: Annotated[
        User | None, Field(description="The user details for the component's lead user.")
    ] = None
    name: Annotated[str | None, Field(description="The name for the component.")] = None
    project: Annotated[
        str | None, Field(description="The key of the project to which the component is assigned.")
    ] = None
    project_id: Annotated[int | None, Field(alias="projectId", description="Not used.")] = None
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
    self: Annotated[
        AnyUrl | None,
        Field(description="The URL for this count of the issues contained in the component."),
    ] = None


class FieldCapabilityPayload(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    custom_field_definitions: Annotated[
        list[CustomFieldPayload | None] | None,
        Field(
            alias="customFieldDefinitions",
            description="The custom field definitions. See https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-fields/\\#api-rest-api-3-field-post",
        ),
    ] = None
    field_layout_scheme: Annotated[
        FieldLayoutSchemePayload | None, Field(alias="fieldLayoutScheme")
    ] = None
    field_layouts: Annotated[
        list[FieldLayoutPayload | None] | None,
        Field(alias="fieldLayouts", description="The field layouts configuration."),
    ] = None
    issue_layouts: Annotated[
        list[IssueLayoutPayload | None] | None,
        Field(alias="issueLayouts", description="The issue layouts configuration"),
    ] = None
    issue_type_screen_scheme: Annotated[
        IssueTypeScreenSchemePayload | None, Field(alias="issueTypeScreenScheme")
    ] = None
    screen_scheme: Annotated[
        list[ScreenSchemePayload | None] | None,
        Field(
            alias="screenScheme",
            description="The screen schemes See https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-screen-schemes/\\#api-rest-api-3-screenscheme-post",
        ),
    ] = None
    screens: Annotated[
        list[ScreenPayload | None] | None,
        Field(
            description="The screens. See https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-screens/\\#api-rest-api-3-screens-post"
        ),
    ] = None


class IssueTypeProjectCreatePayload(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    issue_type_hierarchy: Annotated[
        list[IssueTypeHierarchyPayload | None] | None,
        Field(
            alias="issueTypeHierarchy",
            description="Defines the issue type hierarhy to be created and used during this project creation. This will only add new levels if there isn't an existing level",
        ),
    ] = None
    issue_type_scheme: Annotated[IssueTypeSchemePayload | None, Field(alias="issueTypeScheme")] = (
        None
    )
    issue_types: Annotated[
        list[IssueTypePayload | None] | None,
        Field(
            alias="issueTypes",
            description="Only needed if you want to create issue types, you can otherwise use the ids of issue types in the scheme configuration",
        ),
    ] = None


class IssueTypeWithStatus(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    id: Annotated[str, Field(description="The ID of the issue type.")]
    name: Annotated[str, Field(description="The name of the issue type.")]
    self: Annotated[str, Field(description="The URL of the issue type's status details.")]
    statuses: Annotated[
        list[StatusDetails], Field(description="List of status details for the issue type.")
    ]
    subtask: Annotated[bool, Field(description="Whether this issue type represents subtasks.")]


class LegacyJackson1ListIssueTypeWithStatus(RootModel[list[IssueTypeWithStatus]]):
    root: list[IssueTypeWithStatus]


class PageBeanComponentWithIssueCount(BaseModel):
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
        list[ComponentWithIssueCount] | None, Field(description="The list of items.")
    ] = None


class PageBeanVersion(BaseModel):
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
    values: Annotated[list[Version] | None, Field(description="The list of items.")] = None


class ProjectRoleDetails(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    admin: Annotated[
        bool | None, Field(description="Whether this role is the admin role for the project.")
    ] = None
    default: Annotated[
        bool | None, Field(description="Whether this role is the default role for the project.")
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
    type: Annotated[
        Type19 | None,
        Field(description='The type of the project role. This is "DEFAULT" or "GUEST\\_ROLE".'),
    ] = None


class WorkflowCapabilityPayload(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    statuses: Annotated[
        list[StatusPayload] | None, Field(description="The statuses for the workflow")
    ] = None
    workflow_scheme: Annotated[WorkflowSchemePayload | None, Field(alias="workflowScheme")] = None
    workflows: Annotated[
        list[WorkflowPayload] | None, Field(description="The transitions for the workflow")
    ] = None


class CustomTemplateRequestDTO(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    boards: BoardsPayload | None = None
    field: FieldCapabilityPayload | None = None
    issue_type: Annotated[IssueTypeProjectCreatePayload | None, Field(alias="issueType")] = None
    notification: NotificationSchemePayload | None = None
    permission_scheme: Annotated[PermissionPayloadDTO | None, Field(alias="permissionScheme")] = (
        None
    )
    project: ProjectPayload | None = None
    role: RolesCapabilityPayload | None = None
    scope: ScopePayload | None = None
    security: SecuritySchemePayload | None = None
    workflow: WorkflowCapabilityPayload | None = None


class LegacyJackson1ListProjectRoleDetails(RootModel[list[ProjectRoleDetails]]):
    root: list[ProjectRoleDetails]


class ProjectCustomTemplateCreateRequestDTO(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    details: CustomTemplatesProjectDetails | None = None
    template: CustomTemplateRequestDTO | None = None


__all__ = [
    "ActorsMap",
    "BoardFeaturePayload",
    "CardLayout",
    "CardLayoutField",
    "ComponentIssuesCount",
    "CreateProjectDetails",
    "CustomFieldReplacement",
    "CustomTemplateOptions",
    "CustomTemplatesProjectDetails",
    "EditTemplateRequest",
    "IssueTypeInfo",
    "NonWorkingDay",
    "NotificationSchemeEventIDPayload",
    "NotificationSchemeNotificationDetailsPayload",
    "ProjectArchetype",
    "ProjectAvatars",
    "ProjectCreateResourceIdentifier",
    "ProjectEmailAddress",
    "ProjectFeature",
    "ProjectFeatureState",
    "ProjectIdentifiers",
    "ProjectIssueTypesHierarchyLevel",
    "ProjectPayload",
    "ProjectTemplateModel",
    "ProjectType",
    "QuickFilterPayload",
    "RolePayload",
    "RolesCapabilityPayload",
    "RulePayload",
    "SaveProjectTemplateRequest",
    "SaveTemplateRequest",
    "SaveTemplateResponse",
    "ScopePayload",
    "ScreenSchemePayload",
    "SecurityLevelMemberPayload",
    "SecurityLevelPayload",
    "SecuritySchemePayload",
    "StatusPayload",
    "SwimlanePayload",
    "SwimlanesPayload",
    "TabPayload",
    "ToLayoutPayload",
    "UpdateProjectDetails",
    "VersionRelatedWork",
    "VersionUnresolvedIssuesCount",
    "VersionUsageInCustomField",
    "WorkflowSchemePayload",
    "WorkflowStatusLayoutPayload",
    "WorkflowStatusPayload",
    "WorkingDaysConfig",
    "BoardColumnPayload",
    "BoardPayload",
    "BoardsPayload",
    "ConditionGroupPayload",
    "ContainerForProjectFeatures",
    "CustomFieldPayload",
    "FieldLayoutConfiguration",
    "FieldLayoutPayload",
    "FieldLayoutSchemePayload",
    "FromLayoutPayload",
    "IssueLayoutItemPayload",
    "IssueLayoutPayload",
    "IssueTypeHierarchyPayload",
    "IssueTypePayload",
    "IssueTypeSchemePayload",
    "IssueTypeScreenSchemePayload",
    "LegacyJackson1ListProjectType",
    "NotificationSchemeEventPayload",
    "NotificationSchemePayload",
    "PermissionGrantDTO",
    "PermissionPayloadDTO",
    "ProjectIssueSecurityLevels",
    "ProjectIssueTypeHierarchy",
    "ScreenPayload",
    "TransitionPayload",
    "VersionIssueCounts",
    "WorkflowPayload",
    "ComponentWithIssueCount",
    "FieldCapabilityPayload",
    "IssueTypeProjectCreatePayload",
    "IssueTypeWithStatus",
    "LegacyJackson1ListIssueTypeWithStatus",
    "PageBeanComponentWithIssueCount",
    "PageBeanVersion",
    "ProjectRoleDetails",
    "WorkflowCapabilityPayload",
    "CustomTemplateRequestDTO",
    "LegacyJackson1ListProjectRoleDetails",
    "ProjectCustomTemplateCreateRequestDTO",
]
