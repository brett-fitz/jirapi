"""Resource classes for projects."""

from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING

from jirapi._resource import AsyncAPIResource, SyncAPIResource
from jirapi.models import (
    ContainerForProjectFeatures,
    CreateProjectDetails,
    ErrorCollection,
    IssueTypeWithStatus,
    NotificationScheme,
    PageBeanProject,
    Project,
    ProjectEmailAddress,
    ProjectFeatureState,
    ProjectIdentifiers,
    ProjectIssueTypeHierarchy,
    UpdateDefaultProjectClassification,
    UpdateProjectDetails,
)


if TYPE_CHECKING:
    from jirapi.projects.avatars import AsyncProjectAvatars, ProjectAvatars
    from jirapi.projects.categories import AsyncProjectCategories, ProjectCategories
    from jirapi.projects.components import AsyncProjectComponents, ProjectComponents
    from jirapi.projects.permission_schemes import (
        AsyncProjectPermissionSchemes,
        ProjectPermissionSchemes,
    )
    from jirapi.projects.properties import AsyncProjectProperties, ProjectProperties
    from jirapi.projects.roles import AsyncProjectRoles, ProjectRoles
    from jirapi.projects.templates import AsyncProjectTemplates, ProjectTemplates
    from jirapi.projects.types import AsyncProjectTypes, ProjectTypes
    from jirapi.projects.versions import AsyncProjectVersions, ProjectVersions


