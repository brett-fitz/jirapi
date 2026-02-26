"""Resource classes for users."""

from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING

from jirapi._resource import AsyncAPIResource, SyncAPIResource
from jirapi.models import (
    ColumnItem,
    FoundUsers,
    FoundUsersAndGroups,
    GroupName,
    Locale,
    NewUserDetails,
    PageBeanUser,
    PageBeanUserKey,
    UnrestrictedUserEmail,
    User,
    UserMigration,
)


if TYPE_CHECKING:
    from jirapi.users.properties import AsyncUserProperties, UserProperties


class Users(SyncAPIResource):
    """Synchronous resource for users."""

    @cached_property
    def properties(self) -> UserProperties:
        from jirapi.users.properties import UserProperties

        return UserProperties(self._client)

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

    def remove_preference(self, *, key: str) -> None:
        """Delete preference"""
        params = self._client._build_params(**{"key": key})
        self._client._request("DELETE", "/rest/api/3/mypreferences", params=params)
        return None

    def get_preference(self, *, key: str) -> str:
        """Get preference"""
        params = self._client._build_params(**{"key": key})
        resp = self._client._request("GET", "/rest/api/3/mypreferences", params=params)
        return resp.json()

    def set_preference(self, *, key: str) -> None:
        """Set preference"""
        params = self._client._build_params(**{"key": key})
        self._client._request("PUT", "/rest/api/3/mypreferences", params=params)
        return None

    def get_locale(self) -> Locale:
        """Get locale"""
        resp = self._client._request("GET", "/rest/api/3/mypreferences/locale")
        return Locale.model_validate(resp.json())

    def get_current_user(self, *, expand: str | None = None) -> User:
        """Get current user"""
        params = self._client._build_params(**{"expand": expand})
        resp = self._client._request("GET", "/rest/api/3/myself", params=params)
        return User.model_validate(resp.json())

    def remove(
        self, *, account_id: str, username: str | None = None, key: str | None = None
    ) -> None:
        """Delete user"""
        params = self._client._build_params(
            **{"accountId": account_id, "username": username, "key": key}
        )
        self._client._request("DELETE", "/rest/api/3/user", params=params)
        return None

    def get(
        self,
        *,
        account_id: str | None = None,
        username: str | None = None,
        key: str | None = None,
        expand: str | None = None,
    ) -> User:
        """Get user"""
        params = self._client._build_params(
            **{"accountId": account_id, "username": username, "key": key, "expand": expand}
        )
        resp = self._client._request("GET", "/rest/api/3/user", params=params)
        return User.model_validate(resp.json())

    def create(self, body: NewUserDetails) -> User:
        """Create user"""
        resp = self._client._request(
            "POST", "/rest/api/3/user", json=body.model_dump(by_alias=True, exclude_none=True)
        )
        return User.model_validate(resp.json())

    def find_bulk_assignable(
        self,
        *,
        query: str | None = None,
        username: str | None = None,
        account_id: str | None = None,
        project_keys: str,
        start_at: int | None = None,
        max_results: int | None = None,
    ) -> User:
        """Find users assignable to projects"""
        params = self._client._build_params(
            **{
                "query": query,
                "username": username,
                "accountId": account_id,
                "projectKeys": project_keys,
                "startAt": start_at,
                "maxResults": max_results,
            }
        )
        resp = self._client._request(
            "GET", "/rest/api/3/user/assignable/multiProjectSearch", params=params
        )
        return User.model_validate(resp.json())

    def find_assignable(
        self,
        *,
        query: str | None = None,
        session_id: str | None = None,
        username: str | None = None,
        account_id: str | None = None,
        project: str | None = None,
        issue_key: str | None = None,
        issue_id: str | None = None,
        start_at: int | None = None,
        max_results: int | None = None,
        action_descriptor_id: int | None = None,
        recommend: bool | None = None,
        account_type: list[str] | None = None,
        app_type: list[str] | None = None,
    ) -> User:
        """Find users assignable to issues"""
        params = self._client._build_params(
            **{
                "query": query,
                "sessionId": session_id,
                "username": username,
                "accountId": account_id,
                "project": project,
                "issueKey": issue_key,
                "issueId": issue_id,
                "startAt": start_at,
                "maxResults": max_results,
                "actionDescriptorId": action_descriptor_id,
                "recommend": recommend,
                "accountType": account_type,
                "appType": app_type,
            }
        )
        resp = self._client._request("GET", "/rest/api/3/user/assignable/search", params=params)
        return User.model_validate(resp.json())

    def bulk_get(
        self,
        *,
        start_at: int | None = None,
        max_results: int | None = None,
        username: list[str] | None = None,
        key: list[str] | None = None,
        account_id: list[str],
    ) -> PageBeanUser:
        """Bulk get users"""
        params = self._client._build_params(
            **{
                "startAt": start_at,
                "maxResults": max_results,
                "username": username,
                "key": key,
                "accountId": account_id,
            }
        )
        resp = self._client._request("GET", "/rest/api/3/user/bulk", params=params)
        return PageBeanUser.model_validate(resp.json())

    def bulk_get_migration(
        self,
        *,
        start_at: int | None = None,
        max_results: int | None = None,
        username: list[str] | None = None,
        key: list[str] | None = None,
    ) -> UserMigration:
        """Get account IDs for users"""
        params = self._client._build_params(
            **{"startAt": start_at, "maxResults": max_results, "username": username, "key": key}
        )
        resp = self._client._request("GET", "/rest/api/3/user/bulk/migration", params=params)
        return UserMigration.model_validate(resp.json())

    def reset_columns(self, *, account_id: str | None = None, username: str | None = None) -> None:
        """Reset user default columns"""
        params = self._client._build_params(**{"accountId": account_id, "username": username})
        self._client._request("DELETE", "/rest/api/3/user/columns", params=params)
        return None

    def get_default_columns(
        self, *, account_id: str | None = None, username: str | None = None
    ) -> ColumnItem:
        """Get user default columns"""
        params = self._client._build_params(**{"accountId": account_id, "username": username})
        resp = self._client._request("GET", "/rest/api/3/user/columns", params=params)
        return ColumnItem.model_validate(resp.json())

    def set_columns(self, *, account_id: str | None = None) -> None:
        """Set user default columns"""
        params = self._client._build_params(**{"accountId": account_id})
        self._client._request("PUT", "/rest/api/3/user/columns", params=params)
        return None

    def get_email(self, *, account_id: str) -> UnrestrictedUserEmail:
        """Get user email"""
        params = self._client._build_params(**{"accountId": account_id})
        resp = self._client._request("GET", "/rest/api/3/user/email", params=params)
        return UnrestrictedUserEmail.model_validate(resp.json())

    def get_email_bulk(self, *, account_id: list[str]) -> UnrestrictedUserEmail:
        """Get user email bulk"""
        params = self._client._build_params(**{"accountId": account_id})
        resp = self._client._request("GET", "/rest/api/3/user/email/bulk", params=params)
        return UnrestrictedUserEmail.model_validate(resp.json())

    def get_groups(
        self, *, account_id: str, username: str | None = None, key: str | None = None
    ) -> GroupName:
        """Get user groups"""
        params = self._client._build_params(
            **{"accountId": account_id, "username": username, "key": key}
        )
        resp = self._client._request("GET", "/rest/api/3/user/groups", params=params)
        return GroupName.model_validate(resp.json())

    def find_with_permissions(
        self,
        *,
        query: str | None = None,
        username: str | None = None,
        account_id: str | None = None,
        permissions: str,
        issue_key: str | None = None,
        project_key: str | None = None,
        start_at: int | None = None,
        max_results: int | None = None,
    ) -> User:
        """Find users with permissions"""
        params = self._client._build_params(
            **{
                "query": query,
                "username": username,
                "accountId": account_id,
                "permissions": permissions,
                "issueKey": issue_key,
                "projectKey": project_key,
                "startAt": start_at,
                "maxResults": max_results,
            }
        )
        resp = self._client._request("GET", "/rest/api/3/user/permission/search", params=params)
        return User.model_validate(resp.json())

    def find_for_picker(
        self,
        *,
        query: str,
        max_results: int | None = None,
        show_avatar: bool | None = None,
        exclude: list[str] | None = None,
        exclude_account_ids: list[str] | None = None,
        avatar_size: str | None = None,
        exclude_connect_users: bool | None = None,
    ) -> FoundUsers:
        """Find users for picker"""
        params = self._client._build_params(
            **{
                "query": query,
                "maxResults": max_results,
                "showAvatar": show_avatar,
                "exclude": exclude,
                "excludeAccountIds": exclude_account_ids,
                "avatarSize": avatar_size,
                "excludeConnectUsers": exclude_connect_users,
            }
        )
        resp = self._client._request("GET", "/rest/api/3/user/picker", params=params)
        return FoundUsers.model_validate(resp.json())

    def find(
        self,
        *,
        query: str | None = None,
        username: str | None = None,
        account_id: str | None = None,
        start_at: int | None = None,
        max_results: int | None = None,
        property: str | None = None,
    ) -> User:
        """Find users"""
        params = self._client._build_params(
            **{
                "query": query,
                "username": username,
                "accountId": account_id,
                "startAt": start_at,
                "maxResults": max_results,
                "property": property,
            }
        )
        resp = self._client._request("GET", "/rest/api/3/user/search", params=params)
        return User.model_validate(resp.json())

    def find_by_query(
        self, *, query: str, start_at: int | None = None, max_results: int | None = None
    ) -> PageBeanUser:
        """Find users by query"""
        params = self._client._build_params(
            **{"query": query, "startAt": start_at, "maxResults": max_results}
        )
        resp = self._client._request("GET", "/rest/api/3/user/search/query", params=params)
        return PageBeanUser.model_validate(resp.json())

    def find_keys_by_query(
        self, *, query: str, start_at: int | None = None, max_result: int | None = None
    ) -> PageBeanUserKey:
        """Find user keys by query"""
        params = self._client._build_params(
            **{"query": query, "startAt": start_at, "maxResult": max_result}
        )
        resp = self._client._request("GET", "/rest/api/3/user/search/query/key", params=params)
        return PageBeanUserKey.model_validate(resp.json())

    def find_with_browse_permission(
        self,
        *,
        query: str | None = None,
        username: str | None = None,
        account_id: str | None = None,
        issue_key: str | None = None,
        project_key: str | None = None,
        start_at: int | None = None,
        max_results: int | None = None,
    ) -> User:
        """Find users with browse permission"""
        params = self._client._build_params(
            **{
                "query": query,
                "username": username,
                "accountId": account_id,
                "issueKey": issue_key,
                "projectKey": project_key,
                "startAt": start_at,
                "maxResults": max_results,
            }
        )
        resp = self._client._request("GET", "/rest/api/3/user/viewissue/search", params=params)
        return User.model_validate(resp.json())

    def list(self, *, start_at: int | None = None, max_results: int | None = None) -> User:
        """Get all users default"""
        params = self._client._build_params(**{"startAt": start_at, "maxResults": max_results})
        resp = self._client._request("GET", "/rest/api/3/users", params=params)
        return User.model_validate(resp.json())

    def list_all(self, *, start_at: int | None = None, max_results: int | None = None) -> User:
        """Get all users"""
        params = self._client._build_params(**{"startAt": start_at, "maxResults": max_results})
        resp = self._client._request("GET", "/rest/api/3/users/search", params=params)
        return User.model_validate(resp.json())


