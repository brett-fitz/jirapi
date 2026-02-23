"""Resource classes for the Service Registry API group."""

from __future__ import annotations

from jirapi._resource import AsyncAPIResource, SyncAPIResource
from jirapi.models import ServiceRegistry as ServiceRegistryModel


class ServiceRegistry(SyncAPIResource):
    """Synchronous resource for the Service Registry API group."""

    def services_get(self, *, service_ids: list[str]) -> ServiceRegistryModel:
        """Retrieve the attributes of service registries"""
        params = self._client._build_params(**{"serviceIds": service_ids})
        resp = self._client._request(
            "GET", "/rest/atlassian-connect/1/service-registry", params=params
        )
        return ServiceRegistryModel.model_validate(resp.json())


class AsyncServiceRegistry(AsyncAPIResource):
    """Asynchronous resource for the Service Registry API group."""

    async def services_get(self, *, service_ids: list[str]) -> ServiceRegistryModel:
        """Retrieve the attributes of service registries"""
        params = self._client._build_params(**{"serviceIds": service_ids})
        resp = await self._client._request(
            "GET", "/rest/atlassian-connect/1/service-registry", params=params
        )
        return ServiceRegistryModel.model_validate(resp.json())
