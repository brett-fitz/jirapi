"""Resource classes for webhooks."""

from __future__ import annotations

from jirapi._resource import AsyncAPIResource, SyncAPIResource
from jirapi.models import (
    ContainerForRegisteredWebhooks,
    ContainerForWebhookIDs,
    FailedWebhooks,
    PageBeanWebhook,
    WebhookRegistrationDetails,
    WebhooksExpirationDate,
)


class Webhooks(SyncAPIResource):
    """Synchronous resource for webhooks."""

    def delete_by_id(self, body: ContainerForWebhookIDs) -> None:
        """Delete webhooks by ID"""
        self._client._request(
            "DELETE", "/rest/api/3/webhook", json=body.model_dump(by_alias=True, exclude_none=True)
        )
        return None

    def get_dynamic_for_app(
        self, *, start_at: int | None = None, max_results: int | None = None
    ) -> PageBeanWebhook:
        """Get dynamic webhooks for app"""
        params = self._client._build_params(**{"startAt": start_at, "maxResults": max_results})
        resp = self._client._request("GET", "/rest/api/3/webhook", params=params)
        return PageBeanWebhook.model_validate(resp.json())

    def register_dynamic(self, body: WebhookRegistrationDetails) -> ContainerForRegisteredWebhooks:
        """Register dynamic webhooks"""
        resp = self._client._request(
            "POST", "/rest/api/3/webhook", json=body.model_dump(by_alias=True, exclude_none=True)
        )
        return ContainerForRegisteredWebhooks.model_validate(resp.json())

    def get_failed(
        self, *, max_results: int | None = None, after: int | None = None
    ) -> FailedWebhooks:
        """Get failed webhooks"""
        params = self._client._build_params(**{"maxResults": max_results, "after": after})
        resp = self._client._request("GET", "/rest/api/3/webhook/failed", params=params)
        return FailedWebhooks.model_validate(resp.json())

    def refresh(self, body: ContainerForWebhookIDs) -> WebhooksExpirationDate:
        """Extend webhook life"""
        resp = self._client._request(
            "PUT",
            "/rest/api/3/webhook/refresh",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return WebhooksExpirationDate.model_validate(resp.json())


class AsyncWebhooks(AsyncAPIResource):
    """Asynchronous resource for webhooks."""

    async def delete_by_id(self, body: ContainerForWebhookIDs) -> None:
        """Delete webhooks by ID"""
        await self._client._request(
            "DELETE", "/rest/api/3/webhook", json=body.model_dump(by_alias=True, exclude_none=True)
        )
        return None

    async def get_dynamic_for_app(
        self, *, start_at: int | None = None, max_results: int | None = None
    ) -> PageBeanWebhook:
        """Get dynamic webhooks for app"""
        params = self._client._build_params(**{"startAt": start_at, "maxResults": max_results})
        resp = await self._client._request("GET", "/rest/api/3/webhook", params=params)
        return PageBeanWebhook.model_validate(resp.json())

    async def register_dynamic(
        self, body: WebhookRegistrationDetails
    ) -> ContainerForRegisteredWebhooks:
        """Register dynamic webhooks"""
        resp = await self._client._request(
            "POST", "/rest/api/3/webhook", json=body.model_dump(by_alias=True, exclude_none=True)
        )
        return ContainerForRegisteredWebhooks.model_validate(resp.json())

    async def get_failed(
        self, *, max_results: int | None = None, after: int | None = None
    ) -> FailedWebhooks:
        """Get failed webhooks"""
        params = self._client._build_params(**{"maxResults": max_results, "after": after})
        resp = await self._client._request("GET", "/rest/api/3/webhook/failed", params=params)
        return FailedWebhooks.model_validate(resp.json())

    async def refresh(self, body: ContainerForWebhookIDs) -> WebhooksExpirationDate:
        """Extend webhook life"""
        resp = await self._client._request(
            "PUT",
            "/rest/api/3/webhook/refresh",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return WebhooksExpirationDate.model_validate(resp.json())
