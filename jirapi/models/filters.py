"""Pydantic models for the filters domain."""

from __future__ import annotations

from typing import Annotated

from pydantic import AnyUrl, AwareDatetime, BaseModel, ConfigDict, Field


class ChangeFilterOwner(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    account_id: Annotated[
        str, Field(alias="accountId", description="The account ID of the new owner.")
    ]


class DefaultShareScope(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    scope: Annotated[
        Scope2,
        Field(
            description="The scope of the default sharing for new filters and dashboards:\n\n *  `AUTHENTICATED` Shared with all logged-in users.\n *  `GLOBAL` Shared with all logged-in users. This shows as `AUTHENTICATED` in the response.\n *  `PRIVATE` Not shared with any users."
        ),
    ]


class UserList(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    end_index: Annotated[
        int | None,
        Field(
            alias="end-index",
            description="The index of the last item returned on the page.",
        ),
    ] = None
    items: Annotated[list[User] | None, Field(description="The list of items.")] = None
    max_results: Annotated[
        int | None,
        Field(
            alias="max-results",
            description="The maximum number of results that could be on the page.",
        ),
    ] = None
    size: Annotated[int | None, Field(description="The number of items on the page.")] = None
    start_index: Annotated[
        int | None,
        Field(
            alias="start-index",
            description="The index of the first item returned on the page.",
        ),
    ] = None


class FilterSubscription(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    group: Annotated[GroupName | None, Field(description="The group subscribing to filter.")] = None
    id: Annotated[int | None, Field(description="The ID of the filter subscription.")] = None
    user: Annotated[User | None, Field(description="The user subscribing to filter.")] = None


class FilterSubscriptionsList(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    end_index: Annotated[
        int | None,
        Field(
            alias="end-index",
            description="The index of the last item returned on the page.",
        ),
    ] = None
    items: Annotated[list[FilterSubscription] | None, Field(description="The list of items.")] = (
        None
    )
    max_results: Annotated[
        int | None,
        Field(
            alias="max-results",
            description="The maximum number of results that could be on the page.",
        ),
    ] = None
    size: Annotated[int | None, Field(description="The number of items on the page.")] = None
    start_index: Annotated[
        int | None,
        Field(
            alias="start-index",
            description="The index of the first item returned on the page.",
        ),
    ] = None


class Filter(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    approximate_last_used: Annotated[
        AwareDatetime | None,
        Field(
            alias="approximateLastUsed",
            description="\\[Experimental\\] Approximate last used time. Returns the date and time when the filter was last used. Returns `null` if the filter hasn't been used after tracking was enabled. For performance reasons, timestamps aren't updated in real time and therefore may not be exactly accurate.",
        ),
    ] = None
    description: Annotated[str | None, Field(description="A description of the filter.")] = None
    edit_permissions: Annotated[
        list[SharePermission] | None,
        Field(
            alias="editPermissions",
            description="The groups and projects that can edit the filter.",
        ),
    ] = None
    favourite: Annotated[
        bool | None, Field(description="Whether the filter is selected as a favorite.")
    ] = None
    favourited_count: Annotated[
        int | None,
        Field(
            alias="favouritedCount",
            description="The count of how many users have selected this filter as a favorite, including the filter owner.",
        ),
    ] = None
    id: Annotated[str | None, Field(description="The unique identifier for the filter.")] = None
    jql: Annotated[
        str | None,
        Field(
            description="The JQL query for the filter. For example, *project = SSP AND issuetype = Bug*."
        ),
    ] = None
    name: Annotated[str, Field(description="The name of the filter. Must be unique.")]
    owner: Annotated[
        User | None,
        Field(
            description="The user who owns the filter. This is defaulted to the creator of the filter, however Jira administrators can change the owner of a shared filter in the admin settings."
        ),
    ] = None
    search_url: Annotated[
        AnyUrl | None,
        Field(
            alias="searchUrl",
            description="A URL to view the filter results in Jira, using the [Search for issues using JQL](#api-rest-api-3-filter-search-get) operation with the filter's JQL string to return the filter results. For example, *https://your-domain.atlassian.net/rest/api/3/search?jql=project+%3D+SSP+AND+issuetype+%3D+Bug*.",
        ),
    ] = None
    self: Annotated[AnyUrl | None, Field(description="The URL of the filter.")] = None
    share_permissions: Annotated[
        list[SharePermission] | None,
        Field(
            alias="sharePermissions",
            description="The groups and projects that the filter is shared with.",
        ),
    ] = None
    shared_users: Annotated[
        UserList | None,
        Field(
            alias="sharedUsers",
            description="A paginated list of the users that the filter is shared with. This includes users that are members of the groups or can browse the projects that the filter is shared with.",
        ),
    ] = None
    subscriptions: Annotated[
        FilterSubscriptionsList | None,
        Field(description="A paginated list of the users that are subscribed to the filter."),
    ] = None
    view_url: Annotated[
        AnyUrl | None,
        Field(
            alias="viewUrl",
            description="A URL to view the filter results in Jira, using the ID of the filter. For example, *https://your-domain.atlassian.net/issues/?filter=10100*.",
        ),
    ] = None


class FilterDetails(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    approximate_last_used: Annotated[
        AwareDatetime | None,
        Field(
            alias="approximateLastUsed",
            description="\\[Experimental\\] Approximate last used time. Returns the date and time when the filter was last used. Returns `null` if the filter hasn't been used after tracking was enabled. For performance reasons, timestamps aren't updated in real time and therefore may not be exactly accurate.",
        ),
    ] = None
    description: Annotated[str | None, Field(description="The description of the filter.")] = None
    edit_permissions: Annotated[
        list[SharePermission] | None,
        Field(
            alias="editPermissions",
            description="The groups and projects that can edit the filter. This can be specified when updating a filter, but not when creating a filter.",
        ),
    ] = None
    expand: Annotated[
        str | None,
        Field(description="Expand options that include additional filter details in the response."),
    ] = None
    favourite: Annotated[
        bool | None,
        Field(
            description="Whether the filter is selected as a favorite by any users, not including the filter owner."
        ),
    ] = None
    favourited_count: Annotated[
        int | None,
        Field(
            alias="favouritedCount",
            description="The count of how many users have selected this filter as a favorite, including the filter owner.",
        ),
    ] = None
    id: Annotated[str | None, Field(description="The unique identifier for the filter.")] = None
    jql: Annotated[
        str | None,
        Field(
            description="The JQL query for the filter. For example, *project = SSP AND issuetype = Bug*."
        ),
    ] = None
    name: Annotated[str, Field(description="The name of the filter.")]
    owner: Annotated[
        User | None,
        Field(
            description="The user who owns the filter. Defaults to the creator of the filter, however, Jira administrators can change the owner of a shared filter in the admin settings."
        ),
    ] = None
    search_url: Annotated[
        AnyUrl | None,
        Field(
            alias="searchUrl",
            description="A URL to view the filter results in Jira, using the [Search for issues using JQL](#api-rest-api-3-filter-search-get) operation with the filter's JQL string to return the filter results. For example, *https://your-domain.atlassian.net/rest/api/3/search?jql=project+%3D+SSP+AND+issuetype+%3D+Bug*.",
        ),
    ] = None
    self: Annotated[AnyUrl | None, Field(description="The URL of the filter.")] = None
    share_permissions: Annotated[
        list[SharePermission] | None,
        Field(
            alias="sharePermissions",
            description="The groups and projects that the filter is shared with. This can be specified when updating a filter, but not when creating a filter.",
        ),
    ] = None
    subscriptions: Annotated[
        list[FilterSubscription] | None,
        Field(description="The users that are subscribed to the filter."),
    ] = None
    view_url: Annotated[
        AnyUrl | None,
        Field(
            alias="viewUrl",
            description="A URL to view the filter results in Jira, using the ID of the filter. For example, *https://your-domain.atlassian.net/issues/?filter=10100*.",
        ),
    ] = None


class PageBeanFilterDetails(BaseModel):
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
    values: Annotated[list[FilterDetails] | None, Field(description="The list of items.")] = None


__all__ = [
    "ChangeFilterOwner",
    "DefaultShareScope",
    "UserList",
    "FilterSubscription",
    "FilterSubscriptionsList",
    "Filter",
    "FilterDetails",
    "PageBeanFilterDetails",
]
