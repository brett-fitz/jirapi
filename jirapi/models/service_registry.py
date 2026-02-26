"""Pydantic models for the service registry domain."""

from __future__ import annotations

from typing import Annotated
from uuid import UUID

from pydantic import BaseModel, Field


class ServiceRegistryTier(BaseModel):
    description: Annotated[str | None, Field(description="tier description")] = None
    id: Annotated[UUID | None, Field(description="tier ID")] = None
    level: Annotated[int | None, Field(description="tier level")] = None
    name: Annotated[str | None, Field(description="tier name")] = None
    name_key: Annotated[
        str | None,
        Field(
            alias="nameKey",
            description="name key of the tier",
            examples=["service-registry.tier1.name"],
        ),
    ] = None


class ServiceRegistry(BaseModel):
    description: Annotated[str | None, Field(description="service description")] = None
    id: Annotated[UUID | None, Field(description="service ID")] = None
    name: Annotated[str | None, Field(description="service name")] = None
    organization_id: Annotated[
        str | None, Field(alias="organizationId", description="organization ID")
    ] = None
    revision: Annotated[str | None, Field(description="service revision")] = None
    service_tier: Annotated[ServiceRegistryTier | None, Field(alias="serviceTier")] = None


__all__ = [
    "ServiceRegistryTier",
    "ServiceRegistry",
]
