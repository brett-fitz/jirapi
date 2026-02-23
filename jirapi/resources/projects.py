"""Resource classes for the Projects API group."""

from __future__ import annotations

from jirapi._resource import AsyncAPIResource, SyncAPIResource
from jirapi.models import (
    CreateProjectDetails,
    IssueTypeWithStatus,
    NotificationScheme,
    PageBeanProject,
    Project,
    ProjectIdentifiers,
    ProjectIssueTypeHierarchy,
    UpdateProjectDetails,
)


class Projects(SyncAPIResource):
    """Synchronous resource for the Projects API group."""

    def create_project(self, body: CreateProjectDetails) -> ProjectIdentifiers:
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

    def search_projects(
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

    def delete_project(self, project_id_or_key: str, *, enable_undo: bool | None = None) -> None:
        """Delete project"""
        params = self._client._build_params(**{"enableUndo": enable_undo})
        resp = self._client._request(
            "DELETE", f"/rest/api/3/project/{project_id_or_key}", params=params
        )
        return None

    def get_project(
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

    def update_project(
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

    def archive_project(self, project_id_or_key: str) -> None:
        """Archive project"""
        resp = self._client._request("POST", f"/rest/api/3/project/{project_id_or_key}/archive")
        return None

    def delete_project_asynchronously(self, project_id_or_key: str) -> None:
        """Delete project asynchronously"""
        resp = self._client._request("POST", f"/rest/api/3/project/{project_id_or_key}/delete")
        return None

    def restore(self, project_id_or_key: str) -> Project:
        """Restore deleted or archived project"""
        resp = self._client._request("POST", f"/rest/api/3/project/{project_id_or_key}/restore")
        return Project.model_validate(resp.json())

    def get_all_statuses(self, project_id_or_key: str) -> IssueTypeWithStatus:
        """Get all statuses for project"""
        resp = self._client._request("GET", f"/rest/api/3/project/{project_id_or_key}/statuses")
        return IssueTypeWithStatus.model_validate(resp.json())

    def get_hierarchy(self, project_id: str) -> ProjectIssueTypeHierarchy:
        """Get project issue type hierarchy"""
        resp = self._client._request("GET", f"/rest/api/3/project/{project_id}/hierarchy")
        return ProjectIssueTypeHierarchy.model_validate(resp.json())

    def get_notification_scheme_for_project(
        self, project_key_or_id: str, *, expand: str | None = None
    ) -> NotificationScheme:
        """Get project notification scheme"""
        params = self._client._build_params(**{"expand": expand})
        resp = self._client._request(
            "GET", f"/rest/api/3/project/{project_key_or_id}/notificationscheme", params=params
        )
        return NotificationScheme.model_validate(resp.json())


class AsyncProjects(AsyncAPIResource):
    """Asynchronous resource for the Projects API group."""

    async def create_project(self, body: CreateProjectDetails) -> ProjectIdentifiers:
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

    async def search_projects(
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

    async def delete_project(
        self, project_id_or_key: str, *, enable_undo: bool | None = None
    ) -> None:
        """Delete project"""
        params = self._client._build_params(**{"enableUndo": enable_undo})
        resp = await self._client._request(
            "DELETE", f"/rest/api/3/project/{project_id_or_key}", params=params
        )
        return None

    async def get_project(
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

    async def update_project(
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

    async def archive_project(self, project_id_or_key: str) -> None:
        """Archive project"""
        resp = await self._client._request(
            "POST", f"/rest/api/3/project/{project_id_or_key}/archive"
        )
        return None

    async def delete_project_asynchronously(self, project_id_or_key: str) -> None:
        """Delete project asynchronously"""
        resp = await self._client._request(
            "POST", f"/rest/api/3/project/{project_id_or_key}/delete"
        )
        return None

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

    async def get_hierarchy(self, project_id: str) -> ProjectIssueTypeHierarchy:
        """Get project issue type hierarchy"""
        resp = await self._client._request("GET", f"/rest/api/3/project/{project_id}/hierarchy")
        return ProjectIssueTypeHierarchy.model_validate(resp.json())

    async def get_notification_scheme_for_project(
        self, project_key_or_id: str, *, expand: str | None = None
    ) -> NotificationScheme:
        """Get project notification scheme"""
        params = self._client._build_params(**{"expand": expand})
        resp = await self._client._request(
            "GET", f"/rest/api/3/project/{project_key_or_id}/notificationscheme", params=params
        )
        return NotificationScheme.model_validate(resp.json())
