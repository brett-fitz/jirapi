"""Resource classes for the Project email API group."""

from __future__ import annotations

from jirapi._resource import AsyncAPIResource, SyncAPIResource
from jirapi.models import ProjectEmailAddress


class ProjectEmail(SyncAPIResource):
    """Synchronous resource for the Project email API group."""

    def get_project_email(self, project_id: str) -> ProjectEmailAddress:
        """Get project's sender email"""
        resp = self._client._request("GET", f"/rest/api/3/project/{project_id}/email")
        return ProjectEmailAddress.model_validate(resp.json())

    def update_project_email(self, project_id: str, body: ProjectEmailAddress) -> None:
        """Set project's sender email"""
        self._client._request(
            "PUT",
            f"/rest/api/3/project/{project_id}/email",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None


class AsyncProjectEmail(AsyncAPIResource):
    """Asynchronous resource for the Project email API group."""

    async def get_project_email(self, project_id: str) -> ProjectEmailAddress:
        """Get project's sender email"""
        resp = await self._client._request("GET", f"/rest/api/3/project/{project_id}/email")
        return ProjectEmailAddress.model_validate(resp.json())

    async def update_project_email(self, project_id: str, body: ProjectEmailAddress) -> None:
        """Set project's sender email"""
        await self._client._request(
            "PUT",
            f"/rest/api/3/project/{project_id}/email",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None
