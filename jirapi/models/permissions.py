"""Pydantic models for the permissions domain."""

from __future__ import annotations

from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field


class BulkProjectPermissionGrants(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    issues: Annotated[
        list[int], Field(description="IDs of the issues the user has the permission for.")
    ]
    permission: Annotated[str, Field(description="A project permission,")]
    projects: Annotated[
        list[int], Field(description="IDs of the projects the user has the permission for.")
    ]


class BulkProjectPermissions(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    issues: Annotated[list[int] | None, Field(description="List of issue IDs.")] = None
    permissions: Annotated[list[str], Field(description="List of project permissions.")]
    projects: Annotated[list[int] | None, Field(description="List of project IDs.")] = None


class UserPermission(BaseModel):
    model_config = ConfigDict(
        extra="allow",
    )
    deprecated_key: Annotated[
        bool | None,
        Field(
            alias="deprecatedKey",
            description="Indicate whether the permission key is deprecated. Note that deprecated keys cannot be used in the `permissions parameter of Get my permissions. Deprecated keys are not returned by Get all permissions.`",
        ),
    ] = None
    description: Annotated[str | None, Field(description="The description of the permission.")] = (
        None
    )
    have_permission: Annotated[
        bool | None,
        Field(
            alias="havePermission",
            description="Whether the permission is available to the user in the queried context.",
        ),
    ] = None
    id: Annotated[
        str | None,
        Field(
            description="The ID of the permission. Either `id` or `key` must be specified. Use [Get all permissions](#api-rest-api-3-permissions-get) to get the list of permissions."
        ),
    ] = None
    key: Annotated[
        str | None,
        Field(
            description="The key of the permission. Either `id` or `key` must be specified. Use [Get all permissions](#api-rest-api-3-permissions-get) to get the list of permissions."
        ),
    ] = None
    name: Annotated[str | None, Field(description="The name of the permission.")] = None
    type: Annotated[Type33 | None, Field(description="The type of the permission.")] = None


class BulkPermissionGrants(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    global_permissions: Annotated[
        list[str],
        Field(
            alias="globalPermissions",
            description="List of permissions granted to the user.",
        ),
    ]
    project_permissions: Annotated[
        list[BulkProjectPermissionGrants],
        Field(
            alias="projectPermissions",
            description="List of project permissions and the projects and issues those permissions provide access to.",
        ),
    ]


class PermissionGrants(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    expand: Annotated[
        str | None,
        Field(
            description="Expand options that include additional permission grant details in the response."
        ),
    ] = None
    permissions: Annotated[
        list[PermissionGrant] | None, Field(description="Permission grants list.")
    ] = None


class Permissions(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    permissions: Annotated[
        dict[str, UserPermission] | None, Field(description="List of permissions.")
    ] = None


class PermittedProjects(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    projects: Annotated[
        list[ProjectIdentifier] | None, Field(description="A list of projects.")
    ] = None


class PermissionSchemes(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    permission_schemes: Annotated[
        list[PermissionScheme] | None,
        Field(alias="permissionSchemes", description="Permission schemes list."),
    ] = None


__all__ = [
    "BulkProjectPermissionGrants",
    "BulkProjectPermissions",
    "UserPermission",
    "BulkPermissionGrants",
    "PermissionGrants",
    "Permissions",
    "PermittedProjects",
    "PermissionSchemes",
]
