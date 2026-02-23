"""Resource classes for the Users API group."""

from __future__ import annotations

from jirapi._resource import AsyncAPIResource, SyncAPIResource
from jirapi.models import (
    ColumnItem,
    GroupName,
    NewUserDetails,
    PageBeanUser,
    UnrestrictedUserEmail,
    User,
    UserMigrationBean,
)


class Users(SyncAPIResource):
    """Synchronous resource for the Users API group."""

    def remove_user(
        self, *, account_id: str, username: str | None = None, key: str | None = None
    ) -> None:
        """Delete user"""
        params = self._client._build_params(
            **{"accountId": account_id, "username": username, "key": key}
        )
        self._client._request("DELETE", "/rest/api/3/user", params=params)
        return None

    def get_user(
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

    def create_user(self, body: NewUserDetails) -> User:
        """Create user"""
        resp = self._client._request(
            "POST", "/rest/api/3/user", json=body.model_dump(by_alias=True, exclude_none=True)
        )
        return User.model_validate(resp.json())

    def bulk_get_users(
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

    def bulk_get_users_migration(
        self,
        *,
        start_at: int | None = None,
        max_results: int | None = None,
        username: list[str] | None = None,
        key: list[str] | None = None,
    ) -> UserMigrationBean:
        """Get account IDs for users"""
        params = self._client._build_params(
            **{"startAt": start_at, "maxResults": max_results, "username": username, "key": key}
        )
        resp = self._client._request("GET", "/rest/api/3/user/bulk/migration", params=params)
        return UserMigrationBean.model_validate(resp.json())

    def reset_user_columns(
        self, *, account_id: str | None = None, username: str | None = None
    ) -> None:
        """Reset user default columns"""
        params = self._client._build_params(**{"accountId": account_id, "username": username})
        self._client._request("DELETE", "/rest/api/3/user/columns", params=params)
        return None

    def get_user_default_columns(
        self, *, account_id: str | None = None, username: str | None = None
    ) -> ColumnItem:
        """Get user default columns"""
        params = self._client._build_params(**{"accountId": account_id, "username": username})
        resp = self._client._request("GET", "/rest/api/3/user/columns", params=params)
        return ColumnItem.model_validate(resp.json())

    def set_user_columns(self, *, account_id: str | None = None) -> None:
        """Set user default columns"""
        params = self._client._build_params(**{"accountId": account_id})
        self._client._request("PUT", "/rest/api/3/user/columns", params=params)
        return None

    def get_user_email(self, *, account_id: str) -> UnrestrictedUserEmail:
        """Get user email"""
        params = self._client._build_params(**{"accountId": account_id})
        resp = self._client._request("GET", "/rest/api/3/user/email", params=params)
        return UnrestrictedUserEmail.model_validate(resp.json())

    def get_user_email_bulk(self, *, account_id: list[str]) -> UnrestrictedUserEmail:
        """Get user email bulk"""
        params = self._client._build_params(**{"accountId": account_id})
        resp = self._client._request("GET", "/rest/api/3/user/email/bulk", params=params)
        return UnrestrictedUserEmail.model_validate(resp.json())

    def get_user_groups(
        self, *, account_id: str, username: str | None = None, key: str | None = None
    ) -> GroupName:
        """Get user groups"""
        params = self._client._build_params(
            **{"accountId": account_id, "username": username, "key": key}
        )
        resp = self._client._request("GET", "/rest/api/3/user/groups", params=params)
        return GroupName.model_validate(resp.json())

    def get_all_users_default(
        self, *, start_at: int | None = None, max_results: int | None = None
    ) -> User:
        """Get all users default"""
        params = self._client._build_params(**{"startAt": start_at, "maxResults": max_results})
        resp = self._client._request("GET", "/rest/api/3/users", params=params)
        return User.model_validate(resp.json())

    def get_all_users(self, *, start_at: int | None = None, max_results: int | None = None) -> User:
        """Get all users"""
        params = self._client._build_params(**{"startAt": start_at, "maxResults": max_results})
        resp = self._client._request("GET", "/rest/api/3/users/search", params=params)
        return User.model_validate(resp.json())


class AsyncUsers(AsyncAPIResource):
    """Asynchronous resource for the Users API group."""

    async def remove_user(
        self, *, account_id: str, username: str | None = None, key: str | None = None
    ) -> None:
        """Delete user"""
        params = self._client._build_params(
            **{"accountId": account_id, "username": username, "key": key}
        )
        await self._client._request("DELETE", "/rest/api/3/user", params=params)
        return None

    async def get_user(
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

    async def create_user(self, body: NewUserDetails) -> User:
        """Create user"""
        resp = await self._client._request(
            "POST", "/rest/api/3/user", json=body.model_dump(by_alias=True, exclude_none=True)
        )
        return User.model_validate(resp.json())

    async def bulk_get_users(
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

    async def bulk_get_users_migration(
        self,
        *,
        start_at: int | None = None,
        max_results: int | None = None,
        username: list[str] | None = None,
        key: list[str] | None = None,
    ) -> UserMigrationBean:
        """Get account IDs for users"""
        params = self._client._build_params(
            **{"startAt": start_at, "maxResults": max_results, "username": username, "key": key}
        )
        resp = await self._client._request("GET", "/rest/api/3/user/bulk/migration", params=params)
        return UserMigrationBean.model_validate(resp.json())

    async def reset_user_columns(
        self, *, account_id: str | None = None, username: str | None = None
    ) -> None:
        """Reset user default columns"""
        params = self._client._build_params(**{"accountId": account_id, "username": username})
        await self._client._request("DELETE", "/rest/api/3/user/columns", params=params)
        return None

    async def get_user_default_columns(
        self, *, account_id: str | None = None, username: str | None = None
    ) -> ColumnItem:
        """Get user default columns"""
        params = self._client._build_params(**{"accountId": account_id, "username": username})
        resp = await self._client._request("GET", "/rest/api/3/user/columns", params=params)
        return ColumnItem.model_validate(resp.json())

    async def set_user_columns(self, *, account_id: str | None = None) -> None:
        """Set user default columns"""
        params = self._client._build_params(**{"accountId": account_id})
        await self._client._request("PUT", "/rest/api/3/user/columns", params=params)
        return None

    async def get_user_email(self, *, account_id: str) -> UnrestrictedUserEmail:
        """Get user email"""
        params = self._client._build_params(**{"accountId": account_id})
        resp = await self._client._request("GET", "/rest/api/3/user/email", params=params)
        return UnrestrictedUserEmail.model_validate(resp.json())

    async def get_user_email_bulk(self, *, account_id: list[str]) -> UnrestrictedUserEmail:
        """Get user email bulk"""
        params = self._client._build_params(**{"accountId": account_id})
        resp = await self._client._request("GET", "/rest/api/3/user/email/bulk", params=params)
        return UnrestrictedUserEmail.model_validate(resp.json())

    async def get_user_groups(
        self, *, account_id: str, username: str | None = None, key: str | None = None
    ) -> GroupName:
        """Get user groups"""
        params = self._client._build_params(
            **{"accountId": account_id, "username": username, "key": key}
        )
        resp = await self._client._request("GET", "/rest/api/3/user/groups", params=params)
        return GroupName.model_validate(resp.json())

    async def get_all_users_default(
        self, *, start_at: int | None = None, max_results: int | None = None
    ) -> User:
        """Get all users default"""
        params = self._client._build_params(**{"startAt": start_at, "maxResults": max_results})
        resp = await self._client._request("GET", "/rest/api/3/users", params=params)
        return User.model_validate(resp.json())

    async def get_all_users(
        self, *, start_at: int | None = None, max_results: int | None = None
    ) -> User:
        """Get all users"""
        params = self._client._build_params(**{"startAt": start_at, "maxResults": max_results})
        resp = await self._client._request("GET", "/rest/api/3/users/search", params=params)
        return User.model_validate(resp.json())
