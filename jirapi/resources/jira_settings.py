"""Resource classes for the Jira settings API group."""

from __future__ import annotations

from jirapi._resource import AsyncAPIResource, SyncAPIResource
from jirapi.models import ApplicationProperty, Configuration, SimpleApplicationPropertyBean


class JiraSettings(SyncAPIResource):
    """Synchronous resource for the Jira settings API group."""

    def get_application_property(
        self,
        *,
        key: str | None = None,
        permission_level: str | None = None,
        key_filter: str | None = None,
    ) -> ApplicationProperty:
        """Get application property"""
        params = self._client._build_params(
            **{"key": key, "permissionLevel": permission_level, "keyFilter": key_filter}
        )
        resp = self._client._request("GET", "/rest/api/3/application-properties", params=params)
        return ApplicationProperty.model_validate(resp.json())

    def get_advanced_settings(self) -> ApplicationProperty:
        """Get advanced settings"""
        resp = self._client._request("GET", "/rest/api/3/application-properties/advanced-settings")
        return ApplicationProperty.model_validate(resp.json())

    def set_application_property(
        self, id_: str, body: SimpleApplicationPropertyBean
    ) -> ApplicationProperty:
        """Set application property"""
        resp = self._client._request(
            "PUT",
            f"/rest/api/3/application-properties/{id_}",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return ApplicationProperty.model_validate(resp.json())

    def get_configuration(self) -> Configuration:
        """Get global settings"""
        resp = self._client._request("GET", "/rest/api/3/configuration")
        return Configuration.model_validate(resp.json())


class AsyncJiraSettings(AsyncAPIResource):
    """Asynchronous resource for the Jira settings API group."""

    async def get_application_property(
        self,
        *,
        key: str | None = None,
        permission_level: str | None = None,
        key_filter: str | None = None,
    ) -> ApplicationProperty:
        """Get application property"""
        params = self._client._build_params(
            **{"key": key, "permissionLevel": permission_level, "keyFilter": key_filter}
        )
        resp = await self._client._request(
            "GET", "/rest/api/3/application-properties", params=params
        )
        return ApplicationProperty.model_validate(resp.json())

    async def get_advanced_settings(self) -> ApplicationProperty:
        """Get advanced settings"""
        resp = await self._client._request(
            "GET", "/rest/api/3/application-properties/advanced-settings"
        )
        return ApplicationProperty.model_validate(resp.json())

    async def set_application_property(
        self, id_: str, body: SimpleApplicationPropertyBean
    ) -> ApplicationProperty:
        """Set application property"""
        resp = await self._client._request(
            "PUT",
            f"/rest/api/3/application-properties/{id_}",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return ApplicationProperty.model_validate(resp.json())

    async def get_configuration(self) -> Configuration:
        """Get global settings"""
        resp = await self._client._request("GET", "/rest/api/3/configuration")
        return Configuration.model_validate(resp.json())
