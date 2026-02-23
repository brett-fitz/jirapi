"""Resource classes for the Project features API group."""

from __future__ import annotations

from jirapi._resource import AsyncAPIResource, SyncAPIResource
from jirapi.models import ContainerForProjectFeatures, ProjectFeatureState


class ProjectFeatures(SyncAPIResource):
    """Synchronous resource for the Project features API group."""

    def get_features_for_project(self, project_id_or_key: str) -> ContainerForProjectFeatures:
        """Get project features"""
        resp = self._client._request("GET", f"/rest/api/3/project/{project_id_or_key}/features")
        return ContainerForProjectFeatures.model_validate(resp.json())

    def toggle_feature_for_project(
        self, project_id_or_key: str, feature_key: str, body: ProjectFeatureState
    ) -> ContainerForProjectFeatures:
        """Set project feature state"""
        resp = self._client._request(
            "PUT",
            f"/rest/api/3/project/{project_id_or_key}/features/{feature_key}",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return ContainerForProjectFeatures.model_validate(resp.json())


class AsyncProjectFeatures(AsyncAPIResource):
    """Asynchronous resource for the Project features API group."""

    async def get_features_for_project(self, project_id_or_key: str) -> ContainerForProjectFeatures:
        """Get project features"""
        resp = await self._client._request(
            "GET", f"/rest/api/3/project/{project_id_or_key}/features"
        )
        return ContainerForProjectFeatures.model_validate(resp.json())

    async def toggle_feature_for_project(
        self, project_id_or_key: str, feature_key: str, body: ProjectFeatureState
    ) -> ContainerForProjectFeatures:
        """Set project feature state"""
        resp = await self._client._request(
            "PUT",
            f"/rest/api/3/project/{project_id_or_key}/features/{feature_key}",
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return ContainerForProjectFeatures.model_validate(resp.json())
