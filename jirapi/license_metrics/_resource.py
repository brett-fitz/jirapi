"""Resource classes for license_metrics."""

from __future__ import annotations

from jirapi._resource import AsyncAPIResource, SyncAPIResource
from jirapi.models import License, LicenseMetric


class LicenseMetrics(SyncAPIResource):
    """Synchronous resource for license_metrics."""

    def get(self) -> License:
        """Get license"""
        resp = self._client._request("GET", "/rest/api/3/instance/license")
        return License.model_validate(resp.json())

    def get_approximate_count(self) -> LicenseMetric:
        """Get approximate license count"""
        resp = self._client._request("GET", "/rest/api/3/license/approximateLicenseCount")
        return LicenseMetric.model_validate(resp.json())

    def get_approximate_application_count(self, application_key: str) -> LicenseMetric:
        """Get approximate application license count"""
        resp = self._client._request(
            "GET", f"/rest/api/3/license/approximateLicenseCount/product/{application_key}"
        )
        return LicenseMetric.model_validate(resp.json())


class AsyncLicenseMetrics(AsyncAPIResource):
    """Asynchronous resource for license_metrics."""

    async def get(self) -> License:
        """Get license"""
        resp = await self._client._request("GET", "/rest/api/3/instance/license")
        return License.model_validate(resp.json())

    async def get_approximate_count(self) -> LicenseMetric:
        """Get approximate license count"""
        resp = await self._client._request("GET", "/rest/api/3/license/approximateLicenseCount")
        return LicenseMetric.model_validate(resp.json())

    async def get_approximate_application_count(self, application_key: str) -> LicenseMetric:
        """Get approximate application license count"""
        resp = await self._client._request(
            "GET", f"/rest/api/3/license/approximateLicenseCount/product/{application_key}"
        )
        return LicenseMetric.model_validate(resp.json())
