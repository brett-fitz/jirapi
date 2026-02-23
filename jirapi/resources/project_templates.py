"""Resource classes for the Project templates API group."""

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
    """Synchronous resource for the Project templates API group."""

    def create_project_with_custom_template(
        self, body: ProjectCustomTemplateCreateRequestDTO
    ) -> None:
        """Create custom project"""
        resp = self._client._request(
            "POST",
            "/rest/api/3/project-template",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    def edit_template(self, body: EditTemplateRequest) -> None:
        """Edit a custom project template"""
        resp = self._client._request(
            "PUT",
            "/rest/api/3/project-template/edit-template",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    def live_template(
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

    def remove_template(self, *, template_key: str) -> None:
        """Deletes a custom project template"""
        params = self._client._build_params(**{"templateKey": template_key})
        resp = self._client._request(
            "DELETE", "/rest/api/3/project-template/remove-template", params=params
        )
        return None

    def save_template(self, body: SaveTemplateRequest) -> SaveTemplateResponse:
        """Save a custom project template"""
        resp = self._client._request(
            "POST",
            "/rest/api/3/project-template/save-template",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return SaveTemplateResponse.model_validate(resp.json())


class AsyncProjectTemplates(AsyncAPIResource):
    """Asynchronous resource for the Project templates API group."""

    async def create_project_with_custom_template(
        self, body: ProjectCustomTemplateCreateRequestDTO
    ) -> None:
        """Create custom project"""
        resp = await self._client._request(
            "POST",
            "/rest/api/3/project-template",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    async def edit_template(self, body: EditTemplateRequest) -> None:
        """Edit a custom project template"""
        resp = await self._client._request(
            "PUT",
            "/rest/api/3/project-template/edit-template",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    async def live_template(
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

    async def remove_template(self, *, template_key: str) -> None:
        """Deletes a custom project template"""
        params = self._client._build_params(**{"templateKey": template_key})
        resp = await self._client._request(
            "DELETE", "/rest/api/3/project-template/remove-template", params=params
        )
        return None

    async def save_template(self, body: SaveTemplateRequest) -> SaveTemplateResponse:
        """Save a custom project template"""
        resp = await self._client._request(
            "POST",
            "/rest/api/3/project-template/save-template",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return SaveTemplateResponse.model_validate(resp.json())
