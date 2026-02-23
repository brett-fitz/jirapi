"""Resource classes for the Issue attachments API group."""

from __future__ import annotations

from jirapi._resource import AsyncAPIResource, SyncAPIResource
from jirapi.models import (
    Attachment,
    AttachmentArchiveImpl,
    AttachmentArchiveMetadataReadable,
    AttachmentMetadata,
    AttachmentSettings,
)


class IssueAttachments(SyncAPIResource):
    """Synchronous resource for the Issue attachments API group."""

    def get_attachment_content(self, id_: str, *, redirect: bool | None = None) -> None:
        """Get attachment content"""
        params = self._client._build_params(**{"redirect": redirect})
        self._client._request("GET", f"/rest/api/3/attachment/content/{id_}", params=params)
        return None

    def get_attachment_meta(self) -> AttachmentSettings:
        """Get Jira attachment settings"""
        resp = self._client._request("GET", "/rest/api/3/attachment/meta")
        return AttachmentSettings.model_validate(resp.json())

    def get_attachment_thumbnail(
        self,
        id_: str,
        *,
        redirect: bool | None = None,
        fallback_to_default: bool | None = None,
        width: int | None = None,
        height: int | None = None,
    ) -> None:
        """Get attachment thumbnail"""
        params = self._client._build_params(
            **{
                "redirect": redirect,
                "fallbackToDefault": fallback_to_default,
                "width": width,
                "height": height,
            }
        )
        self._client._request("GET", f"/rest/api/3/attachment/thumbnail/{id_}", params=params)
        return None

    def remove_attachment(self, id_: str) -> None:
        """Delete attachment"""
        self._client._request("DELETE", f"/rest/api/3/attachment/{id_}")
        return None

    def get_attachment(self, id_: str) -> AttachmentMetadata:
        """Get attachment metadata"""
        resp = self._client._request("GET", f"/rest/api/3/attachment/{id_}")
        return AttachmentMetadata.model_validate(resp.json())

    def expand_attachment_for_humans(self, id_: str) -> AttachmentArchiveMetadataReadable:
        """Get all metadata for an expanded attachment"""
        resp = self._client._request("GET", f"/rest/api/3/attachment/{id_}/expand/human")
        return AttachmentArchiveMetadataReadable.model_validate(resp.json())

    def expand_attachment_for_machines(self, id_: str) -> AttachmentArchiveImpl:
        """Get contents metadata for an expanded attachment"""
        resp = self._client._request("GET", f"/rest/api/3/attachment/{id_}/expand/raw")
        return AttachmentArchiveImpl.model_validate(resp.json())

    def add_attachment(self, issue_id_or_key: str) -> Attachment:
        """Add attachment"""
        resp = self._client._request("POST", f"/rest/api/3/issue/{issue_id_or_key}/attachments")
        return Attachment.model_validate(resp.json())


class AsyncIssueAttachments(AsyncAPIResource):
    """Asynchronous resource for the Issue attachments API group."""

    async def get_attachment_content(self, id_: str, *, redirect: bool | None = None) -> None:
        """Get attachment content"""
        params = self._client._build_params(**{"redirect": redirect})
        await self._client._request("GET", f"/rest/api/3/attachment/content/{id_}", params=params)
        return None

    async def get_attachment_meta(self) -> AttachmentSettings:
        """Get Jira attachment settings"""
        resp = await self._client._request("GET", "/rest/api/3/attachment/meta")
        return AttachmentSettings.model_validate(resp.json())

    async def get_attachment_thumbnail(
        self,
        id_: str,
        *,
        redirect: bool | None = None,
        fallback_to_default: bool | None = None,
        width: int | None = None,
        height: int | None = None,
    ) -> None:
        """Get attachment thumbnail"""
        params = self._client._build_params(
            **{
                "redirect": redirect,
                "fallbackToDefault": fallback_to_default,
                "width": width,
                "height": height,
            }
        )
        await self._client._request("GET", f"/rest/api/3/attachment/thumbnail/{id_}", params=params)
        return None

    async def remove_attachment(self, id_: str) -> None:
        """Delete attachment"""
        await self._client._request("DELETE", f"/rest/api/3/attachment/{id_}")
        return None

    async def get_attachment(self, id_: str) -> AttachmentMetadata:
        """Get attachment metadata"""
        resp = await self._client._request("GET", f"/rest/api/3/attachment/{id_}")
        return AttachmentMetadata.model_validate(resp.json())

    async def expand_attachment_for_humans(self, id_: str) -> AttachmentArchiveMetadataReadable:
        """Get all metadata for an expanded attachment"""
        resp = await self._client._request("GET", f"/rest/api/3/attachment/{id_}/expand/human")
        return AttachmentArchiveMetadataReadable.model_validate(resp.json())

    async def expand_attachment_for_machines(self, id_: str) -> AttachmentArchiveImpl:
        """Get contents metadata for an expanded attachment"""
        resp = await self._client._request("GET", f"/rest/api/3/attachment/{id_}/expand/raw")
        return AttachmentArchiveImpl.model_validate(resp.json())

    async def add_attachment(self, issue_id_or_key: str) -> Attachment:
        """Add attachment"""
        resp = await self._client._request(
            "POST", f"/rest/api/3/issue/{issue_id_or_key}/attachments"
        )
        return Attachment.model_validate(resp.json())
