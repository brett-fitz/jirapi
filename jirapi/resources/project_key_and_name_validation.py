"""Resource classes for the Project key and name validation API group."""

from __future__ import annotations

from jirapi._resource import AsyncAPIResource, SyncAPIResource
from jirapi.models import ErrorCollection


class ProjectKeyAndNameValidation(SyncAPIResource):
    """Synchronous resource for the Project key and name validation API group."""

    def validate_project_key(self, *, key: str | None = None) -> ErrorCollection:
        """Validate project key"""
        params = self._client._build_params(**{"key": key})
        resp = self._client._request("GET", "/rest/api/3/projectvalidate/key", params=params)
        return ErrorCollection.model_validate(resp.json())

    def get_valid_project_key(self, *, key: str | None = None) -> None:
        """Get valid project key"""
        params = self._client._build_params(**{"key": key})
        resp = self._client._request(
            "GET", "/rest/api/3/projectvalidate/validProjectKey", params=params
        )
        return None

    def get_valid_project_name(self, *, name: str) -> None:
        """Get valid project name"""
        params = self._client._build_params(**{"name": name})
        resp = self._client._request(
            "GET", "/rest/api/3/projectvalidate/validProjectName", params=params
        )
        return None


class AsyncProjectKeyAndNameValidation(AsyncAPIResource):
    """Asynchronous resource for the Project key and name validation API group."""

    async def validate_project_key(self, *, key: str | None = None) -> ErrorCollection:
        """Validate project key"""
        params = self._client._build_params(**{"key": key})
        resp = await self._client._request("GET", "/rest/api/3/projectvalidate/key", params=params)
        return ErrorCollection.model_validate(resp.json())

    async def get_valid_project_key(self, *, key: str | None = None) -> None:
        """Get valid project key"""
        params = self._client._build_params(**{"key": key})
        resp = await self._client._request(
            "GET", "/rest/api/3/projectvalidate/validProjectKey", params=params
        )
        return None

    async def get_valid_project_name(self, *, name: str) -> None:
        """Get valid project name"""
        params = self._client._build_params(**{"name": name})
        resp = await self._client._request(
            "GET", "/rest/api/3/projectvalidate/validProjectName", params=params
        )
        return None