class Projects(SyncAPIResource):
    """Synchronous resource for projects."""

    @cached_property
    def avatars(self) -> ProjectAvatars:
        from jirapi.projects.avatars import ProjectAvatars

        return ProjectAvatars(self._client)

    @cached_property
    def categories(self) -> ProjectCategories:
        from jirapi.projects.categories import ProjectCategories

        return ProjectCategories(self._client)

    @cached_property
    def components(self) -> ProjectComponents:
        from jirapi.projects.components import ProjectComponents

        return ProjectComponents(self._client)

    @cached_property
    def permission_schemes(self) -> ProjectPermissionSchemes:
        from jirapi.projects.permission_schemes import ProjectPermissionSchemes

        return ProjectPermissionSchemes(self._client)

    @cached_property
    def properties(self) -> ProjectProperties:
        from jirapi.projects.properties import ProjectProperties

        return ProjectProperties(self._client)

    @cached_property
    def roles(self) -> ProjectRoles:
        from jirapi.projects.roles import ProjectRoles

        return ProjectRoles(self._client)

    @cached_property
    def templates(self) -> ProjectTemplates:
        from jirapi.projects.templates import ProjectTemplates

        return ProjectTemplates(self._client)

    @cached_property
    def types(self) -> ProjectTypes:
        from jirapi.projects.types import ProjectTypes

        return ProjectTypes(self._client)

    @cached_property
    def versions(self) -> ProjectVersions:
        from jirapi.projects.versions import ProjectVersions

        return ProjectVersions(self._client)

    def create(self, body: CreateProjectDetails) -> ProjectIdentifiers:
        """Create project"""
        resp = self._client._request(
            "POST", "/rest/api/3/project", json=body.model_dump(by_alias=True, exclude_none=True)
        )
        return ProjectIdentifiers.model_validate(resp.json())

    def get_recent(
        self, *, expand: str | None = None, properties: list[str] | None = None
    ) -> Project:
        """Get recent projects"""
        params = self._client._build_params(**{"expand": expand, "properties": properties})
        resp = self._client._request("GET", "/rest/api/3/project/recent", params=params)
        return Project.model_validate(resp.json())

    def search(
        self,
        *,
        start_at: int | None = None,
        max_results: int | None = None,
        order_by: str | None = None,
        id_: list[str] | None = None,
        keys: list[str] | None = None,
        query: str | None = None,
        type_key: str | None = None,
        category_id: int | None = None,
        action: str | None = None,
        expand: str | None = None,
        status: list[str] | None = None,
        properties: list[str] | None = None,
        property_query: str | None = None,
    ) -> PageBeanProject:
        """Get projects paginated"""
        params = self._client._build_params(
            **{
                "startAt": start_at,
                "maxResults": max_results,
                "orderBy": order_by,
                "id": id_,
                "keys": keys,
                "query": query,
                "typeKey": type_key,
                "categoryId": category_id,
                "action": action,
                "expand": expand,
                "status": status,
                "properties": properties,
                "propertyQuery": property_query,
            }
        )
        resp = self._client._request("GET", "/rest/api/3/project/search", params=params)
        return PageBeanProject.model_validate(resp.json())

    def delete(self, project_id_or_key: str, *, enable_undo: bool | None = None) -> None:
        """Delete project"""
        params = self._client._build_params(**{"enableUndo": enable_undo})
        self._client._request("DELETE", f"/rest/api/3/project/{project_id_or_key}", params=params)
        return None

    def get(
        self,
        project_id_or_key: str,
        *,
        expand: str | None = None,
        properties: list[str] | None = None,
    ) -> Project:
        """Get project"""
        params = self._client._build_params(**{"expand": expand, "properties": properties})
        resp = self._client._request(
            "GET", f"/rest/api/3/project/{project_id_or_key}", params=params
        )
        return Project.model_validate(resp.json())

    def update(
        self, project_id_or_key: str, body: UpdateProjectDetails, *, expand: str | None = None
    ) -> Project:
        """Update project"""
        params = self._client._build_params(**{"expand": expand})
        resp = self._client._request(
            "PUT",
            f"/rest/api/3/project/{project_id_or_key}",
            params=params,
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return Project.model_validate(resp.json())

    def archive(self, project_id_or_key: str) -> None:
        """Archive project"""
        self._client._request("POST", f"/rest/api/3/project/{project_id_or_key}/archive")
        return None

    def remove_default_classification(self, project_id_or_key: str) -> None:
        """Remove the default data classification level from a project"""
        self._client._request(
            "DELETE", f"/rest/api/3/project/{project_id_or_key}/classification-level/default"
        )
        return None

    def get_default_classification(self, project_id_or_key: str) -> None:
        """Get the default data classification level of a project"""
        self._client._request(
            "GET", f"/rest/api/3/project/{project_id_or_key}/classification-level/default"
        )
        return None

    def update_default_classification(
        self, project_id_or_key: str, body: UpdateDefaultProjectClassification
    ) -> None:
        """Update the default data classification level of a project"""
        self._client._request(
            "PUT",
            f"/rest/api/3/project/{project_id_or_key}/classification-level/default",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    def delete_async(self, project_id_or_key: str) -> None:
        """Delete project asynchronously"""
        self._client._request("POST", f"/rest/api/3/project/{project_id_or_key}/delete")
        return None

    def get_features(self, project_id_or_key: str) -> ContainerForProjectFeatures:
        """Get project features"""
        resp = self._client._request("GET", f"/rest/api/3/project/{project_id_or_key}/features")
        return ContainerForProjectFeatures.model_validate(resp.json())

    def toggle_feature(
        self, project_id_or_key: str, feature_key: str, body: ProjectFeatureState
    ) -> ContainerForProjectFeatures:
        """Set project feature state"""
        resp = self._client._request(
            "PUT",
            f"/rest/api/3/project/{project_id_or_key}/features/{feature_key}",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return ContainerForProjectFeatures.model_validate(resp.json())

    def restore(self, project_id_or_key: str) -> Project:
        """Restore deleted or archived project"""
        resp = self._client._request("POST", f"/rest/api/3/project/{project_id_or_key}/restore")
        return Project.model_validate(resp.json())

    def get_all_statuses(self, project_id_or_key: str) -> IssueTypeWithStatus:
        """Get all statuses for project"""
        resp = self._client._request("GET", f"/rest/api/3/project/{project_id_or_key}/statuses")
        return IssueTypeWithStatus.model_validate(resp.json())

    def get_email(self, project_id: str) -> ProjectEmailAddress:
        """Get project's sender email"""
        resp = self._client._request("GET", f"/rest/api/3/project/{project_id}/email")
        return ProjectEmailAddress.model_validate(resp.json())

    def update_email(self, project_id: str, body: ProjectEmailAddress) -> None:
        """Set project's sender email"""
        self._client._request(
            "PUT",
            f"/rest/api/3/project/{project_id}/email",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    def get_hierarchy(self, project_id: str) -> ProjectIssueTypeHierarchy:
        """Get project issue type hierarchy"""
        resp = self._client._request("GET", f"/rest/api/3/project/{project_id}/hierarchy")
        return ProjectIssueTypeHierarchy.model_validate(resp.json())

    def get_notification_scheme(
        self, project_key_or_id: str, *, expand: str | None = None
    ) -> NotificationScheme:
        """Get project notification scheme"""
        params = self._client._build_params(**{"expand": expand})
        resp = self._client._request(
            "GET", f"/rest/api/3/project/{project_key_or_id}/notificationscheme", params=params
        )
        return NotificationScheme.model_validate(resp.json())

    def validate_key(self, *, key: str | None = None) -> ErrorCollection:
        """Validate project key"""
        params = self._client._build_params(**{"key": key})
        resp = self._client._request("GET", "/rest/api/3/projectvalidate/key", params=params)
        return ErrorCollection.model_validate(resp.json())

    def get_valid_key(self, *, key: str | None = None) -> str:
        """Get valid project key"""
        params = self._client._build_params(**{"key": key})
        resp = self._client._request(
            "GET", "/rest/api/3/projectvalidate/validProjectKey", params=params
        )
        return resp.json()

    def get_valid_name(self, *, name: str) -> str:
        """Get valid project name"""
        params = self._client._build_params(**{"name": name})
        resp = self._client._request(
            "GET", "/rest/api/3/projectvalidate/validProjectName", params=params
        )
        return resp.json()


class AsyncProjects(AsyncAPIResource):
    """Asynchronous resource for projects."""

    @cached_property
    def avatars(self) -> AsyncProjectAvatars:
        from jirapi.projects.avatars import AsyncProjectAvatars

        return AsyncProjectAvatars(self._client)

    @cached_property
    def categories(self) -> AsyncProjectCategories:
        from jirapi.projects.categories import AsyncProjectCategories

        return AsyncProjectCategories(self._client)

    @cached_property
    def components(self) -> AsyncProjectComponents:
        from jirapi.projects.components import AsyncProjectComponents

        return AsyncProjectComponents(self._client)

    @cached_property
    def permission_schemes(self) -> AsyncProjectPermissionSchemes:
        from jirapi.projects.permission_schemes import AsyncProjectPermissionSchemes

        return AsyncProjectPermissionSchemes(self._client)

    @cached_property
    def properties(self) -> AsyncProjectProperties:
        from jirapi.projects.properties import AsyncProjectProperties

        return AsyncProjectProperties(self._client)

    @cached_property
    def roles(self) -> AsyncProjectRoles:
        from jirapi.projects.roles import AsyncProjectRoles

        return AsyncProjectRoles(self._client)

    @cached_property
    def templates(self) -> AsyncProjectTemplates:
        from jirapi.projects.templates import AsyncProjectTemplates

        return AsyncProjectTemplates(self._client)

    @cached_property
    def types(self) -> AsyncProjectTypes:
        from jirapi.projects.types import AsyncProjectTypes

        return AsyncProjectTypes(self._client)

    @cached_property
    def versions(self) -> AsyncProjectVersions:
        from jirapi.projects.versions import AsyncProjectVersions

        return AsyncProjectVersions(self._client)

    async def create(self, body: CreateProjectDetails) -> ProjectIdentifiers:
        """Create project"""
        resp = await self._client._request(
            "POST", "/rest/api/3/project", json=body.model_dump(by_alias=True, exclude_none=True)
        )
        return ProjectIdentifiers.model_validate(resp.json())

    async def get_recent(
        self, *, expand: str | None = None, properties: list[str] | None = None
    ) -> Project:
        """Get recent projects"""
        params = self._client._build_params(**{"expand": expand, "properties": properties})
        resp = await self._client._request("GET", "/rest/api/3/project/recent", params=params)
        return Project.model_validate(resp.json())

    async def search(
        self,
        *,
        start_at: int | None = None,
        max_results: int | None = None,
        order_by: str | None = None,
        id_: list[str] | None = None,
        keys: list[str] | None = None,
        query: str | None = None,
        type_key: str | None = None,
        category_id: int | None = None,
        action: str | None = None,
        expand: str | None = None,
        status: list[str] | None = None,
        properties: list[str] | None = None,
        property_query: str | None = None,
    ) -> PageBeanProject:
        """Get projects paginated"""
        params = self._client._build_params(
            **{
                "startAt": start_at,
                "maxResults": max_results,
                "orderBy": order_by,
                "id": id_,
                "keys": keys,
                "query": query,
                "typeKey": type_key,
                "categoryId": category_id,
                "action": action,
                "expand": expand,
                "status": status,
                "properties": properties,
                "propertyQuery": property_query,
            }
        )
        resp = await self._client._request("GET", "/rest/api/3/project/search", params=params)
        return PageBeanProject.model_validate(resp.json())

    async def delete(self, project_id_or_key: str, *, enable_undo: bool | None = None) -> None:
        """Delete project"""
        params = self._client._build_params(**{"enableUndo": enable_undo})
        await self._client._request(
            "DELETE", f"/rest/api/3/project/{project_id_or_key}", params=params
        )
        return None

    async def get(
        self,
        project_id_or_key: str,
        *,
        expand: str | None = None,
        properties: list[str] | None = None,
    ) -> Project:
        """Get project"""
        params = self._client._build_params(**{"expand": expand, "properties": properties})
        resp = await self._client._request(
            "GET", f"/rest/api/3/project/{project_id_or_key}", params=params
        )
        return Project.model_validate(resp.json())

    async def update(
        self, project_id_or_key: str, body: UpdateProjectDetails, *, expand: str | None = None
    ) -> Project:
        """Update project"""
        params = self._client._build_params(**{"expand": expand})
        resp = await self._client._request(
            "PUT",
            f"/rest/api/3/project/{project_id_or_key}",
            params=params,
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return Project.model_validate(resp.json())

    async def archive(self, project_id_or_key: str) -> None:
        """Archive project"""
        await self._client._request("POST", f"/rest/api/3/project/{project_id_or_key}/archive")
        return None

    async def remove_default_classification(self, project_id_or_key: str) -> None:
        """Remove the default data classification level from a project"""
        await self._client._request(
            "DELETE", f"/rest/api/3/project/{project_id_or_key}/classification-level/default"
        )
        return None

    async def get_default_classification(self, project_id_or_key: str) -> None:
        """Get the default data classification level of a project"""
        await self._client._request(
            "GET", f"/rest/api/3/project/{project_id_or_key}/classification-level/default"
        )
        return None

    async def update_default_classification(
        self, project_id_or_key: str, body: UpdateDefaultProjectClassification
    ) -> None:
        """Update the default data classification level of a project"""
        await self._client._request(
            "PUT",
            f"/rest/api/3/project/{project_id_or_key}/classification-level/default",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    async def delete_async(self, project_id_or_key: str) -> None:
        """Delete project asynchronously"""
        await self._client._request("POST", f"/rest/api/3/project/{project_id_or_key}/delete")
        return None

    async def get_features(self, project_id_or_key: str) -> ContainerForProjectFeatures:
        """Get project features"""
        resp = await self._client._request(
            "GET", f"/rest/api/3/project/{project_id_or_key}/features"
        )
        return ContainerForProjectFeatures.model_validate(resp.json())

    async def toggle_feature(
        self, project_id_or_key: str, feature_key: str, body: ProjectFeatureState
    ) -> ContainerForProjectFeatures:
        """Set project feature state"""
        resp = await self._client._request(
            "PUT",
            f"/rest/api/3/project/{project_id_or_key}/features/{feature_key}",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return ContainerForProjectFeatures.model_validate(resp.json())

    async def restore(self, project_id_or_key: str) -> Project:
        """Restore deleted or archived project"""
        resp = await self._client._request(
            "POST", f"/rest/api/3/project/{project_id_or_key}/restore"
        )
        return Project.model_validate(resp.json())

    async def get_all_statuses(self, project_id_or_key: str) -> IssueTypeWithStatus:
        """Get all statuses for project"""
        resp = await self._client._request(
            "GET", f"/rest/api/3/project/{project_id_or_key}/statuses"
        )
        return IssueTypeWithStatus.model_validate(resp.json())

    async def get_email(self, project_id: str) -> ProjectEmailAddress:
        """Get project's sender email"""
        resp = await self._client._request("GET", f"/rest/api/3/project/{project_id}/email")
        return ProjectEmailAddress.model_validate(resp.json())

    async def update_email(self, project_id: str, body: ProjectEmailAddress) -> None:
        """Set project's sender email"""
        await self._client._request(
            "PUT",
            f"/rest/api/3/project/{project_id}/email",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    async def get_hierarchy(self, project_id: str) -> ProjectIssueTypeHierarchy:
        """Get project issue type hierarchy"""
        resp = await self._client._request("GET", f"/rest/api/3/project/{project_id}/hierarchy")
        return ProjectIssueTypeHierarchy.model_validate(resp.json())

    async def get_notification_scheme(
        self, project_key_or_id: str, *, expand: str | None = None
    ) -> NotificationScheme:
        """Get project notification scheme"""
        params = self._client._build_params(**{"expand": expand})
        resp = await self._client._request(
            "GET", f"/rest/api/3/project/{project_key_or_id}/notificationscheme", params=params
        )
        return NotificationScheme.model_validate(resp.json())

    async def validate_key(self, *, key: str | None = None) -> ErrorCollection:
        """Validate project key"""
        params = self._client._build_params(**{"key": key})
        resp = await self._client._request("GET", "/rest/api/3/projectvalidate/key", params=params)
        return ErrorCollection.model_validate(resp.json())

    async def get_valid_key(self, *, key: str | None = None) -> str:
        """Get valid project key"""
        params = self._client._build_params(**{"key": key})
        resp = await self._client._request(
            "GET", "/rest/api/3/projectvalidate/validProjectKey", params=params
        )
        return resp.json()

    async def get_valid_name(self, *, name: str) -> str:
        """Get valid project name"""
        params = self._client._build_params(**{"name": name})
        resp = await self._client._request(
            "GET", "/rest/api/3/projectvalidate/validProjectName", params=params
        )
        return resp.json()
