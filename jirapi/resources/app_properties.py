"""Resource classes for the App properties API group."""

from __future__ import annotations

from jirapi._resource import AsyncAPIResource, SyncAPIResource
from jirapi.models import EntityProperty, OperationMessage, PropertyKeys


class AppProperties(SyncAPIResource):
    """Synchronous resource for the App properties API group."""

    def get_addon_properties_get(self, addon_key: str) -> PropertyKeys:
        """Get app properties"""
        resp = self._client._request(
            "GET", f"/rest/atlassian-connect/1/addons/{addon_key}/properties"
        )
        return PropertyKeys.model_validate(resp.json())

    def delete_addon_property_delete(self, addon_key: str, property_key: str) -> None:
        """Delete app property"""
        resp = self._client._request(
            "DELETE", f"/rest/atlassian-connect/1/addons/{addon_key}/properties/{property_key}"
        )
        return None

    def get_addon_property_get(self, addon_key: str, property_key: str) -> EntityProperty:
        """Get app property"""
        resp = self._client._request(
            "GET", f"/rest/atlassian-connect/1/addons/{addon_key}/properties/{property_key}"
        )
        return EntityProperty.model_validate(resp.json())

    def put_addon_property_put(self, addon_key: str, property_key: str) -> OperationMessage:
        """Set app property"""
        resp = self._client._request(
            "PUT", f"/rest/atlassian-connect/1/addons/{addon_key}/properties/{property_key}"
        )
        return OperationMessage.model_validate(resp.json())

    def get_forge_app_property_keys(self) -> None:
        """Get app property keys (Forge)"""
        resp = self._client._request("GET", "/rest/forge/1/app/properties")
        return None

    def delete_forge_app_property(self, property_key: str) -> None:
        """Delete app property (Forge)"""
        resp = self._client._request("DELETE", f"/rest/forge/1/app/properties/{property_key}")
        return None

    def get_forge_app_property(self, property_key: str) -> None:
        """Get app property (Forge)"""
        resp = self._client._request("GET", f"/rest/forge/1/app/properties/{property_key}")
        return None

    def put_forge_app_property(self, property_key: str) -> OperationMessage:
        """Set app property (Forge)"""
        resp = self._client._request("PUT", f"/rest/forge/1/app/properties/{property_key}")
        return OperationMessage.model_validate(resp.json())


class AsyncAppProperties(AsyncAPIResource):
    """Asynchronous resource for the App properties API group."""

    async def get_addon_properties_get(self, addon_key: str) -> PropertyKeys:
        """Get app properties"""
        resp = await self._client._request(
            "GET", f"/rest/atlassian-connect/1/addons/{addon_key}/properties"
        )
        return PropertyKeys.model_validate(resp.json())

    async def delete_addon_property_delete(self, addon_key: str, property_key: str) -> None:
        """Delete app property"""
        resp = await self._client._request(
            "DELETE", f"/rest/atlassian-connect/1/addons/{addon_key}/properties/{property_key}"
        )
        return None

    async def get_addon_property_get(self, addon_key: str, property_key: str) -> EntityProperty:
        """Get app property"""
        resp = await self._client._request(
            "GET", f"/rest/atlassian-connect/1/addons/{addon_key}/properties/{property_key}"
        )
        return EntityProperty.model_validate(resp.json())

    async def put_addon_property_put(self, addon_key: str, property_key: str) -> OperationMessage:
        """Set app property"""
        resp = await self._client._request(
            "PUT", f"/rest/atlassian-connect/1/addons/{addon_key}/properties/{property_key}"
        )
        return OperationMessage.model_validate(resp.json())

    async def get_forge_app_property_keys(self) -> None:
        """Get app property keys (Forge)"""
        resp = await self._client._request("GET", "/rest/forge/1/app/properties")
        return None

    async def delete_forge_app_property(self, property_key: str) -> None:
        """Delete app property (Forge)"""
        resp = await self._client._request("DELETE", f"/rest/forge/1/app/properties/{property_key}")
        return None

    async def get_forge_app_property(self, property_key: str) -> None:
        """Get app property (Forge)"""
        resp = await self._client._request("GET", f"/rest/forge/1/app/properties/{property_key}")
        return None

    async def put_forge_app_property(self, property_key: str) -> OperationMessage:
        """Set app property (Forge)"""
        resp = await self._client._request("PUT", f"/rest/forge/1/app/properties/{property_key}")
        return OperationMessage.model_validate(resp.json())
