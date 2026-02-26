"""Resource classes for projects.templates."""

from __future__ import annotations

from jirapi._resource import AsyncAPIResource, SyncAPIResource
from jirapi.models import (
    EditTemplateRequest,
    ProjectCustomTemplateCreateRequestDTO,
    ProjectTemplateModel,
    SaveTemplateRequest,
    SaveTemplateResponse,
)


class ProjectTemplates(SyncAPIResource):
    """Synchronous resource for projects.templates."""

    def create_with_template(self, body: ProjectCustomTemplateCreateRequestDTO) -> None:
        """Create custom project"""
        self._client._request(
            "POST",
            "/rest/api/3/project-template",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    def edit(self, body: EditTemplateRequest) -> None:
        """Edit a custom project template"""
        self._client._request(
            "PUT",
            "/rest/api/3/project-template/edit-template",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    def go_live(
        self, *, project_id: str | None = None, template_key: str | None = None
    ) -> ProjectTemplateModel:
        """Gets a custom project template"""
        params = self._client._build_params(
            **{"projectId": project_id, "templateKey": template_key}
        )
        resp = self._client._request(
            "GET", "/rest/api/3/project-template/live-template", params=params
        )
        return ProjectTemplateModel.model_validate(resp.json())

    def remove(self, *, template_key: str) -> None:
        """Deletes a custom project template"""
        params = self._client._build_params(**{"templateKey": template_key})
        self._client._request(
            "DELETE", "/rest/api/3/project-template/remove-template", params=params
        )
        return None

    def save(self, body: SaveTemplateRequest) -> SaveTemplateResponse:
        """Save a custom project template"""
        resp = self._client._request(
            "POST",
            "/rest/api/3/project-template/save-template",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return SaveTemplateResponse.model_validate(resp.json())


class AsyncProjectTemplates(AsyncAPIResource):
    """Asynchronous resource for projects.templates."""

    async def create_with_template(self, body: ProjectCustomTemplateCreateRequestDTO) -> None:
        """Create custom project"""
        await self._client._request(
            "POST",
            "/rest/api/3/project-template",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    async def edit(self, body: EditTemplateRequest) -> None:
        """Edit a custom project template"""
        await self._client._request(
            "PUT",
            "/rest/api/3/project-template/edit-template",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    async def go_live(
        self, *, project_id: str | None = None, template_key: str | None = None
    ) -> ProjectTemplateModel:
        """Gets a custom project template"""
        params = self._client._build_params(
            **{"projectId": project_id, "templateKey": template_key}
        )
        resp = await self._client._request(
            "GET", "/rest/api/3/project-template/live-template", params=params
        )
        return ProjectTemplateModel.model_validate(resp.json())

    async def remove(self, *, template_key: str) -> None:
        """Deletes a custom project template"""
        params = self._client._build_params(**{"templateKey": template_key})
        await self._client._request(
            "DELETE", "/rest/api/3/project-template/remove-template", params=params
        )
        return None

    async def save(self, body: SaveTemplateRequest) -> SaveTemplateResponse:
        """Save a custom project template"""
        resp = await self._client._request(
            "POST",
            "/rest/api/3/project-template/save-template",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return SaveTemplateResponse.model_validate(resp.json())
