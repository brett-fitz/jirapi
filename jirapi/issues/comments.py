"""Resource classes for issues.comments."""

from __future__ import annotations

from jirapi._resource import AsyncAPIResource, SyncAPIResource
from jirapi.models import Comment, IssueCommentListRequest, PageBeanComment, PageOfComments


class IssueComments(SyncAPIResource):
    """Synchronous resource for issues.comments."""

    def get_by_ids(
        self, body: IssueCommentListRequest, *, expand: str | None = None
    ) -> PageBeanComment:
        """Get comments by IDs"""
        params = self._client._build_params(**{"expand": expand})
        resp = self._client._request(
            "POST",
            "/rest/api/3/comment/list",
            params=params,
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return PageBeanComment.model_validate(resp.json())

    def list(
        self,
        issue_id_or_key: str,
        *,
        start_at: int | None = None,
        max_results: int | None = None,
        order_by: str | None = None,
        expand: str | None = None,
    ) -> PageOfComments:
        """Get comments"""
        params = self._client._build_params(
            **{
                "startAt": start_at,
                "maxResults": max_results,
                "orderBy": order_by,
                "expand": expand,
            }
        )
        resp = self._client._request(
            "GET", f"/rest/api/3/issue/{issue_id_or_key}/comment", params=params
        )
        return PageOfComments.model_validate(resp.json())

    def add(self, issue_id_or_key: str, body: Comment, *, expand: str | None = None) -> Comment:
        """Add comment"""
        params = self._client._build_params(**{"expand": expand})
        resp = self._client._request(
            "POST",
            f"/rest/api/3/issue/{issue_id_or_key}/comment",
            params=params,
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return Comment.model_validate(resp.json())

    def delete(self, issue_id_or_key: str, id_: str) -> None:
        """Delete comment"""
        self._client._request("DELETE", f"/rest/api/3/issue/{issue_id_or_key}/comment/{id_}")
        return None

    def get(self, issue_id_or_key: str, id_: str, *, expand: str | None = None) -> Comment:
        """Get comment"""
        params = self._client._build_params(**{"expand": expand})
        resp = self._client._request(
            "GET", f"/rest/api/3/issue/{issue_id_or_key}/comment/{id_}", params=params
        )
        return Comment.model_validate(resp.json())

    def update(
        self,
        issue_id_or_key: str,
        id_: str,
        body: Comment,
        *,
        notify_users: bool | None = None,
        override_editable_flag: bool | None = None,
        expand: str | None = None,
    ) -> Comment:
        """Update comment"""
        params = self._client._build_params(
            **{
                "notifyUsers": notify_users,
                "overrideEditableFlag": override_editable_flag,
                "expand": expand,
            }
        )
        resp = self._client._request(
            "PUT",
            f"/rest/api/3/issue/{issue_id_or_key}/comment/{id_}",
            params=params,
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return Comment.model_validate(resp.json())


class AsyncIssueComments(AsyncAPIResource):
    """Asynchronous resource for issues.comments."""

    async def get_by_ids(
        self, body: IssueCommentListRequest, *, expand: str | None = None
    ) -> PageBeanComment:
        """Get comments by IDs"""
        params = self._client._build_params(**{"expand": expand})
        resp = await self._client._request(
            "POST",
            "/rest/api/3/comment/list",
            params=params,
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return PageBeanComment.model_validate(resp.json())

    async def list(
        self,
        issue_id_or_key: str,
        *,
        start_at: int | None = None,
        max_results: int | None = None,
        order_by: str | None = None,
        expand: str | None = None,
    ) -> PageOfComments:
        """Get comments"""
        params = self._client._build_params(
            **{
                "startAt": start_at,
                "maxResults": max_results,
                "orderBy": order_by,
                "expand": expand,
            }
        )
        resp = await self._client._request(
            "GET", f"/rest/api/3/issue/{issue_id_or_key}/comment", params=params
        )
        return PageOfComments.model_validate(resp.json())

    async def add(
        self, issue_id_or_key: str, body: Comment, *, expand: str | None = None
    ) -> Comment:
        """Add comment"""
        params = self._client._build_params(**{"expand": expand})
        resp = await self._client._request(
            "POST",
            f"/rest/api/3/issue/{issue_id_or_key}/comment",
            params=params,
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return Comment.model_validate(resp.json())

    async def delete(self, issue_id_or_key: str, id_: str) -> None:
        """Delete comment"""
        await self._client._request("DELETE", f"/rest/api/3/issue/{issue_id_or_key}/comment/{id_}")
        return None

    async def get(self, issue_id_or_key: str, id_: str, *, expand: str | None = None) -> Comment:
        """Get comment"""
        params = self._client._build_params(**{"expand": expand})
        resp = await self._client._request(
            "GET", f"/rest/api/3/issue/{issue_id_or_key}/comment/{id_}", params=params
        )
        return Comment.model_validate(resp.json())

    async def update(
        self,
        issue_id_or_key: str,
        id_: str,
        body: Comment,
        *,
        notify_users: bool | None = None,
        override_editable_flag: bool | None = None,
        expand: str | None = None,
    ) -> Comment:
        """Update comment"""
        params = self._client._build_params(
            **{
                "notifyUsers": notify_users,
                "overrideEditableFlag": override_editable_flag,
                "expand": expand,
            }
        )
        resp = await self._client._request(
            "PUT",
            f"/rest/api/3/issue/{issue_id_or_key}/comment/{id_}",
            params=params,
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return Comment.model_validate(resp.json())
