"""Public Jira client classes.

``Jira`` provides synchronous access and ``AsyncJira`` provides asynchronous
access to the Jira Cloud REST API.  Resource groups are exposed as
``@cached_property`` attributes (e.g. ``jira.issues``, ``jira.projects``).
"""

from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING, Any

import httpx

from jirapi._base_client import _DEFAULT_TIMEOUT, AsyncAPIClient, SyncAPIClient


if TYPE_CHECKING:
    from jirapi.announcement_banner import AnnouncementBanner, AsyncAnnouncementBanner
    from jirapi.app_data_policies import AppDataPolicies, AsyncAppDataPolicies
    from jirapi.app_migration import AppMigration, AsyncAppMigration
    from jirapi.app_properties import AppProperties, AsyncAppProperties
    from jirapi.application_roles import ApplicationRoles, AsyncApplicationRoles
    from jirapi.audit_records import AsyncAuditRecords, AuditRecords
    from jirapi.avatars import AsyncAvatars, Avatars
    from jirapi.classification_levels import AsyncClassificationLevels, ClassificationLevels
    from jirapi.connect_migration import AsyncConnectMigration, ConnectMigration
    from jirapi.dashboards import AsyncDashboards, Dashboards
    from jirapi.dynamic_modules import AsyncDynamicModules, DynamicModules
    from jirapi.fields import AsyncFields, Fields
    from jirapi.filters import AsyncFilters, Filters
    from jirapi.groups import AsyncGroups, Groups
    from jirapi.issue_link_types import AsyncIssueLinkTypes, IssueLinkTypes
    from jirapi.issue_types import AsyncIssueTypes, IssueTypes
    from jirapi.issues import AsyncIssues, Issues
    from jirapi.jira_expressions import AsyncJiraExpressions, JiraExpressions
    from jirapi.jql import AsyncJql, Jql
    from jirapi.labels import AsyncLabels, Labels
    from jirapi.license_metrics import AsyncLicenseMetrics, LicenseMetrics
    from jirapi.notification_schemes import AsyncNotificationSchemes, NotificationSchemes
    from jirapi.permissions import AsyncPermissions, Permissions
    from jirapi.plans import AsyncPlans, Plans
    from jirapi.priorities import AsyncPriorities, Priorities
    from jirapi.projects import AsyncProjects, Projects
    from jirapi.resolutions import AsyncResolutions, Resolutions
    from jirapi.screens import AsyncScreens, Screens
    from jirapi.security_schemes import AsyncSecuritySchemes, SecuritySchemes
    from jirapi.server_info import AsyncServerInfo, ServerInfo
    from jirapi.service_registry import AsyncServiceRegistry, ServiceRegistry
    from jirapi.settings import AsyncSettings, Settings
    from jirapi.statuses import AsyncStatuses, Statuses
    from jirapi.tasks import AsyncTasks, Tasks
    from jirapi.time_tracking import AsyncTimeTracking, TimeTracking
    from jirapi.ui_modifications import AsyncUiModifications, UiModifications
    from jirapi.users import AsyncUsers, Users
    from jirapi.webhooks import AsyncWebhooks, Webhooks
    from jirapi.workflows import AsyncWorkflows, Workflows

__all__ = ["Jira", "AsyncJira"]


