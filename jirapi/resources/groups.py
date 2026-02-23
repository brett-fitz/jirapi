"""Resource classes for the Groups API group."""

from __future__ import annotations

from jirapi._resource import AsyncAPIResource, SyncAPIResource
from jirapi.models import (
    AddGroupBean,
    FoundGroups,
    Group,
    PageBeanGroupDetails,
    PageBeanUserDetails,
    UpdateUserToGroupBean,
)


class Groups(SyncAPIResource):
    """Synchronous resource for the Groups API group."""

    def remove_group(
        self,
        *,
        groupname: str | None = None,
        group_id: str | None = None,
        swap_group: str | None = None,
        swap_group_id: str | None = None,
    ) -> None:
        """Remove group"""
        params = self._client._build_params(
            **{
                "groupname": groupname,
                "groupId": group_id,
                "swapGroup": swap_group,
                "swapGroupId": swap_group_id,
            }
        )
        self._client._request("DELETE", "/rest/api/3/group", params=params)
        return None

    def create_group(self, body: AddGroupBean) -> Group:
        """Create group"""
        resp = self._client._request(
            "POST", "/rest/api/3/group", json=body.model_dump(by_alias=True, exclude_none=True)
        )
        return Group.model_validate(resp.json())

    def bulk_get_groups(
        self,
        *,
        start_at: int | None = None,
        max_results: int | None = None,
        group_id: list[str] | None = None,
        group_name: list[str] | None = None,
        access_type: str | None = None,
        application_key: str | None = None,
    ) -> PageBeanGroupDetails:
        """Bulk get groups"""
        params = self._client._build_params(
            **{
                "startAt": start_at,
                "maxResults": max_results,
                "groupId": group_id,
                "groupName": group_name,
                "accessType": access_type,
                "applicationKey": application_key,
            }
        )
        resp = self._client._request("GET", "/rest/api/3/group/bulk", params=params)
        return PageBeanGroupDetails.model_validate(resp.json())

    def get_users_from_group(
        self,
        *,
        groupname: str | None = None,
        group_id: str | None = None,
        include_inactive_users: bool | None = None,
        start_at: int | None = None,
        max_results: int | None = None,
    ) -> PageBeanUserDetails:
        """Get users from group"""
        params = self._client._build_params(
            **{
                "groupname": groupname,
                "groupId": group_id,
                "includeInactiveUsers": include_inactive_users,
                "startAt": start_at,
                "maxResults": max_results,
            }
        )
        resp = self._client._request("GET", "/rest/api/3/group/member", params=params)
        return PageBeanUserDetails.model_validate(resp.json())

    def remove_user_from_group(
        self,
        *,
        groupname: str | None = None,
        group_id: str | None = None,
        username: str | None = None,
        account_id: str,
    ) -> None:
        """Remove user from group"""
        params = self._client._build_params(
            **{
                "groupname": groupname,
                "groupId": group_id,
                "username": username,
                "accountId": account_id,
            }
        )
        self._client._request("DELETE", "/rest/api/3/group/user", params=params)
        return None

    def add_user_to_group(
        self,
        body: UpdateUserToGroupBean,
        *,
        groupname: str | None = None,
        group_id: str | None = None,
    ) -> Group:
        """Add user to group"""
        params = self._client._build_params(**{"groupname": groupname, "groupId": group_id})
        resp = self._client._request(
            "POST",
            "/rest/api/3/group/user",
            params=params,
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return Group.model_validate(resp.json())

    def find_groups(
        self,
        *,
        account_id: str | None = None,
        query: str | None = None,
        exclude: list[str] | None = None,
        exclude_id: list[str] | None = None,
        max_results: int | None = None,
        case_insensitive: bool | None = None,
        user_name: str | None = None,
    ) -> FoundGroups:
        """Find groups"""
        params = self._client._build_params(
            **{
                "accountId": account_id,
                "query": query,
                "exclude": exclude,
                "excludeId": exclude_id,
                "maxResults": max_results,
                "caseInsensitive": case_insensitive,
                "userName": user_name,
            }
        )
        resp = self._client._request("GET", "/rest/api/3/groups/picker", params=params)
        return FoundGroups.model_validate(resp.json())


class AsyncGroups(AsyncAPIResource):
    """Asynchronous resource for the Groups API group."""

    async def remove_group(
        self,
        *,
        groupname: str | None = None,
        group_id: str | None = None,
        swap_group: str | None = None,
        swap_group_id: str | None = None,
    ) -> None:
        """Remove group"""
        params = self._client._build_params(
            **{
                "groupname": groupname,
                "groupId": group_id,
                "swapGroup": swap_group,
                "swapGroupId": swap_group_id,
            }
        )
        await self._client._request("DELETE", "/rest/api/3/group", params=params)
        return None

    async def create_group(self, body: AddGroupBean) -> Group:
        """Create group"""
        resp = await self._client._request(
            "POST", "/rest/api/3/group", json=body.model_dump(by_alias=True, exclude_none=True)
        )
        return Group.model_validate(resp.json())

    async def bulk_get_groups(
        self,
        *,
        start_at: int | None = None,
        max_results: int | None = None,
        group_id: list[str] | None = None,
        group_name: list[str] | None = None,
        access_type: str | None = None,
        application_key: str | None = None,
    ) -> PageBeanGroupDetails:
        """Bulk get groups"""
        params = self._client._build_params(
            **{
                "startAt": start_at,
                "maxResults": max_results,
                "groupId": group_id,
                "groupName": group_name,
                "accessType": access_type,
                "applicationKey": application_key,
            }
        )
        resp = await self._client._request("GET", "/rest/api/3/group/bulk", params=params)
        return PageBeanGroupDetails.model_validate(resp.json())

    async def get_users_from_group(
        self,
        *,
        groupname: str | None = None,
        group_id: str | None = None,
        include_inactive_users: bool | None = None,
        start_at: int | None = None,
        max_results: int | None = None,
    ) -> PageBeanUserDetails:
        """Get users from group"""
        params = self._client._build_params(
            **{
                "groupname": groupname,
                "groupId": group_id,
                "includeInactiveUsers": include_inactive_users,
                "startAt": start_at,
                "maxResults": max_results,
            }
        )
        resp = await self._client._request("GET", "/rest/api/3/group/member", params=params)
        return PageBeanUserDetails.model_validate(resp.json())

    async def remove_user_from_group(
        self,
        *,
        groupname: str | None = None,
        group_id: str | None = None,
        username: str | None = None,
        account_id: str,
    ) -> None:
        """Remove user from group"""
        params = self._client._build_params(
            **{
                "groupname": groupname,
                "groupId": group_id,
                "username": username,
                "accountId": account_id,
            }
        )
        await self._client._request("DELETE", "/rest/api/3/group/user", params=params)
        return None

    async def add_user_to_group(
        self,
        body: UpdateUserToGroupBean,
        *,
        groupname: str | None = None,
        group_id: str | None = None,
    ) -> Group:
        """Add user to group"""
        params = self._client._build_params(**{"groupname": groupname, "groupId": group_id})
        resp = await self._client._request(
            "POST",
            "/rest/api/3/group/user",
            params=params,
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return Group.model_validate(resp.json())

    async def find_groups(
        self,
        *,
        account_id: str | None = None,
        query: str | None = None,
        exclude: list[str] | None = None,
        exclude_id: list[str] | None = None,
        max_results: int | None = None,
        case_insensitive: bool | None = None,
        user_name: str | None = None,
    ) -> FoundGroups:
        """Find groups"""
        params = self._client._build_params(
            **{
                "accountId": account_id,
                "query": query,
                "exclude": exclude,
                "excludeId": exclude_id,
                "maxResults": max_results,
                "caseInsensitive": case_insensitive,
                "userName": user_name,
            }
        )
        resp = await self._client._request("GET", "/rest/api/3/groups/picker", params=params)
        return FoundGroups.model_validate(resp.json())
