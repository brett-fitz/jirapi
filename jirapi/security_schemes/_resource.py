"""Resource classes for security_schemes."""

from __future__ import annotations

from jirapi._resource import AsyncAPIResource, SyncAPIResource
from jirapi.models import (
    AddSecuritySchemeLevelsRequest,
    AssociateSecuritySchemeWithProjectDetails,
    CreateIssueSecuritySchemeDetails,
    PageBeanIssueSecurityLevelMember,
    PageBeanIssueSecuritySchemeToProjectMapping,
    PageBeanSecurityLevel,
    PageBeanSecurityLevelMember,
    PageBeanSecuritySchemeWithProjects,
    SecurityLevel,
    SecurityScheme,
    SecuritySchemeId,
    SecuritySchemeMembersRequest,
    SetDefaultLevelsRequest,
    UpdateIssueSecurityLevelDetails,
    UpdateIssueSecuritySchemeRequest,
)
from jirapi.models import SecuritySchemes as SecuritySchemesModel


class SecuritySchemes(SyncAPIResource):
    """Synchronous resource for security_schemes."""

    def list(self) -> SecuritySchemesModel:
        """Get issue security schemes"""
        resp = self._client._request("GET", "/rest/api/3/issuesecurityschemes")
        return SecuritySchemesModel.model_validate(resp.json())

    def create(self, body: CreateIssueSecuritySchemeDetails) -> SecuritySchemeId:
        """Create issue security scheme"""
        resp = self._client._request(
            "POST",
            "/rest/api/3/issuesecurityschemes",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return SecuritySchemeId.model_validate(resp.json())

    def get_levels(
        self,
        *,
        start_at: str | None = None,
        max_results: str | None = None,
        id_: list[str] | None = None,
        scheme_id: list[str] | None = None,
        only_default: bool | None = None,
    ) -> PageBeanSecurityLevel:
        """Get issue security levels"""
        params = self._client._build_params(
            **{
                "startAt": start_at,
                "maxResults": max_results,
                "id": id_,
                "schemeId": scheme_id,
                "onlyDefault": only_default,
            }
        )
        resp = self._client._request("GET", "/rest/api/3/issuesecurityschemes/level", params=params)
        return PageBeanSecurityLevel.model_validate(resp.json())

    def set_default_levels(self, body: SetDefaultLevelsRequest) -> None:
        """Set default issue security levels"""
        self._client._request(
            "PUT",
            "/rest/api/3/issuesecurityschemes/level/default",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    def get_level_members(
        self,
        *,
        start_at: str | None = None,
        max_results: str | None = None,
        id_: list[str] | None = None,
        scheme_id: list[str] | None = None,
        level_id: list[str] | None = None,
        expand: str | None = None,
    ) -> PageBeanSecurityLevelMember:
        """Get issue security level members"""
        params = self._client._build_params(
            **{
                "startAt": start_at,
                "maxResults": max_results,
                "id": id_,
                "schemeId": scheme_id,
                "levelId": level_id,
                "expand": expand,
            }
        )
        resp = self._client._request(
            "GET", "/rest/api/3/issuesecurityschemes/level/member", params=params
        )
        return PageBeanSecurityLevelMember.model_validate(resp.json())

    def search_projects(
        self,
        *,
        start_at: str | None = None,
        max_results: str | None = None,
        issue_security_scheme_id: list[str] | None = None,
        project_id: list[str] | None = None,
    ) -> PageBeanIssueSecuritySchemeToProjectMapping:
        """Get projects using issue security schemes"""
        params = self._client._build_params(
            **{
                "startAt": start_at,
                "maxResults": max_results,
                "issueSecuritySchemeId": issue_security_scheme_id,
                "projectId": project_id,
            }
        )
        resp = self._client._request(
            "GET", "/rest/api/3/issuesecurityschemes/project", params=params
        )
        return PageBeanIssueSecuritySchemeToProjectMapping.model_validate(resp.json())

    def associate_to_projects(self, body: AssociateSecuritySchemeWithProjectDetails) -> None:
        """Associate security scheme to project"""
        self._client._request(
            "PUT",
            "/rest/api/3/issuesecurityschemes/project",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    def search(
        self,
        *,
        start_at: str | None = None,
        max_results: str | None = None,
        id_: list[str] | None = None,
        project_id: list[str] | None = None,
    ) -> PageBeanSecuritySchemeWithProjects:
        """Search issue security schemes"""
        params = self._client._build_params(
            **{"startAt": start_at, "maxResults": max_results, "id": id_, "projectId": project_id}
        )
        resp = self._client._request(
            "GET", "/rest/api/3/issuesecurityschemes/search", params=params
        )
        return PageBeanSecuritySchemeWithProjects.model_validate(resp.json())

    def get(self, id_: str) -> SecurityScheme:
        """Get issue security scheme"""
        resp = self._client._request("GET", f"/rest/api/3/issuesecurityschemes/{id_}")
        return SecurityScheme.model_validate(resp.json())

    def update(self, id_: str, body: UpdateIssueSecuritySchemeRequest) -> None:
        """Update issue security scheme"""
        self._client._request(
            "PUT",
            f"/rest/api/3/issuesecurityschemes/{id_}",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    def get_security_level_members(
        self,
        issue_security_scheme_id: str,
        *,
        start_at: int | None = None,
        max_results: int | None = None,
        issue_security_level_id: list[str] | None = None,
        expand: str | None = None,
    ) -> PageBeanIssueSecurityLevelMember:
        """Get issue security level members by issue security scheme"""
        params = self._client._build_params(
            **{
                "startAt": start_at,
                "maxResults": max_results,
                "issueSecurityLevelId": issue_security_level_id,
                "expand": expand,
            }
        )
        resp = self._client._request(
            "GET",
            f"/rest/api/3/issuesecurityschemes/{issue_security_scheme_id}/members",
            params=params,
        )
        return PageBeanIssueSecurityLevelMember.model_validate(resp.json())

    def delete(self, scheme_id: str) -> None:
        """Delete issue security scheme"""
        self._client._request("DELETE", f"/rest/api/3/issuesecurityschemes/{scheme_id}")
        return None

    def add_level(self, scheme_id: str, body: AddSecuritySchemeLevelsRequest) -> None:
        """Add issue security levels"""
        self._client._request(
            "PUT",
            f"/rest/api/3/issuesecurityschemes/{scheme_id}/level",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    def remove_level(
        self, scheme_id: str, level_id: str, *, replace_with: str | None = None
    ) -> None:
        """Remove issue security level"""
        params = self._client._build_params(**{"replaceWith": replace_with})
        self._client._request(
            "DELETE",
            f"/rest/api/3/issuesecurityschemes/{scheme_id}/level/{level_id}",
            params=params,
        )
        return None

    def update_level(
        self, scheme_id: str, level_id: str, body: UpdateIssueSecurityLevelDetails
    ) -> None:
        """Update issue security level"""
        self._client._request(
            "PUT",
            f"/rest/api/3/issuesecurityschemes/{scheme_id}/level/{level_id}",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    def add_level_members(
        self, scheme_id: str, level_id: str, body: SecuritySchemeMembersRequest
    ) -> None:
        """Add issue security level members"""
        self._client._request(
            "PUT",
            f"/rest/api/3/issuesecurityschemes/{scheme_id}/level/{level_id}/member",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    def remove_level_member(self, scheme_id: str, level_id: str, member_id: str) -> None:
        """Remove member from issue security level"""
        self._client._request(
            "DELETE",
            f"/rest/api/3/issuesecurityschemes/{scheme_id}/level/{level_id}/member/{member_id}",
        )
        return None

    def get_security_level(self, id_: str) -> SecurityLevel:
        """Get issue security level"""
        resp = self._client._request("GET", f"/rest/api/3/securitylevel/{id_}")
        return SecurityLevel.model_validate(resp.json())


class AsyncSecuritySchemes(AsyncAPIResource):
    """Asynchronous resource for security_schemes."""

    async def list(self) -> SecuritySchemesModel:
        """Get issue security schemes"""
        resp = await self._client._request("GET", "/rest/api/3/issuesecurityschemes")
        return SecuritySchemesModel.model_validate(resp.json())

    async def create(self, body: CreateIssueSecuritySchemeDetails) -> SecuritySchemeId:
        """Create issue security scheme"""
        resp = await self._client._request(
            "POST",
            "/rest/api/3/issuesecurityschemes",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return SecuritySchemeId.model_validate(resp.json())

    async def get_levels(
        self,
        *,
        start_at: str | None = None,
        max_results: str | None = None,
        id_: list[str] | None = None,
        scheme_id: list[str] | None = None,
        only_default: bool | None = None,
    ) -> PageBeanSecurityLevel:
        """Get issue security levels"""
        params = self._client._build_params(
            **{
                "startAt": start_at,
                "maxResults": max_results,
                "id": id_,
                "schemeId": scheme_id,
                "onlyDefault": only_default,
            }
        )
        resp = await self._client._request(
            "GET", "/rest/api/3/issuesecurityschemes/level", params=params
        )
        return PageBeanSecurityLevel.model_validate(resp.json())

    async def set_default_levels(self, body: SetDefaultLevelsRequest) -> None:
        """Set default issue security levels"""
        await self._client._request(
            "PUT",
            "/rest/api/3/issuesecurityschemes/level/default",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    async def get_level_members(
        self,
        *,
        start_at: str | None = None,
        max_results: str | None = None,
        id_: list[str] | None = None,
        scheme_id: list[str] | None = None,
        level_id: list[str] | None = None,
        expand: str | None = None,
    ) -> PageBeanSecurityLevelMember:
        """Get issue security level members"""
        params = self._client._build_params(
            **{
                "startAt": start_at,
                "maxResults": max_results,
                "id": id_,
                "schemeId": scheme_id,
                "levelId": level_id,
                "expand": expand,
            }
        )
        resp = await self._client._request(
            "GET", "/rest/api/3/issuesecurityschemes/level/member", params=params
        )
        return PageBeanSecurityLevelMember.model_validate(resp.json())

    async def search_projects(
        self,
        *,
        start_at: str | None = None,
        max_results: str | None = None,
        issue_security_scheme_id: list[str] | None = None,
        project_id: list[str] | None = None,
    ) -> PageBeanIssueSecuritySchemeToProjectMapping:
        """Get projects using issue security schemes"""
        params = self._client._build_params(
            **{
                "startAt": start_at,
                "maxResults": max_results,
                "issueSecuritySchemeId": issue_security_scheme_id,
                "projectId": project_id,
            }
        )
        resp = await self._client._request(
            "GET", "/rest/api/3/issuesecurityschemes/project", params=params
        )
        return PageBeanIssueSecuritySchemeToProjectMapping.model_validate(resp.json())

    async def associate_to_projects(self, body: AssociateSecuritySchemeWithProjectDetails) -> None:
        """Associate security scheme to project"""
        await self._client._request(
            "PUT",
            "/rest/api/3/issuesecurityschemes/project",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    async def search(
        self,
        *,
        start_at: str | None = None,
        max_results: str | None = None,
        id_: list[str] | None = None,
        project_id: list[str] | None = None,
    ) -> PageBeanSecuritySchemeWithProjects:
        """Search issue security schemes"""
        params = self._client._build_params(
            **{"startAt": start_at, "maxResults": max_results, "id": id_, "projectId": project_id}
        )
        resp = await self._client._request(
            "GET", "/rest/api/3/issuesecurityschemes/search", params=params
        )
        return PageBeanSecuritySchemeWithProjects.model_validate(resp.json())

    async def get(self, id_: str) -> SecurityScheme:
        """Get issue security scheme"""
        resp = await self._client._request("GET", f"/rest/api/3/issuesecurityschemes/{id_}")
        return SecurityScheme.model_validate(resp.json())

    async def update(self, id_: str, body: UpdateIssueSecuritySchemeRequest) -> None:
        """Update issue security scheme"""
        await self._client._request(
            "PUT",
            f"/rest/api/3/issuesecurityschemes/{id_}",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    async def get_security_level_members(
        self,
        issue_security_scheme_id: str,
        *,
        start_at: int | None = None,
        max_results: int | None = None,
        issue_security_level_id: list[str] | None = None,
        expand: str | None = None,
    ) -> PageBeanIssueSecurityLevelMember:
        """Get issue security level members by issue security scheme"""
        params = self._client._build_params(
            **{
                "startAt": start_at,
                "maxResults": max_results,
                "issueSecurityLevelId": issue_security_level_id,
                "expand": expand,
            }
        )
        resp = await self._client._request(
            "GET",
            f"/rest/api/3/issuesecurityschemes/{issue_security_scheme_id}/members",
            params=params,
        )
        return PageBeanIssueSecurityLevelMember.model_validate(resp.json())

    async def delete(self, scheme_id: str) -> None:
        """Delete issue security scheme"""
        await self._client._request("DELETE", f"/rest/api/3/issuesecurityschemes/{scheme_id}")
        return None

    async def add_level(self, scheme_id: str, body: AddSecuritySchemeLevelsRequest) -> None:
        """Add issue security levels"""
        await self._client._request(
            "PUT",
            f"/rest/api/3/issuesecurityschemes/{scheme_id}/level",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    async def remove_level(
        self, scheme_id: str, level_id: str, *, replace_with: str | None = None
    ) -> None:
        """Remove issue security level"""
        params = self._client._build_params(**{"replaceWith": replace_with})
        await self._client._request(
            "DELETE",
            f"/rest/api/3/issuesecurityschemes/{scheme_id}/level/{level_id}",
            params=params,
        )
        return None

    async def update_level(
        self, scheme_id: str, level_id: str, body: UpdateIssueSecurityLevelDetails
    ) -> None:
        """Update issue security level"""
        await self._client._request(
            "PUT",
            f"/rest/api/3/issuesecurityschemes/{scheme_id}/level/{level_id}",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    async def add_level_members(
        self, scheme_id: str, level_id: str, body: SecuritySchemeMembersRequest
    ) -> None:
        """Add issue security level members"""
        await self._client._request(
            "PUT",
            f"/rest/api/3/issuesecurityschemes/{scheme_id}/level/{level_id}/member",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    async def remove_level_member(self, scheme_id: str, level_id: str, member_id: str) -> None:
        """Remove member from issue security level"""
        await self._client._request(
            "DELETE",
            f"/rest/api/3/issuesecurityschemes/{scheme_id}/level/{level_id}/member/{member_id}",
        )
        return None

    async def get_security_level(self, id_: str) -> SecurityLevel:
        """Get issue security level"""
        resp = await self._client._request("GET", f"/rest/api/3/securitylevel/{id_}")
        return SecurityLevel.model_validate(resp.json())
