"""Resource classes for the Issue security level API group."""

from __future__ import annotations

from jirapi._resource import AsyncAPIResource, SyncAPIResource
from jirapi.models import PageBeanIssueSecurityLevelMember, SecurityLevel


class IssueSecurityLevel(SyncAPIResource):
    """Synchronous resource for the Issue security level API group."""

    def get_issue_security_level_members(
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

    def get_issue_security_level(self, id_: str) -> SecurityLevel:
        """Get issue security level"""
        resp = self._client._request("GET", f"/rest/api/3/securitylevel/{id_}")
        return SecurityLevel.model_validate(resp.json())


class AsyncIssueSecurityLevel(AsyncAPIResource):
    """Asynchronous resource for the Issue security level API group."""

    async def get_issue_security_level_members(
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

    async def get_issue_security_level(self, id_: str) -> SecurityLevel:
        """Get issue security level"""
        resp = await self._client._request("GET", f"/rest/api/3/securitylevel/{id_}")
        return SecurityLevel.model_validate(resp.json())
