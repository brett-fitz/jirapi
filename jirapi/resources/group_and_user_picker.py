"""Resource classes for the Group and user picker API group."""

from __future__ import annotations

from jirapi._resource import AsyncAPIResource, SyncAPIResource
from jirapi.models import FoundUsersAndGroups


class GroupAndUserPicker(SyncAPIResource):
    """Synchronous resource for the Group and user picker API group."""

    def find_users_and_groups(
        self,
        *,
        query: str,
        max_results: int | None = None,
        show_avatar: bool | None = None,
        field_id: str | None = None,
        project_id: list[str] | None = None,
        issue_type_id: list[str] | None = None,
        avatar_size: str | None = None,
        case_insensitive: bool | None = None,
        exclude_connect_addons: bool | None = None,
    ) -> FoundUsersAndGroups:
        """Find users and groups"""
        params = self._client._build_params(
            **{
                "query": query,
                "maxResults": max_results,
                "showAvatar": show_avatar,
                "fieldId": field_id,
                "projectId": project_id,
                "issueTypeId": issue_type_id,
                "avatarSize": avatar_size,
                "caseInsensitive": case_insensitive,
                "excludeConnectAddons": exclude_connect_addons,
            }
        )
        resp = self._client._request("GET", "/rest/api/3/groupuserpicker", params=params)
        return FoundUsersAndGroups.model_validate(resp.json())


class AsyncGroupAndUserPicker(AsyncAPIResource):
    """Asynchronous resource for the Group and user picker API group."""

    async def find_users_and_groups(
        self,
        *,
        query: str,
        max_results: int | None = None,
        show_avatar: bool | None = None,
        field_id: str | None = None,
        project_id: list[str] | None = None,
        issue_type_id: list[str] | None = None,
        avatar_size: str | None = None,
        case_insensitive: bool | None = None,
        exclude_connect_addons: bool | None = None,
    ) -> FoundUsersAndGroups:
        """Find users and groups"""
        params = self._client._build_params(
            **{
                "query": query,
                "maxResults": max_results,
                "showAvatar": show_avatar,
                "fieldId": field_id,
                "projectId": project_id,
                "issueTypeId": issue_type_id,
                "avatarSize": avatar_size,
                "caseInsensitive": case_insensitive,
                "excludeConnectAddons": exclude_connect_addons,
            }
        )
        resp = await self._client._request("GET", "/rest/api/3/groupuserpicker", params=params)
        return FoundUsersAndGroups.model_validate(resp.json())
