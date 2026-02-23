"""Resource classes for the Announcement banner API group."""

from __future__ import annotations

from jirapi._resource import AsyncAPIResource, SyncAPIResource
from jirapi.models import AnnouncementBannerConfiguration, AnnouncementBannerConfigurationUpdate


class AnnouncementBanner(SyncAPIResource):
    """Synchronous resource for the Announcement banner API group."""

    def get_banner(self) -> AnnouncementBannerConfiguration:
        """Get announcement banner configuration"""
        resp = self._client._request("GET", "/rest/api/3/announcementBanner")
        return AnnouncementBannerConfiguration.model_validate(resp.json())

    def set_banner(self, body: AnnouncementBannerConfigurationUpdate) -> None:
        """Update announcement banner configuration"""
        resp = self._client._request(
            "PUT",
            "/rest/api/3/announcementBanner",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None


class AsyncAnnouncementBanner(AsyncAPIResource):
    """Asynchronous resource for the Announcement banner API group."""

    async def get_banner(self) -> AnnouncementBannerConfiguration:
        """Get announcement banner configuration"""
        resp = await self._client._request("GET", "/rest/api/3/announcementBanner")
        return AnnouncementBannerConfiguration.model_validate(resp.json())

    async def set_banner(self, body: AnnouncementBannerConfigurationUpdate) -> None:
        """Update announcement banner configuration"""
        resp = await self._client._request(
            "PUT",
            "/rest/api/3/announcementBanner",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None
