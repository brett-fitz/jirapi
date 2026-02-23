"""Resource classes for the Issue custom field options (apps) API group."""

from __future__ import annotations

from jirapi._resource import AsyncAPIResource, SyncAPIResource
from jirapi.models import IssueFieldOption, IssueFieldOptionCreateBean, PageBeanIssueFieldOption


class IssueCustomFieldOptionsApps(SyncAPIResource):
    """Synchronous resource for the Issue custom field options (apps) API group."""

    def get_all_issue_field_options(
        self, field_key: str, *, start_at: int | None = None, max_results: int | None = None
    ) -> PageBeanIssueFieldOption:
        """Get all issue field options"""
        params = self._client._build_params(**{"startAt": start_at, "maxResults": max_results})
        resp = self._client._request("GET", f"/rest/api/3/field/{field_key}/option", params=params)
        return PageBeanIssueFieldOption.model_validate(resp.json())

    def create_issue_field_option(
        self, field_key: str, body: IssueFieldOptionCreateBean
    ) -> IssueFieldOption:
        """Create issue field option"""
        resp = self._client._request(
            "POST",
            f"/rest/api/3/field/{field_key}/option",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return IssueFieldOption.model_validate(resp.json())

    def get_selectable_issue_field_options(
        self,
        field_key: str,
        *,
        start_at: int | None = None,
        max_results: int | None = None,
        project_id: int | None = None,
    ) -> PageBeanIssueFieldOption:
        """Get selectable issue field options"""
        params = self._client._build_params(
            **{"startAt": start_at, "maxResults": max_results, "projectId": project_id}
        )
        resp = self._client._request(
            "GET", f"/rest/api/3/field/{field_key}/option/suggestions/edit", params=params
        )
        return PageBeanIssueFieldOption.model_validate(resp.json())

    def get_visible_issue_field_options(
        self,
        field_key: str,
        *,
        start_at: int | None = None,
        max_results: int | None = None,
        project_id: int | None = None,
    ) -> PageBeanIssueFieldOption:
        """Get visible issue field options"""
        params = self._client._build_params(
            **{"startAt": start_at, "maxResults": max_results, "projectId": project_id}
        )
        resp = self._client._request(
            "GET", f"/rest/api/3/field/{field_key}/option/suggestions/search", params=params
        )
        return PageBeanIssueFieldOption.model_validate(resp.json())

    def delete_issue_field_option(self, field_key: str, option_id: str) -> None:
        """Delete issue field option"""
        resp = self._client._request("DELETE", f"/rest/api/3/field/{field_key}/option/{option_id}")
        return None

    def get_issue_field_option(self, field_key: str, option_id: str) -> IssueFieldOption:
        """Get issue field option"""
        resp = self._client._request("GET", f"/rest/api/3/field/{field_key}/option/{option_id}")
        return IssueFieldOption.model_validate(resp.json())

    def update_issue_field_option(
        self, field_key: str, option_id: str, body: IssueFieldOption
    ) -> IssueFieldOption:
        """Update issue field option"""
        resp = self._client._request(
            "PUT",
            f"/rest/api/3/field/{field_key}/option/{option_id}",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return IssueFieldOption.model_validate(resp.json())

    def replace_issue_field_option(
        self,
        field_key: str,
        option_id: str,
        *,
        replace_with: int | None = None,
        jql: str | None = None,
        override_screen_security: bool | None = None,
        override_editable_flag: bool | None = None,
    ) -> None:
        """Replace issue field option"""
        params = self._client._build_params(
            **{
                "replaceWith": replace_with,
                "jql": jql,
                "overrideScreenSecurity": override_screen_security,
                "overrideEditableFlag": override_editable_flag,
            }
        )
        resp = self._client._request(
            "DELETE", f"/rest/api/3/field/{field_key}/option/{option_id}/issue", params=params
        )
        return None


class AsyncIssueCustomFieldOptionsApps(AsyncAPIResource):
    """Asynchronous resource for the Issue custom field options (apps) API group."""

    async def get_all_issue_field_options(
        self, field_key: str, *, start_at: int | None = None, max_results: int | None = None
    ) -> PageBeanIssueFieldOption:
        """Get all issue field options"""
        params = self._client._build_params(**{"startAt": start_at, "maxResults": max_results})
        resp = await self._client._request(
            "GET", f"/rest/api/3/field/{field_key}/option", params=params
        )
        return PageBeanIssueFieldOption.model_validate(resp.json())

    async def create_issue_field_option(
        self, field_key: str, body: IssueFieldOptionCreateBean
    ) -> IssueFieldOption:
        """Create issue field option"""
        resp = await self._client._request(
            "POST",
            f"/rest/api/3/field/{field_key}/option",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return IssueFieldOption.model_validate(resp.json())

    async def get_selectable_issue_field_options(
        self,
        field_key: str,
        *,
        start_at: int | None = None,
        max_results: int | None = None,
        project_id: int | None = None,
    ) -> PageBeanIssueFieldOption:
        """Get selectable issue field options"""
        params = self._client._build_params(
            **{"startAt": start_at, "maxResults": max_results, "projectId": project_id}
        )
        resp = await self._client._request(
            "GET", f"/rest/api/3/field/{field_key}/option/suggestions/edit", params=params
        )
        return PageBeanIssueFieldOption.model_validate(resp.json())

    async def get_visible_issue_field_options(
        self,
        field_key: str,
        *,
        start_at: int | None = None,
        max_results: int | None = None,
        project_id: int | None = None,
    ) -> PageBeanIssueFieldOption:
        """Get visible issue field options"""
        params = self._client._build_params(
            **{"startAt": start_at, "maxResults": max_results, "projectId": project_id}
        )
        resp = await self._client._request(
            "GET", f"/rest/api/3/field/{field_key}/option/suggestions/search", params=params
        )
        return PageBeanIssueFieldOption.model_validate(resp.json())

    async def delete_issue_field_option(self, field_key: str, option_id: str) -> None:
        """Delete issue field option"""
        resp = await self._client._request(
            "DELETE", f"/rest/api/3/field/{field_key}/option/{option_id}"
        )
        return None

    async def get_issue_field_option(self, field_key: str, option_id: str) -> IssueFieldOption:
        """Get issue field option"""
        resp = await self._client._request(
            "GET", f"/rest/api/3/field/{field_key}/option/{option_id}"
        )
        return IssueFieldOption.model_validate(resp.json())

    async def update_issue_field_option(
        self, field_key: str, option_id: str, body: IssueFieldOption
    ) -> IssueFieldOption:
        """Update issue field option"""
        resp = await self._client._request(
            "PUT",
            f"/rest/api/3/field/{field_key}/option/{option_id}",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return IssueFieldOption.model_validate(resp.json())

    async def replace_issue_field_option(
        self,
        field_key: str,
        option_id: str,
        *,
        replace_with: int | None = None,
        jql: str | None = None,
        override_screen_security: bool | None = None,
        override_editable_flag: bool | None = None,
    ) -> None:
        """Replace issue field option"""
        params = self._client._build_params(
            **{
                "replaceWith": replace_with,
                "jql": jql,
                "overrideScreenSecurity": override_screen_security,
                "overrideEditableFlag": override_editable_flag,
            }
        )
        resp = await self._client._request(
            "DELETE", f"/rest/api/3/field/{field_key}/option/{option_id}/issue", params=params
        )
        return None
