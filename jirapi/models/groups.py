"""Pydantic models for the groups domain."""

from __future__ import annotations

from typing import Annotated

from pydantic import AnyUrl, BaseModel, ConfigDict, Field


class GroupDetails(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    group_id: Annotated[
        str | None,
        Field(
            alias="groupId",
            description="The ID of the group, which uniquely identifies the group across all Atlassian products. For example, *952d12c3-5b5b-4d04-bb32-44d383afc4b2*.",
        ),
    ] = None
    name: Annotated[str | None, Field(description="The name of the group.")] = None


class PageBeanGroupDetails(BaseModel):
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
    values: Annotated[list[GroupDetails] | None, Field(description="The list of items.")] = None


class PageBeanUserDetails(BaseModel):
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
    values: Annotated[list[UserDetails] | None, Field(description="The list of items.")] = None


class PagedListUserDetailsApplicationUser(BaseModel):
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
    items: Annotated[list[UserDetails] | None, Field(description="The list of items.")] = None
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


class Group(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    expand: Annotated[
        str | None,
        Field(description="Expand options that include additional group details in the response."),
    ] = None
    group_id: Annotated[
        str | None,
        Field(
            alias="groupId",
            description="The ID of the group, which uniquely identifies the group across all Atlassian products. For example, *952d12c3-5b5b-4d04-bb32-44d383afc4b2*.",
        ),
    ] = None
    name: Annotated[str | None, Field(description="The name of group.")] = None
    self: Annotated[AnyUrl | None, Field(description="The URL for these group details.")] = None
    users: Annotated[
        PagedListUserDetailsApplicationUser | None,
        Field(
            description="A paginated list of the users that are members of the group. A maximum of 50 users is returned in the list, to access additional users append `[start-index:end-index]` to the expand request. For example, to access the next 50 users, use`?expand=users[51:100]`."
        ),
    ] = None


__all__ = [
    "GroupDetails",
    "PageBeanGroupDetails",
    "PageBeanUserDetails",
    "PagedListUserDetailsApplicationUser",
    "Group",
]
