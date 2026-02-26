"""Resource classes for notification_schemes."""

from __future__ import annotations

from jirapi._resource import AsyncAPIResource, SyncAPIResource
from jirapi.models import (
    AddNotificationsDetails,
    CreateNotificationSchemeDetails,
    NotificationScheme,
    NotificationSchemeId,
    PageBeanNotificationScheme,
    PageBeanNotificationSchemeAndProjectMappingJson,
    UpdateNotificationSchemeDetails,
)


class NotificationSchemes(SyncAPIResource):
    """Synchronous resource for notification_schemes."""

    def list(
        self,
        *,
        start_at: str | None = None,
        max_results: str | None = None,
        id_: list[str] | None = None,
        project_id: list[str] | None = None,
        only_default: bool | None = None,
        expand: str | None = None,
    ) -> PageBeanNotificationScheme:
        """Get notification schemes paginated"""
        params = self._client._build_params(
            **{
                "startAt": start_at,
                "maxResults": max_results,
                "id": id_,
                "projectId": project_id,
                "onlyDefault": only_default,
                "expand": expand,
            }
        )
        resp = self._client._request("GET", "/rest/api/3/notificationscheme", params=params)
        return PageBeanNotificationScheme.model_validate(resp.json())

    def create(self, body: CreateNotificationSchemeDetails) -> NotificationSchemeId:
        """Create notification scheme"""
        resp = self._client._request(
            "POST",
            "/rest/api/3/notificationscheme",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return NotificationSchemeId.model_validate(resp.json())

    def get_project_mappings(
        self,
        *,
        start_at: str | None = None,
        max_results: str | None = None,
        notification_scheme_id: list[str] | None = None,
        project_id: list[str] | None = None,
    ) -> PageBeanNotificationSchemeAndProjectMappingJson:
        """Get projects using notification schemes paginated"""
        params = self._client._build_params(
            **{
                "startAt": start_at,
                "maxResults": max_results,
                "notificationSchemeId": notification_scheme_id,
                "projectId": project_id,
            }
        )
        resp = self._client._request("GET", "/rest/api/3/notificationscheme/project", params=params)
        return PageBeanNotificationSchemeAndProjectMappingJson.model_validate(resp.json())

    def get(self, id_: str, *, expand: str | None = None) -> NotificationScheme:
        """Get notification scheme"""
        params = self._client._build_params(**{"expand": expand})
        resp = self._client._request("GET", f"/rest/api/3/notificationscheme/{id_}", params=params)
        return NotificationScheme.model_validate(resp.json())

    def update(self, id_: str, body: UpdateNotificationSchemeDetails) -> None:
        """Update notification scheme"""
        self._client._request(
            "PUT",
            f"/rest/api/3/notificationscheme/{id_}",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    def add_notifications(self, id_: str, body: AddNotificationsDetails) -> None:
        """Add notifications to notification scheme"""
        self._client._request(
            "PUT",
            f"/rest/api/3/notificationscheme/{id_}/notification",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    def delete(self, notification_scheme_id: str) -> None:
        """Delete notification scheme"""
        self._client._request("DELETE", f"/rest/api/3/notificationscheme/{notification_scheme_id}")
        return None

    def remove_notification(self, notification_scheme_id: str, notification_id: str) -> None:
        """Remove notification from notification scheme"""
        self._client._request(
            "DELETE",
            f"/rest/api/3/notificationscheme/{notification_scheme_id}/notification/{notification_id}",
        )
        return None


class AsyncNotificationSchemes(AsyncAPIResource):
    """Asynchronous resource for notification_schemes."""

    async def list(
        self,
        *,
        start_at: str | None = None,
        max_results: str | None = None,
        id_: list[str] | None = None,
        project_id: list[str] | None = None,
        only_default: bool | None = None,
        expand: str | None = None,
    ) -> PageBeanNotificationScheme:
        """Get notification schemes paginated"""
        params = self._client._build_params(
            **{
                "startAt": start_at,
                "maxResults": max_results,
                "id": id_,
                "projectId": project_id,
                "onlyDefault": only_default,
                "expand": expand,
            }
        )
        resp = await self._client._request("GET", "/rest/api/3/notificationscheme", params=params)
        return PageBeanNotificationScheme.model_validate(resp.json())

    async def create(self, body: CreateNotificationSchemeDetails) -> NotificationSchemeId:
        """Create notification scheme"""
        resp = await self._client._request(
            "POST",
            "/rest/api/3/notificationscheme",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return NotificationSchemeId.model_validate(resp.json())

    async def get_project_mappings(
        self,
        *,
        start_at: str | None = None,
        max_results: str | None = None,
        notification_scheme_id: list[str] | None = None,
        project_id: list[str] | None = None,
    ) -> PageBeanNotificationSchemeAndProjectMappingJson:
        """Get projects using notification schemes paginated"""
        params = self._client._build_params(
            **{
                "startAt": start_at,
                "maxResults": max_results,
                "notificationSchemeId": notification_scheme_id,
                "projectId": project_id,
            }
        )
        resp = await self._client._request(
            "GET", "/rest/api/3/notificationscheme/project", params=params
        )
        return PageBeanNotificationSchemeAndProjectMappingJson.model_validate(resp.json())

    async def get(self, id_: str, *, expand: str | None = None) -> NotificationScheme:
        """Get notification scheme"""
        params = self._client._build_params(**{"expand": expand})
        resp = await self._client._request(
            "GET", f"/rest/api/3/notificationscheme/{id_}", params=params
        )
        return NotificationScheme.model_validate(resp.json())

    async def update(self, id_: str, body: UpdateNotificationSchemeDetails) -> None:
        """Update notification scheme"""
        await self._client._request(
            "PUT",
            f"/rest/api/3/notificationscheme/{id_}",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    async def add_notifications(self, id_: str, body: AddNotificationsDetails) -> None:
        """Add notifications to notification scheme"""
        await self._client._request(
            "PUT",
            f"/rest/api/3/notificationscheme/{id_}/notification",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    async def delete(self, notification_scheme_id: str) -> None:
        """Delete notification scheme"""
        await self._client._request(
            "DELETE", f"/rest/api/3/notificationscheme/{notification_scheme_id}"
        )
        return None

    async def remove_notification(self, notification_scheme_id: str, notification_id: str) -> None:
        """Remove notification from notification scheme"""
        await self._client._request(
            "DELETE",
            f"/rest/api/3/notificationscheme/{notification_scheme_id}/notification/{notification_id}",
        )
        return None
