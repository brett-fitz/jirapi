"""Pydantic models for the issues domain."""

from __future__ import annotations

from typing import Annotated, Any, Literal
from uuid import UUID

from pydantic import AnyUrl, AwareDatetime, Base64Str, BaseModel, ConfigDict, Field, RootModel

from jirapi.models._shared import Type15


class Application(BaseModel):
    model_config = ConfigDict(
        extra="allow",
    )
    name: Annotated[
        str | None,
        Field(
            description='The name of the application. Used in conjunction with the (remote) object icon title to display a tooltip for the link\'s icon. The tooltip takes the format "\\[application name\\] icon title". Blank items are excluded from the tooltip title. If both items are blank, the icon tooltop displays as "Web Link". Grouping and sorting of links may place links without an application name last.'
        ),
    ] = None
    type: Annotated[
        str | None,
        Field(
            description="The name-spaced type of the application, used by registered rendering apps."
        ),
    ] = None


class ArchiveIssueAsyncRequest(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    jql: str | None = None


class AttachmentArchiveEntry(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    abbreviated_name: Annotated[str | None, Field(alias="abbreviatedName")] = None
    entry_index: Annotated[int | None, Field(alias="entryIndex")] = None
    media_type: Annotated[str | None, Field(alias="mediaType")] = None
    name: str | None = None
    size: int | None = None


class AttachmentArchiveImpl(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    entries: Annotated[
        list[AttachmentArchiveEntry] | None,
        Field(description="The list of the items included in the archive."),
    ] = None
    total_entry_count: Annotated[
        int | None,
        Field(alias="totalEntryCount", description="The number of items in the archive."),
    ] = None


class AttachmentArchiveItemReadable(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    index: Annotated[
        int | None, Field(description="The position of the item within the archive.")
    ] = None
    label: Annotated[str | None, Field(description="The label for the archive item.")] = None
    media_type: Annotated[
        str | None, Field(alias="mediaType", description="The MIME type of the archive item.")
    ] = None
    path: Annotated[str | None, Field(description="The path of the archive item.")] = None
    size: Annotated[str | None, Field(description="The size of the archive item.")] = None


class AttachmentArchiveMetadataReadable(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    entries: Annotated[
        list[AttachmentArchiveItemReadable] | None,
        Field(description="The list of the items included in the archive."),
    ] = None
    id: Annotated[int | None, Field(description="The ID of the attachment.")] = None
    media_type: Annotated[
        str | None, Field(alias="mediaType", description="The MIME type of the attachment.")
    ] = None
    name: Annotated[str | None, Field(description="The name of the archive file.")] = None
    total_entry_count: Annotated[
        int | None,
        Field(
            alias="totalEntryCount",
            description="The number of items included in the archive.",
        ),
    ] = None


class AttachmentSettings(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    enabled: Annotated[
        bool | None, Field(description="Whether the ability to add attachments is enabled.")
    ] = None
    upload_limit: Annotated[
        int | None,
        Field(
            alias="uploadLimit",
            description="The maximum size of attachments permitted, in bytes.",
        ),
    ] = None


class BulkIssueIsWatching(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    issues_is_watching: Annotated[
        dict[str, bool] | None,
        Field(
            alias="issuesIsWatching",
            description="The map of issue ID to boolean watch status.",
        ),
    ] = None


class BulkTransitionSubmitInput(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    selected_issue_ids_or_keys: Annotated[
        list[str],
        Field(
            alias="selectedIssueIdsOrKeys",
            description="List of all the issue IDs or keys that are to be bulk transitioned.",
        ),
    ]
    transition_id: Annotated[
        str,
        Field(
            alias="transitionId",
            description="The ID of the transition that is to be performed on the issues.",
        ),
    ]


class ChangeDetails(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    field: Annotated[str | None, Field(description="The name of the field changed.")] = None
    field_id: Annotated[
        str | None, Field(alias="fieldId", description="The ID of the field changed.")
    ] = None
    fieldtype: Annotated[str | None, Field(description="The type of the field changed.")] = None
    from_: Annotated[
        str | None, Field(alias="from", description="The details of the original value.")
    ] = None
    from_string: Annotated[
        str | None,
        Field(
            alias="fromString",
            description="The details of the original value as a string.",
        ),
    ] = None
    to: Annotated[str | None, Field(description="The details of the new value.")] = None
    to_string: Annotated[
        str | None, Field(alias="toString", description="The details of the new value as a string.")
    ] = None


class ContentItem(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    entity_id: Annotated[
        str,
        Field(
            alias="entityId",
            description="The ID of the content entity.\n\n *  For redacting an issue field, this will be the field ID (e.g., summary, customfield\\_10000).\n *  For redacting a comment, this will be the comment ID.\n *  For redacting a worklog, this will be the worklog ID.",
            examples=["summary"],
        ),
    ]
    entity_type: Annotated[
        EntityType,
        Field(
            alias="entityType",
            description="The type of the entity to redact; It will be one of the following:\n\n *  **issuefieldvalue** \\- To redact in issue fields\n *  **issue-comment** \\- To redact in issue comments.\n *  **issue-worklog** \\- To redact in issue worklogs",
        ),
    ]
    id: Annotated[str, Field(description="This would be the issue ID", examples=["10000"])]


class DateRangeFilterRequest(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    date_after: Annotated[
        str,
        Field(
            alias="dateAfter",
            description="List issues archived after a specified date, passed in the YYYY-MM-DD format.",
        ),
    ]
    date_before: Annotated[
        str,
        Field(
            alias="dateBefore",
            description="List issues archived before a specified date provided in the YYYY-MM-DD format.",
        ),
    ]


class Error(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    count: int | None = None
    issue_ids_or_keys: Annotated[list[str] | None, Field(alias="issueIdsOrKeys")] = None
    message: str | None = None


class Errors(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    issue_is_subtask: Annotated[Error | None, Field(alias="issueIsSubtask")] = None
    issues_in_archived_projects: Annotated[
        Error | None, Field(alias="issuesInArchivedProjects")
    ] = None
    issues_in_unlicensed_projects: Annotated[
        Error | None, Field(alias="issuesInUnlicensedProjects")
    ] = None
    issues_not_found: Annotated[Error | None, Field(alias="issuesNotFound")] = None
    user_does_not_have_permission: Annotated[
        Error | None, Field(alias="userDoesNotHavePermission")
    ] = None


class ExportArchivedIssuesTaskProgressResponse(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    file_url: Annotated[str | None, Field(alias="fileUrl")] = None
    payload: str | None = None
    progress: int | None = None
    status: str | None = None
    submitted_time: Annotated[AwareDatetime | None, Field(alias="submittedTime")] = None
    task_id: Annotated[str | None, Field(alias="taskId")] = None


class FieldUpdateOperation(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    add: Annotated[
        Any | None, Field(description="The value to add to the field.", examples=["triaged"])
    ] = None
    copy_: Annotated[
        Any | None,
        Field(
            alias="copy",
            description="The field value to copy from another issue.",
            examples=[{"issuelinks": {"sourceIssues": [{"key": "FP-5"}]}}],
        ),
    ] = None
    edit: Annotated[
        Any | None,
        Field(
            description="The value to edit in the field.",
            examples=[{"originalEstimate": "1w 1d", "remainingEstimate": "4d"}],
        ),
    ] = None
    remove: Annotated[
        Any | None, Field(description="The value to removed from the field.", examples=["blocker"])
    ] = None
    set: Annotated[
        Any | None, Field(description="The value to set in the field.", examples=["A new summary"])
    ] = None


class HistoryMetadataParticipant(BaseModel):
    model_config = ConfigDict(
        extra="allow",
    )
    avatar_url: Annotated[
        str | None,
        Field(
            alias="avatarUrl",
            description="The URL to an avatar for the user or system associated with a history record.",
        ),
    ] = None
    display_name: Annotated[
        str | None,
        Field(
            alias="displayName",
            description="The display name of the user or system associated with a history record.",
        ),
    ] = None
    display_name_key: Annotated[
        str | None,
        Field(
            alias="displayNameKey",
            description="The key of the display name of the user or system associated with a history record.",
        ),
    ] = None
    id: Annotated[
        str | None,
        Field(description="The ID of the user or system associated with a history record."),
    ] = None
    type: Annotated[
        str | None,
        Field(description="The type of the user or system associated with a history record."),
    ] = None
    url: Annotated[
        str | None,
        Field(description="The URL of the user or system associated with a history record."),
    ] = None


class Icon(BaseModel):
    model_config = ConfigDict(
        extra="allow",
    )
    link: Annotated[
        str | None,
        Field(
            description="The URL of the tooltip, used only for a status icon. If not set, the status icon in Jira is not clickable."
        ),
    ] = None
    title: Annotated[
        str | None,
        Field(
            description='The title of the icon. This is used as follows:\n\n *  For a status icon it is used as a tooltip on the icon. If not set, the status icon doesn\'t display a tooltip in Jira.\n *  For the remote object icon it is used in conjunction with the application name to display a tooltip for the link\'s icon. The tooltip takes the format "\\[application name\\] icon title". Blank itemsare excluded from the tooltip title. If both items are blank, the icon tooltop displays as "Web Link".'
        ),
    ] = None
    url16x16: Annotated[
        str | None, Field(description="The URL of an icon that displays at 16x16 pixel in Jira.")
    ] = None


class IncludedFields(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    actually_included: Annotated[list[str] | None, Field(alias="actuallyIncluded")] = None
    excluded: list[str] | None = None
    included: list[str] | None = None


class IssueArchivalSyncRequest(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    issue_ids_or_keys: Annotated[list[str] | None, Field(alias="issueIdsOrKeys")] = None


class IssueArchivalSyncResponse(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    errors: Errors | None = None
    number_of_issues_updated: Annotated[int | None, Field(alias="numberOfIssuesUpdated")] = None


class IssueBulkDeletePayload(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    selected_issue_ids_or_keys: Annotated[
        list[str],
        Field(
            alias="selectedIssueIdsOrKeys",
            description="List of issue IDs or keys which are to be bulk deleted. These IDs or keys can be from different projects and issue types.",
        ),
    ]
    send_bulk_notification: Annotated[
        bool | None,
        Field(
            alias="sendBulkNotification",
            description="A boolean value that indicates whether to send a bulk change notification when the issues are being deleted.\n\nIf `true`, dispatches a bulk notification email to users about the updates.",
        ),
    ] = True


class IssueBulkOperationsFieldOption(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )


class IssueBulkTransitionPayload(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    bulk_transition_inputs: Annotated[
        list[BulkTransitionSubmitInput],
        Field(
            alias="bulkTransitionInputs",
            description="List of objects and each object has two properties:\n\n *  Issues that will be bulk transitioned.\n *  TransitionId that corresponds to a specific transition of issues that share the same workflow.",
        ),
    ]
    send_bulk_notification: Annotated[
        bool | None,
        Field(
            alias="sendBulkNotification",
            description="A boolean value that indicates whether to send a bulk change notification when the issues are being transitioned.\n\nIf `true`, dispatches a bulk notification email to users about the updates.",
        ),
    ] = True


class IssueBulkWatchOrUnwatchPayload(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    selected_issue_ids_or_keys: Annotated[
        list[str],
        Field(
            alias="selectedIssueIdsOrKeys",
            description="List of issue IDs or keys which are to be bulk watched or unwatched. These IDs or keys can be from different projects and issue types.",
        ),
    ]


class IssueChangelogIds(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    changelog_ids: Annotated[
        list[int], Field(alias="changelogIds", description="The list of changelog IDs.")
    ]


class IssueError(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    error_message: Annotated[
        str | None,
        Field(
            alias="errorMessage",
            description="The error that occurred when fetching this issue.",
        ),
    ] = None
    id: Annotated[str | None, Field(description="The ID of the issue.")] = None


class IssueEvent(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    id: Annotated[int | None, Field(description="The ID of the event.")] = None
    name: Annotated[str | None, Field(description="The name of the event.")] = None


class IssueFilterForBulkPropertyDelete(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    current_value: Annotated[
        Any | None,
        Field(
            alias="currentValue",
            description="The value of properties to perform the bulk operation on.",
        ),
    ] = None
    entity_ids: Annotated[
        list[int] | None,
        Field(
            alias="entityIds",
            description="List of issues to perform the bulk delete operation on.",
        ),
    ] = None


class IssueFilterForBulkPropertySet(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    current_value: Annotated[
        Any | None,
        Field(
            alias="currentValue",
            description="The value of properties to perform the bulk operation on.",
        ),
    ] = None
    entity_ids: Annotated[
        list[int] | None,
        Field(
            alias="entityIds",
            description="List of issues to perform the bulk operation on.",
        ),
    ] = None
    has_property: Annotated[
        bool | None,
        Field(
            alias="hasProperty",
            description="Whether the bulk operation occurs only when the property is present on or absent from an issue.",
        ),
    ] = None


class IssueList(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    issue_ids: Annotated[list[str], Field(alias="issueIds", description="The list of issue IDs.")]


class IssueMatchesForJQL(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    errors: Annotated[list[str], Field(description="A list of errors.")]
    matched_issues: Annotated[
        list[int], Field(alias="matchedIssues", description="A list of issue IDs.")
    ]


class IssueTransitionStatus(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    status_id: Annotated[
        int | None, Field(alias="statusId", description="The unique ID of the status.")
    ] = None
    status_name: Annotated[
        str | None, Field(alias="statusName", description="The name of the status.")
    ] = None


class IssuesAndJQLQueries(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    issue_ids: Annotated[list[int], Field(alias="issueIds", description="A list of issue IDs.")]
    jqls: Annotated[list[str], Field(description="A list of JQL queries.")]


class JiraColorInput(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    name: str


class JiraComponentField(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    component_id: Annotated[int, Field(alias="componentId")]


class JiraDateInput(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    formatted_date: Annotated[str, Field(alias="formattedDate")]


class JiraDateTimeInput(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    formatted_date_time: Annotated[str, Field(alias="formattedDateTime")]


class JiraDurationField(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    original_estimate_field: Annotated[str, Field(alias="originalEstimateField")]


class JiraGroupInput(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    group_name: Annotated[str, Field(alias="groupName")]


class JiraIssueTypeField(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    issue_type_id: Annotated[str, Field(alias="issueTypeId")]


class JiraLabelPropertiesInputJackson1(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    color: Color1 | None = None
    name: str | None = None


class JiraLabelsInput(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    name: str


class JiraMultiSelectComponentField(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    bulk_edit_multi_select_field_option: Annotated[
        BulkEditMultiSelectFieldOption, Field(alias="bulkEditMultiSelectFieldOption")
    ]
    components: list[JiraComponentField]
    field_id: Annotated[str, Field(alias="fieldId")]


class JiraMultipleGroupPickerField(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    field_id: Annotated[str, Field(alias="fieldId")]
    groups: list[JiraGroupInput]


class JiraNumberField(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    field_id: Annotated[str, Field(alias="fieldId")]
    value: float | None = None


class JiraPriorityField(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    priority_id: Annotated[str, Field(alias="priorityId")]


class JiraRichTextInput(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    adf_value: Annotated[dict[str, Any] | None, Field(alias="adfValue")] = None


class JiraSelectedOptionField(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    option_id: Annotated[int | None, Field(alias="optionId")] = None


class JiraSingleGroupPickerField(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    field_id: Annotated[str, Field(alias="fieldId")]
    group: JiraGroupInput


class JiraSingleLineTextField(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    field_id: Annotated[str, Field(alias="fieldId")]
    text: str


class JiraSingleSelectField(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    field_id: Annotated[str, Field(alias="fieldId")]
    option: JiraSelectedOptionField


class JiraStatusInput(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    status_id: Annotated[str, Field(alias="statusId")]


class JiraTimeTrackingField(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    time_remaining: Annotated[str, Field(alias="timeRemaining")]


class JiraUrlField(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    field_id: Annotated[str, Field(alias="fieldId")]
    url: str


class JiraUserField(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    account_id: Annotated[str, Field(alias="accountId")]


class JiraVersionField(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    version_id: Annotated[str | None, Field(alias="versionId")] = None


class LegacyJackson1ListIssueEvent(RootModel[list[IssueEvent]]):
    root: list[IssueEvent]


class MandatoryFieldValue(BaseModel):
    retain: Annotated[
        bool | None,
        Field(
            description="If `true`, will try to retain original non-null issue field values on move."
        ),
    ] = True
    type: Annotated[
        Type15 | None,
        Field(description="Will treat as `MandatoryFieldValue` if type is `raw` or `empty`"),
    ] = Type15.raw
    value: Annotated[
        list[str],
        Field(description="Value for each field. Provide a `list of strings` for non-ADF fields."),
    ]


class MandatoryFieldValueForADF(BaseModel):
    retain: Annotated[
        bool | None,
        Field(
            description="If `true`, will try to retain original non-null issue field values on move."
        ),
    ] = True
    type: Annotated[
        Type15, Field(description="Will treat as `MandatoryFieldValueForADF` if type is `adf`")
    ]
    value: Annotated[
        dict[str, Any],
        Field(
            description="Value for each field. Accepts Atlassian Document Format (ADF) for rich text fields like `description`, `environments`. For ADF format details, refer to: [Atlassian Document Format](https://developer.atlassian.com/cloud/jira/platform/apis/document/structure)"
        ),
    ]


class RedactionPosition(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    adf_pointer: Annotated[
        str | None,
        Field(
            alias="adfPointer",
            description="The ADF pointer indicating the position of the text to be redacted. This is only required when redacting from rich text(ADF) fields. For plain text fields, this field can be omitted.",
            examples=["/content/0/content/0/text"],
        ),
    ] = None
    expected_text: Annotated[
        str,
        Field(
            alias="expectedText",
            description="The text which will be redacted, encoded using SHA256 hash and Base64 digest",
            examples=[
                "ODFiNjM3ZDhmY2QyYzZkYTYzNTllNjk2MzExM2ExMTcwZGU3OTVlNGI3MjViODRkMWUwYjRjZmQ5ZWM1OGNlOQ=="
            ],
        ),
    ]
    from_: Annotated[
        int,
        Field(
            alias="from",
            description="The start index(inclusive) for the redaction in specified content",
            examples=[14],
        ),
    ]
    to: Annotated[
        int,
        Field(
            description="The ending index(exclusive) for the redaction in specified content",
            examples=[20],
        ),
    ]


class RemoteIssueLinkIdentifies(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    id: Annotated[
        int | None,
        Field(
            description="The ID of the remote issue link, such as the ID of the item on the remote system."
        ),
    ] = None
    self: Annotated[str | None, Field(description="The URL of the remote issue link.")] = None


class Resource(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    description: str | None = None
    file: bytes | None = None
    filename: str | None = None
    input_stream: Annotated[dict[str, Any] | None, Field(alias="inputStream")] = None
    open: bool | None = None
    readable: bool | None = None
    uri: AnyUrl | None = None
    url: str | None = None


class RestrictedPermission(BaseModel):
    model_config = ConfigDict(
        extra="allow",
    )
    id: Annotated[
        str | None,
        Field(
            description="The ID of the permission. Either `id` or `key` must be specified. Use [Get all permissions](#api-rest-api-3-permissions-get) to get the list of permissions."
        ),
    ] = None
    key: Annotated[
        str | None,
        Field(
            description="The key of the permission. Either `id` or `key` must be specified. Use [Get all permissions](#api-rest-api-3-permissions-get) to get the list of permissions."
        ),
    ] = None


class SimplifiedIssueTransition(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    to: Annotated[
        IssueTransitionStatus | None,
        Field(description="The issue status change of the transition."),
    ] = None
    transition_id: Annotated[
        int | None, Field(alias="transitionId", description="The unique ID of the transition.")
    ] = None
    transition_name: Annotated[
        str | None, Field(alias="transitionName", description="The name of the transition.")
    ] = None


class SingleRedactionRequest(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    content_item: Annotated[ContentItem, Field(alias="contentItem")]
    external_id: Annotated[
        UUID,
        Field(
            alias="externalId",
            description="Unique id for the redaction request; ID format should be of UUID",
            examples=["51101de6-d001-429d-a095-b2b96dd57fcb"],
        ),
    ]
    reason: Annotated[
        str,
        Field(
            description="The reason why the content is being redacted",
            examples=["PII data"],
        ),
    ]
    redaction_position: Annotated[RedactionPosition, Field(alias="redactionPosition")]


class SingleRedactionResponse(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    external_id: Annotated[
        UUID, Field(alias="externalId", description="An unique id for the redaction request")
    ]
    successful: Annotated[bool, Field(description="Indicates if redaction was success/failure")]


class SubmittedBulkOperation(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    task_id: Annotated[str | None, Field(alias="taskId")] = None


class SuggestedIssue(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    id: Annotated[int | None, Field(description="The ID of the issue.")] = None
    img: Annotated[str | None, Field(description="The URL of the issue type's avatar.")] = None
    key: Annotated[str | None, Field(description="The key of the issue.")] = None
    key_html: Annotated[
        str | None, Field(alias="keyHtml", description="The key of the issue in HTML format.")
    ] = None
    summary: Annotated[
        str | None,
        Field(
            description="The phrase containing the query string in HTML format, with the string highlighted with HTML bold tags."
        ),
    ] = None
    summary_text: Annotated[
        str | None,
        Field(
            alias="summaryText",
            description="The phrase containing the query string, as plain text.",
        ),
    ] = None


class TimeTrackingDetails(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    original_estimate: Annotated[
        str | None,
        Field(
            alias="originalEstimate",
            description="The original estimate of time needed for this issue in readable format.",
        ),
    ] = None
    original_estimate_seconds: Annotated[
        int | None,
        Field(
            alias="originalEstimateSeconds",
            description="The original estimate of time needed for this issue in seconds.",
        ),
    ] = None
    remaining_estimate: Annotated[
        str | None,
        Field(
            alias="remainingEstimate",
            description="The remaining estimate of time needed for this issue in readable format.",
        ),
    ] = None
    remaining_estimate_seconds: Annotated[
        int | None,
        Field(
            alias="remainingEstimateSeconds",
            description="The remaining estimate of time needed for this issue in seconds.",
        ),
    ] = None
    time_spent: Annotated[
        str | None,
        Field(
            alias="timeSpent",
            description="Time worked on this issue in readable format.",
        ),
    ] = None
    time_spent_seconds: Annotated[
        int | None,
        Field(
            alias="timeSpentSeconds",
            description="Time worked on this issue in seconds.",
        ),
    ] = None


class WarningCollection(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    warnings: list[str] | None = None


class Watchers(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    is_watching: Annotated[
        bool | None,
        Field(
            alias="isWatching",
            description="Whether the calling user is watching this issue.",
        ),
    ] = None
    self: Annotated[str | None, Field(description="The URL of these issue watcher details.")] = None
    watch_count: Annotated[
        int | None,
        Field(alias="watchCount", description="The number of users watching this issue."),
    ] = None
    watchers: Annotated[
        list[UserDetails] | None, Field(description="Details of the users watching this issue.")
    ] = None


class Worklog(BaseModel):
    model_config = ConfigDict(
        extra="allow",
    )
    author: Annotated[
        UserDetails | None, Field(description="Details of the user who created the worklog.")
    ] = None
    comment: Annotated[
        Any | None,
        Field(
            description="A comment about the worklog in [Atlassian Document Format](https://developer.atlassian.com/cloud/jira/platform/apis/document/structure/). Optional when creating or updating a worklog."
        ),
    ] = None
    created: Annotated[
        AwareDatetime | None, Field(description="The datetime on which the worklog was created.")
    ] = None
    id: Annotated[str | None, Field(description="The ID of the worklog record.")] = None
    issue_id: Annotated[
        str | None, Field(alias="issueId", description="The ID of the issue this worklog is for.")
    ] = None
    properties: Annotated[
        list[EntityProperty] | None,
        Field(
            description="Details of properties for the worklog. Optional when creating or updating a worklog."
        ),
    ] = None
    self: Annotated[AnyUrl | None, Field(description="The URL of the worklog item.")] = None
    started: Annotated[
        AwareDatetime | None,
        Field(
            description="The datetime on which the worklog effort was started. Required when creating a worklog. Optional when updating a worklog."
        ),
    ] = None
    time_spent: Annotated[
        str | None,
        Field(
            alias="timeSpent",
            description="The time spent working on the issue as days (\\#d), hours (\\#h), or minutes (\\#m or \\#). Required when creating a worklog if `timeSpentSeconds` isn't provided. Optional when updating a worklog. Cannot be provided if `timeSpentSecond` is provided.",
        ),
    ] = None
    time_spent_seconds: Annotated[
        int | None,
        Field(
            alias="timeSpentSeconds",
            description="The time in seconds spent working on the issue. Required when creating a worklog if `timeSpent` isn't provided. Optional when updating a worklog. Cannot be provided if `timeSpent` is provided.",
        ),
    ] = None
    update_author: Annotated[
        UserDetails | None,
        Field(
            alias="updateAuthor",
            description="Details of the user who last updated the worklog.",
        ),
    ] = None
    updated: Annotated[
        AwareDatetime | None,
        Field(description="The datetime on which the worklog was last updated."),
    ] = None
    visibility: Annotated[
        VisibilityModel | None,
        Field(
            description="Details about any restrictions in the visibility of the worklog. Optional when creating or updating a worklog."
        ),
    ] = None


class WorklogCompositeKey(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    issue_id: Annotated[int | None, Field(alias="issueId", description="The issue ID.")] = None
    worklog_id: Annotated[int | None, Field(alias="worklogId", description="The worklog ID.")] = (
        None
    )


class WorklogKeyResult(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    issue_id: Annotated[int | None, Field(alias="issueId", description="The issue ID.")] = None
    worklog_id: Annotated[int | None, Field(alias="worklogId", description="The worklog ID.")] = (
        None
    )


class Fields2(MandatoryFieldValue):
    model_config = ConfigDict(
        extra="forbid",
    )
    retain: Annotated[
        bool | None,
        Field(
            description="If `true`, will try to retain original non-null issue field values on move."
        ),
    ] = True
    type: Literal["mandatoryField"]
    value: list[str] | None = None


class Fields3(MandatoryFieldValueForADF):
    model_config = ConfigDict(
        extra="forbid",
    )
    retain: Annotated[
        bool | None,
        Field(
            description="If `true`, will try to retain original non-null issue field values on move."
        ),
    ] = True
    type: Literal["mandatoryFieldForADF"]
    value: dict[str, Any] | None = None


class ArchivedIssuesFilterRequest(BaseModel):
    model_config = ConfigDict(
        extra="allow",
    )
    archived_by: Annotated[
        list[str] | None,
        Field(
            alias="archivedBy",
            description="List archived issues archived by a specified account ID.",
        ),
    ] = None
    archived_date_range: Annotated[
        DateRangeFilterRequest | None, Field(alias="archivedDateRange")
    ] = None
    issue_types: Annotated[
        list[str] | None,
        Field(
            alias="issueTypes",
            description="List archived issues with a specified issue type ID.",
        ),
    ] = None
    projects: Annotated[
        list[str] | None, Field(description="List archived issues with a specified project key.")
    ] = None
    reporters: Annotated[
        list[str] | None,
        Field(description="List archived issues where the reporter is a specified account ID."),
    ] = None


class Attachment(BaseModel):
    model_config = ConfigDict(
        extra="allow",
    )
    author: Annotated[
        UserDetails | None, Field(description="Details of the user who added the attachment.")
    ] = None
    content: Annotated[str | None, Field(description="The content of the attachment.")] = None
    created: Annotated[
        AwareDatetime | None, Field(description="The datetime the attachment was created.")
    ] = None
    filename: Annotated[str | None, Field(description="The file name of the attachment.")] = None
    id: Annotated[str | None, Field(description="The ID of the attachment.")] = None
    mime_type: Annotated[
        str | None, Field(alias="mimeType", description="The MIME type of the attachment.")
    ] = None
    self: Annotated[
        str | None, Field(description="The URL of the attachment details response.")
    ] = None
    size: Annotated[int | None, Field(description="The size of the attachment.")] = None
    thumbnail: Annotated[
        str | None, Field(description="The URL of a thumbnail representing the attachment.")
    ] = None


class BulkIssuePropertyUpdateRequest(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    expression: Annotated[
        str | None,
        Field(
            description="EXPERIMENTAL. The Jira expression to calculate the value of the property. The value of the expression must be an object that can be converted to JSON, such as a number, boolean, string, list, or map. The context variables available to the expression are `issue` and `user`. Issues for which the expression returns a value whose JSON representation is longer than 32768 characters are ignored."
        ),
    ] = None
    filter: Annotated[
        IssueFilterForBulkPropertySet | None, Field(description="The bulk operation filter.")
    ] = None
    value: Annotated[
        Any | None,
        Field(
            description="The value of the property. The value must be a [valid](https://tools.ietf.org/html/rfc4627), non-empty JSON blob. The maximum length is 32768 characters."
        ),
    ] = None


class BulkOperationErrorResponse(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    errors: list[ErrorMessage] | None = None


class BulkOperationErrorResult(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    element_errors: Annotated[ErrorCollection | None, Field(alias="elementErrors")] = None
    failed_element_number: Annotated[int | None, Field(alias="failedElementNumber")] = None
    status: int | None = None


class BulkRedactionRequest(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    redactions: list[SingleRedactionRequest] | None = None


class BulkRedactionResponse(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    results: Annotated[
        list[SingleRedactionResponse], Field(description="Result for requested redactions")
    ]


class ChangedWorklog(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    properties: Annotated[
        list[EntityProperty] | None,
        Field(description="Details of properties associated with the change."),
    ] = None
    updated_time: Annotated[
        int | None, Field(alias="updatedTime", description="The datetime of the change.")
    ] = None
    worklog_id: Annotated[
        int | None, Field(alias="worklogId", description="The ID of the worklog.")
    ] = None


class ChangedWorklogs(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    last_page: Annotated[bool | None, Field(alias="lastPage")] = None
    next_page: Annotated[
        AnyUrl | None,
        Field(
            alias="nextPage",
            description="The URL of the next list of changed worklogs.",
        ),
    ] = None
    self: Annotated[AnyUrl | None, Field(description="The URL of this changed worklogs list.")] = (
        None
    )
    since: Annotated[
        int | None, Field(description="The datetime of the first worklog item in the list.")
    ] = None
    until: Annotated[
        int | None, Field(description="The datetime of the last worklog item in the list.")
    ] = None
    values: Annotated[list[ChangedWorklog] | None, Field(description="Changed worklog list.")] = (
        None
    )


class Comment(BaseModel):
    model_config = ConfigDict(
        extra="allow",
    )
    author: Annotated[
        UserDetails | None, Field(description="The ID of the user who created the comment.")
    ] = None
    body: Annotated[
        Any | None,
        Field(
            description="The comment text in [Atlassian Document Format](https://developer.atlassian.com/cloud/jira/platform/apis/document/structure/)."
        ),
    ] = None
    created: Annotated[
        AwareDatetime | None,
        Field(description="The date and time at which the comment was created."),
    ] = None
    id: Annotated[str | None, Field(description="The ID of the comment.")] = None
    jsd_author_can_see_request: Annotated[
        bool | None,
        Field(
            alias="jsdAuthorCanSeeRequest",
            description="Whether the comment was added from an email sent by a person who is not part of the issue. See [Allow external emails to be added as comments on issues](https://support.atlassian.com/jira-service-management-cloud/docs/allow-external-emails-to-be-added-as-comments-on-issues/)for information on setting up this feature.",
        ),
    ] = None
    jsd_public: Annotated[
        bool | None,
        Field(
            alias="jsdPublic",
            description="Whether the comment is visible in Jira Service Desk. Defaults to true when comments are created in the Jira Cloud Platform. This includes when the site doesn't use Jira Service Desk or the project isn't a Jira Service Desk project and, therefore, there is no Jira Service Desk for the issue to be visible on. To create a comment with its visibility in Jira Service Desk set to false, use the Jira Service Desk REST API [Create request comment](https://developer.atlassian.com/cloud/jira/service-desk/rest/#api-rest-servicedeskapi-request-issueIdOrKey-comment-post) operation.",
        ),
    ] = None
    properties: Annotated[
        list[EntityProperty] | None,
        Field(description="A list of comment properties. Optional on create and update."),
    ] = None
    rendered_body: Annotated[
        str | None, Field(alias="renderedBody", description="The rendered version of the comment.")
    ] = None
    self: Annotated[str | None, Field(description="The URL of the comment.")] = None
    update_author: Annotated[
        UserDetails | None,
        Field(
            alias="updateAuthor",
            description="The ID of the user who updated the comment last.",
        ),
    ] = None
    updated: Annotated[
        AwareDatetime | None,
        Field(description="The date and time at which the comment was updated last."),
    ] = None
    visibility: Annotated[
        VisibilityModel | None,
        Field(
            description="The group or role to which this comment is visible. Optional on create and update."
        ),
    ] = None


class FieldCreateMetadata(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    allowed_values: Annotated[
        list[Any] | None,
        Field(
            alias="allowedValues",
            description="The list of values allowed in the field.",
        ),
    ] = None
    auto_complete_url: Annotated[
        str | None,
        Field(
            alias="autoCompleteUrl",
            description="The URL that can be used to automatically complete the field.",
        ),
    ] = None
    configuration: Annotated[
        dict[str, Any] | None, Field(description="The configuration properties.")
    ] = None
    default_value: Annotated[
        Any | None, Field(alias="defaultValue", description="The default value of the field.")
    ] = None
    field_id: Annotated[str, Field(alias="fieldId", description="The field id.")]
    has_default_value: Annotated[
        bool | None,
        Field(
            alias="hasDefaultValue",
            description="Whether the field has a default value.",
        ),
    ] = None
    key: Annotated[str, Field(description="The key of the field.")]
    name: Annotated[str, Field(description="The name of the field.")]
    operations: Annotated[
        list[str], Field(description="The list of operations that can be performed on the field.")
    ]
    required: Annotated[bool, Field(description="Whether the field is required.")]
    schema_: Annotated[JsonType, Field(alias="schema", description="The data type of the field.")]


class FieldMetadata(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    allowed_values: Annotated[
        list[Any] | None,
        Field(
            alias="allowedValues",
            description="The list of values allowed in the field.",
        ),
    ] = None
    auto_complete_url: Annotated[
        str | None,
        Field(
            alias="autoCompleteUrl",
            description="The URL that can be used to automatically complete the field.",
        ),
    ] = None
    configuration: Annotated[
        dict[str, Any] | None, Field(description="The configuration properties.")
    ] = None
    default_value: Annotated[
        Any | None, Field(alias="defaultValue", description="The default value of the field.")
    ] = None
    has_default_value: Annotated[
        bool | None,
        Field(
            alias="hasDefaultValue",
            description="Whether the field has a default value.",
        ),
    ] = None
    key: Annotated[str, Field(description="The key of the field.")]
    name: Annotated[str, Field(description="The name of the field.")]
    operations: Annotated[
        list[str], Field(description="The list of operations that can be performed on the field.")
    ]
    required: Annotated[bool, Field(description="Whether the field is required.")]
    schema_: Annotated[JsonType, Field(alias="schema", description="The data type of the field.")]


class HistoryMetadata(BaseModel):
    model_config = ConfigDict(
        extra="allow",
    )
    activity_description: Annotated[
        str | None,
        Field(
            alias="activityDescription",
            description="The activity described in the history record.",
        ),
    ] = None
    activity_description_key: Annotated[
        str | None,
        Field(
            alias="activityDescriptionKey",
            description="The key of the activity described in the history record.",
        ),
    ] = None
    actor: Annotated[
        HistoryMetadataParticipant | None,
        Field(description="Details of the user whose action created the history record."),
    ] = None
    cause: Annotated[
        HistoryMetadataParticipant | None,
        Field(description="Details of the cause that triggered the creation the history record."),
    ] = None
    description: Annotated[
        str | None, Field(description="The description of the history record.")
    ] = None
    description_key: Annotated[
        str | None,
        Field(
            alias="descriptionKey",
            description="The description key of the history record.",
        ),
    ] = None
    email_description: Annotated[
        str | None,
        Field(
            alias="emailDescription",
            description="The description of the email address associated the history record.",
        ),
    ] = None
    email_description_key: Annotated[
        str | None,
        Field(
            alias="emailDescriptionKey",
            description="The description key of the email address associated the history record.",
        ),
    ] = None
    extra_data: Annotated[
        dict[str, str] | None,
        Field(
            alias="extraData",
            description="Additional arbitrary information about the history record.",
        ),
    ] = None
    generator: Annotated[
        HistoryMetadataParticipant | None,
        Field(description="Details of the system that generated the history record."),
    ] = None
    type: Annotated[str | None, Field(description="The type of the history record.")] = None


class IssueBulkEditField(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    description: Annotated[str | None, Field(description="Description of the field.")] = None
    field_options: Annotated[
        list[IssueBulkOperationsFieldOption] | None,
        Field(
            alias="fieldOptions",
            description="A list of options related to the field, applicable in contexts where multiple selections are allowed.",
        ),
    ] = None
    id: Annotated[str | None, Field(description="The unique ID of the field.")] = None
    is_required: Annotated[
        bool | None,
        Field(
            alias="isRequired",
            description="Indicates whether the field is mandatory for the operation.",
        ),
    ] = None
    multi_select_field_options: Annotated[
        list[MultiSelectFieldOption] | None,
        Field(
            alias="multiSelectFieldOptions",
            description="Specifies supported actions (like add, replace, remove) on multi-select fields via an enum.",
        ),
    ] = None
    name: Annotated[str | None, Field(description="The display name of the field.")] = None
    search_url: Annotated[
        str | None,
        Field(
            alias="searchUrl",
            description="A URL to fetch additional data for the field",
        ),
    ] = None
    type: Annotated[str | None, Field(description="The type of the field.")] = None
    unavailable_message: Annotated[
        str | None,
        Field(
            alias="unavailableMessage",
            description="A message indicating why the field is unavailable for editing.",
        ),
    ] = None


class IssueBulkMovePayload(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    send_bulk_notification: Annotated[
        bool | None,
        Field(
            alias="sendBulkNotification",
            description="A boolean value that indicates whether to send a bulk change notification when the issues are being moved.\n\nIf `true`, dispatches a bulk notification email to users about the updates.",
        ),
    ] = True
    target_to_sources_mapping: Annotated[
        dict[str, TargetToSourcesMapping] | None,
        Field(
            alias="targetToSourcesMapping",
            description="An object representing the mapping of issues and data related to destination entities, like fields and statuses, that are required during a bulk move.\n\nThe key is a string that is created by concatenating the following three entities in order, separated by commas. The format is `<project ID or key>,<issueType ID>,<parent ID or key>`. It should be unique across mappings provided in the payload. If you provide multiple mappings for the same key, only one will be processed. However, the operation won't fail, so the error may be hard to track down.\n\n *  ***Destination project*** (Required): ID or key of the project to which the issues are being moved.\n *  ***Destination issueType*** (Required): ID of the issueType to which the issues are being moved.\n *  ***Destination parent ID or key*** (Optional): ID or key of the issue which will become the parent of the issues being moved. Only required when the destination issueType is a subtask.",
        ),
    ] = None


class IssueBulkTransitionForWorkflow(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    is_transitions_filtered: Annotated[
        bool | None,
        Field(
            alias="isTransitionsFiltered",
            description="Indicates whether all the transitions of this workflow are available in the transitions list or not.",
        ),
    ] = None
    issues: Annotated[
        list[str] | None,
        Field(
            description="List of issue keys from the request which are associated with this workflow."
        ),
    ] = None
    transitions: Annotated[
        list[SimplifiedIssueTransition] | None,
        Field(
            description="List of transitions available for issues from the request which are associated with this workflow.\n\n **This list includes only those transitions that are common across the issues in this workflow and do not involve any additional field updates.** "
        ),
    ] = None


class IssueEntityProperties(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    entities_ids: Annotated[
        list[int] | None,
        Field(
            alias="entitiesIds",
            description="A list of entity property IDs.",
            max_length=10000,
            min_length=1,
        ),
    ] = None
    properties: Annotated[
        dict[str, JsonNode] | None, Field(description="A list of entity property keys and values.")
    ] = None


class IssueEntityPropertiesForMultiUpdate(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    issue_id: Annotated[int | None, Field(alias="issueID", description="The ID of the issue.")] = (
        None
    )
    properties: Annotated[
        dict[str, JsonNode] | None,
        Field(
            description="Entity properties to set on the issue. The maximum length of an issue property value is 32768 characters."
        ),
    ] = None


class IssueMatches(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    matches: list[IssueMatchesForJQL]


class IssuePickerSuggestionsIssueType(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    id: Annotated[
        str | None,
        Field(description="The ID of the type of issues suggested for use in auto-completion."),
    ] = None
    issues: Annotated[
        list[SuggestedIssue] | None,
        Field(description="A list of issues suggested for use in auto-completion."),
    ] = None
    label: Annotated[
        str | None,
        Field(description="The label of the type of issues suggested for use in auto-completion."),
    ] = None
    msg: Annotated[
        str | None,
        Field(
            description="If no issue suggestions are found, returns a message indicating no suggestions were found,"
        ),
    ] = None
    sub: Annotated[
        str | None,
        Field(
            description="If issue suggestions are found, returns a message indicating the number of issues suggestions found and returned."
        ),
    ] = None


class IssueUpdateMetadata(BaseModel):
    fields: dict[str, FieldMetadata] | None = None


class JiraCascadingSelectField(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    child_option_value: Annotated[
        JiraSelectedOptionField | None, Field(alias="childOptionValue")
    ] = None
    field_id: Annotated[str, Field(alias="fieldId")]
    parent_option_value: Annotated[JiraSelectedOptionField, Field(alias="parentOptionValue")]


class JiraColorField(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    color: JiraColorInput
    field_id: Annotated[str, Field(alias="fieldId")]


class JiraDateField(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    date: JiraDateInput | None = None
    field_id: Annotated[str, Field(alias="fieldId")]


class JiraDateTimeField(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    date_time: Annotated[JiraDateTimeInput, Field(alias="dateTime")]
    field_id: Annotated[str, Field(alias="fieldId")]


class JiraLabelsField(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    bulk_edit_multi_select_field_option: Annotated[
        BulkEditMultiSelectFieldOption, Field(alias="bulkEditMultiSelectFieldOption")
    ]
    field_id: Annotated[str, Field(alias="fieldId")]
    label_properties: Annotated[
        list[JiraLabelPropertiesInputJackson1] | None, Field(alias="labelProperties")
    ] = None
    labels: list[JiraLabelsInput]


class JiraMultipleSelectField(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    field_id: Annotated[str, Field(alias="fieldId")]
    options: list[JiraSelectedOptionField]


class JiraMultipleSelectUserPickerField(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    field_id: Annotated[str, Field(alias="fieldId")]
    users: list[JiraUserField] | None = None


class JiraMultipleVersionPickerField(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    bulk_edit_multi_select_field_option: Annotated[
        BulkEditMultiSelectFieldOption, Field(alias="bulkEditMultiSelectFieldOption")
    ]
    field_id: Annotated[str, Field(alias="fieldId")]
    versions: list[JiraVersionField]


class JiraRichTextField(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    field_id: Annotated[str, Field(alias="fieldId")]
    rich_text: Annotated[JiraRichTextInput, Field(alias="richText")]


class JiraSingleSelectUserPickerField(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    field_id: Annotated[str, Field(alias="fieldId")]
    user: JiraUserField | None = None


class JiraSingleVersionPickerField(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    field_id: Annotated[str, Field(alias="fieldId")]
    version: JiraVersionField


class LegacyJackson1ListAttachment(RootModel[list[Attachment]]):
    root: list[Attachment]


class LegacyJackson1ListWorklog(RootModel[list[Worklog]]):
    root: list[Worklog]


class LinkGroup(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    groups: list[LinkGroup] | None = None
    header: SimpleLink | None = None
    id: str | None = None
    links: list[SimpleLink] | None = None
    style_class: Annotated[str | None, Field(alias="styleClass")] = None
    weight: int | None = None


class MultiIssueEntityProperties(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    issues: Annotated[
        list[IssueEntityPropertiesForMultiUpdate] | None,
        Field(description="A list of issue IDs and their respective properties."),
    ] = None


class MultipartFile(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    bytes: list[Base64Str] | None = None
    content_type: Annotated[str | None, Field(alias="contentType")] = None
    empty: bool | None = None
    input_stream: Annotated[dict[str, Any] | None, Field(alias="inputStream")] = None
    name: str | None = None
    original_filename: Annotated[str | None, Field(alias="originalFilename")] = None
    resource: Resource | None = None
    size: int | None = None


class NestedResponse(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    error_collection: Annotated[ErrorCollection | None, Field(alias="errorCollection")] = None
    status: int | None = None
    warning_collection: Annotated[WarningCollection | None, Field(alias="warningCollection")] = None


class NotificationRecipients(BaseModel):
    model_config = ConfigDict(
        extra="allow",
    )
    assignee: Annotated[
        bool | None,
        Field(description="Whether the notification should be sent to the issue's assignees."),
    ] = None
    group_ids: Annotated[
        list[str] | None,
        Field(
            alias="groupIds",
            description="List of groupIds to receive the notification.",
        ),
    ] = None
    groups: Annotated[
        list[GroupName] | None, Field(description="List of groups to receive the notification.")
    ] = None
    reporter: Annotated[
        bool | None,
        Field(description="Whether the notification should be sent to the issue's reporter."),
    ] = None
    users: Annotated[
        list[UserDetails] | None, Field(description="List of users to receive the notification.")
    ] = None
    voters: Annotated[
        bool | None,
        Field(description="Whether the notification should be sent to the issue's voters."),
    ] = None
    watchers: Annotated[
        bool | None,
        Field(description="Whether the notification should be sent to the issue's watchers."),
    ] = None


class NotificationRecipientsRestrictions(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    group_ids: Annotated[
        list[str] | None,
        Field(
            alias="groupIds",
            description="List of groupId memberships required to receive the notification.",
        ),
    ] = None
    groups: Annotated[
        list[GroupName] | None,
        Field(description="List of group memberships required to receive the notification."),
    ] = None
    permissions: Annotated[
        list[RestrictedPermission] | None,
        Field(description="List of permissions required to receive the notification."),
    ] = None


class Operations(BaseModel):
    model_config = ConfigDict(
        extra="allow",
    )
    link_groups: Annotated[
        list[LinkGroup] | None,
        Field(
            alias="linkGroups",
            description="Details of the link groups defining issue operations.",
        ),
    ] = None


class PageBeanComment(BaseModel):
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
    values: Annotated[list[Comment] | None, Field(description="The list of items.")] = None


class PageOfComments(BaseModel):
    model_config = ConfigDict(
        extra="allow",
    )
    comments: Annotated[list[Comment] | None, Field(description="The list of comments.")] = None
    max_results: Annotated[
        int | None,
        Field(
            alias="maxResults",
            description="The maximum number of items that could be returned.",
        ),
    ] = None
    start_at: Annotated[
        int | None, Field(alias="startAt", description="The index of the first item returned.")
    ] = None
    total: Annotated[int | None, Field(description="The number of items returned.")] = None


class PageOfCreateMetaIssueTypeWithField(BaseModel):
    model_config = ConfigDict(
        extra="allow",
    )
    fields: Annotated[
        list[FieldCreateMetadata] | None,
        Field(description="The collection of FieldCreateMetaBeans."),
    ] = None
    max_results: Annotated[
        int | None,
        Field(
            alias="maxResults",
            description="The maximum number of items to return per page.",
        ),
    ] = None
    results: list[FieldCreateMetadata] | None = None
    start_at: Annotated[
        int | None, Field(alias="startAt", description="The index of the first item returned.")
    ] = None
    total: Annotated[int | None, Field(description="The total number of items in all pages.")] = (
        None
    )


class PageOfWorklogs(BaseModel):
    model_config = ConfigDict(
        extra="allow",
    )
    max_results: Annotated[
        int | None,
        Field(
            alias="maxResults",
            description="The maximum number of results that could be on the page.",
        ),
    ] = None
    start_at: Annotated[
        int | None,
        Field(
            alias="startAt",
            description="The index of the first item returned on the page.",
        ),
    ] = None
    total: Annotated[int | None, Field(description="The number of results on the page.")] = None
    worklogs: Annotated[list[Worklog] | None, Field(description="List of worklogs.")] = None


class RedactionJobStatusResponse(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    bulk_redaction_response: Annotated[
        BulkRedactionResponse | None, Field(alias="bulkRedactionResponse")
    ] = None
    job_status: Annotated[JobStatus | None, Field(alias="jobStatus")] = None


class RemoteObject(BaseModel):
    model_config = ConfigDict(
        extra="allow",
    )
    icon: Annotated[
        Icon | None,
        Field(
            description="Details of the icon for the item. If no icon is defined, the default link icon is used in Jira."
        ),
    ] = None
    status: Annotated[StatusModel | None, Field(description="The status of the item.")] = None
    summary: Annotated[str | None, Field(description="The summary details of the item.")] = None
    title: Annotated[str, Field(description="The title of the item.")]
    url: Annotated[str, Field(description="The URL of the item.")]


class Votes(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    has_voted: Annotated[
        bool | None,
        Field(
            alias="hasVoted",
            description="Whether the user making this request has voted on the issue.",
        ),
    ] = None
    self: Annotated[AnyUrl | None, Field(description="The URL of these issue vote details.")] = None
    voters: Annotated[
        list[User] | None,
        Field(
            description="List of the users who have voted on this issue. An empty list is returned when the calling user doesn't have the *View voters and watchers* project permission."
        ),
    ] = None
    votes: Annotated[int | None, Field(description="The number of votes on the issue.")] = None


class AttachmentMetadata(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    author: Annotated[
        User | None, Field(description="Details of the user who attached the file.")
    ] = None
    content: Annotated[str | None, Field(description="The URL of the attachment.")] = None
    created: Annotated[
        AwareDatetime | None, Field(description="The datetime the attachment was created.")
    ] = None
    filename: Annotated[str | None, Field(description="The name of the attachment file.")] = None
    id: Annotated[int | None, Field(description="The ID of the attachment.")] = None
    mime_type: Annotated[
        str | None, Field(alias="mimeType", description="The MIME type of the attachment.")
    ] = None
    properties: Annotated[
        dict[str, Any] | None, Field(description="Additional properties of the attachment.")
    ] = None
    self: Annotated[
        AnyUrl | None, Field(description="The URL of the attachment metadata details.")
    ] = None
    size: Annotated[int | None, Field(description="The size of the attachment.")] = None
    thumbnail: Annotated[
        str | None, Field(description="The URL of a thumbnail representing the attachment.")
    ] = None


class BulkEditGetFields(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    ending_before: Annotated[
        str | None, Field(alias="endingBefore", description="The end cursor for use in pagination.")
    ] = None
    fields: Annotated[
        list[IssueBulkEditField] | None, Field(description="List of all the fields")
    ] = None
    starting_after: Annotated[
        str | None,
        Field(alias="startingAfter", description="The start cursor for use in pagination."),
    ] = None


class BulkOperationProgress(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    created: Annotated[
        AwareDatetime | None, Field(description="A timestamp of when the task was submitted.")
    ] = None
    failed_accessible_issues: Annotated[
        dict[str, list[str]] | None,
        Field(
            alias="failedAccessibleIssues",
            description="Map of issue IDs for which the operation failed and that the user has permission to view, to their one or more reasons for failure. These reasons are open-ended text descriptions of the error and are not selected from a predefined list of standard reasons.",
        ),
    ] = None
    invalid_or_inaccessible_issue_count: Annotated[
        int | None,
        Field(
            alias="invalidOrInaccessibleIssueCount",
            description="The number of issues that are either invalid or issues that the user doesn't have permission to view, regardless of the success or failure of the operation.",
        ),
    ] = None
    processed_accessible_issues: Annotated[
        list[int] | None,
        Field(
            alias="processedAccessibleIssues",
            description="List of issue IDs for which the operation was successful and that the user has permission to view.",
        ),
    ] = None
    progress_percent: Annotated[
        int | None,
        Field(alias="progressPercent", description="Progress of the task as a percentage."),
    ] = None
    started: Annotated[
        AwareDatetime | None, Field(description="A timestamp of when the task was started.")
    ] = None
    status: Annotated[Status | None, Field(description="The status of the task.")] = None
    submitted_by: Annotated[User | None, Field(alias="submittedBy")] = None
    task_id: Annotated[str | None, Field(alias="taskId", description="The ID of the task.")] = None
    total_issue_count: Annotated[
        int | None,
        Field(
            alias="totalIssueCount",
            description="The number of issues that the bulk operation was attempted on.",
        ),
    ] = None
    updated: Annotated[
        AwareDatetime | None,
        Field(description="A timestamp of when the task progress was last updated."),
    ] = None


class BulkTransitionGetAvailableTransitions(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    available_transitions: Annotated[
        list[IssueBulkTransitionForWorkflow] | None,
        Field(
            alias="availableTransitions",
            description="List of available transitions for bulk transition operation for requested issues grouped by workflow",
        ),
    ] = None
    ending_before: Annotated[
        str | None, Field(alias="endingBefore", description="The end cursor for use in pagination.")
    ] = None
    starting_after: Annotated[
        str | None,
        Field(alias="startingAfter", description="The start cursor for use in pagination."),
    ] = None


class Changelog(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    author: Annotated[UserDetails | None, Field(description="The user who made the change.")] = None
    created: Annotated[
        AwareDatetime | None, Field(description="The date on which the change took place.")
    ] = None
    history_metadata: Annotated[
        HistoryMetadata | None,
        Field(
            alias="historyMetadata",
            description="The history metadata associated with the changed.",
        ),
    ] = None
    id: Annotated[str | None, Field(description="The ID of the changelog.")] = None
    items: Annotated[
        list[ChangeDetails] | None, Field(description="The list of items changed.")
    ] = None


class CreatedIssue(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    id: Annotated[str | None, Field(description="The ID of the created issue or subtask.")] = None
    key: Annotated[str | None, Field(description="The key of the created issue or subtask.")] = None
    self: Annotated[str | None, Field(description="The URL of the created issue or subtask.")] = (
        None
    )
    transition: Annotated[
        NestedResponse | None,
        Field(description="The response code and messages related to any requested transition."),
    ] = None
    watchers: Annotated[
        NestedResponse | None,
        Field(description="The response code and messages related to any requested watchers."),
    ] = None


class CreatedIssues(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    errors: Annotated[
        list[BulkOperationErrorResult] | None,
        Field(description="Error details for failed issue creation requests."),
    ] = None
    issues: Annotated[
        list[CreatedIssue] | None, Field(description="Details of the issues created.")
    ] = None


class IssueChangeLog(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    change_histories: Annotated[
        list[Changelog] | None,
        Field(
            alias="changeHistories",
            description="List of changelogs that belongs to given issueId.",
        ),
    ] = None
    issue_id: Annotated[str | None, Field(alias="issueId", description="The ID of the issue.")] = (
        None
    )


class IssuePickerSuggestions(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    sections: Annotated[
        list[IssuePickerSuggestionsIssueType] | None,
        Field(
            description="A list of issues for an issue type suggested for use in auto-completion."
        ),
    ] = None


class IssueTransition(BaseModel):
    model_config = ConfigDict(
        extra="allow",
    )
    expand: Annotated[
        str | None,
        Field(
            description="Expand options that include additional transition details in the response."
        ),
    ] = None
    fields: Annotated[
        dict[str, FieldMetadata] | None,
        Field(
            description="Details of the fields associated with the issue transition screen. Use this information to populate `fields` and `update` in a transition request."
        ),
    ] = None
    has_screen: Annotated[
        bool | None,
        Field(
            alias="hasScreen",
            description="Whether there is a screen associated with the issue transition.",
        ),
    ] = None
    id: Annotated[
        str | None,
        Field(
            description="The ID of the issue transition. Required when specifying a transition to undertake."
        ),
    ] = None
    is_available: Annotated[
        bool | None,
        Field(
            alias="isAvailable",
            description="Whether the transition is available to be performed.",
        ),
    ] = None
    is_conditional: Annotated[
        bool | None,
        Field(
            alias="isConditional",
            description="Whether the issue has to meet criteria before the issue transition is applied.",
        ),
    ] = None
    is_global: Annotated[
        bool | None,
        Field(
            alias="isGlobal",
            description="Whether the issue transition is global, that is, the transition is applied to issues regardless of their status.",
        ),
    ] = None
    is_initial: Annotated[
        bool | None,
        Field(
            alias="isInitial",
            description="Whether this is the initial issue transition for the workflow.",
        ),
    ] = None
    looped: bool | None = None
    name: Annotated[str | None, Field(description="The name of the issue transition.")] = None
    to: Annotated[
        StatusDetails | None, Field(description="Details of the issue status after the transition.")
    ] = None


class IssueTypeIssueCreateMetadata(BaseModel):
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
    expand: Annotated[
        str | None,
        Field(
            description="Expand options that include additional issue type metadata details in the response."
        ),
    ] = None
    fields: Annotated[
        dict[str, FieldMetadata] | None,
        Field(
            description="List of the fields available when creating an issue for the issue type."
        ),
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


class IssueUpdateDetails(BaseModel):
    model_config = ConfigDict(
        extra="allow",
    )
    fields: Annotated[
        dict[str, Any] | None,
        Field(
            description="List of issue screen fields to update, specifying the sub-field to update and its value for each field. This field provides a straightforward option when setting a sub-field. When multiple sub-fields or other operations are required, use `update`. Fields included in here cannot be included in `update`."
        ),
    ] = None
    history_metadata: Annotated[
        HistoryMetadata | None,
        Field(alias="historyMetadata", description="Additional issue history details."),
    ] = None
    properties: Annotated[
        list[EntityProperty] | None,
        Field(description="Details of issue properties to be add or update."),
    ] = None
    transition: Annotated[
        IssueTransition | None,
        Field(
            description="Details of a transition. Required when performing a transition, optional when creating or editing an issue."
        ),
    ] = None
    update: Annotated[
        dict[str, list[FieldUpdateOperation]] | None,
        Field(
            description="A Map containing the field field name and a list of operations to perform on the issue screen field. Note that fields included in here cannot be included in `fields`."
        ),
    ] = None


class JiraIssueFields(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    cascading_select_fields: Annotated[
        list[JiraCascadingSelectField] | None,
        Field(
            alias="cascadingSelectFields",
            description="Add or clear a cascading select field:\n\n *  To add, specify `optionId` for both parent and child.\n *  To clear the child, set its `optionId` to null.\n *  To clear both, set the parent's `optionId` to null.",
        ),
    ] = None
    clearable_number_fields: Annotated[
        list[JiraNumberField] | None,
        Field(
            alias="clearableNumberFields",
            description="Add or clear a number field:\n\n *  To add, specify a numeric `value`.\n *  To clear, set `value` to `null`.",
        ),
    ] = None
    color_fields: Annotated[
        list[JiraColorField] | None,
        Field(
            alias="colorFields",
            description="Add or clear a color field:\n\n *  To add, specify the color `name`. Available colors are: `purple`, `blue`, `green`, `teal`, `yellow`, `orange`, `grey`, `dark purple`, `dark blue`, `dark green`, `dark teal`, `dark yellow`, `dark orange`, `dark grey`.\n *  To clear, set the color `name` to an empty string.",
        ),
    ] = None
    date_picker_fields: Annotated[
        list[JiraDateField] | None,
        Field(
            alias="datePickerFields",
            description="Add or clear a date picker field:\n\n *  To add, specify the date in `d/mmm/yy` format or ISO format `dd-mm-yyyy`.\n *  To clear, set `formattedDate` to an empty string.",
        ),
    ] = None
    date_time_picker_fields: Annotated[
        list[JiraDateTimeField] | None,
        Field(
            alias="dateTimePickerFields",
            description="Add or clear the planned start date and time:\n\n *  To add, specify the date and time in ISO format for `formattedDateTime`.\n *  To clear, provide an empty string for `formattedDateTime`.",
        ),
    ] = None
    issue_type: Annotated[
        JiraIssueTypeField | None,
        Field(
            alias="issueType",
            description="Set the issue type field by providing an `issueTypeId`.",
        ),
    ] = None
    labels_fields: Annotated[
        list[JiraLabelsField] | None,
        Field(
            alias="labelsFields",
            description="Edit a labels field:\n\n *  Options include `ADD`, `REPLACE`, `REMOVE`, or `REMOVE_ALL` for bulk edits.\n *  To clear labels, use the `REMOVE_ALL` option with an empty `labels` array.",
        ),
    ] = None
    multiple_group_picker_fields: Annotated[
        list[JiraMultipleGroupPickerField] | None,
        Field(
            alias="multipleGroupPickerFields",
            description="Add or clear a multi-group picker field:\n\n *  To add groups, provide an array of groups with `groupName`s.\n *  To clear all groups, use an empty `groups` array.",
        ),
    ] = None
    multiple_select_clearable_user_picker_fields: Annotated[
        list[JiraMultipleSelectUserPickerField] | None,
        Field(
            alias="multipleSelectClearableUserPickerFields",
            description="Assign or unassign multiple users to/from a field:\n\n *  To assign, provide an array of user `accountId`s.\n *  To clear, set `users` to `null`.",
        ),
    ] = None
    multiple_select_fields: Annotated[
        list[JiraMultipleSelectField] | None,
        Field(
            alias="multipleSelectFields",
            description="Add or clear a multi-select field:\n\n *  To add, provide an array of options with `optionId`s.\n *  To clear, use an empty `options` array.",
        ),
    ] = None
    multiple_version_picker_fields: Annotated[
        list[JiraMultipleVersionPickerField] | None,
        Field(
            alias="multipleVersionPickerFields",
            description="Edit a multi-version picker field like Fix Versions/Affects Versions:\n\n *  Options include `ADD`, `REPLACE`, `REMOVE`, or `REMOVE_ALL` for bulk edits.\n *  To clear the field, use the `REMOVE_ALL` option with an empty `versions` array.",
        ),
    ] = None
    multiselect_components: Annotated[
        JiraMultiSelectComponentField | None,
        Field(
            alias="multiselectComponents",
            description="Edit a multi select components field:\n\n *  Options include `ADD`, `REPLACE`, `REMOVE`, or `REMOVE_ALL` for bulk edits.\n *  To clear, use the `REMOVE_ALL` option with an empty `components` array.",
        ),
    ] = None
    original_estimate_field: Annotated[
        JiraDurationField | None,
        Field(
            alias="originalEstimateField",
            description="Edit the original estimate field.",
        ),
    ] = None
    priority: Annotated[
        JiraPriorityField | None,
        Field(description="Set the priority of an issue by specifying a `priorityId`."),
    ] = None
    rich_text_fields: Annotated[
        list[JiraRichTextField] | None,
        Field(
            alias="richTextFields",
            description="Add or clear a rich text field:\n\n *  To add, provide `adfValue`. Note that rich text fields only support ADF values.\n *  To clear, use an empty `richText` object.\n\nFor ADF format details, refer to: [Atlassian Document Format](https://developer.atlassian.com/cloud/jira/platform/apis/document/structure).",
        ),
    ] = None
    single_group_picker_fields: Annotated[
        list[JiraSingleGroupPickerField] | None,
        Field(
            alias="singleGroupPickerFields",
            description="Add or clear a single group picker field:\n\n *  To add, specify the group with `groupName`.\n *  To clear, set `groupName` to an empty string.",
        ),
    ] = None
    single_line_text_fields: Annotated[
        list[JiraSingleLineTextField] | None,
        Field(
            alias="singleLineTextFields",
            description="Add or clear a single line text field:\n\n *  To add, provide the `text` value.\n *  To clear, set `text` to an empty string.",
        ),
    ] = None
    single_select_clearable_user_picker_fields: Annotated[
        list[JiraSingleSelectUserPickerField] | None,
        Field(
            alias="singleSelectClearableUserPickerFields",
            description="Edit assignment for single select user picker fields like Assignee/Reporter:\n\n *  To assign an issue, specify the user's `accountId`.\n *  To unassign an issue, set `user` to `null`.\n *  For automatic assignment, set `accountId` to `-1`.",
        ),
    ] = None
    single_select_fields: Annotated[
        list[JiraSingleSelectField] | None,
        Field(
            alias="singleSelectFields",
            description="Add or clear a single select field:\n\n *  To add, specify the option with an `optionId`.\n *  To clear, pass an option with `optionId` as `-1`.",
        ),
    ] = None
    single_version_picker_fields: Annotated[
        list[JiraSingleVersionPickerField] | None,
        Field(
            alias="singleVersionPickerFields",
            description="Add or clear a single version picker field:\n\n *  To add, specify the version with a `versionId`.\n *  To clear, set `versionId` to `-1`.",
        ),
    ] = None
    status: JiraStatusInput | None = None
    time_tracking_field: Annotated[
        JiraTimeTrackingField | None,
        Field(alias="timeTrackingField", description="Edit the time tracking field."),
    ] = None
    url_fields: Annotated[
        list[JiraUrlField] | None,
        Field(
            alias="urlFields",
            description="Add or clear a URL field:\n\n *  To add, provide the `url` with the desired URL value.\n *  To clear, set `url` to an empty string.",
        ),
    ] = None


class Notification(BaseModel):
    model_config = ConfigDict(
        extra="allow",
    )
    html_body: Annotated[
        str | None,
        Field(
            alias="htmlBody",
            description="The HTML body of the email notification for the issue.",
        ),
    ] = None
    restrict: Annotated[
        NotificationRecipientsRestrictions | None,
        Field(description="Restricts the notifications to users with the specified permissions."),
    ] = None
    subject: Annotated[
        str | None,
        Field(
            description="The subject of the email notification for the issue. If this is not specified, then the subject is set to the issue key and summary."
        ),
    ] = None
    text_body: Annotated[
        str | None,
        Field(
            alias="textBody",
            description="The plain text body of the email notification for the issue.",
        ),
    ] = None
    to: Annotated[
        NotificationRecipients | None,
        Field(description="The recipients of the email notification for the issue."),
    ] = None


class PageBeanChangelog(BaseModel):
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
    values: Annotated[list[Changelog] | None, Field(description="The list of items.")] = None


class PageOfChangelogs(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    histories: Annotated[list[Changelog] | None, Field(description="The list of changelogs.")] = (
        None
    )
    max_results: Annotated[
        int | None,
        Field(
            alias="maxResults",
            description="The maximum number of results that could be on the page.",
        ),
    ] = None
    start_at: Annotated[
        int | None,
        Field(
            alias="startAt",
            description="The index of the first item returned on the page.",
        ),
    ] = None
    total: Annotated[int | None, Field(description="The number of results on the page.")] = None


class PageOfCreateMetaIssueTypes(BaseModel):
    model_config = ConfigDict(
        extra="allow",
    )
    create_meta_issue_type: Annotated[
        list[IssueTypeIssueCreateMetadata] | None, Field(alias="createMetaIssueType")
    ] = None
    issue_types: Annotated[
        list[IssueTypeIssueCreateMetadata] | None,
        Field(alias="issueTypes", description="The list of CreateMetaIssueType."),
    ] = None
    max_results: Annotated[
        int | None,
        Field(
            alias="maxResults",
            description="The maximum number of items to return per page.",
        ),
    ] = None
    start_at: Annotated[
        int | None, Field(alias="startAt", description="The index of the first item returned.")
    ] = None
    total: Annotated[int | None, Field(description="The total number of items in all pages.")] = (
        None
    )


class ProjectIssueCreateMetadata(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    avatar_urls: Annotated[
        AvatarUrls | None,
        Field(
            alias="avatarUrls",
            description="List of the project's avatars, returning the avatar size and associated URL.",
        ),
    ] = None
    expand: Annotated[
        str | None,
        Field(
            description="Expand options that include additional project issue create metadata details in the response."
        ),
    ] = None
    id: Annotated[str | None, Field(description="The ID of the project.")] = None
    issuetypes: Annotated[
        list[IssueTypeIssueCreateMetadata] | None,
        Field(description="List of the issue types supported by the project."),
    ] = None
    key: Annotated[str | None, Field(description="The key of the project.")] = None
    name: Annotated[str | None, Field(description="The name of the project.")] = None
    self: Annotated[str | None, Field(description="The URL of the project.")] = None


class RemoteIssueLink(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    application: Annotated[
        Application | None,
        Field(description="Details of the remote application the linked item is in."),
    ] = None
    global_id: Annotated[
        str | None,
        Field(
            alias="globalId",
            description="The global ID of the link, such as the ID of the item on the remote system.",
        ),
    ] = None
    id: Annotated[int | None, Field(description="The ID of the link.")] = None
    object: Annotated[RemoteObject | None, Field(description="Details of the item linked to.")] = (
        None
    )
    relationship: Annotated[
        str | None,
        Field(description="Description of the relationship between the issue and the linked item."),
    ] = None
    self: Annotated[AnyUrl | None, Field(description="The URL of the link.")] = None


class RemoteIssueLinkRequest(BaseModel):
    model_config = ConfigDict(
        extra="allow",
    )
    application: Annotated[
        Application | None,
        Field(
            description="Details of the remote application the linked item is in. For example, trello."
        ),
    ] = None
    global_id: Annotated[
        str | None,
        Field(
            alias="globalId",
            description="An identifier for the remote item in the remote system. For example, the global ID for a remote item in Confluence would consist of the app ID and page ID, like this: `appId=456&pageId=123`.\n\nSetting this field enables the remote issue link details to be updated or deleted using remote system and item details as the record identifier, rather than using the record's Jira ID.\n\nThe maximum length is 255 characters.",
        ),
    ] = None
    object: Annotated[RemoteObject, Field(description="Details of the item linked to.")]
    relationship: Annotated[
        str | None,
        Field(
            description='Description of the relationship between the issue and the linked item. If not set, the relationship description "links to" is used in Jira.'
        ),
    ] = None


class Transitions(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    expand: Annotated[
        str | None,
        Field(
            description="Expand options that include additional transitions details in the response."
        ),
    ] = None
    transitions: Annotated[
        list[IssueTransition] | None, Field(description="List of issue transitions.")
    ] = None


class Fields(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    assignee: Annotated[
        UserDetails | None, Field(description="The assignee of the linked issue.")
    ] = None
    issue_type: Annotated[
        IssueTypeDetails | None,
        Field(alias="issueType", description="The type of the linked issue."),
    ] = None
    issuetype: Annotated[
        IssueTypeDetails | None, Field(description="The type of the linked issue.")
    ] = None
    priority: Annotated[Priority | None, Field(description="The priority of the linked issue.")] = (
        None
    )
    status: Annotated[
        StatusDetails | None, Field(description="The status of the linked issue.")
    ] = None
    summary: Annotated[
        str | None, Field(description="The summary description of the linked issue.")
    ] = None
    timetracking: Annotated[
        TimeTrackingDetails | None, Field(description="The time tracking of the linked issue.")
    ] = None


class IssueBulkEditPayload(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    edited_fields_input: Annotated[
        JiraIssueFields,
        Field(
            alias="editedFieldsInput",
            description="An object that defines the values to be updated in specified fields of an issue. The structure and content of this parameter vary depending on the type of field being edited. Although the order is not significant, ensure that field IDs align with those in selectedActions.",
        ),
    ]
    selected_actions: Annotated[
        list[str],
        Field(
            alias="selectedActions",
            description="List of all the field IDs that are to be bulk edited. Each field ID in this list corresponds to a specific attribute of an issue that is set to be modified in the bulk edit operation. The relevant field ID can be obtained by calling the Bulk Edit Get Fields REST API (documentation available on this page itself).",
        ),
    ]
    selected_issue_ids_or_keys: Annotated[
        list[str],
        Field(
            alias="selectedIssueIdsOrKeys",
            description="List of issue IDs or keys which are to be bulk edited. These IDs or keys can be from different projects and issue types.",
        ),
    ]
    send_bulk_notification: Annotated[
        bool | None,
        Field(
            alias="sendBulkNotification",
            description="A boolean value that indicates whether to send a bulk change notification when the issues are being edited.\n\nIf `true`, dispatches a bulk notification email to users about the updates.",
        ),
    ] = True


class IssueCreateMetadata(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    expand: Annotated[
        str | None,
        Field(
            description="Expand options that include additional project details in the response."
        ),
    ] = None
    projects: Annotated[
        list[ProjectIssueCreateMetadata] | None,
        Field(description="List of projects and their issue creation metadata."),
    ] = None


class LinkedIssue(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    fields: Annotated[Fields | None, Field(description="The fields associated with the issue.")] = (
        None
    )
    id: Annotated[
        str | None, Field(description="The ID of an issue. Required if `key` isn't provided.")
    ] = None
    key: Annotated[
        str | None, Field(description="The key of an issue. Required if `id` isn't provided.")
    ] = None
    self: Annotated[AnyUrl | None, Field(description="The URL of the issue.")] = None


class SearchAndReconcileResults(BaseModel):
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
    issues: Annotated[
        list[Issue] | None,
        Field(description="The list of issues found by the search or reconsiliation."),
    ] = None
    names: Annotated[
        dict[str, str] | None,
        Field(description="The ID and name of each field in the search results."),
    ] = None
    next_page_token: Annotated[
        str | None,
        Field(
            alias="nextPageToken",
            description="Continuation token to fetch the next page. If this result represents the last or the only page this token will be null. This token will expire in 7 days.",
        ),
    ] = None
    schema_: Annotated[
        dict[str, JsonType] | None,
        Field(
            alias="schema",
            description="The schema describing the field types in the search results.",
        ),
    ] = None


class SearchResults(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    expand: Annotated[
        str | None,
        Field(
            description="Expand options that include additional search result details in the response."
        ),
    ] = None
    issues: Annotated[
        list[Issue] | None, Field(description="The list of issues found by the search.")
    ] = None
    max_results: Annotated[
        int | None,
        Field(
            alias="maxResults",
            description="The maximum number of results that could be on the page.",
        ),
    ] = None
    names: Annotated[
        dict[str, str] | None,
        Field(description="The ID and name of each field in the search results."),
    ] = None
    schema_: Annotated[
        dict[str, JsonType] | None,
        Field(
            alias="schema",
            description="The schema describing the field types in the search results.",
        ),
    ] = None
    start_at: Annotated[
        int | None,
        Field(
            alias="startAt",
            description="The index of the first item returned on the page.",
        ),
    ] = None
    total: Annotated[int | None, Field(description="The number of results on the page.")] = None
    warning_messages: Annotated[
        list[str] | None,
        Field(
            alias="warningMessages",
            description="Any warnings related to the JQL query.",
        ),
    ] = None


class BulkIssueResults(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    issue_errors: Annotated[
        list[IssueError] | None,
        Field(
            alias="issueErrors",
            description="When Jira can't return an issue enumerated in a request due to a retriable error or payload constraint, we'll return the respective issue ID with a corresponding error message. This list is empty when there are no errors Issues which aren't found or that the user doesn't have permission to view won't be returned in this list.",
        ),
    ] = None
    issues: Annotated[list[Issue] | None, Field(description="The list of issues.")] = None


class IssueLink(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    id: Annotated[str | None, Field(description="The ID of the issue link.")] = None
    inward_issue: Annotated[
        LinkedIssue,
        Field(
            alias="inwardIssue",
            description="Provides details about the linked issue. If presenting this link in a user interface, use the `inward` field of the issue link type to label the link.",
        ),
    ]
    outward_issue: Annotated[
        LinkedIssue,
        Field(
            alias="outwardIssue",
            description="Provides details about the linked issue. If presenting this link in a user interface, use the `outward` field of the issue link type to label the link.",
        ),
    ]
    self: Annotated[AnyUrl | None, Field(description="The URL of the issue link.")] = None
    type: Annotated[IssueLinkType, Field(description="The type of link between the issues.")]


__all__ = [
    "Application",
    "ArchiveIssueAsyncRequest",
    "AttachmentArchiveEntry",
    "AttachmentArchiveImpl",
    "AttachmentArchiveItemReadable",
    "AttachmentArchiveMetadataReadable",
    "AttachmentSettings",
    "BulkIssueIsWatching",
    "BulkTransitionSubmitInput",
    "ChangeDetails",
    "ContentItem",
    "DateRangeFilterRequest",
    "Error",
    "Errors",
    "ExportArchivedIssuesTaskProgressResponse",
    "FieldUpdateOperation",
    "HistoryMetadataParticipant",
    "Icon",
    "IncludedFields",
    "IssueArchivalSyncRequest",
    "IssueArchivalSyncResponse",
    "IssueBulkDeletePayload",
    "IssueBulkOperationsFieldOption",
    "IssueBulkTransitionPayload",
    "IssueBulkWatchOrUnwatchPayload",
    "IssueChangelogIds",
    "IssueError",
    "IssueEvent",
    "IssueFilterForBulkPropertyDelete",
    "IssueFilterForBulkPropertySet",
    "IssueList",
    "IssueMatchesForJQL",
    "IssueTransitionStatus",
    "IssuesAndJQLQueries",
    "JiraColorInput",
    "JiraComponentField",
    "JiraDateInput",
    "JiraDateTimeInput",
    "JiraDurationField",
    "JiraGroupInput",
    "JiraIssueTypeField",
    "JiraLabelPropertiesInputJackson1",
    "JiraLabelsInput",
    "JiraMultiSelectComponentField",
    "JiraMultipleGroupPickerField",
    "JiraNumberField",
    "JiraPriorityField",
    "JiraRichTextInput",
    "JiraSelectedOptionField",
    "JiraSingleGroupPickerField",
    "JiraSingleLineTextField",
    "JiraSingleSelectField",
    "JiraStatusInput",
    "JiraTimeTrackingField",
    "JiraUrlField",
    "JiraUserField",
    "JiraVersionField",
    "LegacyJackson1ListIssueEvent",
    "MandatoryFieldValue",
    "MandatoryFieldValueForADF",
    "RedactionPosition",
    "RemoteIssueLinkIdentifies",
    "Resource",
    "RestrictedPermission",
    "SimplifiedIssueTransition",
    "SingleRedactionRequest",
    "SingleRedactionResponse",
    "SubmittedBulkOperation",
    "SuggestedIssue",
    "TimeTrackingDetails",
    "WarningCollection",
    "Watchers",
    "Worklog",
    "WorklogCompositeKey",
    "WorklogKeyResult",
    "Fields2",
    "Fields3",
    "ArchivedIssuesFilterRequest",
    "Attachment",
    "BulkIssuePropertyUpdateRequest",
    "BulkOperationErrorResponse",
    "BulkOperationErrorResult",
    "BulkRedactionRequest",
    "BulkRedactionResponse",
    "ChangedWorklog",
    "ChangedWorklogs",
    "Comment",
    "FieldCreateMetadata",
    "FieldMetadata",
    "HistoryMetadata",
    "IssueBulkEditField",
    "IssueBulkMovePayload",
    "IssueBulkTransitionForWorkflow",
    "IssueEntityProperties",
    "IssueEntityPropertiesForMultiUpdate",
    "IssueMatches",
    "IssuePickerSuggestionsIssueType",
    "IssueUpdateMetadata",
    "JiraCascadingSelectField",
    "JiraColorField",
    "JiraDateField",
    "JiraDateTimeField",
    "JiraLabelsField",
    "JiraMultipleSelectField",
    "JiraMultipleSelectUserPickerField",
    "JiraMultipleVersionPickerField",
    "JiraRichTextField",
    "JiraSingleSelectUserPickerField",
    "JiraSingleVersionPickerField",
    "LegacyJackson1ListAttachment",
    "LegacyJackson1ListWorklog",
    "LinkGroup",
    "MultiIssueEntityProperties",
    "MultipartFile",
    "NestedResponse",
    "NotificationRecipients",
    "NotificationRecipientsRestrictions",
    "Operations",
    "PageBeanComment",
    "PageOfComments",
    "PageOfCreateMetaIssueTypeWithField",
    "PageOfWorklogs",
    "RedactionJobStatusResponse",
    "RemoteObject",
    "Votes",
    "AttachmentMetadata",
    "BulkEditGetFields",
    "BulkOperationProgress",
    "BulkTransitionGetAvailableTransitions",
    "Changelog",
    "CreatedIssue",
    "CreatedIssues",
    "IssueChangeLog",
    "IssuePickerSuggestions",
    "IssueTransition",
    "IssueTypeIssueCreateMetadata",
    "IssueUpdateDetails",
    "JiraIssueFields",
    "Notification",
    "PageBeanChangelog",
    "PageOfChangelogs",
    "PageOfCreateMetaIssueTypes",
    "ProjectIssueCreateMetadata",
    "RemoteIssueLink",
    "RemoteIssueLinkRequest",
    "Transitions",
    "Fields",
    "IssueBulkEditPayload",
    "IssueCreateMetadata",
    "LinkedIssue",
    "SearchAndReconcileResults",
    "SearchResults",
    "BulkIssueResults",
    "IssueLink",
]
