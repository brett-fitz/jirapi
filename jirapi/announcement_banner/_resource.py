"""Resource classes for announcement_banner."""

from __future__ import annotations

from jirapi._resource import AsyncAPIResource, SyncAPIResource
from jirapi.models import AnnouncementBannerConfiguration, AnnouncementBannerConfigurationUpdate


class AnnouncementBanner(SyncAPIResource):
    """Synchronous resource for announcement_banner."""

    def get(self) -> AnnouncementBannerConfiguration:
        """Get announcement banner configuration"""
        resp = self._client._request("GET", "/rest/api/3/announcementBanner")
        return AnnouncementBannerConfiguration.model_validate(resp.json())

    def set(self, body: AnnouncementBannerConfigurationUpdate) -> None:
        """Update announcement banner configuration"""
        self._client._request(
            "PUT",
            "/rest/api/3/announcementBanner",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None


class AsyncAnnouncementBanner(AsyncAPIResource):
    """Asynchronous resource for announcement_banner."""

    async def get(self) -> AnnouncementBannerConfiguration:
        """Get announcement banner configuration"""
        resp = await self._client._request("GET", "/rest/api/3/announcementBanner")
        return AnnouncementBannerConfiguration.model_validate(resp.json())

    async def set(self, body: AnnouncementBannerConfigurationUpdate) -> None:
        """Update announcement banner configuration"""
        await self._client._request(
            "PUT",
            "/rest/api/3/announcementBanner",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None
