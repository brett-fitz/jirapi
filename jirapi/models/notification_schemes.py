"""Pydantic models for the notification schemes domain."""

from __future__ import annotations

from typing import Annotated

from pydantic import AnyUrl, BaseModel, ConfigDict, Field


class NotificationSchemeEventTypeId(BaseModel):
    model_config = ConfigDict(
        extra="allow",
    )
    id: Annotated[str, Field(description="The ID of the notification scheme event.")]


class NotificationSchemeId(BaseModel):
    model_config = ConfigDict(
        extra="allow",
    )
    id: Annotated[str, Field(description="The ID of a notification scheme.")]


class NotificationSchemeNotificationDetails(BaseModel):
    model_config = ConfigDict(
        extra="allow",
    )
    notification_type: Annotated[
        str,
        Field(
            alias="notificationType",
            description="The notification type, e.g `CurrentAssignee`, `Group`, `EmailAddress`.",
        ),
    ]
    parameter: Annotated[
        str | None, Field(description="The value corresponding to the specified notification type.")
    ] = None


class UpdateNotificationSchemeDetails(BaseModel):
    model_config = ConfigDict(
        extra="allow",
    )
    description: Annotated[
        str | None,
        Field(description="The description of the notification scheme.", max_length=4000),
    ] = None
    name: Annotated[
        str | None,
        Field(
            description="The name of the notification scheme. Must be unique.",
            max_length=255,
        ),
    ] = None


class NotificationSchemeEventDetails(BaseModel):
    model_config = ConfigDict(
        extra="allow",
    )
    event: Annotated[NotificationSchemeEventTypeId, Field(description="The ID of the event.")]
    notifications: Annotated[
        list[NotificationSchemeNotificationDetails],
        Field(
            description="The list of notifications mapped to a specified event.",
            max_length=255,
        ),
    ]


class AddNotificationsDetails(BaseModel):
    model_config = ConfigDict(
        extra="allow",
    )
    notification_scheme_events: Annotated[
        list[NotificationSchemeEventDetails],
        Field(
            alias="notificationSchemeEvents",
            description="The list of notifications which should be added to the notification scheme.",
        ),
    ]


class CreateNotificationSchemeDetails(BaseModel):
    model_config = ConfigDict(
        extra="allow",
    )
    description: Annotated[
        str | None,
        Field(description="The description of the notification scheme.", max_length=4000),
    ] = None
    name: Annotated[
        str,
        Field(
            description="The name of the notification scheme. Must be unique (case-insensitive).",
            max_length=255,
        ),
    ]
    notification_scheme_events: Annotated[
        list[NotificationSchemeEventDetails] | None,
        Field(
            alias="notificationSchemeEvents",
            description="The list of notifications which should be added to the notification scheme.",
        ),
    ] = None


class PageBeanNotificationScheme(BaseModel):
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
    values: Annotated[list[NotificationScheme] | None, Field(description="The list of items.")] = (
        None
    )


__all__ = [
    "NotificationSchemeEventTypeId",
    "NotificationSchemeId",
    "NotificationSchemeNotificationDetails",
    "UpdateNotificationSchemeDetails",
    "NotificationSchemeEventDetails",
    "AddNotificationsDetails",
    "CreateNotificationSchemeDetails",
    "PageBeanNotificationScheme",
]
