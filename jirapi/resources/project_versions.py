"""Resource classes for the Project versions API group."""

from __future__ import annotations

from jirapi._resource import AsyncAPIResource, SyncAPIResource
from jirapi.models import (
    DeleteAndReplaceVersionBean,
    PageBeanVersion,
    Version,
    VersionIssueCounts,
    VersionMoveBean,
    VersionRelatedWork,
    VersionUnresolvedIssuesCount,
)


class ProjectVersions(SyncAPIResource):
    """Synchronous resource for the Project versions API group."""

    def get_project_versions_paginated(
        self,
        project_id_or_key: str,
        *,
        start_at: int | None = None,
        max_results: int | None = None,
        order_by: str | None = None,
        query: str | None = None,
        status: str | None = None,
        expand: str | None = None,
    ) -> PageBeanVersion:
        """Get project versions paginated"""
        params = self._client._build_params(
            **{
                "startAt": start_at,
                "maxResults": max_results,
                "orderBy": order_by,
                "query": query,
                "status": status,
                "expand": expand,
            }
        )
        resp = self._client._request(
            "GET", f"/rest/api/3/project/{project_id_or_key}/version", params=params
        )
        return PageBeanVersion.model_validate(resp.json())

    def get_project_versions(self, project_id_or_key: str, *, expand: str | None = None) -> Version:
        """Get project versions"""
        params = self._client._build_params(**{"expand": expand})
        resp = self._client._request(
            "GET", f"/rest/api/3/project/{project_id_or_key}/versions", params=params
        )
        return Version.model_validate(resp.json())

    def create_version(self, body: Version) -> Version:
        """Create version"""
        resp = self._client._request(
            "POST", "/rest/api/3/version", json=body.model_dump(by_alias=True, exclude_none=True)
        )
        return Version.model_validate(resp.json())

    def get_version(self, id_: str, *, expand: str | None = None) -> Version:
        """Get version"""
        params = self._client._build_params(**{"expand": expand})
        resp = self._client._request("GET", f"/rest/api/3/version/{id_}", params=params)
        return Version.model_validate(resp.json())

    def update_version(self, id_: str, body: Version) -> Version:
        """Update version"""
        resp = self._client._request(
            "PUT",
            f"/rest/api/3/version/{id_}",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return Version.model_validate(resp.json())

    def merge_versions(self, id_: str, move_issues_to: str) -> None:
        """Merge versions"""
        resp = self._client._request("PUT", f"/rest/api/3/version/{id_}/mergeto/{move_issues_to}")
        return None

    def move_version(self, id_: str, body: VersionMoveBean) -> Version:
        """Move version"""
        resp = self._client._request(
            "POST",
            f"/rest/api/3/version/{id_}/move",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return Version.model_validate(resp.json())

    def get_version_related_issues(self, id_: str) -> VersionIssueCounts:
        """Get version's related issues count"""
        resp = self._client._request("GET", f"/rest/api/3/version/{id_}/relatedIssueCounts")
        return VersionIssueCounts.model_validate(resp.json())

    def get_related_work(self, id_: str) -> VersionRelatedWork:
        """Get related work"""
        resp = self._client._request("GET", f"/rest/api/3/version/{id_}/relatedwork")
        return VersionRelatedWork.model_validate(resp.json())

    def create_related_work(self, id_: str, body: VersionRelatedWork) -> VersionRelatedWork:
        """Create related work"""
        resp = self._client._request(
            "POST",
            f"/rest/api/3/version/{id_}/relatedwork",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return VersionRelatedWork.model_validate(resp.json())

    def update_related_work(self, id_: str, body: VersionRelatedWork) -> VersionRelatedWork:
        """Update related work"""
        resp = self._client._request(
            "PUT",
            f"/rest/api/3/version/{id_}/relatedwork",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return VersionRelatedWork.model_validate(resp.json())

    def delete_and_replace_version(self, id_: str, body: DeleteAndReplaceVersionBean) -> None:
        """Delete and replace version"""
        resp = self._client._request(
            "POST",
            f"/rest/api/3/version/{id_}/removeAndSwap",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    def get_version_unresolved_issues(self, id_: str) -> VersionUnresolvedIssuesCount:
        """Get version's unresolved issues count"""
        resp = self._client._request("GET", f"/rest/api/3/version/{id_}/unresolvedIssueCount")
        return VersionUnresolvedIssuesCount.model_validate(resp.json())

    def delete_related_work(self, version_id: str, related_work_id: str) -> None:
        """Delete related work"""
        resp = self._client._request(
            "DELETE", f"/rest/api/3/version/{version_id}/relatedwork/{related_work_id}"
        )
        return None


class AsyncProjectVersions(AsyncAPIResource):
    """Asynchronous resource for the Project versions API group."""

    async def get_project_versions_paginated(
        self,
        project_id_or_key: str,
        *,
        start_at: int | None = None,
        max_results: int | None = None,
        order_by: str | None = None,
        query: str | None = None,
        status: str | None = None,
        expand: str | None = None,
    ) -> PageBeanVersion:
        """Get project versions paginated"""
        params = self._client._build_params(
            **{
                "startAt": start_at,
                "maxResults": max_results,
                "orderBy": order_by,
                "query": query,
                "status": status,
                "expand": expand,
            }
        )
        resp = await self._client._request(
            "GET", f"/rest/api/3/project/{project_id_or_key}/version", params=params
        )
        return PageBeanVersion.model_validate(resp.json())

    async def get_project_versions(
        self, project_id_or_key: str, *, expand: str | None = None
    ) -> Version:
        """Get project versions"""
        params = self._client._build_params(**{"expand": expand})
        resp = await self._client._request(
            "GET", f"/rest/api/3/project/{project_id_or_key}/versions", params=params
        )
        return Version.model_validate(resp.json())

    async def create_version(self, body: Version) -> Version:
        """Create version"""
        resp = await self._client._request(
            "POST", "/rest/api/3/version", json=body.model_dump(by_alias=True, exclude_none=True)
        )
        return Version.model_validate(resp.json())

    async def get_version(self, id_: str, *, expand: str | None = None) -> Version:
        """Get version"""
        params = self._client._build_params(**{"expand": expand})
        resp = await self._client._request("GET", f"/rest/api/3/version/{id_}", params=params)
        return Version.model_validate(resp.json())

    async def update_version(self, id_: str, body: Version) -> Version:
        """Update version"""
        resp = await self._client._request(
            "PUT",
            f"/rest/api/3/version/{id_}",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return Version.model_validate(resp.json())

    async def merge_versions(self, id_: str, move_issues_to: str) -> None:
        """Merge versions"""
        resp = await self._client._request(
            "PUT", f"/rest/api/3/version/{id_}/mergeto/{move_issues_to}"
        )
        return None

    async def move_version(self, id_: str, body: VersionMoveBean) -> Version:
        """Move version"""
        resp = await self._client._request(
            "POST",
            f"/rest/api/3/version/{id_}/move",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return Version.model_validate(resp.json())

    async def get_version_related_issues(self, id_: str) -> VersionIssueCounts:
        """Get version's related issues count"""
        resp = await self._client._request("GET", f"/rest/api/3/version/{id_}/relatedIssueCounts")
        return VersionIssueCounts.model_validate(resp.json())

    async def get_related_work(self, id_: str) -> VersionRelatedWork:
        """Get related work"""
        resp = await self._client._request("GET", f"/rest/api/3/version/{id_}/relatedwork")
        return VersionRelatedWork.model_validate(resp.json())

    async def create_related_work(self, id_: str, body: VersionRelatedWork) -> VersionRelatedWork:
        """Create related work"""
        resp = await self._client._request(
            "POST",
            f"/rest/api/3/version/{id_}/relatedwork",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return VersionRelatedWork.model_validate(resp.json())

    async def update_related_work(self, id_: str, body: VersionRelatedWork) -> VersionRelatedWork:
        """Update related work"""
        resp = await self._client._request(
            "PUT",
            f"/rest/api/3/version/{id_}/relatedwork",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return VersionRelatedWork.model_validate(resp.json())

    async def delete_and_replace_version(self, id_: str, body: DeleteAndReplaceVersionBean) -> None:
        """Delete and replace version"""
        resp = await self._client._request(
            "POST",
            f"/rest/api/3/version/{id_}/removeAndSwap",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    async def get_version_unresolved_issues(self, id_: str) -> VersionUnresolvedIssuesCount:
        """Get version's unresolved issues count"""
        resp = await self._client._request("GET", f"/rest/api/3/version/{id_}/unresolvedIssueCount")
        return VersionUnresolvedIssuesCount.model_validate(resp.json())

    async def delete_related_work(self, version_id: str, related_work_id: str) -> None:
        """Delete related work"""
        resp = await self._client._request(
            "DELETE", f"/rest/api/3/version/{version_id}/relatedwork/{related_work_id}"
        )
        return None
