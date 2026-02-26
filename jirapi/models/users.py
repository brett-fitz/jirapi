"""Pydantic models for the users domain."""

from __future__ import annotations

from typing import Annotated

from pydantic import AnyUrl, BaseModel, ConfigDict, Field


class Locale(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    locale: Annotated[
        str | None,
        Field(
            description="The locale code. The Java the locale format is used: a two character language code (ISO 639), an underscore, and two letter country code (ISO 3166). For example, en\\_US represents a locale of English (United States). Required on create."
        ),
    ] = None


class NewUserDetails(BaseModel):
    model_config = ConfigDict(
        extra="allow",
    )
    application_keys: Annotated[
        list[str] | None, Field(alias="applicationKeys", description="Deprecated, do not use.")
    ] = None
    display_name: Annotated[
        str | None,
        Field(
            alias="displayName",
            description="This property is no longer available. If the user has an Atlassian account, their display name is not changed. If the user does not have an Atlassian account, they are sent an email asking them set up an account.",
        ),
    ] = None
    email_address: Annotated[
        str, Field(alias="emailAddress", description="The email address for the user.")
    ]
    key: Annotated[
        str | None,
        Field(
            description="This property is no longer available. See the [migration guide](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-user-privacy-api-migration-guide/) for details."
        ),
    ] = None
    name: Annotated[
        str | None,
        Field(
            description="This property is no longer available. See the [migration guide](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-user-privacy-api-migration-guide/) for details."
        ),
    ] = None
    password: Annotated[
        str | None,
        Field(
            description="This property is no longer available. If the user has an Atlassian account, their password is not changed. If the user does not have an Atlassian account, they are sent an email asking them set up an account."
        ),
    ] = None
    products: Annotated[
        list[str],
        Field(
            description="Products the new user has access to. Valid products are: jira-core, jira-servicedesk, jira-product-discovery, jira-software. To create a user without product access, set this field to be an empty array."
        ),
    ]
    self: Annotated[str | None, Field(description="The URL of the user.")] = None


class UnrestrictedUserEmail(BaseModel):
    model_config = ConfigDict(
        extra="allow",
    )
    account_id: Annotated[
        str | None, Field(alias="accountId", description="The accountId of the user")
    ] = None
    email: Annotated[str | None, Field(description="The email of the user")] = None


class UserColumnRequestBody(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    columns: list[str] | None = None


class UserKey(BaseModel):
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
    key: Annotated[
        str | None,
        Field(
            description="This property is no longer available and will be removed from the documentation soon. See the [deprecation notice](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-user-privacy-api-migration-guide/) for details."
        ),
    ] = None


class UserPickerUser(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    account_id: Annotated[
        str | None,
        Field(
            alias="accountId",
            description="The account ID of the user, which uniquely identifies the user across all Atlassian products. For example, *5b10ac8d82e05b22cc7d4ef5*.",
        ),
    ] = None
    account_type: Annotated[
        AccountType | None,
        Field(
            alias="accountType",
            description="The user account type. Can take the following values:\n\n *  `atlassian` regular Atlassian user account\n *  `app` system account used for Connect applications and OAuth to represent external systems\n *  `customer` Jira Service Desk account representing an external service desk",
        ),
    ] = None
    avatar_url: Annotated[
        AnyUrl | None, Field(alias="avatarUrl", description="The avatar URL of the user.")
    ] = None
    display_name: Annotated[
        str | None,
        Field(
            alias="displayName",
            description="The display name of the user. Depending on the user’s privacy setting, this may be returned as null.",
        ),
    ] = None
    html: Annotated[
        str | None,
        Field(
            description="The display name, email address, and key of the user with the matched query string highlighted with the HTML bold tag."
        ),
    ] = None
    key: Annotated[
        str | None,
        Field(
            description="This property is no longer available. See the [deprecation notice](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-user-privacy-api-migration-guide/) for details."
        ),
    ] = None
    name: Annotated[
        str | None,
        Field(
            description="This property is no longer available . See the [deprecation notice](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-user-privacy-api-migration-guide/) for details."
        ),
    ] = None


class FoundUsers(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    header: Annotated[
        str | None,
        Field(
            description="Header text indicating the number of users in the response and the total number of users found in the search."
        ),
    ] = None
    total: Annotated[
        int | None, Field(description="The total number of users found in the search.")
    ] = None
    users: list[UserPickerUser] | None = None


class FoundUsersAndGroups(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    groups: FoundGroups | None = None
    users: FoundUsers | None = None


class PageBeanUserKey(BaseModel):
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
    values: Annotated[list[UserKey] | None, Field(description="The list of items.")] = None


class PageBeanUser(BaseModel):
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
    values: Annotated[list[User] | None, Field(description="The list of items.")] = None


__all__ = [
    "Locale",
    "NewUserDetails",
    "UnrestrictedUserEmail",
    "UserColumnRequestBody",
    "UserKey",
    "UserPickerUser",
    "FoundUsers",
    "FoundUsersAndGroups",
    "PageBeanUserKey",
    "PageBeanUser",
]