class Jira(SyncAPIClient):
    """Synchronous Jira Cloud REST API client.

    Three mutually exclusive authentication strategies are supported:

    1. **Basic auth** (Jira Cloud) — ``email`` + ``api_token``
    2. **Bearer / PAT** (Data Center, OAuth 2.0 access tokens) — ``token``
    3. **Custom auth** — any ``httpx.Auth`` instance via ``auth``

    Usage::

        from jirapi import Jira

        # Basic auth
        jira = Jira(url="https://acme.atlassian.net", email="me@acme.com", api_token="...")

        # Personal Access Token / Bearer
        jira = Jira(url="https://acme.atlassian.net", token="your-pat")

        # Custom httpx.Auth
        jira = Jira(url="https://acme.atlassian.net", auth=my_auth)

    Or as a context manager::

        with Jira(url="...", email="...", api_token="...") as jira:
            issue = jira.issues.get("PROJ-123")
    """

    def __init__(  # noqa: D107
        self,
        *,
        url: str,
        email: str | None = None,
        api_token: str | None = None,
        token: str | None = None,
        auth: httpx.Auth | None = None,
        timeout: float = _DEFAULT_TIMEOUT,
        **httpx_client_kwargs: Any,
    ) -> None:
        super().__init__(
            url=url,
            email=email,
            api_token=api_token,
            token=token,
            auth=auth,
            timeout=timeout,
            **httpx_client_kwargs,
        )

    @cached_property
    def announcement_banner(self) -> AnnouncementBanner:
        from jirapi.announcement_banner import AnnouncementBanner

        return AnnouncementBanner(self)

    @cached_property
    def app_data_policies(self) -> AppDataPolicies:
        from jirapi.app_data_policies import AppDataPolicies

        return AppDataPolicies(self)

    @cached_property
    def app_migration(self) -> AppMigration:
        from jirapi.app_migration import AppMigration

        return AppMigration(self)

    @cached_property
    def app_properties(self) -> AppProperties:
        from jirapi.app_properties import AppProperties

        return AppProperties(self)

    @cached_property
    def application_roles(self) -> ApplicationRoles:
        from jirapi.application_roles import ApplicationRoles

        return ApplicationRoles(self)

    @cached_property
    def audit_records(self) -> AuditRecords:
        from jirapi.audit_records import AuditRecords

        return AuditRecords(self)

    @cached_property
    def avatars(self) -> Avatars:
        from jirapi.avatars import Avatars

        return Avatars(self)

    @cached_property
    def classification_levels(self) -> ClassificationLevels:
        from jirapi.classification_levels import ClassificationLevels

        return ClassificationLevels(self)

    @cached_property
    def connect_migration(self) -> ConnectMigration:
        from jirapi.connect_migration import ConnectMigration

        return ConnectMigration(self)

    @cached_property
    def dashboards(self) -> Dashboards:
        from jirapi.dashboards import Dashboards

        return Dashboards(self)

    @cached_property
    def dynamic_modules(self) -> DynamicModules:
        from jirapi.dynamic_modules import DynamicModules

        return DynamicModules(self)

    @cached_property
    def fields(self) -> Fields:
        from jirapi.fields import Fields

        return Fields(self)

    @cached_property
    def filters(self) -> Filters:
        from jirapi.filters import Filters

        return Filters(self)

    @cached_property
    def groups(self) -> Groups:
        from jirapi.groups import Groups

        return Groups(self)

    @cached_property
    def issue_link_types(self) -> IssueLinkTypes:
        from jirapi.issue_link_types import IssueLinkTypes

        return IssueLinkTypes(self)

    @cached_property
    def issue_types(self) -> IssueTypes:
        from jirapi.issue_types import IssueTypes

        return IssueTypes(self)

    @cached_property
    def issues(self) -> Issues:
        from jirapi.issues import Issues

        return Issues(self)

    @cached_property
    def jira_expressions(self) -> JiraExpressions:
        from jirapi.jira_expressions import JiraExpressions

        return JiraExpressions(self)

    @cached_property
    def jql(self) -> Jql:
        from jirapi.jql import Jql

        return Jql(self)

    @cached_property
    def labels(self) -> Labels:
        from jirapi.labels import Labels

        return Labels(self)

    @cached_property
    def license_metrics(self) -> LicenseMetrics:
        from jirapi.license_metrics import LicenseMetrics

        return LicenseMetrics(self)

    @cached_property
    def notification_schemes(self) -> NotificationSchemes:
        from jirapi.notification_schemes import NotificationSchemes

        return NotificationSchemes(self)

    @cached_property
    def permissions(self) -> Permissions:
        from jirapi.permissions import Permissions

        return Permissions(self)

    @cached_property
    def plans(self) -> Plans:
        from jirapi.plans import Plans

        return Plans(self)

    @cached_property
    def priorities(self) -> Priorities:
        from jirapi.priorities import Priorities

        return Priorities(self)

    @cached_property
    def projects(self) -> Projects:
        from jirapi.projects import Projects

        return Projects(self)

    @cached_property
    def resolutions(self) -> Resolutions:
        from jirapi.resolutions import Resolutions

        return Resolutions(self)

    @cached_property
    def screens(self) -> Screens:
        from jirapi.screens import Screens

        return Screens(self)

    @cached_property
    def security_schemes(self) -> SecuritySchemes:
        from jirapi.security_schemes import SecuritySchemes

        return SecuritySchemes(self)

    @cached_property
    def server_info(self) -> ServerInfo:
        from jirapi.server_info import ServerInfo

        return ServerInfo(self)

    @cached_property
    def service_registry(self) -> ServiceRegistry:
        from jirapi.service_registry import ServiceRegistry

        return ServiceRegistry(self)

    @cached_property
    def settings(self) -> Settings:
        from jirapi.settings import Settings

        return Settings(self)

    @cached_property
    def statuses(self) -> Statuses:
        from jirapi.statuses import Statuses

        return Statuses(self)

    @cached_property
    def tasks(self) -> Tasks:
        from jirapi.tasks import Tasks

        return Tasks(self)

    @cached_property
    def time_tracking(self) -> TimeTracking:
        from jirapi.time_tracking import TimeTracking

        return TimeTracking(self)

    @cached_property
    def ui_modifications(self) -> UiModifications:
        from jirapi.ui_modifications import UiModifications

        return UiModifications(self)

    @cached_property
    def users(self) -> Users:
        from jirapi.users import Users

        return Users(self)

    @cached_property
    def webhooks(self) -> Webhooks:
        from jirapi.webhooks import Webhooks

        return Webhooks(self)

    @cached_property
    def workflows(self) -> Workflows:
        from jirapi.workflows import Workflows

        return Workflows(self)


