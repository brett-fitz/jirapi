"""Resource classes for the Issue security schemes API group."""

from __future__ import annotations

from jirapi._resource import AsyncAPIResource, SyncAPIResource
from jirapi.models import (
    AddSecuritySchemeLevelsRequestBean,
    AssociateSecuritySchemeWithProjectDetails,
    CreateIssueSecuritySchemeDetails,
    PageBeanIssueSecuritySchemeToProjectMapping,
    PageBeanSecurityLevel,
    PageBeanSecurityLevelMember,
    PageBeanSecuritySchemeWithProjects,
    SecurityScheme,
    SecuritySchemeId,
    SecuritySchemeMembersRequest,
    SecuritySchemes,
    SetDefaultLevelsRequest,
    UpdateIssueSecurityLevelDetails,
    UpdateIssueSecuritySchemeRequestBean,
)


class IssueSecuritySchemes(SyncAPIResource):
    """Synchronous resource for the Issue security schemes API group."""

    def get_issue_security_schemes(self) -> SecuritySchemes:
        """Get issue security schemes"""
        resp = self._client._request("GET", "/rest/api/3/issuesecurityschemes")
        return SecuritySchemes.model_validate(resp.json())

    def create_issue_security_scheme(
        self, body: CreateIssueSecuritySchemeDetails
    ) -> SecuritySchemeId:
        """Create issue security scheme"""
        resp = self._client._request(
            "POST",
            "/rest/api/3/issuesecurityschemes",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return SecuritySchemeId.model_validate(resp.json())

    def get_security_levels(
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

    def get_security_level_members(
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

    def search_projects_using_security_schemes(
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

    def associate_schemes_to_projects(
        self, body: AssociateSecuritySchemeWithProjectDetails
    ) -> None:
        """Associate security scheme to project"""
        self._client._request(
            "PUT",
            "/rest/api/3/issuesecurityschemes/project",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    def search_security_schemes(
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

    def get_issue_security_scheme(self, id_: str) -> SecurityScheme:
        """Get issue security scheme"""
        resp = self._client._request("GET", f"/rest/api/3/issuesecurityschemes/{id_}")
        return SecurityScheme.model_validate(resp.json())

    def update_issue_security_scheme(
        self, id_: str, body: UpdateIssueSecuritySchemeRequestBean
    ) -> None:
        """Update issue security scheme"""
        self._client._request(
            "PUT",
            f"/rest/api/3/issuesecurityschemes/{id_}",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    def delete_security_scheme(self, scheme_id: str) -> None:
        """Delete issue security scheme"""
        self._client._request("DELETE", f"/rest/api/3/issuesecurityschemes/{scheme_id}")
        return None

    def add_security_level(self, scheme_id: str, body: AddSecuritySchemeLevelsRequestBean) -> None:
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

    def update_security_level(
        self, scheme_id: str, level_id: str, body: UpdateIssueSecurityLevelDetails
    ) -> None:
        """Update issue security level"""
        self._client._request(
            "PUT",
            f"/rest/api/3/issuesecurityschemes/{scheme_id}/level/{level_id}",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    def add_security_level_members(
        self, scheme_id: str, level_id: str, body: SecuritySchemeMembersRequest
    ) -> None:
        """Add issue security level members"""
        self._client._request(
            "PUT",
            f"/rest/api/3/issuesecurityschemes/{scheme_id}/level/{level_id}/member",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    def remove_member_from_security_level(
        self, scheme_id: str, level_id: str, member_id: str
    ) -> None:
        """Remove member from issue security level"""
        self._client._request(
            "DELETE",
            f"/rest/api/3/issuesecurityschemes/{scheme_id}/level/{level_id}/member/{member_id}",
        )
        return None


class AsyncIssueSecuritySchemes(AsyncAPIResource):
    """Asynchronous resource for the Issue security schemes API group."""

    async def get_issue_security_schemes(self) -> SecuritySchemes:
        """Get issue security schemes"""
        resp = await self._client._request("GET", "/rest/api/3/issuesecurityschemes")
        return SecuritySchemes.model_validate(resp.json())

    async def create_issue_security_scheme(
        self, body: CreateIssueSecuritySchemeDetails
    ) -> SecuritySchemeId:
        """Create issue security scheme"""
        resp = await self._client._request(
            "POST",
            "/rest/api/3/issuesecurityschemes",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return SecuritySchemeId.model_validate(resp.json())

    async def get_security_levels(
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

    async def get_security_level_members(
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

    async def search_projects_using_security_schemes(
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

    async def associate_schemes_to_projects(
        self, body: AssociateSecuritySchemeWithProjectDetails
    ) -> None:
        """Associate security scheme to project"""
        await self._client._request(
            "PUT",
            "/rest/api/3/issuesecurityschemes/project",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    async def search_security_schemes(
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

    async def get_issue_security_scheme(self, id_: str) -> SecurityScheme:
        """Get issue security scheme"""
        resp = await self._client._request("GET", f"/rest/api/3/issuesecurityschemes/{id_}")
        return SecurityScheme.model_validate(resp.json())

    async def update_issue_security_scheme(
        self, id_: str, body: UpdateIssueSecuritySchemeRequestBean
    ) -> None:
        """Update issue security scheme"""
        await self._client._request(
            "PUT",
            f"/rest/api/3/issuesecurityschemes/{id_}",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    async def delete_security_scheme(self, scheme_id: str) -> None:
        """Delete issue security scheme"""
        await self._client._request("DELETE", f"/rest/api/3/issuesecurityschemes/{scheme_id}")
        return None

    async def add_security_level(
        self, scheme_id: str, body: AddSecuritySchemeLevelsRequestBean
    ) -> None:
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

    async def update_security_level(
        self, scheme_id: str, level_id: str, body: UpdateIssueSecurityLevelDetails
    ) -> None:
        """Update issue security level"""
        await self._client._request(
            "PUT",
            f"/rest/api/3/issuesecurityschemes/{scheme_id}/level/{level_id}",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    async def add_security_level_members(
        self, scheme_id: str, level_id: str, body: SecuritySchemeMembersRequest
    ) -> None:
        """Add issue security level members"""
        await self._client._request(
            "PUT",
            f"/rest/api/3/issuesecurityschemes/{scheme_id}/level/{level_id}/member",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    async def remove_member_from_security_level(
        self, scheme_id: str, level_id: str, member_id: str
    ) -> None:
        """Remove member from issue security level"""
        await self._client._request(
            "DELETE",
            f"/rest/api/3/issuesecurityschemes/{scheme_id}/level/{level_id}/member/{member_id}",
        )
        return None
