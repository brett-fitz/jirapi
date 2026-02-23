"""Resource classes for the Issue notification schemes API group."""

from __future__ import annotations

from jirapi._resource import AsyncAPIResource, SyncAPIResource
from jirapi.models import (
    AddNotificationsDetails,
    CreateNotificationSchemeDetails,
    NotificationScheme,
    NotificationSchemeId,
    PageBeanNotificationScheme,
    PageBeanNotificationSchemeAndProjectMappingJsonBean,
    UpdateNotificationSchemeDetails,
)


class IssueNotificationSchemes(SyncAPIResource):
    """Synchronous resource for the Issue notification schemes API group."""

    def get_notification_schemes(
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

    def create_notification_scheme(
        self, body: CreateNotificationSchemeDetails
    ) -> NotificationSchemeId:
        """Create notification scheme"""
        resp = self._client._request(
            "POST",
            "/rest/api/3/notificationscheme",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return NotificationSchemeId.model_validate(resp.json())

    def get_notification_scheme_to_project_mappings(
        self,
        *,
        start_at: str | None = None,
        max_results: str | None = None,
        notification_scheme_id: list[str] | None = None,
        project_id: list[str] | None = None,
    ) -> PageBeanNotificationSchemeAndProjectMappingJsonBean:
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
        return PageBeanNotificationSchemeAndProjectMappingJsonBean.model_validate(resp.json())

    def get_notification_scheme(self, id_: str, *, expand: str | None = None) -> NotificationScheme:
        """Get notification scheme"""
        params = self._client._build_params(**{"expand": expand})
        resp = self._client._request("GET", f"/rest/api/3/notificationscheme/{id_}", params=params)
        return NotificationScheme.model_validate(resp.json())

    def update_notification_scheme(self, id_: str, body: UpdateNotificationSchemeDetails) -> None:
        """Update notification scheme"""
        resp = self._client._request(
            "PUT",
            f"/rest/api/3/notificationscheme/{id_}",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    def add_notifications(self, id_: str, body: AddNotificationsDetails) -> None:
        """Add notifications to notification scheme"""
        resp = self._client._request(
            "PUT",
            f"/rest/api/3/notificationscheme/{id_}/notification",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    def delete_notification_scheme(self, notification_scheme_id: str) -> None:
        """Delete notification scheme"""
        resp = self._client._request(
            "DELETE", f"/rest/api/3/notificationscheme/{notification_scheme_id}"
        )
        return None

    def remove_notification_from_notification_scheme(
        self, notification_scheme_id: str, notification_id: str
    ) -> None:
        """Remove notification from notification scheme"""
        resp = self._client._request(
            "DELETE",
            f"/rest/api/3/notificationscheme/{notification_scheme_id}/notification/{notification_id}",
        )
        return None


class AsyncIssueNotificationSchemes(AsyncAPIResource):
    """Asynchronous resource for the Issue notification schemes API group."""

    async def get_notification_schemes(
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

    async def create_notification_scheme(
        self, body: CreateNotificationSchemeDetails
    ) -> NotificationSchemeId:
        """Create notification scheme"""
        resp = await self._client._request(
            "POST",
            "/rest/api/3/notificationscheme",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return NotificationSchemeId.model_validate(resp.json())

    async def get_notification_scheme_to_project_mappings(
        self,
        *,
        start_at: str | None = None,
        max_results: str | None = None,
        notification_scheme_id: list[str] | None = None,
        project_id: list[str] | None = None,
    ) -> PageBeanNotificationSchemeAndProjectMappingJsonBean:
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
        return PageBeanNotificationSchemeAndProjectMappingJsonBean.model_validate(resp.json())

    async def get_notification_scheme(
        self, id_: str, *, expand: str | None = None
    ) -> NotificationScheme:
        """Get notification scheme"""
        params = self._client._build_params(**{"expand": expand})
        resp = await self._client._request(
            "GET", f"/rest/api/3/notificationscheme/{id_}", params=params
        )
        return NotificationScheme.model_validate(resp.json())

    async def update_notification_scheme(
        self, id_: str, body: UpdateNotificationSchemeDetails
    ) -> None:
        """Update notification scheme"""
        resp = await self._client._request(
            "PUT",
            f"/rest/api/3/notificationscheme/{id_}",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    async def add_notifications(self, id_: str, body: AddNotificationsDetails) -> None:
        """Add notifications to notification scheme"""
        resp = await self._client._request(
            "PUT",
            f"/rest/api/3/notificationscheme/{id_}/notification",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    async def delete_notification_scheme(self, notification_scheme_id: str) -> None:
        """Delete notification scheme"""
        resp = await self._client._request(
            "DELETE", f"/rest/api/3/notificationscheme/{notification_scheme_id}"
        )
        return None

    async def remove_notification_from_notification_scheme(
        self, notification_scheme_id: str, notification_id: str
    ) -> None:
        """Remove notification from notification scheme"""
        resp = await self._client._request(
            "DELETE",
            f"/rest/api/3/notificationscheme/{notification_scheme_id}/notification/{notification_id}",
        )
        return None
