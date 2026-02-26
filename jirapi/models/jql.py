"""Pydantic models for the jql domain."""

from __future__ import annotations

from typing import Annotated, Literal

from pydantic import BaseModel, ConfigDict, Field


class AutoCompleteSuggestion(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    display_name: Annotated[
        str | None,
        Field(
            alias="displayName",
            description="The display name of a suggested item. If `fieldValue` or `predicateValue` are provided, the matching text is highlighted with the HTML bold tag.",
        ),
    ] = None
    value: Annotated[str | None, Field(description="The value of a suggested item.")] = None


class AutoCompleteSuggestions(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    results: Annotated[
        list[AutoCompleteSuggestion] | None, Field(description="The list of suggested item.")
    ] = None


class FieldReferenceData(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    auto: Annotated[
        Auto | None, Field(description="Whether the field provide auto-complete suggestions.")
    ] = None
    cfid: Annotated[
        str | None, Field(description="If the item is a custom field, the ID of the custom field.")
    ] = None
    deprecated: Annotated[
        Deprecated | None, Field(description="Whether this field has been deprecated.")
    ] = None
    deprecated_searcher_key: Annotated[
        str | None,
        Field(
            alias="deprecatedSearcherKey",
            description="The searcher key of the field, only passed when the field is deprecated.",
        ),
    ] = None
    display_name: Annotated[
        str | None,
        Field(
            alias="displayName",
            description="The display name contains the following:\n\n *  for system fields, the field name. For example, `Summary`.\n *  for collapsed custom fields, the field name followed by a hyphen and then the field name and field type. For example, `Component - Component[Dropdown]`.\n *  for other custom fields, the field name followed by a hyphen and then the custom field ID. For example, `Component - cf[10061]`.",
        ),
    ] = None
    operators: Annotated[
        list[str] | None, Field(description="The valid search operators for the field.")
    ] = None
    orderable: Annotated[
        Orderable | None,
        Field(description="Whether the field can be used in a query's `ORDER BY` clause."),
    ] = None
    searchable: Annotated[
        Searchable | None, Field(description="Whether the content of this field can be searched.")
    ] = None
    types: Annotated[
        list[str] | None, Field(description="The data types of items in the field.")
    ] = None
    value: Annotated[str | None, Field(description="The field identifier.")] = None


class FunctionOperand(BaseModel):
    arguments: Annotated[list[str], Field(description="The list of function arguments.")]
    encoded_operand: Annotated[
        str | None,
        Field(
            alias="encodedOperand",
            description="Encoded operand, which can be used directly in a JQL query.",
        ),
    ] = None
    function: Annotated[str, Field(description="The name of the function.")]


class FunctionReferenceData(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    display_name: Annotated[
        str | None, Field(alias="displayName", description="The display name of the function.")
    ] = None
    is_list: Annotated[
        IsList | None,
        Field(
            alias="isList",
            description="Whether the function can take a list of arguments.",
        ),
    ] = None
    supports_list_and_single_value_operators: Annotated[
        SupportsListAndSingleValueOperators | None,
        Field(
            alias="supportsListAndSingleValueOperators",
            description="Whether the function supports both single and list value operators.",
        ),
    ] = None
    types: Annotated[
        list[str] | None, Field(description="The data types returned by the function.")
    ] = None
    value: Annotated[str | None, Field(description="The function identifier.")] = None


class JQLPersonalDataMigrationRequest(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    query_strings: Annotated[
        list[str] | None,
        Field(
            alias="queryStrings",
            description="A list of queries with user identifiers. Maximum of 100 queries.",
        ),
    ] = None


class JQLQueryWithUnknownUsers(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    converted_query: Annotated[
        str | None,
        Field(
            alias="convertedQuery",
            description="The converted query, with accountIDs instead of user identifiers, or 'unknown' for users that could not be found",
        ),
    ] = None
    original_query: Annotated[
        str | None, Field(alias="originalQuery", description="The original query, for reference")
    ] = None


class JQLReferenceData(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    jql_reserved_words: Annotated[
        list[str] | None,
        Field(alias="jqlReservedWords", description="List of JQL query reserved words."),
    ] = None
    visible_field_names: Annotated[
        list[FieldReferenceData] | None,
        Field(
            alias="visibleFieldNames",
            description="List of fields usable in JQL queries.",
        ),
    ] = None
    visible_function_names: Annotated[
        list[FunctionReferenceData] | None,
        Field(
            alias="visibleFunctionNames",
            description="List of functions usable in JQL queries.",
        ),
    ] = None


class JqlFunctionPrecomputationGetByIdRequest(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    precomputation_i_ds: Annotated[list[str] | None, Field(alias="precomputationIDs")] = None


class JqlFunctionPrecomputationGetByIdResponse(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    not_found_precomputation_i_ds: Annotated[
        list[str] | None,
        Field(
            alias="notFoundPrecomputationIDs",
            description="List of precomputations that were not found.",
        ),
    ] = None
    precomputations: Annotated[
        list[JqlFunctionPrecomputation] | None, Field(description="The list of precomputations.")
    ] = None


class JqlFunctionPrecomputationUpdateErrorResponse(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    error_messages: Annotated[
        list[str] | None,
        Field(
            alias="errorMessages",
            description="The list of error messages produced by this operation.",
        ),
    ] = None
    not_found_precomputation_i_ds: Annotated[
        list[str] | None,
        Field(
            alias="notFoundPrecomputationIDs",
            description="List of precomputations that were not found.",
        ),
    ] = None


class JqlFunctionPrecomputationUpdateResponse(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    not_found_precomputation_i_ds: Annotated[
        list[str] | None,
        Field(
            alias="notFoundPrecomputationIDs",
            description="List of precomputations that were not found and skipped. Only returned if the request passed skipNotFoundPrecomputations=true.",
        ),
    ] = None


class JqlQueriesToParse(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    queries: Annotated[list[Query], Field(description="A list of queries to parse.", min_length=1)]


class JqlQueryFieldEntityProperty(BaseModel):
    entity: Annotated[
        str, Field(description="The object on which the property is set.", examples=["issue"])
    ]
    key: Annotated[str, Field(description="The key of the property.", examples=["stats"])]
    path: Annotated[
        str,
        Field(
            description="The path in the property value to query.",
            examples=["comments.count"],
        ),
    ]
    type: Annotated[
        Type14 | None,
        Field(
            description="The type of the property value extraction. Not available if the extraction for the property is not registered on the instance with the [Entity property](https://developer.atlassian.com/cloud/jira/platform/modules/entity-property/) module.",
            examples=["number"],
        ),
    ] = None


class JqlQueryToSanitize(BaseModel):
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
    query: Annotated[str, Field(description="The query to sanitize.")]


class KeywordOperand(BaseModel):
    keyword: Annotated[
        Literal["empty"], Field(description="The keyword that is the operand value.")
    ]


class SanitizedJqlQuery(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    account_id: Annotated[
        str | None,
        Field(
            alias="accountId",
            description="The account ID of the user for whom sanitization was performed.",
            max_length=128,
        ),
    ] = None
    errors: Annotated[ErrorCollection | None, Field(description="The list of errors.")] = None
    initial_query: Annotated[
        str | None, Field(alias="initialQuery", description="The initial query.")
    ] = None
    sanitized_query: Annotated[
        str | None,
        Field(
            alias="sanitizedQuery",
            description="The sanitized query, if there were no errors.",
        ),
    ] = None


class SearchAutoCompleteFilter(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    include_collapsed_fields: Annotated[
        bool,
        Field(
            alias="includeCollapsedFields",
            description="Include collapsed fields for fields that have non-unique names.",
        ),
    ] = False
    project_ids: Annotated[
        list[int] | None,
        Field(
            alias="projectIds",
            description="List of project IDs used to filter the visible field details returned.",
        ),
    ] = None


class ValueOperand(BaseModel):
    encoded_value: Annotated[
        str | None,
        Field(
            alias="encodedValue",
            description="Encoded value, which can be used directly in a JQL query.",
        ),
    ] = None
    value: Annotated[str, Field(description="The operand value.")]


class ConvertedJQLQueries(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    queries_with_unknown_users: Annotated[
        list[JQLQueryWithUnknownUsers] | None,
        Field(
            alias="queriesWithUnknownUsers",
            description="List of queries containing user information that could not be mapped to an existing user",
        ),
    ] = None
    query_strings: Annotated[
        list[str] | None,
        Field(
            alias="queryStrings",
            description="The list of converted query strings with account IDs in place of user identifiers.",
        ),
    ] = None


class JqlQueriesToSanitize(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    queries: Annotated[
        list[JqlQueryToSanitize],
        Field(
            description="The list of JQL queries to sanitize. Must contain unique values. Maximum of 20 queries."
        ),
    ]


class JqlQueryField(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    encoded_name: Annotated[
        str | None,
        Field(
            alias="encodedName",
            description="The encoded name of the field, which can be used directly in a JQL query.",
        ),
    ] = None
    name: Annotated[str, Field(description="The name of the field.")]
    property: Annotated[
        list[JqlQueryFieldEntityProperty] | None,
        Field(
            description="When the field refers to a value in an entity property, details of the entity property value."
        ),
    ] = None


class JqlQueryOrderByClauseElement(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    direction: Annotated[
        Direction | None, Field(description="The direction in which to order the results.")
    ] = None
    field: JqlQueryField


class ListOperand(BaseModel):
    encoded_operand: Annotated[
        str | None,
        Field(
            alias="encodedOperand",
            description="Encoded operand, which can be used directly in a JQL query.",
        ),
    ] = None
    values: Annotated[
        list[ValueOperand | FunctionOperand | KeywordOperand],
        Field(description="The list of operand values.", min_length=1),
    ]


class SanitizedJqlQueries(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    queries: Annotated[
        list[SanitizedJqlQuery] | None, Field(description="The list of sanitized JQL queries.")
    ] = None


class JqlQueryClauseTimePredicate(BaseModel):
    operand: Annotated[
        ListOperand | ValueOperand | FunctionOperand | KeywordOperand,
        Field(description="Details of an operand in a JQL clause."),
    ]
    operator: Annotated[
        Operator4, Field(description="The operator between the field and the operand.")
    ]


class JqlQueryOrderByClause(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    fields: Annotated[
        list[JqlQueryOrderByClauseElement],
        Field(description="The list of order-by clause fields and their ordering directives."),
    ]


class FieldChangedClause(BaseModel):
    field: JqlQueryField
    operator: Annotated[Literal["changed"], Field(description="The operator applied to the field.")]
    predicates: Annotated[
        list[JqlQueryClauseTimePredicate], Field(description="The list of time predicates.")
    ]


class FieldValueClause(BaseModel):
    field: JqlQueryField
    operand: Annotated[
        ListOperand | ValueOperand | FunctionOperand | KeywordOperand,
        Field(description="Details of an operand in a JQL clause."),
    ]
    operator: Annotated[Operator2, Field(description="The operator between the field and operand.")]


class FieldWasClause(BaseModel):
    field: JqlQueryField
    operand: Annotated[
        ListOperand | ValueOperand | FunctionOperand | KeywordOperand,
        Field(description="Details of an operand in a JQL clause."),
    ]
    operator: Annotated[Operator3, Field(description="The operator between the field and operand.")]
    predicates: Annotated[
        list[JqlQueryClauseTimePredicate], Field(description="The list of time predicates.")
    ]


class CompoundClause(BaseModel):
    clauses: Annotated[
        list[CompoundClause | FieldValueClause | FieldWasClause | FieldChangedClause],
        Field(description="The list of nested clauses."),
    ]
    operator: Annotated[Operator, Field(description="The operator between the clauses.")]


class JqlQuery(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    order_by: Annotated[JqlQueryOrderByClause | None, Field(alias="orderBy")] = None
    where: Annotated[
        CompoundClause | FieldValueClause | FieldWasClause | FieldChangedClause | None,
        Field(description="A JQL query clause."),
    ] = None


class ParsedJqlQueries(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    queries: Annotated[
        list[ParsedJqlQuery], Field(description="A list of parsed JQL queries.", min_length=1)
    ]


class ParsedJqlQuery(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    errors: Annotated[
        list[str] | None, Field(description="The list of syntax or validation errors.")
    ] = None
    query: Annotated[str, Field(description="The JQL query that was parsed and validated.")]
    structure: Annotated[
        JqlQuery | None,
        Field(description="The syntax tree of the query. Empty if the query was invalid."),
    ] = None
    warnings: Annotated[list[str] | None, Field(description="The list of warning messages")] = None


__all__ = [
    "AutoCompleteSuggestion",
    "AutoCompleteSuggestions",
    "FieldReferenceData",
    "FunctionOperand",
    "FunctionReferenceData",
    "JQLPersonalDataMigrationRequest",
    "JQLQueryWithUnknownUsers",
    "JQLReferenceData",
    "JqlFunctionPrecomputationGetByIdRequest",
    "JqlFunctionPrecomputationGetByIdResponse",
    "JqlFunctionPrecomputationUpdateErrorResponse",
    "JqlFunctionPrecomputationUpdateResponse",
    "JqlQueriesToParse",
    "JqlQueryFieldEntityProperty",
    "JqlQueryToSanitize",
    "KeywordOperand",
    "SanitizedJqlQuery",
    "SearchAutoCompleteFilter",
    "ValueOperand",
    "ConvertedJQLQueries",
    "JqlQueriesToSanitize",
    "JqlQueryField",
    "JqlQueryOrderByClauseElement",
    "ListOperand",
    "SanitizedJqlQueries",
    "JqlQueryClauseTimePredicate",
    "JqlQueryOrderByClause",
    "FieldChangedClause",
    "FieldValueClause",
    "FieldWasClause",
    "CompoundClause",
    "JqlQuery",
    "ParsedJqlQueries",
    "ParsedJqlQuery",
]
