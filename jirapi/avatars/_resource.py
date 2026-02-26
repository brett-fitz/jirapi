"""Resource classes for avatars."""

from __future__ import annotations

from jirapi._resource import AsyncAPIResource, SyncAPIResource
from jirapi.models import Avatar, StreamingResponseBody, SystemAvatars
from jirapi.models import Avatars as AvatarsModel


class Avatars(SyncAPIResource):
    """Synchronous resource for avatars."""

    def get_all_system(self, type_: str) -> SystemAvatars:
        """Get system avatars by type"""
        resp = self._client._request("GET", f"/rest/api/3/avatar/{type_}/system")
        return SystemAvatars.model_validate(resp.json())

    def get(self, type_: str, entity_id: str) -> AvatarsModel:
        """Get avatars"""
        resp = self._client._request(
            "GET", f"/rest/api/3/universal_avatar/type/{type_}/owner/{entity_id}"
        )
        return AvatarsModel.model_validate(resp.json())

    def store(
        self, type_: str, entity_id: str, *, x: int | None = None, y: int | None = None, size: int
    ) -> Avatar:
        """Load avatar"""
        params = self._client._build_params(**{"x": x, "y": y, "size": size})
        resp = self._client._request(
            "POST", f"/rest/api/3/universal_avatar/type/{type_}/owner/{entity_id}", params=params
        )
        return Avatar.model_validate(resp.json())

    def delete(self, type_: str, owning_object_id: str, id_: str) -> None:
        """Delete avatar"""
        self._client._request(
            "DELETE",
            f"/rest/api/3/universal_avatar/type/{type_}/owner/{owning_object_id}/avatar/{id_}",
        )
        return None

    def get_image_by_type(
        self, type_: str, *, size: str | None = None, format_: str | None = None
    ) -> StreamingResponseBody:
        """Get avatar image by type"""
        params = self._client._build_params(**{"size": size, "format": format_})
        resp = self._client._request(
            "GET", f"/rest/api/3/universal_avatar/view/type/{type_}", params=params
        )
        return StreamingResponseBody.model_validate(resp.json())

    def get_image_by_id(
        self, type_: str, id_: str, *, size: str | None = None, format_: str | None = None
    ) -> StreamingResponseBody:
        """Get avatar image by ID"""
        params = self._client._build_params(**{"size": size, "format": format_})
        resp = self._client._request(
            "GET", f"/rest/api/3/universal_avatar/view/type/{type_}/avatar/{id_}", params=params
        )
        return StreamingResponseBody.model_validate(resp.json())

    def get_image_by_owner(
        self, type_: str, entity_id: str, *, size: str | None = None, format_: str | None = None
    ) -> StreamingResponseBody:
        """Get avatar image by owner"""
        params = self._client._build_params(**{"size": size, "format": format_})
        resp = self._client._request(
            "GET",
            f"/rest/api/3/universal_avatar/view/type/{type_}/owner/{entity_id}",
            params=params,
        )
        return StreamingResponseBody.model_validate(resp.json())


class AsyncAvatars(AsyncAPIResource):
    """Asynchronous resource for avatars."""

    async def get_all_system(self, type_: str) -> SystemAvatars:
        """Get system avatars by type"""
        resp = await self._client._request("GET", f"/rest/api/3/avatar/{type_}/system")
        return SystemAvatars.model_validate(resp.json())

    async def get(self, type_: str, entity_id: str) -> AvatarsModel:
        """Get avatars"""
        resp = await self._client._request(
            "GET", f"/rest/api/3/universal_avatar/type/{type_}/owner/{entity_id}"
        )
        return AvatarsModel.model_validate(resp.json())

    async def store(
        self, type_: str, entity_id: str, *, x: int | None = None, y: int | None = None, size: int
    ) -> Avatar:
        """Load avatar"""
        params = self._client._build_params(**{"x": x, "y": y, "size": size})
        resp = await self._client._request(
            "POST", f"/rest/api/3/universal_avatar/type/{type_}/owner/{entity_id}", params=params
        )
        return Avatar.model_validate(resp.json())

    async def delete(self, type_: str, owning_object_id: str, id_: str) -> None:
        """Delete avatar"""
        await self._client._request(
            "DELETE",
            f"/rest/api/3/universal_avatar/type/{type_}/owner/{owning_object_id}/avatar/{id_}",
        )
        return None

    async def get_image_by_type(
        self, type_: str, *, size: str | None = None, format_: str | None = None
    ) -> StreamingResponseBody:
        """Get avatar image by type"""
        params = self._client._build_params(**{"size": size, "format": format_})
        resp = await self._client._request(
            "GET", f"/rest/api/3/universal_avatar/view/type/{type_}", params=params
        )
        return StreamingResponseBody.model_validate(resp.json())

    async def get_image_by_id(
        self, type_: str, id_: str, *, size: str | None = None, format_: str | None = None
    ) -> StreamingResponseBody:
        """Get avatar image by ID"""
        params = self._client._build_params(**{"size": size, "format": format_})
        resp = await self._client._request(
            "GET", f"/rest/api/3/universal_avatar/view/type/{type_}/avatar/{id_}", params=params
        )
        return StreamingResponseBody.model_validate(resp.json())

    async def get_image_by_owner(
        self, type_: str, entity_id: str, *, size: str | None = None, format_: str | None = None
    ) -> StreamingResponseBody:
        """Get avatar image by owner"""
        params = self._client._build_params(**{"size": size, "format": format_})
        resp = await self._client._request(
            "GET",
            f"/rest/api/3/universal_avatar/view/type/{type_}/owner/{entity_id}",
            params=params,
        )
        return StreamingResponseBody.model_validate(resp.json())
