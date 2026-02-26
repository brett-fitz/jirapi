"""Pydantic models for the jira expressions domain."""

from __future__ import annotations

from typing import Annotated, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

from jirapi.models._shared import Validation


class IssueContextVariable(BaseModel):
    id: Annotated[int | None, Field(description="The issue ID.")] = None
    key: Annotated[str | None, Field(description="The issue key.")] = None
    type: Annotated[str, Field(description="Type of custom context variable.")]


class JexpEvaluateCtxJqlIssues(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    max_results: Annotated[
        int | None,
        Field(
            alias="maxResults",
            description="The maximum number of issues to return from the JQL query. max results value considered may be lower than the number specific here.",
        ),
    ] = None
    next_page_token: Annotated[
        str | None,
        Field(
            alias="nextPageToken",
            description="The token for a page to fetch that is not the first page. The first page has a `nextPageToken` of `null`. Use the `nextPageToken` to fetch the next page of issues.",
        ),
    ] = None
    query: Annotated[
        str | None,
        Field(
            description="The JQL query, required to be bounded. Additionally, `orderBy` clause can contain a maximum of 7 fields"
        ),
    ] = None


class JexpJqlIssues(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    max_results: Annotated[
        int | None,
        Field(
            alias="maxResults",
            description="The maximum number of issues to return from the JQL query. Inspect `meta.issues.jql.maxResults` in the response to ensure the maximum value has not been exceeded.",
        ),
    ] = None
    query: Annotated[str | None, Field(description="The JQL query.")] = None
    start_at: Annotated[
        int | None,
        Field(
            alias="startAt",
            description="The index of the first issue to return from the JQL query.",
        ),
    ] = None
    validation: Annotated[
        Validation,
        Field(
            description="Determines how to validate the JQL query and treat the validation results."
        ),
    ] = Validation.strict


class JiraExpressionComplexity(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    expensive_operations: Annotated[
        str,
        Field(
            alias="expensiveOperations",
            description="Information that can be used to determine how many [expensive operations](https://developer.atlassian.com/cloud/jira/platform/jira-expressions/#expensive-operations) the evaluation of the expression will perform. This information may be a formula or number. For example:\n\n *  `issues.map(i => i.comments)` performs as many expensive operations as there are issues on the issues list. So this parameter returns `N`, where `N` is the size of issue list.\n *  `new Issue(10010).comments` gets comments for one issue, so its complexity is `2` (`1` to retrieve issue 10010 from the database plus `1` to get its comments).",
        ),
    ]
    variables: Annotated[
        dict[str, str] | None,
        Field(
            description="Variables used in the formula, mapped to the parts of the expression they refer to."
        ),
    ] = None


class JiraExpressionForAnalysis(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    context_variables: Annotated[
        dict[str, str] | None,
        Field(
            alias="contextVariables",
            description="Context variables and their types. The type checker assumes that [common context variables](https://developer.atlassian.com/cloud/jira/platform/jira-expressions/#context-variables), such as `issue` or `project`, are available in context and sets their type. Use this property to override the default types or provide details of new variables.",
        ),
    ] = None
    expressions: Annotated[
        list[str],
        Field(
            description="The list of Jira expressions to analyse.",
            examples=["issues.map(issue => issue.properties['property_key'])"],
        ),
    ]


class JiraExpressionValidationError(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    column: Annotated[
        int | None, Field(description="The text column in which the error occurred.")
    ] = None
    expression: Annotated[
        str | None, Field(description="The part of the expression in which the error occurred.")
    ] = None
    line: Annotated[int | None, Field(description="The text line in which the error occurred.")] = (
        None
    )
    message: Annotated[
        str,
        Field(
            description="Details about the error.",
            examples=[
                "!, -, typeof, (, IDENTIFIER, null, true, false, NUMBER, STRING, TEMPLATE_LITERAL, new, [ or { expected, > encountered."
            ],
        ),
    ]
    type: Annotated[Type13, Field(description="The error type.")]


class JsonContextVariable(BaseModel):
    type: Annotated[str, Field(description="Type of custom context variable.")]
    value: Annotated[
        dict[str, Any] | None, Field(description="A JSON object containing custom content.")
    ] = None


class UserContextVariable(BaseModel):
    account_id: Annotated[str, Field(alias="accountId", description="The account ID of the user.")]
    type: Annotated[str, Field(description="Type of custom context variable.")]


class CustomContextVariable1(UserContextVariable):
    model_config = ConfigDict(
        extra="forbid",
    )
    type: Annotated[Literal["user"], Field(description="Type of custom context variable.")]


class CustomContextVariable2(IssueContextVariable):
    model_config = ConfigDict(
        extra="forbid",
    )
    type: Annotated[Literal["issue"], Field(description="Type of custom context variable.")]


class CustomContextVariable3(JsonContextVariable):
    model_config = ConfigDict(
        extra="forbid",
    )
    type: Annotated[Literal["json"], Field(description="Type of custom context variable.")]


class JexpEvaluateCtxIssues(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    jql: Annotated[
        JexpEvaluateCtxJqlIssues | None,
        Field(
            description="The JQL query that specifies the set of issues available in the Jira expression."
        ),
    ] = None


class JexpIssues(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    jql: Annotated[
        JexpJqlIssues | None,
        Field(
            description="The JQL query that specifies the set of issues available in the Jira expression."
        ),
    ] = None


class JiraExpressionAnalysis(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    complexity: JiraExpressionComplexity | None = None
    errors: Annotated[
        list[JiraExpressionValidationError] | None,
        Field(description="A list of validation errors. Not included if the expression is valid."),
    ] = None
    expression: Annotated[str, Field(description="The analysed expression.")]
    type: Annotated[
        str | None, Field(description="EXPERIMENTAL. The inferred type of the expression.")
    ] = None
    valid: Annotated[
        bool,
        Field(
            description="Whether the expression is valid and the interpreter will evaluate it. Note that the expression may fail at runtime (for example, if it executes too many expensive operations)."
        ),
    ]


class JiraExpressionsAnalysis(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    results: Annotated[
        list[JiraExpressionAnalysis], Field(description="The results of Jira expressions analysis.")
    ]


class JiraExpressionResult(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    meta: Annotated[
        JiraExpressionEvaluationMetaData | None,
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


__all__ = [
    "IssueContextVariable",
    "JexpEvaluateCtxJqlIssues",
    "JexpJqlIssues",
    "JiraExpressionComplexity",
    "JiraExpressionForAnalysis",
    "JiraExpressionValidationError",
    "JsonContextVariable",
    "UserContextVariable",
    "CustomContextVariable1",
    "CustomContextVariable2",
    "CustomContextVariable3",
    "JexpEvaluateCtxIssues",
    "JexpIssues",
    "JiraExpressionAnalysis",
    "JiraExpressionsAnalysis",
    "JiraExpressionResult",
]
