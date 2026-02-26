"""Pydantic models for the workflows domain."""

from __future__ import annotations

from typing import Annotated, Any, Literal
from uuid import UUID

from pydantic import AnyUrl, AwareDatetime, BaseModel, ConfigDict, Field


class ApprovalConfiguration(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    active: Annotated[Active, Field(description="Whether the approval configuration is active.")]
    condition_type: Annotated[
        ConditionType,
        Field(
            alias="conditionType",
            description="How the required approval count is calculated. It may be configured to require a specific number of approvals, or approval by a percentage of approvers. If the approvers source field is Approver groups, you can configure how many approvals per group are required for the request to be approved. The number will be the same across all groups.",
        ),
    ]
    condition_value: Annotated[
        str,
        Field(
            alias="conditionValue",
            description="The number or percentage of approvals required for a request to be approved. If `conditionType` is `number`, the value must be 20 or less. If `conditionType` is `percent`, the value must be 100 or less.",
        ),
    ]
    exclude: Annotated[
        list[ExcludeEnum] | None,
        Field(description="A list of roles that should be excluded as possible approvers."),
    ] = None
    field_id: Annotated[
        str,
        Field(
            alias="fieldId",
            description='The custom field ID of the "Approvers" or "Approver Groups" field.',
        ),
    ]
    pre_populated_field_id: Annotated[
        str | None,
        Field(
            alias="prePopulatedFieldId",
            description='The custom field ID of the field used to pre-populate the Approver field. Only supports the "Affected Services" field.',
        ),
    ] = None
    transition_approved: Annotated[
        str,
        Field(
            alias="transitionApproved",
            description="The numeric ID of the transition to be executed if the request is approved.",
        ),
    ]
    transition_rejected: Annotated[
        str,
        Field(
            alias="transitionRejected",
            description="The numeric ID of the transition to be executed if the request is declined.",
        ),
    ]


class ApprovalConfigurationPreview(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    active: Annotated[str | None, Field(description="The active approval configuration.")] = None
    transition_approved: Annotated[
        str | None,
        Field(
            alias="transitionApproved",
            description="The transition ID for approved state.",
        ),
    ] = None
    transition_rejected: Annotated[
        str | None,
        Field(
            alias="transitionRejected",
            description="The transition ID for rejected state.",
        ),
    ] = None


class AvailableWorkflowConnectRule(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    addon_key: Annotated[
        str | None, Field(alias="addonKey", description="The add-on providing the rule.")
    ] = None
    create_url: Annotated[
        str | None,
        Field(
            alias="createUrl",
            description="The URL creation path segment defined in the Connect module.",
        ),
    ] = None
    description: Annotated[str | None, Field(description="The rule description.")] = None
    edit_url: Annotated[
        str | None,
        Field(
            alias="editUrl",
            description="The URL edit path segment defined in the Connect module.",
        ),
    ] = None
    module_key: Annotated[
        str | None, Field(alias="moduleKey", description="The module providing the rule.")
    ] = None
    name: Annotated[str | None, Field(description="The rule name.")] = None
    rule_key: Annotated[str | None, Field(alias="ruleKey", description="The rule key.")] = None
    rule_type: Annotated[RuleType | None, Field(alias="ruleType", description="The rule type.")] = (
        None
    )
    view_url: Annotated[
        str | None,
        Field(
            alias="viewUrl",
            description="The URL view path segment defined in the Connect module.",
        ),
    ] = None


class AvailableWorkflowForgeRule(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    description: Annotated[str | None, Field(description="The rule description.")] = None
    id: Annotated[str | None, Field(description="The unique ARI of the forge rule type.")] = None
    name: Annotated[str | None, Field(description="The rule name.")] = None
    rule_key: Annotated[str | None, Field(alias="ruleKey", description="The rule key.")] = None
    rule_type: Annotated[RuleType | None, Field(alias="ruleType", description="The rule type.")] = (
        None
    )


class AvailableWorkflowSystemRule(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    description: Annotated[str, Field(description="The rule description.")]
    incompatible_rule_keys: Annotated[
        list[str],
        Field(
            alias="incompatibleRuleKeys",
            description="List of rules that conflict with this one.",
        ),
    ]
    is_available_for_initial_transition: Annotated[
        bool,
        Field(
            alias="isAvailableForInitialTransition",
            description="Whether the rule can be added added to an initial transition.",
        ),
    ]
    is_visible: Annotated[
        bool, Field(alias="isVisible", description="Whether the rule is visible.")
    ]
    name: Annotated[str, Field(description="The rule name.")]
    rule_key: Annotated[str, Field(alias="ruleKey", description="The rule key.")]
    rule_type: Annotated[RuleType, Field(alias="ruleType", description="The rule type.")]


class AvailableWorkflowTriggerTypes(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    description: Annotated[
        str | None, Field(description="The description of the trigger rule.")
    ] = None
    name: Annotated[str | None, Field(description="The name of the trigger rule.")] = None
    type: Annotated[str | None, Field(description="The type identifier of trigger rule.")] = None


class AvailableWorkflowTriggers(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    available_types: Annotated[
        list[AvailableWorkflowTriggerTypes],
        Field(alias="availableTypes", description="The list of available trigger types."),
    ]
    rule_key: Annotated[str, Field(alias="ruleKey", description="The rule key of the rule.")]


class CreateWorkflowCondition(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    conditions: Annotated[
        list[CreateWorkflowCondition] | None, Field(description="The list of workflow conditions.")
    ] = None
    configuration: Annotated[
        dict[str, Any] | None,
        Field(description="EXPERIMENTAL. The configuration of the transition rule."),
    ] = None
    operator: Annotated[Operator1 | None, Field(description="The compound condition operator.")] = (
        None
    )
    type: Annotated[str | None, Field(description="The type of the transition rule.")] = None


class CreateWorkflowStatusDetails(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    id: Annotated[str, Field(description="The ID of the status.")]
    properties: Annotated[
        dict[str, str] | None, Field(description="The properties of the status.")
    ] = None


class CreateWorkflowTransitionRule(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    configuration: Annotated[
        dict[str, Any] | None,
        Field(description="EXPERIMENTAL. The configuration of the transition rule."),
    ] = None
    type: Annotated[str, Field(description="The type of the transition rule.")]


class CreateWorkflowTransitionRulesDetails(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    conditions: Annotated[
        CreateWorkflowCondition | None, Field(description="The workflow conditions.")
    ] = None
    post_functions: Annotated[
        list[CreateWorkflowTransitionRule] | None,
        Field(
            alias="postFunctions",
            description='The workflow post functions.\n\n**Note:** The default post functions are always added to the *initial* transition, as in:\n\n    "postFunctions": [\n        {\n            "type": "IssueCreateFunction"\n        },\n        {\n            "type": "IssueReindexFunction"\n        },\n        {\n            "type": "FireIssueEventFunction",\n            "configuration": {\n                "event": {\n                    "id": "1",\n                    "name": "issue_created"\n                }\n            }\n        }\n    ]\n\n**Note:** The default post functions are always added to the *global* and *directed* transitions, as in:\n\n    "postFunctions": [\n        {\n            "type": "UpdateIssueStatusFunction"\n        },\n        {\n            "type": "CreateCommentFunction"\n        },\n        {\n            "type": "GenerateChangeHistoryFunction"\n        },\n        {\n            "type": "IssueReindexFunction"\n        },\n        {\n            "type": "FireIssueEventFunction",\n            "configuration": {\n                "event": {\n                    "id": "13",\n                    "name": "issue_generic"\n                }\n            }\n        }\n    ]',
        ),
    ] = None
    validators: Annotated[
        list[CreateWorkflowTransitionRule] | None,
        Field(
            description='The workflow validators.\n\n**Note:** The default permission validator is always added to the *initial* transition, as in:\n\n    "validators": [\n        {\n            "type": "PermissionValidator",\n            "configuration": {\n                "permissionKey": "CREATE_ISSUES"\n            }\n        }\n    ]'
        ),
    ] = None


class CreateWorkflowTransitionScreenDetails(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    id: Annotated[str, Field(description="The ID of the screen.")]


class DefaultWorkflow(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    update_draft_if_needed: Annotated[
        bool | None,
        Field(
            alias="updateDraftIfNeeded",
            description="Whether a draft workflow scheme is created or updated when updating an active workflow scheme. The draft is updated with the new default workflow. Defaults to `false`.",
        ),
    ] = None
    workflow: Annotated[
        str, Field(description="The name of the workflow to set as the default workflow.")
    ]


class DefaultWorkflowEditorResponse(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    value: Value | None = None


class DocumentVersion(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    id: Annotated[str | None, Field(description="The version UUID.")] = None
    version_number: Annotated[
        int | None, Field(alias="versionNumber", description="The version number.")
    ] = None


class IssueTypeWorkflowMapping(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    issue_type: Annotated[
        str | None,
        Field(
            alias="issueType",
            description="The ID of the issue type. Not required if updating the issue type-workflow mapping.",
        ),
    ] = None
    update_draft_if_needed: Annotated[
        bool | None,
        Field(
            alias="updateDraftIfNeeded",
            description="Set to true to create or update the draft of a workflow scheme and update the mapping in the draft, when the workflow scheme cannot be edited. Defaults to `false`. Only applicable when updating the workflow-issue types mapping.",
        ),
    ] = None
    workflow: Annotated[str | None, Field(description="The name of the workflow.")] = None


class IssueTypesWorkflowMapping(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    default_mapping: Annotated[
        bool | None,
        Field(
            alias="defaultMapping",
            description="Whether the workflow is the default workflow for the workflow scheme.",
        ),
    ] = None
    issue_types: Annotated[
        list[str] | None, Field(alias="issueTypes", description="The list of issue type IDs.")
    ] = None
    update_draft_if_needed: Annotated[
        bool | None,
        Field(
            alias="updateDraftIfNeeded",
            description="Whether a draft workflow scheme is created or updated when updating an active workflow scheme. The draft is updated with the new workflow-issue types mapping. Defaults to `false`.",
        ),
    ] = None
    workflow: Annotated[
        str | None,
        Field(
            description="The name of the workflow. Optional if updating the workflow-issue types mapping."
        ),
    ] = None


class PreviewRuleConfiguration(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    id: Annotated[
        str | None,
        Field(
            description="A transient identifier for this element, unique within this response but not guaranteed to stable across requests."
        ),
    ] = None
    parameters: Annotated[
        dict[str, str] | None, Field(description="The parameters of the rule.")
    ] = None
    rule_key: Annotated[
        str | None, Field(alias="ruleKey", description="The rule key of the rule.")
    ] = None


class PreviewTrigger(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    id: Annotated[str | None, Field(description="The ID of the trigger.")] = None
    rule_key: Annotated[
        str | None, Field(alias="ruleKey", description="The key of the trigger rule.")
    ] = None


class ProjectAndIssueTypePair(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    issue_type_id: Annotated[
        str, Field(alias="issueTypeId", description="The ID of the issue type.")
    ]
    project_id: Annotated[str, Field(alias="projectId", description="The ID of the project.")]


class ProjectIssueTypeQueryContext(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    issue_types: Annotated[
        list[str] | None, Field(alias="issueTypes", description="The set of issue type IDs.")
    ] = None
    project: Annotated[str | None, Field(description="The ID of the project.")] = None


class ProjectUsage(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    id: Annotated[str | None, Field(description="The project ID.")] = None


class ProjectUsagePage(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    next_page_token: Annotated[
        str | None,
        Field(
            alias="nextPageToken",
            description="Page token for the next page of project usages.",
        ),
    ] = None
    values: Annotated[list[ProjectUsage] | None, Field(description="The list of projects.")] = None


class PublishedWorkflowId(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    entity_id: Annotated[
        str | None, Field(alias="entityId", description="The entity ID of the workflow.")
    ] = None
    name: Annotated[str, Field(description="The name of the workflow.")]


class RequiredMappingByIssueType(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    issue_type_id: Annotated[
        str | None, Field(alias="issueTypeId", description="The ID of the issue type.")
    ] = None
    status_ids: Annotated[
        list[str] | None, Field(alias="statusIds", description="The status IDs requiring mapping.")
    ] = None


class RequiredMappingByWorkflows(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    source_workflow_id: Annotated[
        str | None, Field(alias="sourceWorkflowId", description="The ID of the source workflow.")
    ] = None
    status_ids: Annotated[
        list[str] | None, Field(alias="statusIds", description="The status IDs requiring mapping.")
    ] = None
    target_workflow_id: Annotated[
        str | None, Field(alias="targetWorkflowId", description="The ID of the target workflow.")
    ] = None


class StatusMapping(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    issue_type_id: Annotated[
        str, Field(alias="issueTypeId", description="The ID of the issue type.")
    ]
    new_status_id: Annotated[
        str, Field(alias="newStatusId", description="The ID of the new status.")
    ]
    status_id: Annotated[str, Field(alias="statusId", description="The ID of the status.")]


class StatusMetadata(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    category: Annotated[Category | None, Field(description="The category of the status.")] = None
    id: Annotated[str | None, Field(description="The ID of the status.")] = None
    name: Annotated[str | None, Field(description="The name of the status.")] = None


class StatusMigration(BaseModel):
    model_config = ConfigDict(
        extra="allow",
    )
    new_status_reference: Annotated[
        str, Field(alias="newStatusReference", description="The new status ID.")
    ]
    old_status_reference: Annotated[
        str, Field(alias="oldStatusReference", description="The old status ID.")
    ]


class StatusesPerWorkflow(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    initial_status_id: Annotated[
        str | None,
        Field(
            alias="initialStatusId",
            description="The ID of the initial status for the workflow.",
        ),
    ] = None
    statuses: Annotated[
        list[str] | None, Field(description="The status IDs associated with the workflow.")
    ] = None
    workflow_id: Annotated[
        str | None, Field(alias="workflowId", description="The ID of the workflow.")
    ] = None


class TransitionLink(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    from_port: Annotated[
        int | None, Field(alias="fromPort", description="The from port number.")
    ] = None
    from_status_reference: Annotated[
        str | None, Field(alias="fromStatusReference", description="The from status reference.")
    ] = None
    to_port: Annotated[int | None, Field(alias="toPort", description="The to port number.")] = None


class TransitionScreenDetails(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    id: Annotated[str, Field(description="The ID of the screen.")]
    name: Annotated[str | None, Field(description="The name of the screen.")] = None


class ValidationOptionsForCreate(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    levels: Annotated[list[Level] | None, Field(max_length=2)] = None


class ValidationOptionsForUpdate(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    levels: Annotated[list[Level] | None, Field(max_length=2)] = None


class WorkflowAssociationStatusMapping(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    new_status_id: Annotated[str | None, Field(alias="newStatusId")] = None
    old_status_id: Annotated[str | None, Field(alias="oldStatusId")] = None


class WorkflowCapabilities(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    connect_rules: Annotated[
        list[AvailableWorkflowConnectRule] | None,
        Field(
            alias="connectRules",
            description="The Connect provided ecosystem rules available.",
        ),
    ] = None
    editor_scope: Annotated[
        EditorScope | None,
        Field(
            alias="editorScope",
            description="The scope of the workflow capabilities. `GLOBAL` for company-managed projects and `PROJECT` for team-managed projects.",
        ),
    ] = None
    forge_rules: Annotated[
        list[AvailableWorkflowForgeRule] | None,
        Field(
            alias="forgeRules",
            description="The Forge provided ecosystem rules available.",
        ),
    ] = None
    project_types: Annotated[
        list[ProjectType1] | None,
        Field(
            alias="projectTypes",
            description="The types of projects that this capability set is available for.",
        ),
    ] = None
    system_rules: Annotated[
        list[AvailableWorkflowSystemRule] | None,
        Field(
            alias="systemRules",
            description="The Atlassian provided system rules available.",
        ),
    ] = None
    trigger_rules: Annotated[
        list[AvailableWorkflowTriggers] | None,
        Field(alias="triggerRules", description="The trigger rules available."),
    ] = None


class WorkflowElementReference(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    property_key: Annotated[
        str | None, Field(alias="propertyKey", description="A property key.")
    ] = None
    rule_id: Annotated[str | None, Field(alias="ruleId", description="A rule ID.")] = None
    status_mapping_reference: Annotated[
        ProjectAndIssueTypePair | None, Field(alias="statusMappingReference")
    ] = None
    status_reference: Annotated[
        str | None, Field(alias="statusReference", description="A status reference.")
    ] = None
    transition_id: Annotated[
        str | None, Field(alias="transitionId", description="A transition ID.")
    ] = None


class WorkflowHistoryItemDTO(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    is_intermediate: Annotated[
        bool | None,
        Field(
            alias="isIntermediate",
            description="Whether the version is an intermediate workflow state, sometimes created during workflow updates.",
        ),
    ] = None
    workflow_id: Annotated[str | None, Field(alias="workflowId")] = None
    workflow_version: Annotated[int | None, Field(alias="workflowVersion")] = None
    written_at: Annotated[
        str | None,
        Field(
            alias="writtenAt",
            description="The timestamp when this workflow version was created.",
        ),
    ] = None


class WorkflowHistoryListRequest(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    workflow_id: Annotated[
        str | None,
        Field(
            alias="workflowId",
            description="The id of the workflow to read the history for.",
        ),
    ] = None


class WorkflowHistoryListResponseDTO(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    entries: list[WorkflowHistoryItemDTO] | None = None


class WorkflowHistoryReadRequest(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    version: int | None = None
    workflow_id: Annotated[str | None, Field(alias="workflowId")] = None


class WorkflowIDs(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    entity_id: Annotated[
        str | None, Field(alias="entityId", description="The entity ID of the workflow.")
    ] = None
    name: Annotated[str, Field(description="The name of the workflow.")]


class WorkflowLayout(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    x: Annotated[float | None, Field(description="The x axis location.")] = None
    y: Annotated[float | None, Field(description="The y axis location.")] = None


class WorkflowMetadataRestModel(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    description: Annotated[str, Field(description="The description of the workflow.")]
    id: Annotated[str, Field(description="The ID of the workflow.")]
    name: Annotated[str, Field(description="The name of the workflow.")]
    version: DocumentVersion


class WorkflowOperations(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    can_delete: Annotated[
        bool, Field(alias="canDelete", description="Whether the workflow can be deleted.")
    ]
    can_edit: Annotated[
        bool, Field(alias="canEdit", description="Whether the workflow can be updated.")
    ]


class WorkflowPreviewLayout(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    x: Annotated[float | None, Field(description="The X coordinate.")] = None
    y: Annotated[float | None, Field(description="The Y coordinate.")] = None


class WorkflowPreviewRequest(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    issue_type_ids: Annotated[
        list[str] | None,
        Field(
            alias="issueTypeIds",
            description="The list of issue type IDs. At most 25 issue type IDs can be specified.",
            max_length=25,
            min_length=0,
        ),
    ] = None
    project_id: Annotated[
        str,
        Field(
            alias="projectId",
            description="The projectId parameter is required and will be used for permission checks. In addition, you must supply at least one of the following lookup terms: *workflowNames*, *workflowIds*, or *issueTypeIds*. The specified workflows must be associated with the given project.",
        ),
    ]
    workflow_ids: Annotated[
        list[str] | None,
        Field(
            alias="workflowIds",
            description="The list of workflow IDs to be returned. At most 25 workflow IDs can be specified.",
            max_length=25,
            min_length=0,
        ),
    ] = None
    workflow_names: Annotated[
        list[str] | None,
        Field(
            alias="workflowNames",
            description="The list of workflow names to be returned. At most 25 workflow names can be specified.",
            max_length=25,
            min_length=0,
        ),
    ] = None


class WorkflowPreviewStatus(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    approval_configuration: Annotated[
        ApprovalConfigurationPreview | None, Field(alias="approvalConfiguration")
    ] = None
    deprecated: Annotated[bool | None, Field(description="Whether the status is deprecated.")] = (
        None
    )
    layout: WorkflowPreviewLayout | None = None
    status_reference: Annotated[
        str | None, Field(alias="statusReference", description="The reference of the status.")
    ] = None


class WorkflowProjectIdScope(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    id: Annotated[str | None, Field(description="The ID of the project.")] = None


class WorkflowProjectIssueTypeUsage(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    id: Annotated[str | None, Field(description="The ID of the issue type.")] = None


class WorkflowProjectIssueTypeUsagePage(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    next_page_token: Annotated[
        str | None,
        Field(
            alias="nextPageToken",
            description="Token for the next page of issue type usages.",
        ),
    ] = None
    values: Annotated[
        list[WorkflowProjectIssueTypeUsage] | None, Field(description="The list of issue types.")
    ] = None


class WorkflowProjectUsageDTO(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    projects: ProjectUsagePage | None = None
    workflow_id: Annotated[
        str | None, Field(alias="workflowId", description="The workflow ID.")
    ] = None


class WorkflowReadRequest(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    project_and_issue_types: Annotated[
        list[ProjectAndIssueTypePair] | None,
        Field(
            alias="projectAndIssueTypes",
            description="The list of projects and issue types to query.",
        ),
    ] = None
    workflow_ids: Annotated[
        list[str] | None,
        Field(alias="workflowIds", description="The list of workflow IDs to query."),
    ] = None
    workflow_names: Annotated[
        list[str] | None,
        Field(alias="workflowNames", description="The list of workflow names to query."),
    ] = None


class WorkflowRuleConfiguration(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    id: Annotated[str | None, Field(description="The ID of the rule.")] = None
    parameters: Annotated[
        dict[str, str] | None, Field(description="The parameters related to the rule.")
    ] = None
    rule_key: Annotated[str, Field(alias="ruleKey", description="The rule key of the rule.")]


class WorkflowSchemeAssociation(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    issue_type_ids: Annotated[
        list[str],
        Field(
            alias="issueTypeIds",
            description="The issue types assigned to the workflow.",
        ),
    ]
    workflow_id: Annotated[str, Field(alias="workflowId", description="The ID of the workflow.")]


class WorkflowSchemeIdName(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    id: Annotated[str, Field(description="The ID of the workflow scheme.")]
    name: Annotated[str, Field(description="The name of the workflow scheme.")]


class WorkflowSchemeProjectAssociation(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    project_id: Annotated[str, Field(alias="projectId", description="The ID of the project.")]
    workflow_scheme_id: Annotated[
        str | None,
        Field(
            alias="workflowSchemeId",
            description="The ID of the workflow scheme. If the workflow scheme ID is `null`, the operation assigns the default workflow scheme.",
        ),
    ] = None


class WorkflowSchemeProjectUsageDTO(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    projects: ProjectUsagePage | None = None
    workflow_scheme_id: Annotated[
        str | None, Field(alias="workflowSchemeId", description="The workflow scheme ID.")
    ] = None


class WorkflowSchemeReadRequest(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    project_ids: Annotated[
        list[str | None] | None,
        Field(alias="projectIds", description="The list of project IDs to query."),
    ] = None
    workflow_scheme_ids: Annotated[
        list[str | None] | None,
        Field(
            alias="workflowSchemeIds",
            description="The list of workflow scheme IDs to query.",
        ),
    ] = None


class WorkflowSchemeUpdateRequiredMappingsRequest(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    default_workflow_id: Annotated[
        str | None,
        Field(
            alias="defaultWorkflowId",
            description="The ID of the new default workflow for this workflow scheme. Only used in global-scoped workflow schemes. If it isn't specified, is set to *Jira Workflow (jira)*.",
        ),
    ] = None
    id: Annotated[str, Field(description="The ID of the workflow scheme.")]
    workflows_for_issue_types: Annotated[
        list[WorkflowSchemeAssociation],
        Field(
            alias="workflowsForIssueTypes",
            description="The new workflow to issue type mappings for this workflow scheme.",
        ),
    ]


class WorkflowSchemeUpdateRequiredMappingsResponse(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    status_mappings_by_issue_types: Annotated[
        list[RequiredMappingByIssueType] | None,
        Field(
            alias="statusMappingsByIssueTypes",
            description="The list of required status mappings by issue type.",
        ),
    ] = None
    status_mappings_by_workflows: Annotated[
        list[RequiredMappingByWorkflows] | None,
        Field(
            alias="statusMappingsByWorkflows",
            description="The list of required status mappings by workflow.",
        ),
    ] = None
    statuses: Annotated[
        list[StatusMetadata] | None,
        Field(description="The details of the statuses in the associated workflows."),
    ] = None
    statuses_per_workflow: Annotated[
        list[StatusesPerWorkflow] | None,
        Field(
            alias="statusesPerWorkflow",
            description="The statuses associated with each workflow.",
        ),
    ] = None


class WorkflowSchemeUsage(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    id: Annotated[str | None, Field(description="The workflow scheme ID.")] = None


class WorkflowSchemeUsagePage(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    next_page_token: Annotated[
        str | None,
        Field(
            alias="nextPageToken",
            description="Token for the next page of issue type usages.",
        ),
    ] = None
    values: Annotated[
        list[WorkflowSchemeUsage] | None, Field(description="The list of workflow schemes.")
    ] = None


class WorkflowScope(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    project: ProjectId | None = None
    type: Annotated[
        Type35 | None,
        Field(
            description="The scope of the workflow. `GLOBAL` for company-managed projects and `PROJECT` for team-managed projects."
        ),
    ] = None


class WorkflowSimpleCondition(BaseModel):
    configuration: Annotated[
        dict[str, Any] | None,
        Field(description="EXPERIMENTAL. The configuration of the transition rule."),
    ] = None
    node_type: Annotated[Literal["simple"], Field(alias="nodeType")]
    type: Annotated[str, Field(description="The type of the transition rule.")]


class WorkflowStatus(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    id: Annotated[str, Field(description="The ID of the issue status.")]
    name: Annotated[str, Field(description="The name of the status in the workflow.")]
    properties: Annotated[
        dict[str, Any] | None,
        Field(
            description="Additional properties that modify the behavior of issues in this status. Supports the properties `jira.issue.editable` and `issueEditable` (deprecated) that indicate whether issues are editable."
        ),
    ] = None


class WorkflowStatusLayout(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    x: Annotated[float | None, Field(description="The x axis location.")] = None
    y: Annotated[float | None, Field(description="The y axis location.")] = None


class WorkflowStatusUpdate(BaseModel):
    model_config = ConfigDict(
        extra="allow",
    )
    description: Annotated[str | None, Field(description="The description of the status.")] = None
    id: Annotated[
        str | None,
        Field(
            description="The ID of the status. When reusing an existing status, this field should be provided."
        ),
    ] = None
    name: Annotated[str, Field(description="The name of the status.")]
    status_category: Annotated[
        StatusCategory4, Field(alias="statusCategory", description="The category of the status.")
    ]
    status_reference: Annotated[
        str,
        Field(
            alias="statusReference",
            description="The reference of the status. If adding a new status to a team-managed workflow, this must be a UUID (for company-managed a UUID is not needed).",
        ),
    ]


class WorkflowTransitionLinks(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    from_port: Annotated[
        int | None, Field(alias="fromPort", description="The port that the transition starts from.")
    ] = None
    from_status_reference: Annotated[
        str | None,
        Field(
            alias="fromStatusReference",
            description="The status that the transition starts from.",
        ),
    ] = None
    to_port: Annotated[
        int | None, Field(alias="toPort", description="The port that the transition goes to.")
    ] = None


class WorkflowTransitionRule(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    configuration: Annotated[
        Any | None, Field(description="EXPERIMENTAL. The configuration of the transition rule.")
    ] = None
    type: Annotated[str, Field(description="The type of the transition rule.")]


class WorkflowTransitionRulesDetails(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    workflow_id: Annotated[WorkflowId, Field(alias="workflowId")]
    workflow_rule_ids: Annotated[
        list[str],
        Field(
            alias="workflowRuleIds",
            description="The list of connect workflow rule IDs.",
        ),
    ]


class WorkflowTransitionRulesUpdateErrorDetails(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    rule_update_errors: Annotated[
        dict[str, list[str]],
        Field(
            alias="ruleUpdateErrors",
            description="A list of transition rule update errors, indexed by the transition rule ID. Any transition rule that appears here wasn't updated.",
        ),
    ]
    update_errors: Annotated[
        list[str],
        Field(
            alias="updateErrors",
            description="The list of errors that specify why the workflow update failed. The workflow was not updated if the list contains any entries.",
        ),
    ]
    workflow_id: Annotated[WorkflowId, Field(alias="workflowId")]


class WorkflowTransitionRulesUpdateErrors(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    update_results: Annotated[
        list[WorkflowTransitionRulesUpdateErrorDetails],
        Field(alias="updateResults", description="A list of workflows."),
    ]


class WorkflowTrigger(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    id: Annotated[str | None, Field(description="The ID of the trigger.")] = None
    parameters: Annotated[dict[str, str], Field(description="The parameters of the trigger.")]
    rule_key: Annotated[str, Field(alias="ruleKey", description="The rule key of the trigger.")]


class WorkflowValidationError(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    code: Annotated[str | None, Field(description="An error code.")] = None
    element_reference: Annotated[
        WorkflowElementReference | None, Field(alias="elementReference")
    ] = None
    level: Annotated[Level | None, Field(description="The validation error level.")] = None
    message: Annotated[str | None, Field(description="An error message.")] = None
    type: Annotated[
        Type38 | None, Field(description="The type of element the error or warning references.")
    ] = None


class WorkflowValidationErrorList(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    errors: Annotated[
        list[WorkflowValidationError] | None, Field(description="The list of validation errors.")
    ] = None


class WorkflowsWithTransitionRulesDetails(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    workflows: Annotated[
        list[WorkflowTransitionRulesDetails],
        Field(description="The list of workflows with transition rules to delete."),
    ]


class ConditionGroupConfiguration(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    condition_groups: Annotated[
        list[ConditionGroupConfiguration | None] | None,
        Field(
            alias="conditionGroups",
            description="The nested conditions of the condition group.",
        ),
    ] = None
    conditions: Annotated[
        list[WorkflowRuleConfiguration | None] | None,
        Field(description="The rules for this condition."),
    ] = None
    operation: Annotated[
        Operation | None,
        Field(
            description="Determines how the conditions in the group are evaluated. Accepts either `ANY` or `ALL`. If `ANY` is used, at least one condition in the group must be true for the group to evaluate to true. If `ALL` is used, all conditions in the group must be true for the group to evaluate to true."
        ),
    ] = None


class ConditionGroupUpdate(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    condition_groups: Annotated[
        list[ConditionGroupUpdate | None] | None,
        Field(
            alias="conditionGroups",
            description="The nested conditions of the condition group.",
        ),
    ] = None
    conditions: Annotated[
        list[WorkflowRuleConfiguration | None] | None,
        Field(description="The rules for this condition."),
    ] = None
    operation: Annotated[
        Operation,
        Field(
            description="Determines how the conditions in the group are evaluated. Accepts either `ANY` or `ALL`. If `ANY` is used, at least one condition in the group must be true for the group to evaluate to true. If `ALL` is used, all conditions in the group must be true for the group to evaluate to true."
        ),
    ]


class CreateWorkflowTransitionDetails(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    description: Annotated[
        str | None,
        Field(
            description="The description of the transition. The maximum length is 1000 characters."
        ),
    ] = None
    from_: Annotated[
        list[str] | None,
        Field(alias="from", description="The statuses the transition can start from."),
    ] = None
    name: Annotated[
        str, Field(description="The name of the transition. The maximum length is 60 characters.")
    ]
    properties: Annotated[
        dict[str, str] | None, Field(description="The properties of the transition.")
    ] = None
    rules: Annotated[
        CreateWorkflowTransitionRulesDetails | None,
        Field(description="The rules of the transition."),
    ] = None
    screen: Annotated[
        CreateWorkflowTransitionScreenDetails | None,
        Field(description="The screen of the transition."),
    ] = None
    to: Annotated[str, Field(description="The status the transition goes to.")]
    type: Annotated[Type4, Field(description="The type of the transition.")]


class JiraWorkflowStatus(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    description: Annotated[str | None, Field(description="The description of the status.")] = None
    id: Annotated[str | None, Field(description="The ID of the status.")] = None
    name: Annotated[str | None, Field(description="The name of the status.")] = None
    scope: WorkflowScope | None = None
    status_category: Annotated[
        StatusCategory | None,
        Field(alias="statusCategory", description="The category of the status."),
    ] = None
    status_reference: Annotated[
        str | None, Field(alias="statusReference", description="The reference of the status.")
    ] = None


class MappingsByIssueTypeOverride(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    issue_type_id: Annotated[str | None, Field(alias="issueTypeId")] = None
    status_mappings: Annotated[
        list[WorkflowAssociationStatusMapping] | None, Field(alias="statusMappings")
    ] = None


class MappingsByWorkflow(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    new_workflow_id: Annotated[
        str, Field(alias="newWorkflowId", description="The ID of the new workflow.")
    ]
    old_workflow_id: Annotated[
        str, Field(alias="oldWorkflowId", description="The ID of the old workflow.")
    ]
    status_mappings: Annotated[
        list[WorkflowAssociationStatusMapping],
        Field(alias="statusMappings", description="The list of status mappings."),
    ]


class PreviewConditionGroupConfiguration(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    condition_groups: Annotated[
        list[PreviewConditionGroupConfiguration | None] | None,
        Field(
            alias="conditionGroups",
            description="The nested conditions of the condition group.",
        ),
    ] = None
    conditions: Annotated[
        list[PreviewRuleConfiguration | None] | None,
        Field(description="The rules for this condition."),
    ] = None
    operation: Annotated[
        Operation | None,
        Field(
            description="Determines how the conditions in the group are evaluated. Accepts either `ANY` or `ALL`. If `ANY` is used, at least one condition in the group must be true for the group to evaluate to true. If `ALL` is used, all conditions in the group must be true for the group to evaluate to true."
        ),
    ] = None


class PublishDraftWorkflowScheme(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    status_mappings: Annotated[
        list[StatusMapping] | None,
        Field(
            alias="statusMappings",
            description="Mappings of statuses to new statuses for issue types.",
        ),
    ] = None


class StatusLayoutUpdate(BaseModel):
    model_config = ConfigDict(
        extra="allow",
    )
    approval_configuration: Annotated[
        ApprovalConfiguration | None, Field(alias="approvalConfiguration")
    ] = None
    layout: WorkflowLayout | None = None
    properties: Annotated[
        dict[str, str], Field(description="The properties for this status layout.")
    ]
    status_reference: Annotated[
        str,
        Field(
            alias="statusReference",
            description="A unique ID which the status will use to refer to this layout configuration.",
        ),
    ]


class StatusMappingDTO(BaseModel):
    model_config = ConfigDict(
        extra="allow",
    )
    issue_type_id: Annotated[
        str, Field(alias="issueTypeId", description="The issue type for the status mapping.")
    ]
    project_id: Annotated[
        str, Field(alias="projectId", description="The project for the status mapping.")
    ]
    status_migrations: Annotated[
        list[StatusMigration],
        Field(
            alias="statusMigrations",
            description="The list of old and new status ID mappings for the specified project and issue type.",
        ),
    ]


class TransitionPreview(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    actions: Annotated[
        list[PreviewRuleConfiguration | None] | None,
        Field(description="The post-functions of the transition."),
    ] = None
    conditions: PreviewConditionGroupConfiguration | None = None
    custom_issue_event_id: Annotated[
        str | None,
        Field(
            alias="customIssueEventId",
            description="The custom issue event ID for the transition.",
        ),
    ] = None
    description: Annotated[str | None, Field(description="The description of the transition.")] = (
        None
    )
    id: Annotated[str | None, Field(description="The ID of the transition.")] = None
    links: Annotated[
        list[TransitionLink] | None,
        Field(
            description="The statuses the transition can start from, and the mapping of ports between the statuses."
        ),
    ] = None
    name: Annotated[str | None, Field(description="The name of the transition.")] = None
    to_status_reference: Annotated[
        str | None,
        Field(alias="toStatusReference", description="The status the transition goes to."),
    ] = None
    transition_screen: Annotated[
        PreviewRuleConfiguration | None, Field(alias="transitionScreen")
    ] = None
    triggers: Annotated[
        list[PreviewTrigger] | None, Field(description="The triggers of the transition.")
    ] = None
    type: Annotated[Type31 | None, Field(description="The transition type.")] = None
    validators: Annotated[
        list[PreviewRuleConfiguration | None] | None,
        Field(description="The validators of the transition."),
    ] = None


class TransitionUpdateDTO(BaseModel):
    model_config = ConfigDict(
        extra="allow",
    )
    actions: Annotated[
        list[WorkflowRuleConfiguration | None] | None,
        Field(description="The post-functions of the transition."),
    ] = None
    conditions: ConditionGroupUpdate | None = None
    custom_issue_event_id: Annotated[
        str | None,
        Field(
            alias="customIssueEventId",
            description="The custom event ID of the transition.",
        ),
    ] = None
    description: Annotated[str | None, Field(description="The description of the transition.")] = (
        None
    )
    id: Annotated[str | None, Field(description="The ID of the transition.")] = None
    links: Annotated[
        list[WorkflowTransitionLinks | None] | None,
        Field(
            description="The statuses the transition can start from, and the mapping of ports between the statuses."
        ),
    ] = None
    name: Annotated[str | None, Field(description="The name of the transition.")] = None
    properties: Annotated[
        dict[str, str] | None, Field(description="The properties of the transition.")
    ] = None
    to_status_reference: Annotated[
        str | None,
        Field(alias="toStatusReference", description="The status the transition goes to."),
    ] = None
    transition_screen: Annotated[
        WorkflowRuleConfiguration | None, Field(alias="transitionScreen")
    ] = None
    triggers: Annotated[
        list[WorkflowTrigger] | None, Field(description="The triggers of the transition.")
    ] = None
    type: Annotated[Type31 | None, Field(description="The transition type.")] = None
    validators: Annotated[
        list[WorkflowRuleConfiguration | None] | None,
        Field(description="The validators of the transition."),
    ] = None


class WorkflowCreate(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    description: Annotated[
        str | None, Field(description="The description of the workflow to create.")
    ] = None
    looped_transition_container_layout: Annotated[
        WorkflowLayout | None, Field(alias="loopedTransitionContainerLayout")
    ] = None
    name: Annotated[str, Field(description="The name of the workflow to create.")]
    start_point_layout: Annotated[WorkflowLayout | None, Field(alias="startPointLayout")] = None
    statuses: Annotated[
        list[StatusLayoutUpdate], Field(description="The statuses associated with this workflow.")
    ]
    transitions: Annotated[
        list[TransitionUpdateDTO], Field(description="The transitions of this workflow.")
    ]


class WorkflowCreateRequest(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    scope: WorkflowScope | None = None
    statuses: Annotated[
        list[WorkflowStatusUpdate] | None,
        Field(description="The statuses to associate with the workflows.", le=1000),
    ] = None
    workflows: Annotated[
        list[WorkflowCreate] | None,
        Field(description="The details of the workflows to create.", le=20),
    ] = None


class WorkflowCreateValidateRequest(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    payload: WorkflowCreateRequest
    validation_options: Annotated[
        ValidationOptionsForCreate | None, Field(alias="validationOptions")
    ] = None


class WorkflowDocumentStatusDTO(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    description: str | None = None
    id: str | None = None
    name: str | None = None
    scope: WorkflowScope | None = None
    status_category: Annotated[str | None, Field(alias="statusCategory")] = None
    status_reference: Annotated[str | None, Field(alias="statusReference")] = None


class WorkflowMetadataAndIssueTypeRestModel(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    issue_type_ids: Annotated[
        list[str],
        Field(
            alias="issueTypeIds",
            description="The list of issue type IDs for the mapping.",
        ),
    ]
    workflow: WorkflowMetadataRestModel


class WorkflowPreviewScope(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    project: WorkflowProjectIdScope | None = None
    type: Annotated[
        Type35 | None,
        Field(
            description="The scope of the workflow. `GLOBAL` for company-managed projects and `PROJECT` for team-managed projects."
        ),
    ] = None


class WorkflowProjectIssueTypeUsageDTO(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    issue_types: Annotated[WorkflowProjectIssueTypeUsagePage | None, Field(alias="issueTypes")] = (
        None
    )
    project_id: Annotated[
        str | None, Field(alias="projectId", description="The ID of the project.")
    ] = None
    workflow_id: Annotated[
        str | None, Field(alias="workflowId", description="The ID of the workflow.")
    ] = None


class WorkflowReferenceStatus(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    approval_configuration: Annotated[
        ApprovalConfiguration | None, Field(alias="approvalConfiguration")
    ] = None
    deprecated: Annotated[
        bool | None, Field(description="Indicates if the status is deprecated.")
    ] = None
    layout: WorkflowStatusLayout | None = None
    properties: Annotated[
        dict[str, str] | None, Field(description="The properties associated with the status.")
    ] = None
    status_reference: Annotated[
        str | None, Field(alias="statusReference", description="The reference of the status.")
    ] = None


class WorkflowSchemeReadResponse(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    default_workflow: Annotated[
        WorkflowMetadataRestModel | None, Field(alias="defaultWorkflow")
    ] = None
    description: Annotated[
        str | None, Field(description="The description of the workflow scheme.")
    ] = None
    id: Annotated[str, Field(description="The ID of the workflow scheme.")]
    name: Annotated[str, Field(description="The name of the workflow scheme.")]
    scope: WorkflowScope
    task_id: Annotated[
        str | None,
        Field(
            alias="taskId",
            description="Indicates if there's an [asynchronous task](#async-operations) for this workflow scheme.",
        ),
    ] = None
    version: DocumentVersion
    workflows_for_issue_types: Annotated[
        list[WorkflowMetadataAndIssueTypeRestModel],
        Field(
            alias="workflowsForIssueTypes",
            description="Mappings from workflows to issue types.",
        ),
    ]


class WorkflowSchemeUpdateRequest(BaseModel):
    model_config = ConfigDict(
        extra="allow",
    )
    default_workflow_id: Annotated[
        str | None,
        Field(
            alias="defaultWorkflowId",
            description="The ID of the workflow for issue types without having a mapping defined in this workflow scheme. Only used in global-scoped workflow schemes. If the `defaultWorkflowId` isn't specified, this is set to *Jira Workflow (jira)*.",
        ),
    ] = None
    description: Annotated[str, Field(description="The new description for this workflow scheme.")]
    id: Annotated[str, Field(description="The ID of this workflow scheme.")]
    name: Annotated[str, Field(description="The new name for this workflow scheme.")]
    status_mappings_by_issue_type_override: Annotated[
        list[MappingsByIssueTypeOverride] | None,
        Field(
            alias="statusMappingsByIssueTypeOverride",
            description="Overrides, for the selected issue types, any status mappings provided in `statusMappingsByWorkflows`. Status mappings are required when the new workflow for an issue type doesn't contain all statuses that the old workflow has. Status mappings can be provided by a combination of `statusMappingsByWorkflows` and `statusMappingsByIssueTypeOverride`.",
        ),
    ] = None
    status_mappings_by_workflows: Annotated[
        list[MappingsByWorkflow] | None,
        Field(
            alias="statusMappingsByWorkflows",
            description="The status mappings by workflows. Status mappings are required when the new workflow for an issue type doesn't contain all statuses that the old workflow has. Status mappings can be provided by a combination of `statusMappingsByWorkflows` and `statusMappingsByIssueTypeOverride`.",
        ),
    ] = None
    version: DocumentVersion
    workflows_for_issue_types: Annotated[
        list[WorkflowSchemeAssociation] | None,
        Field(
            alias="workflowsForIssueTypes",
            description="Mappings from workflows to issue types.",
        ),
    ] = None


class WorkflowSchemeUsageDTO(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    workflow_id: Annotated[
        str | None, Field(alias="workflowId", description="The workflow ID.")
    ] = None
    workflow_schemes: Annotated[WorkflowSchemeUsagePage | None, Field(alias="workflowSchemes")] = (
        None
    )


class WorkflowTransitionRulesUpdate(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    workflows: Annotated[
        list[WorkflowTransitionRules],
        Field(description="The list of workflows with transition rules to update."),
    ]


class WorkflowTransitions(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    actions: Annotated[
        list[WorkflowRuleConfiguration | None] | None,
        Field(description="The post-functions of the transition."),
    ] = None
    conditions: ConditionGroupConfiguration | None = None
    custom_issue_event_id: Annotated[
        str | None,
        Field(
            alias="customIssueEventId",
            description="The custom event ID of the transition.",
        ),
    ] = None
    description: Annotated[str | None, Field(description="The description of the transition.")] = (
        None
    )
    id: Annotated[str | None, Field(description="The ID of the transition.")] = None
    links: Annotated[
        list[WorkflowTransitionLinks | None] | None,
        Field(
            description="The statuses the transition can start from, and the mapping of ports between the statuses."
        ),
    ] = None
    name: Annotated[str | None, Field(description="The name of the transition.")] = None
    properties: Annotated[
        dict[str, str] | None, Field(description="The properties of the transition.")
    ] = None
    to_status_reference: Annotated[
        str | None,
        Field(alias="toStatusReference", description="The status the transition goes to."),
    ] = None
    transition_screen: Annotated[
        WorkflowRuleConfiguration | None, Field(alias="transitionScreen")
    ] = None
    triggers: Annotated[
        list[WorkflowTrigger] | None, Field(description="The triggers of the transition.")
    ] = None
    type: Annotated[Type37 | None, Field(description="The transition type.")] = None
    validators: Annotated[
        list[WorkflowRuleConfiguration | None] | None,
        Field(description="The validators of the transition."),
    ] = None


class WorkflowUpdate(BaseModel):
    model_config = ConfigDict(
        extra="allow",
    )
    default_status_mappings: Annotated[
        list[StatusMigration] | None,
        Field(
            alias="defaultStatusMappings",
            description="The mapping of old to new status ID.",
        ),
    ] = None
    description: Annotated[
        str | None, Field(description="The new description for this workflow.")
    ] = None
    id: Annotated[str, Field(description="The ID of this workflow.")]
    looped_transition_container_layout: Annotated[
        WorkflowLayout | None, Field(alias="loopedTransitionContainerLayout")
    ] = None
    start_point_layout: Annotated[WorkflowLayout | None, Field(alias="startPointLayout")] = None
    status_mappings: Annotated[
        list[StatusMappingDTO] | None,
        Field(
            alias="statusMappings",
            description="The mapping of old to new status ID for a specific project and issue type.",
        ),
    ] = None
    statuses: Annotated[
        list[StatusLayoutUpdate], Field(description="The statuses associated with this workflow.")
    ]
    transitions: Annotated[
        list[TransitionUpdateDTO], Field(description="The transitions of this workflow.")
    ]
    version: DocumentVersion


class WorkflowUpdateRequest(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    statuses: Annotated[
        list[WorkflowStatusUpdate] | None,
        Field(description="The statuses to associate with the workflows.", le=1000),
    ] = None
    workflows: Annotated[
        list[WorkflowUpdate] | None,
        Field(description="The details of the workflows to update.", le=20),
    ] = None


class CreateWorkflowDetails(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    description: Annotated[
        str | None,
        Field(
            description="The description of the workflow. The maximum length is 1000 characters."
        ),
    ] = None
    name: Annotated[
        str,
        Field(
            description="The name of the workflow. The name must be unique. The maximum length is 255 characters. Characters can be separated by a whitespace but the name cannot start or end with a whitespace."
        ),
    ]
    statuses: Annotated[
        list[CreateWorkflowStatusDetails],
        Field(
            description="The statuses of the workflow. Any status that does not include a transition is added to the workflow without a transition."
        ),
    ]
    transitions: Annotated[
        list[CreateWorkflowTransitionDetails],
        Field(
            description="The transitions of the workflow. For the request to be valid, these transitions must:\n\n *  include one *initial* transition.\n *  not use the same name for a *global* and *directed* transition.\n *  have a unique name for each *global* transition.\n *  have a unique 'to' status for each *global* transition.\n *  have unique names for each transition from a status.\n *  not have a 'from' status on *initial* and *global* transitions.\n *  have a 'from' status on *directed* transitions.\n\nAll the transition statuses must be included in `statuses`."
        ),
    ]


class DeprecatedWorkflow(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    default: bool | None = None
    description: Annotated[str | None, Field(description="The description of the workflow.")] = None
    last_modified_date: Annotated[
        str | None,
        Field(
            alias="lastModifiedDate",
            description="The datetime the workflow was last modified.",
        ),
    ] = None
    last_modified_user: Annotated[
        str | None,
        Field(
            alias="lastModifiedUser",
            description="This property is no longer available and will be removed from the documentation soon. See the [deprecation notice](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-user-privacy-api-migration-guide/) for details.",
        ),
    ] = None
    last_modified_user_account_id: Annotated[
        str | None,
        Field(
            alias="lastModifiedUserAccountId",
            description="The account ID of the user that last modified the workflow.",
        ),
    ] = None
    name: Annotated[str | None, Field(description="The name of the workflow.")] = None
    scope: Annotated[Scope | None, Field(description="The scope where this workflow applies")] = (
        None
    )
    steps: Annotated[
        int | None, Field(description="The number of steps included in the workflow.")
    ] = None


class JiraWorkflow(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    created: Annotated[str | None, Field(description="The creation date of the workflow.")] = None
    description: Annotated[str | None, Field(description="The description of the workflow.")] = None
    id: Annotated[str | None, Field(description="The ID of the workflow.")] = None
    is_editable: Annotated[
        bool | None,
        Field(alias="isEditable", description="Indicates if the workflow can be edited."),
    ] = None
    looped_transition_container_layout: Annotated[
        WorkflowLayout | None, Field(alias="loopedTransitionContainerLayout")
    ] = None
    name: Annotated[str | None, Field(description="The name of the workflow.")] = None
    scope: WorkflowScope | None = None
    start_point_layout: Annotated[WorkflowLayout | None, Field(alias="startPointLayout")] = None
    statuses: Annotated[
        list[WorkflowReferenceStatus] | None,
        Field(description="The statuses referenced in this workflow."),
    ] = None
    task_id: Annotated[
        str | None,
        Field(
            alias="taskId",
            description="If there is a current [asynchronous task](#async-operations) operation for this workflow.",
        ),
    ] = None
    transitions: Annotated[
        list[WorkflowTransitions] | None, Field(description="The transitions of the workflow.")
    ] = None
    updated: Annotated[str | None, Field(description="The last edited date of the workflow.")] = (
        None
    )
    version: DocumentVersion | None = None


class JiraWorkflowPreviewStatus(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    description: Annotated[str | None, Field(description="The description of the status.")] = None
    id: Annotated[str | None, Field(description="The ID of the status.")] = None
    name: Annotated[str | None, Field(description="The name of the status.")] = None
    raw_name: Annotated[
        str | None, Field(alias="rawName", description="The raw name of the status.")
    ] = None
    scope: WorkflowPreviewScope | None = None
    status_category: Annotated[
        StatusCategory | None,
        Field(alias="statusCategory", description="The category of the status."),
    ] = None
    status_reference: Annotated[
        str | None,
        Field(
            alias="statusReference",
            description="The reference of the status. Unique within this response but not guaranteed to be stable across requests.",
        ),
    ] = None


class PageBeanWorkflowTransitionRules(BaseModel):
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
        list[WorkflowTransitionRules] | None, Field(description="The list of items.")
    ] = None


class WorkflowCreateResponse(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    statuses: Annotated[
        list[JiraWorkflowStatus] | None, Field(description="List of created statuses.")
    ] = None
    workflows: Annotated[
        list[JiraWorkflow] | None, Field(description="List of created workflows.")
    ] = None


class WorkflowDocumentDTO(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    created: str | None = None
    description: str | None = None
    id: str | None = None
    last_update_author_aaid: Annotated[str | None, Field(alias="lastUpdateAuthorAAID")] = None
    looped_transition_container_layout: Annotated[
        WorkflowLayout | None, Field(alias="loopedTransitionContainerLayout")
    ] = None
    name: str | None = None
    scope: WorkflowScope | None = None
    start_point_layout: Annotated[WorkflowLayout | None, Field(alias="startPointLayout")] = None
    statuses: list[WorkflowReferenceStatus] | None = None
    transitions: list[WorkflowTransitions] | None = None
    updated: str | None = None
    version: DocumentVersion | None = None


class WorkflowHistoryReadResponseDTO(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    statuses: list[WorkflowDocumentStatusDTO] | None = None
    workflows: list[WorkflowDocumentDTO] | None = None


class WorkflowPreview(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    description: Annotated[str | None, Field(description="The description of the workflow.")] = None
    id: Annotated[str | None, Field(description="The ID of the workflow.")] = None
    looped_transition_container_layout: Annotated[
        WorkflowPreviewLayout | None, Field(alias="loopedTransitionContainerLayout")
    ] = None
    name: Annotated[str | None, Field(description="The name of the workflow.")] = None
    query_context: Annotated[
        list[ProjectIssueTypeQueryContext] | None,
        Field(
            alias="queryContext",
            description="The project and issue type context for this workflow query.",
        ),
    ] = None
    scope: WorkflowPreviewScope | None = None
    start_point_layout: Annotated[WorkflowPreviewLayout | None, Field(alias="startPointLayout")] = (
        None
    )
    statuses: Annotated[
        list[WorkflowPreviewStatus] | None,
        Field(description="The statuses referenced in this workflow."),
    ] = None
    transitions: Annotated[
        list[TransitionPreview] | None, Field(description="The transitions of the workflow.")
    ] = None
    version: WorkflowDocumentVersion | None = None


class WorkflowPreviewResponse(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    statuses: Annotated[
        list[JiraWorkflowPreviewStatus] | None,
        Field(description="The list of statuses referenced by the workflows."),
    ] = None
    workflows: Annotated[
        list[WorkflowPreview] | None,
        Field(
            description="The list of workflows. The workflows are returned in the same order as specified in the request."
        ),
    ] = None


class WorkflowReadResponse(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    statuses: Annotated[list[JiraWorkflowStatus] | None, Field(description="List of statuses.")] = (
        None
    )
    workflows: Annotated[list[JiraWorkflow] | None, Field(description="List of workflows.")] = None


class WorkflowScheme(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    default_workflow: Annotated[
        str | None,
        Field(
            alias="defaultWorkflow",
            description="The name of the default workflow for the workflow scheme. The default workflow has *All Unassigned Issue Types* assigned to it in Jira. If `defaultWorkflow` is not specified when creating a workflow scheme, it is set to *Jira Workflow (jira)*.",
        ),
    ] = None
    description: Annotated[
        str | None, Field(description="The description of the workflow scheme.")
    ] = None
    draft: Annotated[
        bool | None, Field(description="Whether the workflow scheme is a draft or not.")
    ] = None
    id: Annotated[int | None, Field(description="The ID of the workflow scheme.")] = None
    issue_type_mappings: Annotated[
        dict[str, str] | None,
        Field(
            alias="issueTypeMappings",
            description="The issue type to workflow mappings, where each mapping is an issue type ID and workflow name pair. Note that an issue type can only be mapped to one workflow in a workflow scheme.",
        ),
    ] = None
    issue_types: Annotated[
        dict[str, IssueTypeDetails] | None,
        Field(alias="issueTypes", description="The issue types available in Jira."),
    ] = None
    last_modified: Annotated[
        str | None,
        Field(
            alias="lastModified",
            description="The date-time that the draft workflow scheme was last modified. A modification is a change to the issue type-project mappings only. This property does not apply to non-draft workflows.",
        ),
    ] = None
    last_modified_user: Annotated[
        User | None,
        Field(
            alias="lastModifiedUser",
            description="The user that last modified the draft workflow scheme. A modification is a change to the issue type-project mappings only. This property does not apply to non-draft workflows.",
        ),
    ] = None
    name: Annotated[
        str | None,
        Field(
            description="The name of the workflow scheme. The name must be unique. The maximum length is 255 characters. Required when creating a workflow scheme."
        ),
    ] = None
    original_default_workflow: Annotated[
        str | None,
        Field(
            alias="originalDefaultWorkflow",
            description="For draft workflow schemes, this property is the name of the default workflow for the original workflow scheme. The default workflow has *All Unassigned Issue Types* assigned to it in Jira.",
        ),
    ] = None
    original_issue_type_mappings: Annotated[
        dict[str, str] | None,
        Field(
            alias="originalIssueTypeMappings",
            description="For draft workflow schemes, this property is the issue type to workflow mappings for the original workflow scheme, where each mapping is an issue type ID and workflow name pair. Note that an issue type can only be mapped to one workflow in a workflow scheme.",
        ),
    ] = None
    self: AnyUrl | None = None
    update_draft_if_needed: Annotated[
        bool | None,
        Field(
            alias="updateDraftIfNeeded",
            description="Whether to create or update a draft workflow scheme when updating an active workflow scheme. An active workflow scheme is a workflow scheme that is used by at least one project. The following examples show how this property works:\n\n *  Update an active workflow scheme with `updateDraftIfNeeded` set to `true`: If a draft workflow scheme exists, it is updated. Otherwise, a draft workflow scheme is created.\n *  Update an active workflow scheme with `updateDraftIfNeeded` set to `false`: An error is returned, as active workflow schemes cannot be updated.\n *  Update an inactive workflow scheme with `updateDraftIfNeeded` set to `true`: The workflow scheme is updated, as inactive workflow schemes do not require drafts to update.\n\nDefaults to `false`.",
        ),
    ] = None


class WorkflowSchemeAssociations(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    project_ids: Annotated[
        list[str],
        Field(
            alias="projectIds",
            description="The list of projects that use the workflow scheme.",
        ),
    ]
    workflow_scheme: Annotated[
        WorkflowScheme, Field(alias="workflowScheme", description="The workflow scheme.")
    ]


class WorkflowSearchResponse(BaseModel):
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
        Field(
            alias="nextPage",
            description="If there is another page of results, the URL of the next page.",
        ),
    ] = None
    self: Annotated[str | None, Field(description="The URL of the page.")] = None
    start_at: Annotated[
        int | None, Field(alias="startAt", description="The index of the first item returned.")
    ] = None
    statuses: Annotated[list[JiraWorkflowStatus] | None, Field(description="List of statuses.")] = (
        None
    )
    total: Annotated[int | None, Field(description="The number of items returned.")] = None
    values: Annotated[list[JiraWorkflow] | None, Field(description="List of workflows.")] = None


class WorkflowUpdateResponse(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    statuses: Annotated[
        list[JiraWorkflowStatus] | None, Field(description="List of updated statuses.")
    ] = None
    task_id: Annotated[
        str | None,
        Field(
            alias="taskId",
            description="If there is a [asynchronous task](#async-operations) operation, as a result of this update.",
        ),
    ] = None
    workflows: Annotated[
        list[JiraWorkflow] | None, Field(description="List of updated workflows.")
    ] = None


class ContainerOfWorkflowSchemeAssociations(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    values: Annotated[
        list[WorkflowSchemeAssociations],
        Field(
            description="A list of workflow schemes together with projects they are associated with."
        ),
    ]


class PageBeanWorkflowScheme(BaseModel):
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
    values: Annotated[list[WorkflowScheme] | None, Field(description="The list of items.")] = None


class PageBeanWorkflow(BaseModel):
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
    values: Annotated[list[Workflow] | None, Field(description="The list of items.")] = None


class Transition(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    description: Annotated[str, Field(description="The description of the transition.")]
    from_: Annotated[
        list[str], Field(alias="from", description="The statuses the transition can start from.")
    ]
    id: Annotated[str, Field(description="The ID of the transition.")]
    name: Annotated[str, Field(description="The name of the transition.")]
    properties: Annotated[
        dict[str, Any] | None, Field(description="The properties of the transition.")
    ] = None
    rules: WorkflowRules | None = None
    screen: TransitionScreenDetails | None = None
    to: Annotated[str, Field(description="The status the transition goes to.")]
    type: Annotated[Type29, Field(description="The type of the transition.")]


class Workflow(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    created: Annotated[
        AwareDatetime | None, Field(description="The creation date of the workflow.")
    ] = None
    description: Annotated[str, Field(description="The description of the workflow.")]
    has_draft_workflow: Annotated[
        bool | None,
        Field(
            alias="hasDraftWorkflow",
            description="Whether the workflow has a draft version.",
        ),
    ] = None
    id: PublishedWorkflowId
    is_default: Annotated[
        bool | None, Field(alias="isDefault", description="Whether this is the default workflow.")
    ] = None
    operations: WorkflowOperations | None = None
    projects: Annotated[
        list[ProjectDetails] | None,
        Field(description="The projects the workflow is assigned to, through workflow schemes."),
    ] = None
    schemes: Annotated[
        list[WorkflowSchemeIdName] | None,
        Field(description="The workflow schemes the workflow is assigned to."),
    ] = None
    statuses: Annotated[
        list[WorkflowStatus] | None, Field(description="The statuses of the workflow.")
    ] = None
    transitions: Annotated[
        list[Transition] | None, Field(description="The transitions of the workflow.")
    ] = None
    updated: Annotated[
        AwareDatetime | None, Field(description="The last edited date of the workflow.")
    ] = None


class WorkflowCompoundCondition(BaseModel):
    conditions: Annotated[
        list[WorkflowSimpleCondition | WorkflowCompoundCondition],
        Field(description="The list of workflow conditions."),
    ]
    node_type: Annotated[Literal["compound"], Field(alias="nodeType")]
    operator: Annotated[Operator5, Field(description="The compound condition operator.")]


class WorkflowRules(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    conditions_tree: Annotated[
        WorkflowSimpleCondition | WorkflowCompoundCondition | None,
        Field(
            alias="conditionsTree",
            description="The workflow transition rule conditions tree.",
        ),
    ] = None
    post_functions: Annotated[
        list[WorkflowTransitionRule] | None,
        Field(alias="postFunctions", description="The workflow post functions."),
    ] = None
    validators: Annotated[
        list[WorkflowTransitionRule] | None, Field(description="The workflow validators.")
    ] = None


__all__ = [
    "ApprovalConfiguration",
    "ApprovalConfigurationPreview",
    "AvailableWorkflowConnectRule",
    "AvailableWorkflowForgeRule",
    "AvailableWorkflowSystemRule",
    "AvailableWorkflowTriggerTypes",
    "AvailableWorkflowTriggers",
    "CreateWorkflowCondition",
    "CreateWorkflowStatusDetails",
    "CreateWorkflowTransitionRule",
    "CreateWorkflowTransitionRulesDetails",
    "CreateWorkflowTransitionScreenDetails",
    "DefaultWorkflow",
    "DefaultWorkflowEditorResponse",
    "DocumentVersion",
    "IssueTypeWorkflowMapping",
    "IssueTypesWorkflowMapping",
    "PreviewRuleConfiguration",
    "PreviewTrigger",
    "ProjectAndIssueTypePair",
    "ProjectIssueTypeQueryContext",
    "ProjectUsage",
    "ProjectUsagePage",
    "PublishedWorkflowId",
    "RequiredMappingByIssueType",
    "RequiredMappingByWorkflows",
    "StatusMapping",
    "StatusMetadata",
    "StatusMigration",
    "StatusesPerWorkflow",
    "TransitionLink",
    "TransitionScreenDetails",
    "ValidationOptionsForCreate",
    "ValidationOptionsForUpdate",
    "WorkflowAssociationStatusMapping",
    "WorkflowCapabilities",
    "WorkflowElementReference",
    "WorkflowHistoryItemDTO",
    "WorkflowHistoryListRequest",
    "WorkflowHistoryListResponseDTO",
    "WorkflowHistoryReadRequest",
    "WorkflowIDs",
    "WorkflowLayout",
    "WorkflowMetadataRestModel",
    "WorkflowOperations",
    "WorkflowPreviewLayout",
    "WorkflowPreviewRequest",
    "WorkflowPreviewStatus",
    "WorkflowProjectIdScope",
    "WorkflowProjectIssueTypeUsage",
    "WorkflowProjectIssueTypeUsagePage",
    "WorkflowProjectUsageDTO",
    "WorkflowReadRequest",
    "WorkflowRuleConfiguration",
    "WorkflowSchemeAssociation",
    "WorkflowSchemeIdName",
    "WorkflowSchemeProjectAssociation",
    "WorkflowSchemeProjectUsageDTO",
    "WorkflowSchemeReadRequest",
    "WorkflowSchemeUpdateRequiredMappingsRequest",
    "WorkflowSchemeUpdateRequiredMappingsResponse",
    "WorkflowSchemeUsage",
    "WorkflowSchemeUsagePage",
    "WorkflowScope",
    "WorkflowSimpleCondition",
    "WorkflowStatus",
    "WorkflowStatusLayout",
    "WorkflowStatusUpdate",
    "WorkflowTransitionLinks",
    "WorkflowTransitionRule",
    "WorkflowTransitionRulesDetails",
    "WorkflowTransitionRulesUpdateErrorDetails",
    "WorkflowTransitionRulesUpdateErrors",
    "WorkflowTrigger",
    "WorkflowValidationError",
    "WorkflowValidationErrorList",
    "WorkflowsWithTransitionRulesDetails",
    "ConditionGroupConfiguration",
    "ConditionGroupUpdate",
    "CreateWorkflowTransitionDetails",
    "JiraWorkflowStatus",
    "MappingsByIssueTypeOverride",
    "MappingsByWorkflow",
    "PreviewConditionGroupConfiguration",
    "PublishDraftWorkflowScheme",
    "StatusLayoutUpdate",
    "StatusMappingDTO",
    "TransitionPreview",
    "TransitionUpdateDTO",
    "WorkflowCreate",
    "WorkflowCreateRequest",
    "WorkflowCreateValidateRequest",
    "WorkflowDocumentStatusDTO",
    "WorkflowMetadataAndIssueTypeRestModel",
    "WorkflowPreviewScope",
    "WorkflowProjectIssueTypeUsageDTO",
    "WorkflowReferenceStatus",
    "WorkflowSchemeReadResponse",
    "WorkflowSchemeUpdateRequest",
    "WorkflowSchemeUsageDTO",
    "WorkflowTransitionRulesUpdate",
    "WorkflowTransitions",
    "WorkflowUpdate",
    "WorkflowUpdateRequest",
    "CreateWorkflowDetails",
    "DeprecatedWorkflow",
    "JiraWorkflow",
    "JiraWorkflowPreviewStatus",
    "PageBeanWorkflowTransitionRules",
    "WorkflowCreateResponse",
    "WorkflowDocumentDTO",
    "WorkflowHistoryReadResponseDTO",
    "WorkflowPreview",
    "WorkflowPreviewResponse",
    "WorkflowReadResponse",
    "WorkflowScheme",
    "WorkflowSchemeAssociations",
    "WorkflowSearchResponse",
    "WorkflowUpdateResponse",
    "ContainerOfWorkflowSchemeAssociations",
    "PageBeanWorkflowScheme",
    "PageBeanWorkflow",
    "Transition",
    "Workflow",
    "WorkflowCompoundCondition",
    "WorkflowRules",
]
