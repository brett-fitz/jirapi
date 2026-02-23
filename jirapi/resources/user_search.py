"""Resource classes for the User search API group."""

from __future__ import annotations

from jirapi._resource import AsyncAPIResource, SyncAPIResource
from jirapi.models import FoundUsers, PageBeanUser, PageBeanUserKey, User


class UserSearch(SyncAPIResource):
    """Synchronous resource for the User search API group."""

    def find_bulk_assignable_users(
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

    def find_assignable_users(
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

    def find_users_with_all_permissions(
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

    def find_users_for_picker(
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

    def find_users(
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

    def find_users_by_query(
        self, *, query: str, start_at: int | None = None, max_results: int | None = None
    ) -> PageBeanUser:
        """Find users by query"""
        params = self._client._build_params(
            **{"query": query, "startAt": start_at, "maxResults": max_results}
        )
        resp = self._client._request("GET", "/rest/api/3/user/search/query", params=params)
        return PageBeanUser.model_validate(resp.json())

    def find_user_keys_by_query(
        self, *, query: str, start_at: int | None = None, max_result: int | None = None
    ) -> PageBeanUserKey:
        """Find user keys by query"""
        params = self._client._build_params(
            **{"query": query, "startAt": start_at, "maxResult": max_result}
        )
        resp = self._client._request("GET", "/rest/api/3/user/search/query/key", params=params)
        return PageBeanUserKey.model_validate(resp.json())

    def find_users_with_browse_permission(
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


class AsyncUserSearch(AsyncAPIResource):
    """Asynchronous resource for the User search API group."""

    async def find_bulk_assignable_users(
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

    async def find_assignable_users(
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

    async def find_users_with_all_permissions(
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

    async def find_users_for_picker(
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

    async def find_users(
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

    async def find_users_by_query(
        self, *, query: str, start_at: int | None = None, max_results: int | None = None
    ) -> PageBeanUser:
        """Find users by query"""
        params = self._client._build_params(
            **{"query": query, "startAt": start_at, "maxResults": max_results}
        )
        resp = await self._client._request("GET", "/rest/api/3/user/search/query", params=params)
        return PageBeanUser.model_validate(resp.json())

    async def find_user_keys_by_query(
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

    async def find_users_with_browse_permission(
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
