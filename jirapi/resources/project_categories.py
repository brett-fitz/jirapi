"""Resource classes for the Project categories API group."""

from __future__ import annotations

from jirapi._resource import AsyncAPIResource, SyncAPIResource
from jirapi.models import ProjectCategory, UpdatedProjectCategory


class ProjectCategories(SyncAPIResource):
    """Synchronous resource for the Project categories API group."""

    def get_all_project_categories(self) -> ProjectCategory:
        """Get all project categories"""
        resp = self._client._request("GET", "/rest/api/3/projectCategory")
        return ProjectCategory.model_validate(resp.json())

    def create_project_category(self, body: ProjectCategory) -> ProjectCategory:
        """Create project category"""
        resp = self._client._request(
            "POST",
            "/rest/api/3/projectCategory",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return ProjectCategory.model_validate(resp.json())

    def remove_project_category(self, id_: str) -> None:
        """Delete project category"""
        resp = self._client._request("DELETE", f"/rest/api/3/projectCategory/{id_}")
        return None

    def get_project_category_by_id(self, id_: str) -> ProjectCategory:
        """Get project category by ID"""
        resp = self._client._request("GET", f"/rest/api/3/projectCategory/{id_}")
        return ProjectCategory.model_validate(resp.json())

    def update_project_category(self, id_: str, body: ProjectCategory) -> UpdatedProjectCategory:
        """Update project category"""
        resp = self._client._request(
            "PUT",
            f"/rest/api/3/projectCategory/{id_}",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return UpdatedProjectCategory.model_validate(resp.json())


class AsyncProjectCategories(AsyncAPIResource):
    """Asynchronous resource for the Project categories API group."""

    async def get_all_project_categories(self) -> ProjectCategory:
        """Get all project categories"""
        resp = await self._client._request("GET", "/rest/api/3/projectCategory")
        return ProjectCategory.model_validate(resp.json())

    async def create_project_category(self, body: ProjectCategory) -> ProjectCategory:
        """Create project category"""
        resp = await self._client._request(
            "POST",
            "/rest/api/3/projectCategory",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return ProjectCategory.model_validate(resp.json())

    async def remove_project_category(self, id_: str) -> None:
        """Delete project category"""
        resp = await self._client._request("DELETE", f"/rest/api/3/projectCategory/{id_}")
        return None

    async def get_project_category_by_id(self, id_: str) -> ProjectCategory:
        """Get project category by ID"""
        resp = await self._client._request("GET", f"/rest/api/3/projectCategory/{id_}")
        return ProjectCategory.model_validate(resp.json())

    async def update_project_category(
        self, id_: str, body: ProjectCategory
    ) -> UpdatedProjectCategory:
        """Update project category"""
        resp = await self._client._request(
            "PUT",
            f"/rest/api/3/projectCategory/{id_}",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return UpdatedProjectCategory.model_validate(resp.json())
