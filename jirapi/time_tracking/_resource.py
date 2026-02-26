"""Resource classes for time_tracking."""

from __future__ import annotations

from jirapi._resource import AsyncAPIResource, SyncAPIResource
from jirapi.models import TimeTrackingConfiguration, TimeTrackingProvider


class TimeTracking(SyncAPIResource):
    """Synchronous resource for time_tracking."""

    def get_selected_implementation(self) -> TimeTrackingProvider:
        """Get selected time tracking provider"""
        resp = self._client._request("GET", "/rest/api/3/configuration/timetracking")
        return TimeTrackingProvider.model_validate(resp.json())

    def select_implementation(self, body: TimeTrackingProvider) -> None:
        """Select time tracking provider"""
        self._client._request(
            "PUT",
            "/rest/api/3/configuration/timetracking",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    def get_available_implementations(self) -> TimeTrackingProvider:
        """Get all time tracking providers"""
        resp = self._client._request("GET", "/rest/api/3/configuration/timetracking/list")
        return TimeTrackingProvider.model_validate(resp.json())

    def get_shared_configuration(self) -> TimeTrackingConfiguration:
        """Get time tracking settings"""
        resp = self._client._request("GET", "/rest/api/3/configuration/timetracking/options")
        return TimeTrackingConfiguration.model_validate(resp.json())

    def set_shared_configuration(
        self, body: TimeTrackingConfiguration
    ) -> TimeTrackingConfiguration:
        """Set time tracking settings"""
        resp = self._client._request(
            "PUT",
            "/rest/api/3/configuration/timetracking/options",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return TimeTrackingConfiguration.model_validate(resp.json())


class AsyncTimeTracking(AsyncAPIResource):
    """Asynchronous resource for time_tracking."""

    async def get_selected_implementation(self) -> TimeTrackingProvider:
        """Get selected time tracking provider"""
        resp = await self._client._request("GET", "/rest/api/3/configuration/timetracking")
        return TimeTrackingProvider.model_validate(resp.json())

    async def select_implementation(self, body: TimeTrackingProvider) -> None:
        """Select time tracking provider"""
        await self._client._request(
            "PUT",
            "/rest/api/3/configuration/timetracking",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    async def get_available_implementations(self) -> TimeTrackingProvider:
        """Get all time tracking providers"""
        resp = await self._client._request("GET", "/rest/api/3/configuration/timetracking/list")
        return TimeTrackingProvider.model_validate(resp.json())

    async def get_shared_configuration(self) -> TimeTrackingConfiguration:
        """Get time tracking settings"""
        resp = await self._client._request("GET", "/rest/api/3/configuration/timetracking/options")
        return TimeTrackingConfiguration.model_validate(resp.json())

    async def set_shared_configuration(
        self, body: TimeTrackingConfiguration
    ) -> TimeTrackingConfiguration:
        """Set time tracking settings"""
        resp = await self._client._request(
            "PUT",
            "/rest/api/3/configuration/timetracking/options",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return TimeTrackingConfiguration.model_validate(resp.json())
