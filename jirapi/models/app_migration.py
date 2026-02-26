"""Pydantic models for the app migration domain."""

from __future__ import annotations

from typing import Annotated
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class ConnectCustomFieldValue(BaseModel):
    field_type: Annotated[FieldType, Field(alias="_type", description="The type of custom field.")]
    field_id: Annotated[int, Field(alias="fieldID", description="The custom field ID.")]
    issue_id: Annotated[int, Field(alias="issueID", description="The issue ID.")]
    number: Annotated[
        float | None,
        Field(
            description="The value of number type custom field when `_type` is `NumberIssueField`."
        ),
    ] = None
    option_id: Annotated[
        str | None,
        Field(
            alias="optionID",
            description="The value of single select and multiselect custom field type when `_type` is `SingleSelectIssueField` or `MultiSelectIssueField`.",
        ),
    ] = None
    rich_text: Annotated[
        str | None,
        Field(
            alias="richText",
            description="The value of richText type custom field when `_type` is `RichTextIssueField`.",
        ),
    ] = None
    string: Annotated[
        str | None,
        Field(
            description="The value of string type custom field when `_type` is `StringIssueField`."
        ),
    ] = None
    text: Annotated[
        str | None,
        Field(
            description="The value of of text custom field type when `_type` is `TextIssueField`."
        ),
    ] = None


class ConnectCustomFieldValues(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    update_value_list: Annotated[
        list[ConnectCustomFieldValue] | None,
        Field(
            alias="updateValueList",
            description="The list of custom field update details.",
        ),
    ] = None


class EntityPropertyDetails(BaseModel):
    entity_id: Annotated[
        float, Field(alias="entityId", description="The entity property ID.", examples=[123])
    ]
    key: Annotated[str, Field(description="The entity property key.", examples=["mykey"])]
    value: Annotated[
        str, Field(description="The new value of the entity property.", examples=["newValue"])
    ]


class WorkflowRulesSearch(BaseModel):
    expand: Annotated[
        str | None,
        Field(
            description="Use expand to include additional information in the response. This parameter accepts `transition` which, for each rule, returns information about the transition the rule is assigned to.",
            examples=["transition"],
        ),
    ] = None
    rule_ids: Annotated[
        list[UUID],
        Field(
            alias="ruleIds",
            description="The list of workflow rule IDs.",
            max_length=10,
            min_length=1,
        ),
    ]
    workflow_entity_id: Annotated[
        UUID,
        Field(
            alias="workflowEntityId",
            description="The workflow ID.",
            examples=["a498d711-685d-428d-8c3e-bc03bb450ea7"],
        ),
    ]


class WorkflowRulesSearchDetails(BaseModel):
    invalid_rules: Annotated[
        list[UUID] | None,
        Field(
            alias="invalidRules",
            description="List of workflow rule IDs that do not belong to the workflow or can not be found.",
        ),
    ] = None
    valid_rules: Annotated[
        list[WorkflowTransitionRules] | None,
        Field(alias="validRules", description="List of valid workflow transition rules."),
    ] = None
    workflow_entity_id: Annotated[
        UUID | None,
        Field(
            alias="workflowEntityId",
            description="The workflow ID.",
            examples=["a498d711-685d-428d-8c3e-bc03bb450ea7"],
        ),
    ] = None


__all__ = [
    "ConnectCustomFieldValue",
    "ConnectCustomFieldValues",
    "EntityPropertyDetails",
    "WorkflowRulesSearch",
    "WorkflowRulesSearchDetails",
]
