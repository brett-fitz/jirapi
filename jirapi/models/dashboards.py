"""Pydantic models for the dashboards domain."""

from __future__ import annotations

from typing import Annotated

from pydantic import AnyUrl, BaseModel, ConfigDict, Field


class AvailableDashboardGadget(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    module_key: Annotated[
        str | None, Field(alias="moduleKey", description="The module key of the gadget type.")
    ] = None
    title: Annotated[str, Field(description="The title of the gadget.")]
    uri: Annotated[str | None, Field(description="The URI of the gadget type.")] = None


class AvailableDashboardGadgetsResponse(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    gadgets: Annotated[
        list[AvailableDashboardGadget], Field(description="The list of available gadgets.")
    ]


class BulkChangeOwnerDetails(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    autofix_name: Annotated[
        bool,
        Field(
            alias="autofixName",
            description="Whether the name is fixed automatically if it's duplicated after changing owner.",
        ),
    ]
    new_owner: Annotated[
        str, Field(alias="newOwner", description="The account id of the new owner.")
    ]


class BulkEditActionError(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    error_messages: Annotated[
        list[str], Field(alias="errorMessages", description="The error messages.")
    ]
    errors: Annotated[dict[str, str], Field(description="The errors.")]


class BulkEditShareableEntityResponse(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    action: Annotated[Action, Field(description="Allowed action for bulk edit shareable entity")]
    entity_errors: Annotated[
        dict[str, BulkEditActionError] | None,
        Field(
            alias="entityErrors",
            description="The mapping dashboard id to errors if any.",
        ),
    ] = None


class DashboardGadgetPosition(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    the_column_position_of_the_gadget_: Annotated[
        int, Field(alias="The column position of the gadget.")
    ]
    the_row_position_of_the_gadget_: Annotated[int, Field(alias="The row position of the gadget.")]


class DashboardGadgetSettings(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    color: Annotated[
        str | None,
        Field(
            description="The color of the gadget. Should be one of `blue`, `red`, `yellow`, `green`, `cyan`, `purple`, `gray`, or `white`."
        ),
    ] = None
    ignore_uri_and_module_key_validation: Annotated[
        bool | None,
        Field(
            alias="ignoreUriAndModuleKeyValidation",
            description="Whether to ignore the validation of module key and URI. For example, when a gadget is created that is a part of an application that isn't installed.",
        ),
    ] = None
    module_key: Annotated[
        str | None,
        Field(
            alias="moduleKey",
            description="The module key of the gadget type. Can't be provided with `uri`.",
        ),
    ] = None
    position: Annotated[
        DashboardGadgetPosition | None,
        Field(
            description="The position of the gadget. When the gadget is placed into the position, other gadgets in the same column are moved down to accommodate it."
        ),
    ] = None
    title: Annotated[str | None, Field(description="The title of the gadget.")] = None
    uri: Annotated[
        str | None,
        Field(description="The URI of the gadget type. Can't be provided with `moduleKey`."),
    ] = None


class DashboardGadgetUpdateRequest(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    color: Annotated[
        str | None,
        Field(
            description="The color of the gadget. Should be one of `blue`, `red`, `yellow`, `green`, `cyan`, `purple`, `gray`, or `white`."
        ),
    ] = None
    position: Annotated[
        DashboardGadgetPosition | None, Field(description="The position of the gadget.")
    ] = None
    title: Annotated[str | None, Field(description="The title of the gadget.")] = None


class DashboardGadget(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    color: Annotated[
        Color,
        Field(
            description="The color of the gadget. Should be one of `blue`, `red`, `yellow`, `green`, `cyan`, `purple`, `gray`, or `white`."
        ),
    ]
    id: Annotated[int, Field(description="The ID of the gadget instance.")]
    module_key: Annotated[
        str | None, Field(alias="moduleKey", description="The module key of the gadget type.")
    ] = None
    position: Annotated[DashboardGadgetPosition, Field(description="The position of the gadget.")]
    title: Annotated[str, Field(description="The title of the gadget.")]
    uri: Annotated[str | None, Field(description="The URI of the gadget type.")] = None


class DashboardGadgetResponse(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    gadgets: Annotated[list[DashboardGadget], Field(description="The list of gadgets.")]


class Dashboard(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    automatic_refresh_ms: Annotated[
        int | None,
        Field(
            alias="automaticRefreshMs",
            description="The automatic refresh interval for the dashboard in milliseconds.",
        ),
    ] = None
    description: str | None = None
    edit_permissions: Annotated[
        list[SharePermission] | None,
        Field(
            alias="editPermissions",
            description="The details of any edit share permissions for the dashboard.",
        ),
    ] = None
    id: Annotated[str | None, Field(description="The ID of the dashboard.")] = None
    is_favourite: Annotated[
        bool | None,
        Field(
            alias="isFavourite",
            description="Whether the dashboard is selected as a favorite by the user.",
        ),
    ] = None
    is_writable: Annotated[
        bool | None,
        Field(
            alias="isWritable",
            description="Whether the current user has permission to edit the dashboard.",
        ),
    ] = None
    name: Annotated[str | None, Field(description="The name of the dashboard.")] = None
    owner: Annotated[User | None, Field(description="The owner of the dashboard.")] = None
    popularity: Annotated[
        int | None, Field(description="The number of users who have this dashboard as a favorite.")
    ] = None
    rank: Annotated[int | None, Field(description="The rank of this dashboard.")] = None
    self: Annotated[AnyUrl | None, Field(description="The URL of these dashboard details.")] = None
    share_permissions: Annotated[
        list[SharePermission] | None,
        Field(
            alias="sharePermissions",
            description="The details of any view share permissions for the dashboard.",
        ),
    ] = None
    system_dashboard: Annotated[
        bool | None,
        Field(
            alias="systemDashboard",
            description="Whether the current dashboard is system dashboard.",
        ),
    ] = None
    view: Annotated[str | None, Field(description="The URL of the dashboard.")] = None


class DashboardDetails(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    description: Annotated[str | None, Field(description="The description of the dashboard.")] = (
        None
    )
    edit_permissions: Annotated[
        list[SharePermission],
        Field(
            alias="editPermissions",
            description="The edit permissions for the dashboard.",
        ),
    ]
    name: Annotated[str, Field(description="The name of the dashboard.")]
    share_permissions: Annotated[
        list[SharePermission],
        Field(
            alias="sharePermissions",
            description="The share permissions for the dashboard.",
        ),
    ]


class PageBeanDashboard(BaseModel):
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
    values: Annotated[list[Dashboard] | None, Field(description="The list of items.")] = None


class PageOfDashboards(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    dashboards: Annotated[list[Dashboard] | None, Field(description="List of dashboards.")] = None
    max_results: Annotated[
        int | None,
        Field(
            alias="maxResults",
            description="The maximum number of results that could be on the page.",
        ),
    ] = None
    next: Annotated[
        str | None, Field(description="The URL of the next page of results, if any.")
    ] = None
    prev: Annotated[
        str | None, Field(description="The URL of the previous page of results, if any.")
    ] = None
    start_at: Annotated[
        int | None,
        Field(
            alias="startAt",
            description="The index of the first item returned on the page.",
        ),
    ] = None
    total: Annotated[int | None, Field(description="The number of results on the page.")] = None


class PermissionDetails(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    edit_permissions: Annotated[
        list[SharePermission],
        Field(
            alias="editPermissions",
            description="The edit permissions for the shareable entities.",
        ),
    ]
    share_permissions: Annotated[
        list[SharePermission],
        Field(
            alias="sharePermissions",
            description="The share permissions for the shareable entities.",
        ),
    ]


class BulkEditShareableEntityRequest(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    action: Annotated[Action, Field(description="Allowed action for bulk edit shareable entity")]
    change_owner_details: Annotated[
        BulkChangeOwnerDetails | None,
        Field(
            alias="changeOwnerDetails",
            description="The details of change owner action.",
        ),
    ] = None
    entity_ids: Annotated[
        list[int],
        Field(
            alias="entityIds",
            description="The id list of shareable entities to be changed.",
        ),
    ]
    extend_admin_permissions: Annotated[
        bool | None,
        Field(
            alias="extendAdminPermissions",
            description="Whether the actions are executed by users with Administer Jira global permission.",
        ),
    ] = None
    permission_details: Annotated[
        PermissionDetails | None,
        Field(
            alias="permissionDetails",
            description="The permission details to be changed.",
        ),
    ] = None


__all__ = [
    "AvailableDashboardGadget",
    "AvailableDashboardGadgetsResponse",
    "BulkChangeOwnerDetails",
    "BulkEditActionError",
    "BulkEditShareableEntityResponse",
    "DashboardGadgetPosition",
    "DashboardGadgetSettings",
    "DashboardGadgetUpdateRequest",
    "DashboardGadget",
    "DashboardGadgetResponse",
    "Dashboard",
    "DashboardDetails",
    "PageBeanDashboard",
    "PageOfDashboards",
    "PermissionDetails",
    "BulkEditShareableEntityRequest",
]
