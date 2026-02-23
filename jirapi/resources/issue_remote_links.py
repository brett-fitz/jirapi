"""Resource classes for the Issue remote links API group."""

from __future__ import annotations

from jirapi._resource import AsyncAPIResource, SyncAPIResource
from jirapi.models import RemoteIssueLink, RemoteIssueLinkIdentifies, RemoteIssueLinkRequest


class IssueRemoteLinks(SyncAPIResource):
    """Synchronous resource for the Issue remote links API group."""

    def delete_remote_issue_link_by_global_id(
        self, issue_id_or_key: str, *, global_id: str
    ) -> None:
        """Delete remote issue link by global ID"""
        params = self._client._build_params(**{"globalId": global_id})
        self._client._request(
            "DELETE", f"/rest/api/3/issue/{issue_id_or_key}/remotelink", params=params
        )
        return None

    def get_remote_issue_links(
        self, issue_id_or_key: str, *, global_id: str | None = None
    ) -> RemoteIssueLink:
        """Get remote issue links"""
        params = self._client._build_params(**{"globalId": global_id})
        resp = self._client._request(
            "GET", f"/rest/api/3/issue/{issue_id_or_key}/remotelink", params=params
        )
        return RemoteIssueLink.model_validate(resp.json())

    def create_or_update_remote_issue_link(
        self, issue_id_or_key: str, body: RemoteIssueLinkRequest
    ) -> RemoteIssueLinkIdentifies:
        """Create or update remote issue link"""
        resp = self._client._request(
            "POST",
            f"/rest/api/3/issue/{issue_id_or_key}/remotelink",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return RemoteIssueLinkIdentifies.model_validate(resp.json())

    def delete_remote_issue_link_by_id(self, issue_id_or_key: str, link_id: str) -> None:
        """Delete remote issue link by ID"""
        self._client._request("DELETE", f"/rest/api/3/issue/{issue_id_or_key}/remotelink/{link_id}")
        return None

    def get_remote_issue_link_by_id(self, issue_id_or_key: str, link_id: str) -> RemoteIssueLink:
        """Get remote issue link by ID"""
        resp = self._client._request(
            "GET", f"/rest/api/3/issue/{issue_id_or_key}/remotelink/{link_id}"
        )
        return RemoteIssueLink.model_validate(resp.json())

    def update_remote_issue_link(
        self, issue_id_or_key: str, link_id: str, body: RemoteIssueLinkRequest
    ) -> None:
        """Update remote issue link by ID"""
        self._client._request(
            "PUT",
            f"/rest/api/3/issue/{issue_id_or_key}/remotelink/{link_id}",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None


class AsyncIssueRemoteLinks(AsyncAPIResource):
    """Asynchronous resource for the Issue remote links API group."""

    async def delete_remote_issue_link_by_global_id(
        self, issue_id_or_key: str, *, global_id: str
    ) -> None:
        """Delete remote issue link by global ID"""
        params = self._client._build_params(**{"globalId": global_id})
        await self._client._request(
            "DELETE", f"/rest/api/3/issue/{issue_id_or_key}/remotelink", params=params
        )
        return None

    async def get_remote_issue_links(
        self, issue_id_or_key: str, *, global_id: str | None = None
    ) -> RemoteIssueLink:
        """Get remote issue links"""
        params = self._client._build_params(**{"globalId": global_id})
        resp = await self._client._request(
            "GET", f"/rest/api/3/issue/{issue_id_or_key}/remotelink", params=params
        )
        return RemoteIssueLink.model_validate(resp.json())

    async def create_or_update_remote_issue_link(
        self, issue_id_or_key: str, body: RemoteIssueLinkRequest
    ) -> RemoteIssueLinkIdentifies:
        """Create or update remote issue link"""
        resp = await self._client._request(
            "POST",
            f"/rest/api/3/issue/{issue_id_or_key}/remotelink",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return RemoteIssueLinkIdentifies.model_validate(resp.json())

    async def delete_remote_issue_link_by_id(self, issue_id_or_key: str, link_id: str) -> None:
        """Delete remote issue link by ID"""
        await self._client._request(
            "DELETE", f"/rest/api/3/issue/{issue_id_or_key}/remotelink/{link_id}"
        )
        return None

    async def get_remote_issue_link_by_id(
        self, issue_id_or_key: str, link_id: str
    ) -> RemoteIssueLink:
        """Get remote issue link by ID"""
        resp = await self._client._request(
            "GET", f"/rest/api/3/issue/{issue_id_or_key}/remotelink/{link_id}"
        )
        return RemoteIssueLink.model_validate(resp.json())

    async def update_remote_issue_link(
        self, issue_id_or_key: str, link_id: str, body: RemoteIssueLinkRequest
    ) -> None:
        """Update remote issue link by ID"""
        await self._client._request(
            "PUT",
            f"/rest/api/3/issue/{issue_id_or_key}/remotelink/{link_id}",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None
