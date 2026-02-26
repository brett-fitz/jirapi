"""Pydantic models for the webhooks domain."""

from __future__ import annotations

from typing import Annotated

from pydantic import AnyUrl, BaseModel, ConfigDict, Field


class ContainerForWebhookIDs(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    webhook_ids: Annotated[
        list[int], Field(alias="webhookIds", description="A list of webhook IDs.")
    ]


class FailedWebhook(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    body: Annotated[str | None, Field(description="The webhook body.")] = None
    failure_time: Annotated[
        int,
        Field(
            alias="failureTime",
            description="The time the webhook was added to the list of failed webhooks (that is, the time of the last failed retry).",
        ),
    ]
    id: Annotated[
        str,
        Field(
            description="The webhook ID, as sent in the `X-Atlassian-Webhook-Identifier` header with the webhook."
        ),
    ]
    url: Annotated[str, Field(description="The original webhook destination.")]


class FailedWebhooks(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    max_results: Annotated[
        int,
        Field(
            alias="maxResults",
            description="The maximum number of items on the page. If the list of values is shorter than this number, then there are no more pages.",
        ),
    ]
    next: Annotated[
        AnyUrl | None,
        Field(
            description="The URL to the next page of results. Present only if the request returned at least one result.The next page may be empty at the time of receiving the response, but new failed webhooks may appear in time. You can save the URL to the next page and query for new results periodically (for example, every hour)."
        ),
    ] = None
    values: Annotated[list[FailedWebhook], Field(description="The list of webhooks.")]


class RegisteredWebhook(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    created_webhook_id: Annotated[
        int | None,
        Field(
            alias="createdWebhookId",
            description="The ID of the webhook. Returned if the webhook is created.",
        ),
    ] = None
    errors: Annotated[
        list[str] | None,
        Field(description="Error messages specifying why the webhook creation failed."),
    ] = None


class Webhook(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    events: Annotated[list[Event], Field(description="The Jira events that trigger the webhook.")]
    expiration_date: Annotated[
        int | None,
        Field(
            alias="expirationDate",
            description="The date after which the webhook is no longer sent. Use [Extend webhook life](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-webhooks/#api-rest-api-3-webhook-refresh-put) to extend the date.",
        ),
    ] = None
    field_ids_filter: Annotated[
        list[str] | None,
        Field(
            alias="fieldIdsFilter",
            description="A list of field IDs. When the issue changelog contains any of the fields, the webhook `jira:issue_updated` is sent. If this parameter is not present, the app is notified about all field updates.",
        ),
    ] = None
    id: Annotated[int, Field(description="The ID of the webhook.")]
    issue_property_keys_filter: Annotated[
        list[str] | None,
        Field(
            alias="issuePropertyKeysFilter",
            description="A list of issue property keys. A change of those issue properties triggers the `issue_property_set` or `issue_property_deleted` webhooks. If this parameter is not present, the app is notified about all issue property updates.",
        ),
    ] = None
    jql_filter: Annotated[
        str,
        Field(
            alias="jqlFilter",
            description="The JQL filter that specifies which issues the webhook is sent for.",
        ),
    ]
    url: Annotated[str, Field(description="The URL that specifies where the webhooks are sent.")]


class WebhookDetails(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    events: Annotated[list[Event], Field(description="The Jira events that trigger the webhook.")]
    field_ids_filter: Annotated[
        list[str] | None,
        Field(
            alias="fieldIdsFilter",
            description="A list of field IDs. When the issue changelog contains any of the fields, the webhook `jira:issue_updated` is sent. If this parameter is not present, the app is notified about all field updates.",
        ),
    ] = None
    issue_property_keys_filter: Annotated[
        list[str] | None,
        Field(
            alias="issuePropertyKeysFilter",
            description="A list of issue property keys. A change of those issue properties triggers the `issue_property_set` or `issue_property_deleted` webhooks. If this parameter is not present, the app is notified about all issue property updates.",
        ),
    ] = None
    jql_filter: Annotated[
        str,
        Field(
            alias="jqlFilter",
            description='The JQL filter that specifies which issues the webhook is sent for. Only a subset of JQL can be used. The supported elements are:\n\n *  Fields: `issueKey`, `project`, `issuetype`, `status`, `assignee`, `reporter`, `issue.property`, and `cf[id]`. For custom fields (`cf[id]`), only the epic label custom field is supported.".\n *  Operators: `=`, `!=`, `IN`, and `NOT IN`.',
        ),
    ]


class WebhookRegistrationDetails(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    url: Annotated[
        str,
        Field(
            description="The URL that specifies where to send the webhooks. This URL must use the same base URL as the Connect app. Only a single URL per app is allowed to be registered."
        ),
    ]
    webhooks: Annotated[list[WebhookDetails], Field(description="A list of webhooks.")]


class WebhooksExpirationDate(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    expiration_date: Annotated[
        int,
        Field(
            alias="expirationDate",
            description="The expiration date of all the refreshed webhooks.",
        ),
    ]


class ContainerForRegisteredWebhooks(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    webhook_registration_result: Annotated[
        list[RegisteredWebhook] | None,
        Field(
            alias="webhookRegistrationResult",
            description="A list of registered webhooks.",
        ),
    ] = None


class PageBeanWebhook(BaseModel):
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
    values: Annotated[list[Webhook] | None, Field(description="The list of items.")] = None


__all__ = [
    "ContainerForWebhookIDs",
    "FailedWebhook",
    "FailedWebhooks",
    "RegisteredWebhook",
    "Webhook",
    "WebhookDetails",
    "WebhookRegistrationDetails",
    "WebhooksExpirationDate",
    "ContainerForRegisteredWebhooks",
    "PageBeanWebhook",
]
