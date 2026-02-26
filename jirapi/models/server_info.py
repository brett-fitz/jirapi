"""Pydantic models for the server info domain."""

from __future__ import annotations

from typing import Annotated

from pydantic import AwareDatetime, BaseModel, ConfigDict, Field


class HealthCheckResult(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    description: Annotated[
        str | None, Field(description="The description of the Jira health check item.")
    ] = None
    name: Annotated[str | None, Field(description="The name of the Jira health check item.")] = None
    passed: Annotated[
        bool | None, Field(description="Whether the Jira health check item passed or failed.")
    ] = None


class ServerInformation(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    base_url: Annotated[
        str | None, Field(alias="baseUrl", description="The base URL of the Jira instance.")
    ] = None
    build_date: Annotated[
        AwareDatetime | None,
        Field(
            alias="buildDate",
            description="The timestamp when the Jira version was built.",
        ),
    ] = None
    build_number: Annotated[
        int | None, Field(alias="buildNumber", description="The build number of the Jira version.")
    ] = None
    deployment_type: Annotated[
        str | None,
        Field(
            alias="deploymentType",
            description="The type of server deployment. This is always returned as *Cloud*.",
        ),
    ] = None
    display_url: Annotated[
        str | None, Field(alias="displayUrl", description="The display URL of the Jira instance.")
    ] = None
    display_url_confluence: Annotated[
        str | None,
        Field(alias="displayUrlConfluence", description="The display URL of Confluence."),
    ] = None
    display_url_servicedesk_help_center: Annotated[
        str | None,
        Field(
            alias="displayUrlServicedeskHelpCenter",
            description="The display URL of the Servicedesk Help Center.",
        ),
    ] = None
    health_checks: Annotated[
        list[HealthCheckResult] | None,
        Field(
            alias="healthChecks",
            description="Jira instance health check results. Deprecated and no longer returned.",
        ),
    ] = None
    scm_info: Annotated[
        str | None, Field(alias="scmInfo", description="The unique identifier of the Jira version.")
    ] = None
    server_time: Annotated[
        AwareDatetime | None,
        Field(
            alias="serverTime",
            description="The time in Jira when this request was responded to.",
        ),
    ] = None
    server_time_zone: Annotated[
        str | None,
        Field(
            alias="serverTimeZone",
            description="The default timezone of the Jira server. In a format known as Olson Time Zones, IANA Time Zones or TZ Database Time Zones.",
        ),
    ] = None
    server_title: Annotated[
        str | None, Field(alias="serverTitle", description="The name of the Jira instance.")
    ] = None
    version: Annotated[str | None, Field(description="The version of Jira.")] = None
    version_numbers: Annotated[
        list[int] | None,
        Field(
            alias="versionNumbers",
            description="The major, minor, and revision version numbers of the Jira version.",
        ),
    ] = None


__all__ = [
    "HealthCheckResult",
    "ServerInformation",
]
