"""Resource classes for users.properties."""

from __future__ import annotations

from jirapi._resource import AsyncAPIResource, SyncAPIResource
from jirapi.models import EntityProperty, PropertyKeys


class UserProperties(SyncAPIResource):
    """Synchronous resource for users.properties."""

    def get_keys(
        self,
        *,
        account_id: str | None = None,
        user_key: str | None = None,
        username: str | None = None,
    ) -> PropertyKeys:
        """Get user property keys"""
        params = self._client._build_params(
            **{"accountId": account_id, "userKey": user_key, "username": username}
        )
        resp = self._client._request("GET", "/rest/api/3/user/properties", params=params)
        return PropertyKeys.model_validate(resp.json())

    def delete(
        self,
        property_key: str,
        *,
        account_id: str | None = None,
        user_key: str | None = None,
        username: str | None = None,
    ) -> None:
        """Delete user property"""
        params = self._client._build_params(
            **{"accountId": account_id, "userKey": user_key, "username": username}
        )
        self._client._request(
            "DELETE", f"/rest/api/3/user/properties/{property_key}", params=params
        )
        return None

    def get(
        self,
        property_key: str,
        *,
        account_id: str | None = None,
        user_key: str | None = None,
        username: str | None = None,
    ) -> EntityProperty:
        """Get user property"""
        params = self._client._build_params(
            **{"accountId": account_id, "userKey": user_key, "username": username}
        )
        resp = self._client._request(
            "GET", f"/rest/api/3/user/properties/{property_key}", params=params
        )
        return EntityProperty.model_validate(resp.json())

    def set(
        self,
        property_key: str,
        *,
        account_id: str | None = None,
        user_key: str | None = None,
        username: str | None = None,
    ) -> None:
        """Set user property"""
        params = self._client._build_params(
            **{"accountId": account_id, "userKey": user_key, "username": username}
        )
        self._client._request("PUT", f"/rest/api/3/user/properties/{property_key}", params=params)
        return None


class AsyncUserProperties(AsyncAPIResource):
    """Asynchronous resource for users.properties."""

    async def get_keys(
        self,
        *,
        account_id: str | None = None,
        user_key: str | None = None,
        username: str | None = None,
    ) -> PropertyKeys:
        """Get user property keys"""
        params = self._client._build_params(
            **{"accountId": account_id, "userKey": user_key, "username": username}
        )
        resp = await self._client._request("GET", "/rest/api/3/user/properties", params=params)
        return PropertyKeys.model_validate(resp.json())

    async def delete(
        self,
        property_key: str,
        *,
        account_id: str | None = None,
        user_key: str | None = None,
        username: str | None = None,
    ) -> None:
        """Delete user property"""
        params = self._client._build_params(
            **{"accountId": account_id, "userKey": user_key, "username": username}
        )
        await self._client._request(
            "DELETE", f"/rest/api/3/user/properties/{property_key}", params=params
        )
        return None

    async def get(
        self,
        property_key: str,
        *,
        account_id: str | None = None,
        user_key: str | None = None,
        username: str | None = None,
    ) -> EntityProperty:
        """Get user property"""
        params = self._client._build_params(
            **{"accountId": account_id, "userKey": user_key, "username": username}
        )
        resp = await self._client._request(
            "GET", f"/rest/api/3/user/properties/{property_key}", params=params
        )
        return EntityProperty.model_validate(resp.json())

    async def set(
        self,
        property_key: str,
        *,
        account_id: str | None = None,
        user_key: str | None = None,
        username: str | None = None,
    ) -> None:
        """Set user property"""
        params = self._client._build_params(
            **{"accountId": account_id, "userKey": user_key, "username": username}
        )
        await self._client._request(
            "PUT", f"/rest/api/3/user/properties/{property_key}", params=params
        )
        return None
