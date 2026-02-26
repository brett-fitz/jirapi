"""Pydantic models for the fields domain."""

from __future__ import annotations

from typing import Annotated, Any, Literal

from pydantic import AnyUrl, AwareDatetime, BaseModel, ConfigDict, Field


class AssociationContextObject(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    identifier: dict[str, Any] | None = None
    type: str


class BulkContextualConfiguration(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    configuration: Annotated[Any | None, Field(description="The field configuration.")] = None
    custom_field_id: Annotated[
        str, Field(alias="customFieldId", description="The ID of the custom field.")
    ]
    field_context_id: Annotated[
        str,
        Field(
            alias="fieldContextId",
            description="The ID of the field context the configuration is associated with.",
        ),
    ]
    id: Annotated[str, Field(description="The ID of the configuration.")]
    schema_: Annotated[Any | None, Field(alias="schema", description="The field value schema.")] = (
        None
    )


class ConfigurationsListParameters(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    field_ids_or_keys: Annotated[
        list[str],
        Field(
            alias="fieldIdsOrKeys",
            description="List of IDs or keys of the custom fields. It can be a mix of IDs and keys in the same query.",
            min_length=1,
        ),
    ]


class ContextForProjectAndIssueType(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    context_id: Annotated[
        str, Field(alias="contextId", description="The ID of the custom field context.")
    ]
    issue_type_id: Annotated[
        str, Field(alias="issueTypeId", description="The ID of the issue type.")
    ]
    project_id: Annotated[str, Field(alias="projectId", description="The ID of the project.")]


class ContextualConfiguration(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    configuration: Annotated[Any | None, Field(description="The field configuration.")] = None
    field_context_id: Annotated[
        str,
        Field(
            alias="fieldContextId",
            description="The ID of the field context the configuration is associated with.",
        ),
    ]
    id: Annotated[str, Field(description="The ID of the configuration.")]
    schema_: Annotated[Any | None, Field(alias="schema", description="The field value schema.")] = (
        None
    )


class CreateCustomFieldContext(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    description: Annotated[str | None, Field(description="The description of the context.")] = None
    id: Annotated[str | None, Field(description="The ID of the context.")] = None
    issue_type_ids: Annotated[
        list[str] | None,
        Field(
            alias="issueTypeIds",
            description="The list of issue types IDs for the context. If the list is empty, the context refers to all issue types.",
        ),
    ] = None
    name: Annotated[str, Field(description="The name of the context.")]
    project_ids: Annotated[
        list[str] | None,
        Field(
            alias="projectIds",
            description="The list of project IDs associated with the context. If the list is empty, the context is global.",
        ),
    ] = None


class CreateFieldAssociationSchemeRequest(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    description: Annotated[
        str | None, Field(description="Description of the scheme to be created")
    ] = None
    name: Annotated[str, Field(description="The name of the scheme to be created")]


class CreateFieldAssociationSchemeResponse(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    description: str | None = None
    id: int | None = None
    links: CreateFieldAssociationSchemeLinks | None = None
    name: str | None = None


class CustomFieldConfigurations(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    configurations: Annotated[
        list[ContextualConfiguration],
        Field(
            description="The list of custom field configuration details.",
            max_length=1000,
            min_length=1,
        ),
    ]


class CustomFieldContext(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    description: Annotated[str, Field(description="The description of the context.")]
    id: Annotated[str, Field(description="The ID of the context.")]
    is_any_issue_type: Annotated[
        bool,
        Field(
            alias="isAnyIssueType",
            description="Whether the context apply to all issue types.",
        ),
    ]
    is_global_context: Annotated[
        bool, Field(alias="isGlobalContext", description="Whether the context is global.")
    ]
    name: Annotated[str, Field(description="The name of the context.")]


class CustomFieldContextDefaultValueCascadingOption(BaseModel):
    cascading_option_id: Annotated[
        str | None,
        Field(
            alias="cascadingOptionId",
            description="The ID of the default cascading option.",
        ),
    ] = None
    context_id: Annotated[str, Field(alias="contextId", description="The ID of the context.")]
    option_id: Annotated[str, Field(alias="optionId", description="The ID of the default option.")]
    type: Literal["option.cascading"]


class CustomFieldContextDefaultValueDate(BaseModel):
    date: Annotated[
        str | None,
        Field(description="The default date in ISO format. Ignored if `useCurrent` is true."),
    ] = None
    type: Literal["datepicker"]
    use_current: Annotated[
        bool, Field(alias="useCurrent", description="Whether to use the current date.")
    ] = False


class CustomFieldContextDefaultValueDateTime(BaseModel):
    date_time: Annotated[
        str | None,
        Field(
            alias="dateTime",
            description="The default date-time in ISO format. Ignored if `useCurrent` is true.",
        ),
    ] = None
    type: Literal["datetimepicker"]
    use_current: Annotated[
        bool, Field(alias="useCurrent", description="Whether to use the current date.")
    ] = False


class CustomFieldContextDefaultValueFloat(BaseModel):
    number: Annotated[float, Field(description="The default floating-point number.")]
    type: Literal["float"]


class CustomFieldContextDefaultValueForgeDateTimeField(BaseModel):
    context_id: Annotated[str, Field(alias="contextId", description="The ID of the context.")]
    date_time: Annotated[
        str | None,
        Field(
            alias="dateTime",
            description="The default date-time in ISO format. Ignored if `useCurrent` is true.",
        ),
    ] = None
    type: Literal["forge.datetime"]
    use_current: Annotated[
        bool, Field(alias="useCurrent", description="Whether to use the current date.")
    ] = False


class CustomFieldContextDefaultValueForgeGroupField(BaseModel):
    context_id: Annotated[str, Field(alias="contextId", description="The ID of the context.")]
    group_id: Annotated[str, Field(alias="groupId", description="The ID of the the default group.")]
    type: Literal["forge.group"]


class CustomFieldContextDefaultValueForgeMultiGroupField(BaseModel):
    context_id: Annotated[str, Field(alias="contextId", description="The ID of the context.")]
    group_ids: Annotated[
        list[str], Field(alias="groupIds", description="The IDs of the default groups.")
    ]
    type: Literal["forge.group.list"]


class CustomFieldContextDefaultValueForgeMultiStringField(BaseModel):
    type: Literal["forge.string.list"]
    values: Annotated[
        list[str] | None,
        Field(
            description="List of string values. The maximum length for a value is 254 characters."
        ),
    ] = None


class CustomFieldContextDefaultValueForgeMultiUserField(BaseModel):
    account_ids: Annotated[
        list[str], Field(alias="accountIds", description="The IDs of the default users.")
    ]
    context_id: Annotated[str, Field(alias="contextId", description="The ID of the context.")]
    type: Literal["forge.user.list"]


class CustomFieldContextDefaultValueForgeNumberField(BaseModel):
    context_id: Annotated[str, Field(alias="contextId", description="The ID of the context.")]
    number: Annotated[float, Field(description="The default floating-point number.")]
    type: Literal["forge.number"]


class CustomFieldContextDefaultValueForgeObjectField(BaseModel):
    object: Annotated[dict[str, Any] | None, Field(description="The default JSON object.")] = None
    type: Literal["forge.object"]


class CustomFieldContextDefaultValueForgeStringField(BaseModel):
    context_id: Annotated[str, Field(alias="contextId", description="The ID of the context.")]
    text: Annotated[
        str | None, Field(description="The default text. The maximum length is 254 characters.")
    ] = None
    type: Literal["forge.string"]


class CustomFieldContextDefaultValueLabels(BaseModel):
    labels: Annotated[list[str], Field(description="The default labels value.")]
    type: Literal["labels"]


class CustomFieldContextDefaultValueMultiUserPicker(BaseModel):
    account_ids: Annotated[
        list[str], Field(alias="accountIds", description="The IDs of the default users.")
    ]
    context_id: Annotated[str, Field(alias="contextId", description="The ID of the context.")]
    type: Literal["multi.user.select"]


class CustomFieldContextDefaultValueMultipleGroupPicker(BaseModel):
    context_id: Annotated[str, Field(alias="contextId", description="The ID of the context.")]
    group_ids: Annotated[
        list[str], Field(alias="groupIds", description="The IDs of the default groups.")
    ]
    type: Literal["grouppicker.multiple"]


class CustomFieldContextDefaultValueMultipleOption(BaseModel):
    context_id: Annotated[str, Field(alias="contextId", description="The ID of the context.")]
    option_ids: Annotated[
        list[str], Field(alias="optionIds", description="The list of IDs of the default options.")
    ]
    type: Literal["option.multiple"]


class CustomFieldContextDefaultValueMultipleVersionPicker(BaseModel):
    type: Literal["version.multiple"]
    version_ids: Annotated[
        list[str], Field(alias="versionIds", description="The IDs of the default versions.")
    ]
    version_order: Annotated[
        str | None,
        Field(
            alias="versionOrder",
            description='The order the pickable versions are displayed in. If not provided, the released-first order is used. Available version orders are `"releasedFirst"` and `"unreleasedFirst"`.',
        ),
    ] = None


class CustomFieldContextDefaultValueProject(BaseModel):
    context_id: Annotated[str, Field(alias="contextId", description="The ID of the context.")]
    project_id: Annotated[
        str, Field(alias="projectId", description="The ID of the default project.")
    ]
    type: Literal["project"]


class CustomFieldContextDefaultValueReadOnly(BaseModel):
    text: Annotated[
        str | None, Field(description="The default text. The maximum length is 255 characters.")
    ] = None
    type: Literal["readonly"]


class CustomFieldContextDefaultValueSingleGroupPicker(BaseModel):
    context_id: Annotated[str, Field(alias="contextId", description="The ID of the context.")]
    group_id: Annotated[str, Field(alias="groupId", description="The ID of the the default group.")]
    type: Literal["grouppicker.single"]


class CustomFieldContextDefaultValueSingleOption(BaseModel):
    context_id: Annotated[str, Field(alias="contextId", description="The ID of the context.")]
    option_id: Annotated[str, Field(alias="optionId", description="The ID of the default option.")]
    type: Literal["option.single"]


class CustomFieldContextDefaultValueSingleVersionPicker(BaseModel):
    type: Literal["version.single"]
    version_id: Annotated[
        str, Field(alias="versionId", description="The ID of the default version.")
    ]
    version_order: Annotated[
        str | None,
        Field(
            alias="versionOrder",
            description='The order the pickable versions are displayed in. If not provided, the released-first order is used. Available version orders are `"releasedFirst"` and `"unreleasedFirst"`.',
        ),
    ] = None


class CustomFieldContextDefaultValueTextArea(BaseModel):
    text: Annotated[
        str | None, Field(description="The default text. The maximum length is 32767 characters.")
    ] = None
    type: Literal["textarea"]


class CustomFieldContextDefaultValueTextField(BaseModel):
    text: Annotated[
        str | None, Field(description="The default text. The maximum length is 254 characters.")
    ] = None
    type: Literal["textfield"]


class CustomFieldContextDefaultValueURL(BaseModel):
    context_id: Annotated[str, Field(alias="contextId", description="The ID of the context.")]
    type: Literal["url"]
    url: Annotated[str, Field(description="The default URL.")]


class CustomFieldContextOption(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    disabled: Annotated[bool, Field(description="Whether the option is disabled.")]
    id: Annotated[str, Field(description="The ID of the custom field option.")]
    option_id: Annotated[
        str | None,
        Field(
            alias="optionId",
            description="For cascading options, the ID of the custom field option containing the cascading option.",
        ),
    ] = None
    value: Annotated[str, Field(description="The value of the custom field option.")]


class CustomFieldContextProjectMapping(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    context_id: Annotated[str, Field(alias="contextId", description="The ID of the context.")]
    is_global_context: Annotated[
        bool | None, Field(alias="isGlobalContext", description="Whether context is global.")
    ] = None
    project_id: Annotated[
        str | None, Field(alias="projectId", description="The ID of the project.")
    ] = None


class CustomFieldContextUpdateDetails(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    description: Annotated[
        str | None,
        Field(
            description="The description of the custom field context. The maximum length is 255 characters."
        ),
    ] = None
    name: Annotated[
        str | None,
        Field(
            description="The name of the custom field context. The name must be unique. The maximum length is 255 characters."
        ),
    ] = None


class CustomFieldCreatedContextOptionsList(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    options: Annotated[
        list[CustomFieldContextOption] | None,
        Field(description="The created custom field options."),
    ] = None


class CustomFieldOption(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    self: Annotated[
        AnyUrl | None, Field(description="The URL of these custom field option details.")
    ] = None
    value: Annotated[str | None, Field(description="The value of the custom field option.")] = None


class CustomFieldOptionCreate(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    disabled: Annotated[bool | None, Field(description="Whether the option is disabled.")] = None
    option_id: Annotated[
        str | None,
        Field(
            alias="optionId",
            description="For cascading options, the ID of a parent option.",
        ),
    ] = None
    value: Annotated[str, Field(description="The value of the custom field option.")]


class CustomFieldOptionUpdate(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    disabled: Annotated[bool | None, Field(description="Whether the option is disabled.")] = None
    id: Annotated[str, Field(description="The ID of the custom field option.")]
    value: Annotated[str | None, Field(description="The value of the custom field option.")] = None


class CustomFieldUpdatedContextOptionsList(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    options: Annotated[
        list[CustomFieldOptionUpdate] | None, Field(description="The updated custom field options.")
    ] = None


class CustomFieldValueUpdate(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    issue_ids: Annotated[list[int], Field(alias="issueIds", description="The list of issue IDs.")]
    value: Annotated[
        Any,
        Field(
            description='The value for the custom field. The value must be compatible with the [custom field type](https://developer.atlassian.com/platform/forge/manifest-reference/modules/jira-custom-field/#data-types) as follows:\n\n *  `string` the value must be a string.\n *  `number` the value must be a number.\n *  `datetime` the value must be a string that represents a date in the ISO format or the simplified extended ISO format. For example, `"2023-01-18T12:00:00-03:00"` or `"2023-01-18T12:00:00.000Z"`. However, the milliseconds part is ignored.\n *  `user` the value must be an object that contains the `accountId` field.\n *  `group` the value must be an object that contains the group `name` or `groupId` field. Because group names can change, we recommend using `groupId`.\n\nA list of appropriate values must be provided if the field is of the `list` [collection type](https://developer.atlassian.com/platform/forge/manifest-reference/modules/jira-custom-field/#collection-types).'
        ),
    ]


class CustomFieldValueUpdateDetails(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    updates: Annotated[
        list[CustomFieldValueUpdate] | None,
        Field(description="The list of custom field update details."),
    ] = None


class DeleteFieldAssociationSchemeResponse(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    deleted: bool | None = None
    id: str | None = None


class FieldAssociationParameters(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    description: str | None = None
    is_required: Annotated[bool, Field(alias="isRequired")]


class FieldAssociationSchemeLinks(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    associations: str | None = None
    projects: str | None = None


class FieldAssociationSchemeMatchedFilters(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    project_ids: Annotated[list[int] | None, Field(alias="projectIds")] = None
    query: str | None = None


class FieldAssociationSchemeProjectSearchResult(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    id: str | None = None
    name: str | None = None


class FieldIdentifierObject(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    identifier: dict[str, Any] | None = None
    type: str


class FieldLastUsed(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    type: Annotated[
        Type5 | None,
        Field(
            description="Last used value type:\n\n *  *TRACKED*: field is tracked and a last used date is available.\n *  *NOT\\_TRACKED*: field is not tracked, last used date is not available.\n *  *NO\\_INFORMATION*: field is tracked, but no last used date is available."
        ),
    ] = None
    value: Annotated[
        AwareDatetime | None,
        Field(description="The date when the value of the field last changed."),
    ] = None


class FieldSchemeToFieldsPartialFailure(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    error: str | None = None
    field_id: Annotated[str, Field(alias="fieldId")]
    scheme_id: Annotated[int, Field(alias="schemeId")]
    success: bool
    work_type_ids: Annotated[list[int], Field(alias="workTypeIds")]


class FieldSchemeToFieldsResponse(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    results: list[FieldSchemeToFieldsPartialFailure]


class FieldSchemeToProjectsPartialFailure(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    error: str | None = None
    project_id: Annotated[int, Field(alias="projectId")]
    scheme_id: Annotated[int, Field(alias="schemeId")]
    success: bool


class FieldSchemeToProjectsRequest(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    project_ids: Annotated[
        list[int],
        Field(
            alias="projectIds",
            description="List of project IDs to associate with field schemes",
        ),
    ]


class FieldSchemeToProjectsResponse(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    results: list[FieldSchemeToProjectsPartialFailure]


class FieldsSchemeItemParameter(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    description: Annotated[
        str | None,
        Field(
            description="The custom description for the field, null to preserve current description"
        ),
    ] = None
    is_required: Annotated[
        bool | None,
        Field(
            alias="isRequired",
            description="Whether the field is required, null to preserve current requirement setting",
        ),
    ] = None


class FieldsSchemeItemWorkTypeParameter(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    description: Annotated[
        str | None,
        Field(
            description="The custom description for the field for this work type, null to use default or preserve current"
        ),
    ] = None
    is_required: Annotated[
        bool | None,
        Field(
            alias="isRequired",
            description="Whether the field is required for this work type, null to use default or preserve current",
        ),
    ] = None
    work_type_id: Annotated[
        int | None,
        Field(
            alias="workTypeId",
            description="The ID of the work type (issue type) for which these parameters apply",
        ),
    ] = None


class GetFieldAssociationSchemeByIdResponse(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    description: str | None = None
    id: str | None = None
    is_default: Annotated[bool | None, Field(alias="isDefault")] = None
    links: FieldAssociationSchemeLinks | None = None
    name: str | None = None


class GetFieldAssociationSchemeResponse(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    description: str | None = None
    id: int | None = None
    is_default: Annotated[bool | None, Field(alias="isDefault")] = None
    links: FieldAssociationSchemeLinks | None = None
    matched_filters: Annotated[
        FieldAssociationSchemeMatchedFilters | None, Field(alias="matchedFilters")
    ] = None
    name: str | None = None


class GetProjectsWithFieldSchemesResponse(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    project_id: Annotated[int | None, Field(alias="projectId")] = None
    scheme_id: Annotated[int | None, Field(alias="schemeId")] = None


class IssueTypeToContextMapping(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    context_id: Annotated[str, Field(alias="contextId", description="The ID of the context.")]
    is_any_issue_type: Annotated[
        bool | None,
        Field(
            alias="isAnyIssueType",
            description="Whether the context is mapped to any issue type.",
        ),
    ] = None
    issue_type_id: Annotated[
        str | None, Field(alias="issueTypeId", description="The ID of the issue type.")
    ] = None


class MinimalFieldSchemeToFieldsPartialFailure(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    error: str | None = None
    field_id: Annotated[str, Field(alias="fieldId")]
    scheme_id: Annotated[int, Field(alias="schemeId")]
    success: bool


class MinimalFieldSchemeToFieldsResponse(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    results: list[MinimalFieldSchemeToFieldsPartialFailure]


class MultipleCustomFieldValuesUpdate(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    custom_field: Annotated[
        str,
        Field(
            alias="customField",
            description="The ID or key of the custom field. For example, `customfield_10010`.",
        ),
    ]
    issue_ids: Annotated[list[int], Field(alias="issueIds", description="The list of issue IDs.")]
    value: Annotated[
        Any,
        Field(
            description='The value for the custom field. The value must be compatible with the [custom field type](https://developer.atlassian.com/platform/forge/manifest-reference/modules/jira-custom-field/#data-types) as follows:\n\n *  `string` the value must be a string.\n *  `number` the value must be a number.\n *  `datetime` the value must be a string that represents a date in the ISO format or the simplified extended ISO format. For example, `"2023-01-18T12:00:00-03:00"` or `"2023-01-18T12:00:00.000Z"`. However, the milliseconds part is ignored.\n *  `user` the value must be an object that contains the `accountId` field.\n *  `group` the value must be an object that contains the group `name` or `groupId` field. Because group names can change, we recommend using `groupId`.\n\nA list of appropriate values must be provided if the field is of the `list` [collection type](https://developer.atlassian.com/platform/forge/manifest-reference/modules/jira-custom-field/#collection-types).'
        ),
    ]


class MultipleCustomFieldValuesUpdateDetails(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    updates: list[MultipleCustomFieldValuesUpdate] | None = None


class OrderOfCustomFieldOptions(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    after: Annotated[
        str | None,
        Field(
            description="The ID of the custom field option or cascading option to place the moved options after. Required if `position` isn't provided."
        ),
    ] = None
    custom_field_option_ids: Annotated[
        list[str],
        Field(
            alias="customFieldOptionIds",
            description="A list of IDs of custom field options to move. The order of the custom field option IDs in the list is the order they are given after the move. The list must contain custom field options or cascading options, but not both.",
        ),
    ]
    position: Annotated[
        Position1 | None,
        Field(
            description="The position the custom field options should be moved to. Required if `after` isn't provided."
        ),
    ] = None


class PageBean2FieldAssociationSchemeProjectSearchResult(BaseModel):
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
        list[FieldAssociationSchemeProjectSearchResult] | None,
        Field(description="The list of items."),
    ] = None


class PageBean2GetFieldAssociationSchemeResponse(BaseModel):
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
        list[GetFieldAssociationSchemeResponse] | None, Field(description="The list of items.")
    ] = None


class PageBean2GetProjectsWithFieldSchemesResponse(BaseModel):
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
        list[GetProjectsWithFieldSchemesResponse] | None, Field(description="The list of items.")
    ] = None


class PageBeanBulkContextualConfiguration(BaseModel):
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
        list[BulkContextualConfiguration] | None, Field(description="The list of items.")
    ] = None


class PageBeanContextForProjectAndIssueType(BaseModel):
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
        list[ContextForProjectAndIssueType] | None, Field(description="The list of items.")
    ] = None


class PageBeanContextualConfiguration(BaseModel):
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
        list[ContextualConfiguration] | None, Field(description="The list of items.")
    ] = None


class PageBeanCustomFieldContext(BaseModel):
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
    values: Annotated[list[CustomFieldContext] | None, Field(description="The list of items.")] = (
        None
    )


class PageBeanCustomFieldContextOption(BaseModel):
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
        list[CustomFieldContextOption] | None, Field(description="The list of items.")
    ] = None


class PageBeanCustomFieldContextProjectMapping(BaseModel):
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
        list[CustomFieldContextProjectMapping] | None, Field(description="The list of items.")
    ] = None


class PageBeanIssueTypeToContextMapping(BaseModel):
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
        list[IssueTypeToContextMapping] | None, Field(description="The list of items.")
    ] = None


class ParameterRemovalDetails(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    parameters: Annotated[
        list[str] | None, Field(description="Set of parameter names to remove")
    ] = None
    scheme_id: Annotated[
        int | None, Field(alias="schemeId", description="ID of the field scheme")
    ] = None
    work_type_ids: Annotated[
        list[int] | None,
        Field(alias="workTypeIds", description="Set of work type (issue type) IDs"),
    ] = None


class ProjectIdAssociationContext(AssociationContextObject):
    identifier: int | None = None


class ProjectIds(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    project_ids: Annotated[list[str], Field(alias="projectIds", description="The IDs of projects.")]


class ProjectIssueTypeMapping(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    issue_type_id: Annotated[
        str, Field(alias="issueTypeId", description="The ID of the issue type.")
    ]
    project_id: Annotated[str, Field(alias="projectId", description="The ID of the project.")]


class ProjectIssueTypeMappings(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    mappings: Annotated[
        list[ProjectIssueTypeMapping], Field(description="The project and issue type mappings.")
    ]


class RemoveFieldAssociationsRequestItem(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    scheme_ids: Annotated[
        list[int],
        Field(
            alias="schemeIds",
            description="Set of scheme IDs from which to remove field associations",
        ),
    ]


class RemoveFieldParametersResultError(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    code: str | None = None
    message: str | None = None


class SearchResultFieldParameters(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    description: str | None = None
    is_required: Annotated[bool | None, Field(alias="isRequired")] = None


class SearchResultWorkTypeParameters(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    description: str | None = None
    is_required: Annotated[bool | None, Field(alias="isRequired")] = None
    work_type_id: Annotated[str | None, Field(alias="workTypeId")] = None


class SimpleErrorCollection(BaseModel):
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
    http_status_code: Annotated[int | None, Field(alias="httpStatusCode")] = None


class SuccessOrErrorResults(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    error: RemoveFieldParametersResultError | None = None
    field_id: Annotated[str | None, Field(alias="fieldId")] = None
    scheme_id: Annotated[int | None, Field(alias="schemeId")] = None
    success: bool | None = None
    work_type_ids: Annotated[list[int] | None, Field(alias="workTypeIds")] = None


class UpdateCustomFieldDetails(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    description: Annotated[
        str | None,
        Field(
            description="The description of the custom field. The maximum length is 40000 characters."
        ),
    ] = None
    name: Annotated[
        str | None,
        Field(
            description="The name of the custom field. It doesn't have to be unique. The maximum length is 255 characters."
        ),
    ] = None
    searcher_key: Annotated[
        SearcherKey | None,
        Field(
            alias="searcherKey",
            description="The searcher that defines the way the field is searched in Jira. It can be set to `null`, otherwise you must specify the valid searcher for the field type, as listed below (abbreviated values shown):\n\n *  `cascadingselect`: `cascadingselectsearcher`\n *  `datepicker`: `daterange`\n *  `datetime`: `datetimerange`\n *  `float`: `exactnumber` or `numberrange`\n *  `grouppicker`: `grouppickersearcher`\n *  `importid`: `exactnumber` or `numberrange`\n *  `labels`: `labelsearcher`\n *  `multicheckboxes`: `multiselectsearcher`\n *  `multigrouppicker`: `multiselectsearcher`\n *  `multiselect`: `multiselectsearcher`\n *  `multiuserpicker`: `userpickergroupsearcher`\n *  `multiversion`: `versionsearcher`\n *  `project`: `projectsearcher`\n *  `radiobuttons`: `multiselectsearcher`\n *  `readonlyfield`: `textsearcher`\n *  `select`: `multiselectsearcher`\n *  `textarea`: `textsearcher`\n *  `textfield`: `textsearcher`\n *  `url`: `exacttextsearcher`\n *  `userpicker`: `userpickergroupsearcher`\n *  `version`: `versionsearcher`",
        ),
    ] = None


class UpdateFieldAssociationSchemeRequest(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    description: Annotated[str | None, Field(description="The description value to update")] = None
    name: Annotated[str | None, Field(description="The name value to update")] = None


class UpdateFieldAssociationSchemeResponse(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    description: str | None = None
    id: int | None = None
    links: UpdateFieldAssociationSchemeLinks | None = None
    name: str | None = None


class UpdateFieldAssociationsRequestItem(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    restricted_to_work_types: Annotated[
        list[int] | None,
        Field(
            alias="restrictedToWorkTypes",
            description="(optional) Work types to restrict field to. Replaces any existing work type associations for the field. If not provided, the field is associated to any work types.",
        ),
    ] = None
    scheme_ids: Annotated[
        list[int], Field(alias="schemeIds", description="Scheme IDs to associate field with")
    ]


class UpdateFieldSchemeParametersPartialFailure(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    error: str | None = None
    field_id: Annotated[str, Field(alias="fieldId")]
    scheme_id: Annotated[int, Field(alias="schemeId")]
    success: bool
    work_type_id: Annotated[int | None, Field(alias="workTypeId")] = None


class UpdateFieldSchemeParametersRequest(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    parameters: FieldsSchemeItemParameter | None = None
    scheme_ids: Annotated[
        list[int] | None,
        Field(alias="schemeIds", description="The list of field scheme IDs to update"),
    ] = None
    work_type_parameters: Annotated[
        list[FieldsSchemeItemWorkTypeParameter] | None,
        Field(
            alias="workTypeParameters",
            description="The list of work type-specific parameter overrides, may be empty if only default parameters are being updated",
        ),
    ] = None


class UpdateFieldSchemeParametersResponse(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    results: list[UpdateFieldSchemeParametersPartialFailure]


class UserFilter(BaseModel):
    enabled: Annotated[bool, Field(description="Whether the filter is enabled.")]
    groups: Annotated[
        list[str] | None,
        Field(
            description="User groups autocomplete suggestion users must belong to. If not provided, the default values are used. A maximum of 10 groups can be provided."
        ),
    ] = None
    role_ids: Annotated[
        list[int] | None,
        Field(
            alias="roleIds",
            description="Roles that autocomplete suggestion users must belong to. If not provided, the default values are used. A maximum of 10 roles can be provided.",
        ),
    ] = None


class WorkTypeParameters(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    description: str | None = None
    is_required: Annotated[bool, Field(alias="isRequired")]
    work_type_id: Annotated[int, Field(alias="workTypeId")]


class BulkCustomFieldOptionCreateRequest(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    options: Annotated[
        list[CustomFieldOptionCreate] | None, Field(description="Details of options to create.")
    ] = None


class BulkCustomFieldOptionUpdateRequest(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    options: Annotated[
        list[CustomFieldOptionUpdate] | None, Field(description="Details of the options to update.")
    ] = None


class CustomFieldContextDefaultValueForgeUserField(BaseModel):
    account_id: Annotated[str, Field(alias="accountId", description="The ID of the default user.")]
    context_id: Annotated[str, Field(alias="contextId", description="The ID of the context.")]
    type: Literal["forge.user"]
    user_filter: Annotated[UserFilter, Field(alias="userFilter")]


class CustomFieldContextSingleUserPickerDefaults(BaseModel):
    account_id: Annotated[str, Field(alias="accountId", description="The ID of the default user.")]
    context_id: Annotated[str, Field(alias="contextId", description="The ID of the context.")]
    type: Literal["single.user.select"]
    user_filter: Annotated[UserFilter, Field(alias="userFilter")]


class FieldAssociationSchemeFieldSearchResult(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    allowed_operations: Annotated[list[str] | None, Field(alias="allowedOperations")] = None
    field_id: Annotated[str | None, Field(alias="fieldId")] = None
    parameters: SearchResultFieldParameters | None = None
    restricted_to_work_types: Annotated[list[str] | None, Field(alias="restrictedToWorkTypes")] = (
        None
    )
    work_type_parameters: Annotated[
        list[SearchResultWorkTypeParameters] | None, Field(alias="workTypeParameters")
    ] = None


class FieldIdIdentifier(FieldIdentifierObject):
    identifier: str | None = None


class GetFieldAssociationParametersResponse(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    field_id: Annotated[str, Field(alias="fieldId")]
    parameters: FieldAssociationParameters | None = None
    work_type_parameters: Annotated[
        list[WorkTypeParameters] | None, Field(alias="workTypeParameters")
    ] = None


class PageBean2FieldAssociationSchemeFieldSearchResult(BaseModel):
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
        list[FieldAssociationSchemeFieldSearchResult] | None,
        Field(description="The list of items."),
    ] = None


class PageBeanField(BaseModel):
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
    values: Annotated[list[FieldModel] | None, Field(description="The list of items.")] = None


class RemoveFieldParametersResult(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    results: list[SuccessOrErrorResults] | None = None


class RemoveOptionFromIssuesResult(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    errors: Annotated[
        SimpleErrorCollection | None,
        Field(
            description="A collection of errors related to unchanged issues. The collection size is limited, which means not all errors may be returned."
        ),
    ] = None
    modified_issues: Annotated[
        list[int] | None,
        Field(alias="modifiedIssues", description="The IDs of the modified issues."),
    ] = None
    unmodified_issues: Annotated[
        list[int] | None,
        Field(
            alias="unmodifiedIssues",
            description="The IDs of the unchanged issues, those issues where errors prevent modification.",
        ),
    ] = None


class TaskProgressBeanRemoveOptionFromIssuesResult(BaseModel):
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
    result: Annotated[
        RemoveOptionFromIssuesResult | None, Field(description="The result of the task execution.")
    ] = None
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


class Context(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    id: Annotated[int | None, Field(description="The ID of the context.")] = None
    name: Annotated[str | None, Field(description="The name of the context.")] = None
    scope: Annotated[Scope | None, Field(description="The scope of the context.")] = None


class CustomFieldContextDefaultValueUpdate(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    default_values: Annotated[
        list[
            CustomFieldContextDefaultValueCascadingOption
            | CustomFieldContextDefaultValueMultipleOption
            | CustomFieldContextDefaultValueSingleOption
            | CustomFieldContextSingleUserPickerDefaults
            | CustomFieldContextDefaultValueMultiUserPicker
            | CustomFieldContextDefaultValueSingleGroupPicker
            | CustomFieldContextDefaultValueMultipleGroupPicker
            | CustomFieldContextDefaultValueDate
            | CustomFieldContextDefaultValueDateTime
            | CustomFieldContextDefaultValueURL
            | CustomFieldContextDefaultValueProject
            | CustomFieldContextDefaultValueFloat
            | CustomFieldContextDefaultValueLabels
            | CustomFieldContextDefaultValueTextField
            | CustomFieldContextDefaultValueTextArea
            | CustomFieldContextDefaultValueReadOnly
            | CustomFieldContextDefaultValueSingleVersionPicker
            | CustomFieldContextDefaultValueMultipleVersionPicker
            | CustomFieldContextDefaultValueForgeStringField
            | CustomFieldContextDefaultValueForgeMultiStringField
            | CustomFieldContextDefaultValueForgeObjectField
            | CustomFieldContextDefaultValueForgeDateTimeField
            | CustomFieldContextDefaultValueForgeGroupField
            | CustomFieldContextDefaultValueForgeMultiGroupField
            | CustomFieldContextDefaultValueForgeNumberField
            | CustomFieldContextDefaultValueForgeUserField
            | CustomFieldContextDefaultValueForgeMultiUserField
        ]
        | None,
        Field(alias="defaultValues"),
    ] = None


class FieldAssociationsRequest(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    association_contexts: Annotated[
        list[ProjectIdAssociationContext],
        Field(
            alias="associationContexts",
            description="Contexts to associate/unassociate the fields with.",
        ),
    ]
    fields: Annotated[
        list[FieldIdIdentifier], Field(description="Fields to associate/unassociate with projects.")
    ]


class IssueFieldOptionConfiguration(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    attributes: Annotated[list[Attribute] | None, Field(description="DEPRECATED")] = None
    scope: Annotated[
        IssueFieldOptionScope | None,
        Field(
            description="Defines the projects that the option is available in. If the scope is not defined, then the option is available in all projects."
        ),
    ] = None


class PageBeanContext(BaseModel):
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
    values: Annotated[list[Context] | None, Field(description="The list of items.")] = None


class PageBeanCustomFieldContextDefaultValue(BaseModel):
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
        list[
            CustomFieldContextDefaultValueCascadingOption
            | CustomFieldContextDefaultValueMultipleOption
            | CustomFieldContextDefaultValueSingleOption
            | CustomFieldContextSingleUserPickerDefaults
            | CustomFieldContextDefaultValueMultiUserPicker
            | CustomFieldContextDefaultValueSingleGroupPicker
            | CustomFieldContextDefaultValueMultipleGroupPicker
            | CustomFieldContextDefaultValueDate
            | CustomFieldContextDefaultValueDateTime
            | CustomFieldContextDefaultValueURL
            | CustomFieldContextDefaultValueProject
            | CustomFieldContextDefaultValueFloat
            | CustomFieldContextDefaultValueLabels
            | CustomFieldContextDefaultValueTextField
            | CustomFieldContextDefaultValueTextArea
            | CustomFieldContextDefaultValueReadOnly
            | CustomFieldContextDefaultValueSingleVersionPicker
            | CustomFieldContextDefaultValueMultipleVersionPicker
            | CustomFieldContextDefaultValueForgeStringField
            | CustomFieldContextDefaultValueForgeMultiStringField
            | CustomFieldContextDefaultValueForgeObjectField
            | CustomFieldContextDefaultValueForgeDateTimeField
            | CustomFieldContextDefaultValueForgeGroupField
            | CustomFieldContextDefaultValueForgeMultiGroupField
            | CustomFieldContextDefaultValueForgeNumberField
            | CustomFieldContextDefaultValueForgeUserField
            | CustomFieldContextDefaultValueForgeMultiUserField
        ]
        | None,
        Field(description="The list of items."),
    ] = None


class IssueFieldOption(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    config: IssueFieldOptionConfiguration | None = None
    id: Annotated[
        int,
        Field(
            description="The unique identifier for the option. This is only unique within the select field's set of options."
        ),
    ]
    properties: Annotated[
        dict[str, Any] | None,
        Field(
            description="The properties of the object, as arbitrary key-value pairs. These properties can be searched using JQL, if the extractions (see [Issue Field Option Property Index](https://developer.atlassian.com/cloud/jira/platform/modules/issue-field-option-property-index/)) are defined in the descriptor for the issue field module."
        ),
    ] = None
    value: Annotated[str, Field(description="The option's name, which is displayed in Jira.")]


class PageBeanIssueFieldOption(BaseModel):
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
    values: Annotated[list[IssueFieldOption] | None, Field(description="The list of items.")] = None


__all__ = [
    "AssociationContextObject",
    "BulkContextualConfiguration",
    "ConfigurationsListParameters",
    "ContextForProjectAndIssueType",
    "ContextualConfiguration",
    "CreateCustomFieldContext",
    "CreateFieldAssociationSchemeRequest",
    "CreateFieldAssociationSchemeResponse",
    "CustomFieldConfigurations",
    "CustomFieldContext",
    "CustomFieldContextDefaultValueCascadingOption",
    "CustomFieldContextDefaultValueDate",
    "CustomFieldContextDefaultValueDateTime",
    "CustomFieldContextDefaultValueFloat",
    "CustomFieldContextDefaultValueForgeDateTimeField",
    "CustomFieldContextDefaultValueForgeGroupField",
    "CustomFieldContextDefaultValueForgeMultiGroupField",
    "CustomFieldContextDefaultValueForgeMultiStringField",
    "CustomFieldContextDefaultValueForgeMultiUserField",
    "CustomFieldContextDefaultValueForgeNumberField",
    "CustomFieldContextDefaultValueForgeObjectField",
    "CustomFieldContextDefaultValueForgeStringField",
    "CustomFieldContextDefaultValueLabels",
    "CustomFieldContextDefaultValueMultiUserPicker",
    "CustomFieldContextDefaultValueMultipleGroupPicker",
    "CustomFieldContextDefaultValueMultipleOption",
    "CustomFieldContextDefaultValueMultipleVersionPicker",
    "CustomFieldContextDefaultValueProject",
    "CustomFieldContextDefaultValueReadOnly",
    "CustomFieldContextDefaultValueSingleGroupPicker",
    "CustomFieldContextDefaultValueSingleOption",
    "CustomFieldContextDefaultValueSingleVersionPicker",
    "CustomFieldContextDefaultValueTextArea",
    "CustomFieldContextDefaultValueTextField",
    "CustomFieldContextDefaultValueURL",
    "CustomFieldContextOption",
    "CustomFieldContextProjectMapping",
    "CustomFieldContextUpdateDetails",
    "CustomFieldCreatedContextOptionsList",
    "CustomFieldOption",
    "CustomFieldOptionCreate",
    "CustomFieldOptionUpdate",
    "CustomFieldUpdatedContextOptionsList",
    "CustomFieldValueUpdate",
    "CustomFieldValueUpdateDetails",
    "DeleteFieldAssociationSchemeResponse",
    "FieldAssociationParameters",
    "FieldAssociationSchemeLinks",
    "FieldAssociationSchemeMatchedFilters",
    "FieldAssociationSchemeProjectSearchResult",
    "FieldIdentifierObject",
    "FieldLastUsed",
    "FieldSchemeToFieldsPartialFailure",
    "FieldSchemeToFieldsResponse",
    "FieldSchemeToProjectsPartialFailure",
    "FieldSchemeToProjectsRequest",
    "FieldSchemeToProjectsResponse",
    "FieldsSchemeItemParameter",
    "FieldsSchemeItemWorkTypeParameter",
    "GetFieldAssociationSchemeByIdResponse",
    "GetFieldAssociationSchemeResponse",
    "GetProjectsWithFieldSchemesResponse",
    "IssueTypeToContextMapping",
    "MinimalFieldSchemeToFieldsPartialFailure",
    "MinimalFieldSchemeToFieldsResponse",
    "MultipleCustomFieldValuesUpdate",
    "MultipleCustomFieldValuesUpdateDetails",
    "OrderOfCustomFieldOptions",
    "PageBean2FieldAssociationSchemeProjectSearchResult",
    "PageBean2GetFieldAssociationSchemeResponse",
    "PageBean2GetProjectsWithFieldSchemesResponse",
    "PageBeanBulkContextualConfiguration",
    "PageBeanContextForProjectAndIssueType",
    "PageBeanContextualConfiguration",
    "PageBeanCustomFieldContext",
    "PageBeanCustomFieldContextOption",
    "PageBeanCustomFieldContextProjectMapping",
    "PageBeanIssueTypeToContextMapping",
    "ParameterRemovalDetails",
    "ProjectIdAssociationContext",
    "ProjectIds",
    "ProjectIssueTypeMapping",
    "ProjectIssueTypeMappings",
    "RemoveFieldAssociationsRequestItem",
    "RemoveFieldParametersResultError",
    "SearchResultFieldParameters",
    "SearchResultWorkTypeParameters",
    "SimpleErrorCollection",
    "SuccessOrErrorResults",
    "UpdateCustomFieldDetails",
    "UpdateFieldAssociationSchemeRequest",
    "UpdateFieldAssociationSchemeResponse",
    "UpdateFieldAssociationsRequestItem",
    "UpdateFieldSchemeParametersPartialFailure",
    "UpdateFieldSchemeParametersRequest",
    "UpdateFieldSchemeParametersResponse",
    "UserFilter",
    "WorkTypeParameters",
    "BulkCustomFieldOptionCreateRequest",
    "BulkCustomFieldOptionUpdateRequest",
    "CustomFieldContextDefaultValueForgeUserField",
    "CustomFieldContextSingleUserPickerDefaults",
    "FieldAssociationSchemeFieldSearchResult",
    "FieldIdIdentifier",
    "GetFieldAssociationParametersResponse",
    "PageBean2FieldAssociationSchemeFieldSearchResult",
    "PageBeanField",
    "RemoveFieldParametersResult",
    "RemoveOptionFromIssuesResult",
    "TaskProgressBeanRemoveOptionFromIssuesResult",
    "Context",
    "CustomFieldContextDefaultValueUpdate",
    "FieldAssociationsRequest",
    "IssueFieldOptionConfiguration",
    "PageBeanContext",
    "PageBeanCustomFieldContextDefaultValue",
    "IssueFieldOption",
    "PageBeanIssueFieldOption",
]