class AsyncJira(AsyncAPIClient):
    """Asynchronous Jira Cloud REST API client.

    Three mutually exclusive authentication strategies are supported:

    1. **Basic auth** (Jira Cloud) — ``email`` + ``api_token``
    2. **Bearer / PAT** (Data Center, OAuth 2.0 access tokens) — ``token``
    3. **Custom auth** — any ``httpx.Auth`` instance via ``auth``

    Usage::

        from jirapi import AsyncJira

        async with AsyncJira(
            url="https://acme.atlassian.net", email="me@acme.com", api_token="..."
        ) as jira:
            issue = await jira.issues.get("PROJ-123")
    """

    def __init__(  # noqa: D107
        self,
        *,
        url: str,
        email: str | None = None,
        api_token: str | None = None,
        token: str | None = None,
        auth: httpx.Auth | None = None,
        timeout: float = _DEFAULT_TIMEOUT,
        **httpx_client_kwargs: Any,
    ) -> None:
        super().__init__(
            url=url,
            email=email,
            api_token=api_token,
            token=token,
            auth=auth,
            timeout=timeout,
            **httpx_client_kwargs,
        )

    @cached_property
    def announcement_banner(self) -> AsyncAnnouncementBanner:
        from jirapi.announcement_banner import AsyncAnnouncementBanner

        return AsyncAnnouncementBanner(self)

    @cached_property
    def app_data_policies(self) -> AsyncAppDataPolicies:
        from jirapi.app_data_policies import AsyncAppDataPolicies

        return AsyncAppDataPolicies(self)

    @cached_property
    def app_migration(self) -> AsyncAppMigration:
        from jirapi.app_migration import AsyncAppMigration

        return AsyncAppMigration(self)

    @cached_property
    def app_properties(self) -> AsyncAppProperties:
        from jirapi.app_properties import AsyncAppProperties

        return AsyncAppProperties(self)

    @cached_property
    def application_roles(self) -> AsyncApplicationRoles:
        from jirapi.application_roles import AsyncApplicationRoles

        return AsyncApplicationRoles(self)

    @cached_property
    def audit_records(self) -> AsyncAuditRecords:
        from jirapi.audit_records import AsyncAuditRecords

        return AsyncAuditRecords(self)

    @cached_property
    def avatars(self) -> AsyncAvatars:
        from jirapi.avatars import AsyncAvatars

        return AsyncAvatars(self)

    @cached_property
    def classification_levels(self) -> AsyncClassificationLevels:
        from jirapi.classification_levels import AsyncClassificationLevels

        return AsyncClassificationLevels(self)

    @cached_property
    def connect_migration(self) -> AsyncConnectMigration:
        from jirapi.connect_migration import AsyncConnectMigration

        return AsyncConnectMigration(self)

    @cached_property
    def dashboards(self) -> AsyncDashboards:
        from jirapi.dashboards import AsyncDashboards

        return AsyncDashboards(self)

    @cached_property
    def dynamic_modules(self) -> AsyncDynamicModules:
        from jirapi.dynamic_modules import AsyncDynamicModules

        return AsyncDynamicModules(self)

    @cached_property
    def fields(self) -> AsyncFields:
        from jirapi.fields import AsyncFields

        return AsyncFields(self)

    @cached_property
    def filters(self) -> AsyncFilters:
        from jirapi.filters import AsyncFilters

        return AsyncFilters(self)

    @cached_property
    def groups(self) -> AsyncGroups:
        from jirapi.groups import AsyncGroups

        return AsyncGroups(self)

    @cached_property
    def issue_link_types(self) -> AsyncIssueLinkTypes:
        from jirapi.issue_link_types import AsyncIssueLinkTypes

        return AsyncIssueLinkTypes(self)

    @cached_property
    def issue_types(self) -> AsyncIssueTypes:
        from jirapi.issue_types import AsyncIssueTypes

        return AsyncIssueTypes(self)

    @cached_property
    def issues(self) -> AsyncIssues:
        from jirapi.issues import AsyncIssues

        return AsyncIssues(self)

    @cached_property
    def jira_expressions(self) -> AsyncJiraExpressions:
        from jirapi.jira_expressions import AsyncJiraExpressions

        return AsyncJiraExpressions(self)

    @cached_property
    def jql(self) -> AsyncJql:
        from jirapi.jql import AsyncJql

        return AsyncJql(self)

    @cached_property
    def labels(self) -> AsyncLabels:
        from jirapi.labels import AsyncLabels

        return AsyncLabels(self)

    @cached_property
    def license_metrics(self) -> AsyncLicenseMetrics:
        from jirapi.license_metrics import AsyncLicenseMetrics

        return AsyncLicenseMetrics(self)

    @cached_property
    def notification_schemes(self) -> AsyncNotificationSchemes:
        from jirapi.notification_schemes import AsyncNotificationSchemes

        return AsyncNotificationSchemes(self)

    @cached_property
    def permissions(self) -> AsyncPermissions:
        from jirapi.permissions import AsyncPermissions

        return AsyncPermissions(self)

    @cached_property
    def plans(self) -> AsyncPlans:
        from jirapi.plans import AsyncPlans

        return AsyncPlans(self)

    @cached_property
    def priorities(self) -> AsyncPriorities:
        from jirapi.priorities import AsyncPriorities

        return AsyncPriorities(self)

    @cached_property
    def projects(self) -> AsyncProjects:
        from jirapi.projects import AsyncProjects

        return AsyncProjects(self)

    @cached_property
    def resolutions(self) -> AsyncResolutions:
        from jirapi.resolutions import AsyncResolutions

        return AsyncResolutions(self)

    @cached_property
    def screens(self) -> AsyncScreens:
        from jirapi.screens import AsyncScreens

        return AsyncScreens(self)

    @cached_property
    def security_schemes(self) -> AsyncSecuritySchemes:
        from jirapi.security_schemes import AsyncSecuritySchemes

        return AsyncSecuritySchemes(self)

    @cached_property
    def server_info(self) -> AsyncServerInfo:
        from jirapi.server_info import AsyncServerInfo

        return AsyncServerInfo(self)

    @cached_property
    def service_registry(self) -> AsyncServiceRegistry:
        from jirapi.service_registry import AsyncServiceRegistry

        return AsyncServiceRegistry(self)

    @cached_property
    def settings(self) -> AsyncSettings:
        from jirapi.settings import AsyncSettings

        return AsyncSettings(self)

    @cached_property
    def statuses(self) -> AsyncStatuses:
        from jirapi.statuses import AsyncStatuses

        return AsyncStatuses(self)

    @cached_property
    def tasks(self) -> AsyncTasks:
        from jirapi.tasks import AsyncTasks

        return AsyncTasks(self)

    @cached_property
    def time_tracking(self) -> AsyncTimeTracking:
        from jirapi.time_tracking import AsyncTimeTracking

        return AsyncTimeTracking(self)

    @cached_property
    def ui_modifications(self) -> AsyncUiModifications:
        from jirapi.ui_modifications import AsyncUiModifications

        return AsyncUiModifications(self)

    @cached_property
    def users(self) -> AsyncUsers:
        from jirapi.users import AsyncUsers

        return AsyncUsers(self)

    @cached_property
    def webhooks(self) -> AsyncWebhooks:
        from jirapi.webhooks import AsyncWebhooks

        return AsyncWebhooks(self)

    @cached_property
    def workflows(self) -> AsyncWorkflows:
        from jirapi.workflows import AsyncWorkflows

        return AsyncWorkflows(self)