class AsyncUsers(AsyncAPIResource):
    """Asynchronous resource for users."""

    @cached_property
    def properties(self) -> AsyncUserProperties:
        from jirapi.users.properties import AsyncUserProperties

        return AsyncUserProperties(self._client)

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

    async def remove_preference(self, *, key: str) -> None:
        """Delete preference"""
        params = self._client._build_params(**{"key": key})
        await self._client._request("DELETE", "/rest/api/3/mypreferences", params=params)
        return None

    async def get_preference(self, *, key: str) -> str:
        """Get preference"""
        params = self._client._build_params(**{"key": key})
        resp = await self._client._request("GET", "/rest/api/3/mypreferences", params=params)
        return resp.json()

    async def set_preference(self, *, key: str) -> None:
        """Set preference"""
        params = self._client._build_params(**{"key": key})
        await self._client._request("PUT", "/rest/api/3/mypreferences", params=params)
        return None

    async def get_locale(self) -> Locale:
        """Get locale"""
        resp = await self._client._request("GET", "/rest/api/3/mypreferences/locale")
        return Locale.model_validate(resp.json())

    async def get_current_user(self, *, expand: str | None = None) -> User:
        """Get current user"""
        params = self._client._build_params(**{"expand": expand})
        resp = await self._client._request("GET", "/rest/api/3/myself", params=params)
        return User.model_validate(resp.json())

    async def remove(
        self, *, account_id: str, username: str | None = None, key: str | None = None
    ) -> None:
        """Delete user"""
        params = self._client._build_params(
            **{"accountId": account_id, "username": username, "key": key}
        )
        await self._client._request("DELETE", "/rest/api/3/user", params=params)
        return None

    async def get(
        self,
        *,
        account_id: str | None = None,
        username: str | None = None,
        key: str | None = None,
        expand: str | None = None,
    ) -> User:
        """Get user"""
        params = self._client._build_params(
            **{"accountId": account_id, "username": username, "key": key, "expand": expand}
        )
        resp = await self._client._request("GET", "/rest/api/3/user", params=params)
        return User.model_validate(resp.json())

    async def create(self, body: NewUserDetails) -> User:
        """Create user"""
        resp = await self._client._request(
            "POST", "/rest/api/3/user", json=body.model_dump(by_alias=True, exclude_none=True)
        )
        return User.model_validate(resp.json())

    async def find_bulk_assignable(
        self,
        *,
        query: str | None = None,
        username: str | None = None,
        account_id: str | None = None,
        project_keys: str,
        start_at: int | None = None,
        max_results: int | None = None,
    ) -> User:
        """Find users assignable to projects"""
        params = self._client._build_params(
            **{
                "query": query,
                "username": username,
                "accountId": account_id,
                "projectKeys": project_keys,
                "startAt": start_at,
                "maxResults": max_results,
            }
        )
        resp = await self._client._request(
            "GET", "/rest/api/3/user/assignable/multiProjectSearch", params=params
        )
        return User.model_validate(resp.json())

    async def find_assignable(
        self,
        *,
        query: str | None = None,
        session_id: str | None = None,
        username: str | None = None,
        account_id: str | None = None,
        project: str | None = None,
        issue_key: str | None = None,
        issue_id: str | None = None,
        start_at: int | None = None,
        max_results: int | None = None,
        action_descriptor_id: int | None = None,
        recommend: bool | None = None,
        account_type: list[str] | None = None,
        app_type: list[str] | None = None,
    ) -> User:
        """Find users assignable to issues"""
        params = self._client._build_params(
            **{
                "query": query,
                "sessionId": session_id,
                "username": username,
                "accountId": account_id,
                "project": project,
                "issueKey": issue_key,
                "issueId": issue_id,
                "startAt": start_at,
                "maxResults": max_results,
                "actionDescriptorId": action_descriptor_id,
                "recommend": recommend,
                "accountType": account_type,
                "appType": app_type,
            }
        )
        resp = await self._client._request(
            "GET", "/rest/api/3/user/assignable/search", params=params
        )
        return User.model_validate(resp.json())

    async def bulk_get(
        self,
        *,
        start_at: int | None = None,
        max_results: int | None = None,
        username: list[str] | None = None,
        key: list[str] | None = None,
        account_id: list[str],
    ) -> PageBeanUser:
        """Bulk get users"""
        params = self._client._build_params(
            **{
                "startAt": start_at,
                "maxResults": max_results,
                "username": username,
                "key": key,
                "accountId": account_id,
            }
        )
        resp = await self._client._request("GET", "/rest/api/3/user/bulk", params=params)
        return PageBeanUser.model_validate(resp.json())

    async def bulk_get_migration(
        self,
        *,
        start_at: int | None = None,
        max_results: int | None = None,
        username: list[str] | None = None,
        key: list[str] | None = None,
    ) -> UserMigration:
        """Get account IDs for users"""
        params = self._client._build_params(
            **{"startAt": start_at, "maxResults": max_results, "username": username, "key": key}
        )
        resp = await self._client._request("GET", "/rest/api/3/user/bulk/migration", params=params)
        return UserMigration.model_validate(resp.json())

    async def reset_columns(
        self, *, account_id: str | None = None, username: str | None = None
    ) -> None:
        """Reset user default columns"""
        params = self._client._build_params(**{"accountId": account_id, "username": username})
        await self._client._request("DELETE", "/rest/api/3/user/columns", params=params)
        return None

    async def get_default_columns(
        self, *, account_id: str | None = None, username: str | None = None
    ) -> ColumnItem:
        """Get user default columns"""
        params = self._client._build_params(**{"accountId": account_id, "username": username})
        resp = await self._client._request("GET", "/rest/api/3/user/columns", params=params)
        return ColumnItem.model_validate(resp.json())

    async def set_columns(self, *, account_id: str | None = None) -> None:
        """Set user default columns"""
        params = self._client._build_params(**{"accountId": account_id})
        await self._client._request("PUT", "/rest/api/3/user/columns", params=params)
        return None

    async def get_email(self, *, account_id: str) -> UnrestrictedUserEmail:
        """Get user email"""
        params = self._client._build_params(**{"accountId": account_id})
        resp = await self._client._request("GET", "/rest/api/3/user/email", params=params)
        return UnrestrictedUserEmail.model_validate(resp.json())

    async def get_email_bulk(self, *, account_id: list[str]) -> UnrestrictedUserEmail:
        """Get user email bulk"""
        params = self._client._build_params(**{"accountId": account_id})
        resp = await self._client._request("GET", "/rest/api/3/user/email/bulk", params=params)
        return UnrestrictedUserEmail.model_validate(resp.json())

    async def get_groups(
        self, *, account_id: str, username: str | None = None, key: str | None = None
    ) -> GroupName:
        """Get user groups"""
        params = self._client._build_params(
            **{"accountId": account_id, "username": username, "key": key}
        )
        resp = await self._client._request("GET", "/rest/api/3/user/groups", params=params)
        return GroupName.model_validate(resp.json())

    async def find_with_permissions(
        self,
        *,
        query: str | None = None,
        username: str | None = None,
        account_id: str | None = None,
        permissions: str,
        issue_key: str | None = None,
        project_key: str | None = None,
        start_at: int | None = None,
        max_results: int | None = None,
    ) -> User:
        """Find users with permissions"""
        params = self._client._build_params(
            **{
                "query": query,
                "username": username,
                "accountId": account_id,
                "permissions": permissions,
                "issueKey": issue_key,
                "projectKey": project_key,
                "startAt": start_at,
                "maxResults": max_results,
            }
        )
        resp = await self._client._request(
            "GET", "/rest/api/3/user/permission/search", params=params
        )
        return User.model_validate(resp.json())

    async def find_for_picker(
        self,
        *,
        query: str,
        max_results: int | None = None,
        show_avatar: bool | None = None,
        exclude: list[str] | None = None,
        exclude_account_ids: list[str] | None = None,
        avatar_size: str | None = None,
        exclude_connect_users: bool | None = None,
    ) -> FoundUsers:
        """Find users for picker"""
        params = self._client._build_params(
            **{
                "query": query,
                "maxResults": max_results,
                "showAvatar": show_avatar,
                "exclude": exclude,
                "excludeAccountIds": exclude_account_ids,
                "avatarSize": avatar_size,
                "excludeConnectUsers": exclude_connect_users,
            }
        )
        resp = await self._client._request("GET", "/rest/api/3/user/picker", params=params)
        return FoundUsers.model_validate(resp.json())

    async def find(
        self,
        *,
        query: str | None = None,
        username: str | None = None,
        account_id: str | None = None,
        start_at: int | None = None,
        max_results: int | None = None,
        property: str | None = None,
    ) -> User:
        """Find users"""
        params = self._client._build_params(
            **{
                "query": query,
                "username": username,
                "accountId": account_id,
                "startAt": start_at,
                "maxResults": max_results,
                "property": property,
            }
        )
        resp = await self._client._request("GET", "/rest/api/3/user/search", params=params)
        return User.model_validate(resp.json())

    async def find_by_query(
        self, *, query: str, start_at: int | None = None, max_results: int | None = None
    ) -> PageBeanUser:
        """Find users by query"""
        params = self._client._build_params(
            **{"query": query, "startAt": start_at, "maxResults": max_results}
        )
        resp = await self._client._request("GET", "/rest/api/3/user/search/query", params=params)
        return PageBeanUser.model_validate(resp.json())

    async def find_keys_by_query(
        self, *, query: str, start_at: int | None = None, max_result: int | None = None
    ) -> PageBeanUserKey:
        """Find user keys by query"""
        params = self._client._build_params(
            **{"query": query, "startAt": start_at, "maxResult": max_result}
        )
        resp = await self._client._request(
            "GET", "/rest/api/3/user/search/query/key", params=params
        )
        return PageBeanUserKey.model_validate(resp.json())

    async def find_with_browse_permission(
        self,
        *,
        query: str | None = None,
        username: str | None = None,
        account_id: str | None = None,
        issue_key: str | None = None,
        project_key: str | None = None,
        start_at: int | None = None,
        max_results: int | None = None,
    ) -> User:
        """Find users with browse permission"""
        params = self._client._build_params(
            **{
                "query": query,
                "username": username,
                "accountId": account_id,
                "issueKey": issue_key,
                "projectKey": project_key,
                "startAt": start_at,
                "maxResults": max_results,
            }
        )
        resp = await self._client._request(
            "GET", "/rest/api/3/user/viewissue/search", params=params
        )
        return User.model_validate(resp.json())

    async def list(self, *, start_at: int | None = None, max_results: int | None = None) -> User:
        """Get all users default"""
        params = self._client._build_params(**{"startAt": start_at, "maxResults": max_results})
        resp = await self._client._request("GET", "/rest/api/3/users", params=params)
        return User.model_validate(resp.json())

    async def list_all(
        self, *, start_at: int | None = None, max_results: int | None = None
    ) -> User:
        """Get all users"""
        params = self._client._build_params(**{"startAt": start_at, "maxResults": max_results})
        resp = await self._client._request("GET", "/rest/api/3/users/search", params=params)
        return User.model_validate(resp.json())
