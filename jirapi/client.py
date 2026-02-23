"""Public Jira client classes.

``Jira`` provides synchronous access and ``AsyncJira`` provides asynchronous
access to the Jira Cloud REST API.  Resource groups are exposed as
``@cached_property`` attributes (e.g. ``jira.issues``, ``jira.projects``).
"""

from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING, Any

from jirapi._base_client import _DEFAULT_TIMEOUT, AsyncAPIClient, SyncAPIClient


if TYPE_CHECKING:
    from jirapi.resources.announcement_banner import AnnouncementBanner, AsyncAnnouncementBanner
    from jirapi.resources.app_data_policies import AppDataPolicies, AsyncAppDataPolicies
    from jirapi.resources.app_migration import AppMigration, AsyncAppMigration
    from jirapi.resources.app_properties import AppProperties, AsyncAppProperties
    from jirapi.resources.application_roles import ApplicationRoles, AsyncApplicationRoles
    from jirapi.resources.audit_records import AsyncAuditRecords, AuditRecords
    from jirapi.resources.avatars import AsyncAvatars, Avatars
    from jirapi.resources.classification_levels import (
        AsyncClassificationLevels,
        ClassificationLevels,
    )
    from jirapi.resources.dashboards import AsyncDashboards, Dashboards
    from jirapi.resources.dynamic_modules import AsyncDynamicModules, DynamicModules
    from jirapi.resources.field_schemes import AsyncFieldSchemes, FieldSchemes
    from jirapi.resources.filter_sharing import AsyncFilterSharing, FilterSharing
    from jirapi.resources.filters import AsyncFilters, Filters
    from jirapi.resources.group_and_user_picker import AsyncGroupAndUserPicker, GroupAndUserPicker
    from jirapi.resources.groups import AsyncGroups, Groups
    from jirapi.resources.issue_attachments import AsyncIssueAttachments, IssueAttachments
    from jirapi.resources.issue_bulk_operations import AsyncIssueBulkOperations, IssueBulkOperations
    from jirapi.resources.issue_comment_properties import (
        AsyncIssueCommentProperties,
        IssueCommentProperties,
    )
    from jirapi.resources.issue_comments import AsyncIssueComments, IssueComments
    from jirapi.resources.issue_custom_field_associations import (
        AsyncIssueCustomFieldAssociations,
        IssueCustomFieldAssociations,
    )
    from jirapi.resources.issue_custom_field_configuration_apps import (
        AsyncIssueCustomFieldConfigurationApps,
        IssueCustomFieldConfigurationApps,
    )
    from jirapi.resources.issue_custom_field_contexts import (
        AsyncIssueCustomFieldContexts,
        IssueCustomFieldContexts,
    )
    from jirapi.resources.issue_custom_field_options import (
        AsyncIssueCustomFieldOptions,
        IssueCustomFieldOptions,
    )
    from jirapi.resources.issue_custom_field_options_apps import (
        AsyncIssueCustomFieldOptionsApps,
        IssueCustomFieldOptionsApps,
    )
    from jirapi.resources.issue_custom_field_values_apps import (
        AsyncIssueCustomFieldValuesApps,
        IssueCustomFieldValuesApps,
    )
    from jirapi.resources.issue_fields import AsyncIssueFields, IssueFields
    from jirapi.resources.issue_link_types import AsyncIssueLinkTypes, IssueLinkTypes
    from jirapi.resources.issue_links import AsyncIssueLinks, IssueLinks
    from jirapi.resources.issue_navigator_settings import (
        AsyncIssueNavigatorSettings,
        IssueNavigatorSettings,
    )
    from jirapi.resources.issue_notification_schemes import (
        AsyncIssueNotificationSchemes,
        IssueNotificationSchemes,
    )
    from jirapi.resources.issue_priorities import AsyncIssuePriorities, IssuePriorities
    from jirapi.resources.issue_properties import AsyncIssueProperties, IssueProperties
    from jirapi.resources.issue_redaction import AsyncIssueRedaction, IssueRedaction
    from jirapi.resources.issue_remote_links import AsyncIssueRemoteLinks, IssueRemoteLinks
    from jirapi.resources.issue_resolutions import AsyncIssueResolutions, IssueResolutions
    from jirapi.resources.issue_search import AsyncIssueSearch, IssueSearch
    from jirapi.resources.issue_security_level import AsyncIssueSecurityLevel, IssueSecurityLevel
    from jirapi.resources.issue_security_schemes import (
        AsyncIssueSecuritySchemes,
        IssueSecuritySchemes,
    )
    from jirapi.resources.issue_type_properties import AsyncIssueTypeProperties, IssueTypeProperties
    from jirapi.resources.issue_type_schemes import AsyncIssueTypeSchemes, IssueTypeSchemes
    from jirapi.resources.issue_type_screen_schemes import (
        AsyncIssueTypeScreenSchemes,
        IssueTypeScreenSchemes,
    )
    from jirapi.resources.issue_types import AsyncIssueTypes, IssueTypes
    from jirapi.resources.issue_votes import AsyncIssueVotes, IssueVotes
    from jirapi.resources.issue_watchers import AsyncIssueWatchers, IssueWatchers
    from jirapi.resources.issue_worklog_properties import (
        AsyncIssueWorklogProperties,
        IssueWorklogProperties,
    )
    from jirapi.resources.issue_worklogs import AsyncIssueWorklogs, IssueWorklogs
    from jirapi.resources.issues import AsyncIssues, Issues
    from jirapi.resources.jira_expressions import AsyncJiraExpressions, JiraExpressions
    from jirapi.resources.jira_settings import AsyncJiraSettings, JiraSettings
    from jirapi.resources.jql import AsyncJql, Jql
    from jirapi.resources.jql_functions_apps import AsyncJqlFunctionsApps, JqlFunctionsApps
    from jirapi.resources.labels import AsyncLabels, Labels
    from jirapi.resources.license_metrics import AsyncLicenseMetrics, LicenseMetrics
    from jirapi.resources.migration_of_connect_modules_to_forge import (
        AsyncMigrationOfConnectModulesToForge,
        MigrationOfConnectModulesToForge,
    )
    from jirapi.resources.myself import AsyncMyself, Myself
    from jirapi.resources.permission_schemes import AsyncPermissionSchemes, PermissionSchemes
    from jirapi.resources.permissions import AsyncPermissions, Permissions
    from jirapi.resources.plans import AsyncPlans, Plans
    from jirapi.resources.priority_schemes import AsyncPrioritySchemes, PrioritySchemes
    from jirapi.resources.project_avatars import AsyncProjectAvatars, ProjectAvatars
    from jirapi.resources.project_categories import AsyncProjectCategories, ProjectCategories
    from jirapi.resources.project_classification_levels import (
        AsyncProjectClassificationLevels,
        ProjectClassificationLevels,
    )
    from jirapi.resources.project_components import AsyncProjectComponents, ProjectComponents
    from jirapi.resources.project_email import AsyncProjectEmail, ProjectEmail
    from jirapi.resources.project_features import AsyncProjectFeatures, ProjectFeatures
    from jirapi.resources.project_key_and_name_validation import (
        AsyncProjectKeyAndNameValidation,
        ProjectKeyAndNameValidation,
    )
    from jirapi.resources.project_permission_schemes import (
        AsyncProjectPermissionSchemes,
        ProjectPermissionSchemes,
    )
    from jirapi.resources.project_properties import AsyncProjectProperties, ProjectProperties
    from jirapi.resources.project_role_actors import AsyncProjectRoleActors, ProjectRoleActors
    from jirapi.resources.project_roles import AsyncProjectRoles, ProjectRoles
    from jirapi.resources.project_templates import AsyncProjectTemplates, ProjectTemplates
    from jirapi.resources.project_types import AsyncProjectTypes, ProjectTypes
    from jirapi.resources.project_versions import AsyncProjectVersions, ProjectVersions
    from jirapi.resources.projects import AsyncProjects, Projects
    from jirapi.resources.screen_schemes import AsyncScreenSchemes, ScreenSchemes
    from jirapi.resources.screen_tab_fields import AsyncScreenTabFields, ScreenTabFields
    from jirapi.resources.screen_tabs import AsyncScreenTabs, ScreenTabs
    from jirapi.resources.screens import AsyncScreens, Screens
    from jirapi.resources.server_info import AsyncServerInfo, ServerInfo
    from jirapi.resources.service_registry import AsyncServiceRegistry, ServiceRegistry
    from jirapi.resources.status import AsyncStatus, Status
    from jirapi.resources.tasks import AsyncTasks, Tasks
    from jirapi.resources.teams_in_plan import AsyncTeamsInPlan, TeamsInPlan
    from jirapi.resources.time_tracking import AsyncTimeTracking, TimeTracking
    from jirapi.resources.ui_modifications_apps import AsyncUiModificationsApps, UiModificationsApps
    from jirapi.resources.untagged import AsyncUntagged, Untagged
    from jirapi.resources.user_properties import AsyncUserProperties, UserProperties
    from jirapi.resources.user_search import AsyncUserSearch, UserSearch
    from jirapi.resources.users import AsyncUsers, Users
    from jirapi.resources.webhooks import AsyncWebhooks, Webhooks
    from jirapi.resources.workflow_scheme_drafts import (
        AsyncWorkflowSchemeDrafts,
        WorkflowSchemeDrafts,
    )
    from jirapi.resources.workflow_scheme_project_associations import (
        AsyncWorkflowSchemeProjectAssociations,
        WorkflowSchemeProjectAssociations,
    )
    from jirapi.resources.workflow_schemes import AsyncWorkflowSchemes, WorkflowSchemes
    from jirapi.resources.workflow_status_categories import (
        AsyncWorkflowStatusCategories,
        WorkflowStatusCategories,
    )
    from jirapi.resources.workflow_statuses import AsyncWorkflowStatuses, WorkflowStatuses
    from jirapi.resources.workflow_transition_rules import (
        AsyncWorkflowTransitionRules,
        WorkflowTransitionRules,
    )
    from jirapi.resources.workflows import AsyncWorkflows, Workflows

__all__ = ["Jira", "AsyncJira"]


class Jira(SyncAPIClient):
    """Synchronous Jira Cloud REST API client.

    Usage::

        from jirapi import Jira

        jira = Jira(url="https://acme.atlassian.net", email="me@acme.com", api_token="...")
        issue = jira.issues.get_issue("PROJ-123")

    Or as a context manager::

        with Jira(url="...", email="...", api_token="...") as jira:
            issue = jira.issues.get_issue("PROJ-123")
    """

    def __init__(  # noqa: D107
        self,
        *,
        url: str,
        email: str,
        api_token: str,
        timeout: float = _DEFAULT_TIMEOUT,
        **httpx_client_kwargs: Any,
    ) -> None:
        super().__init__(
            url=url,
            email=email,
            api_token=api_token,
            timeout=timeout,
            **httpx_client_kwargs,
        )

    @cached_property
    def announcement_banner(self) -> AnnouncementBanner:
        from jirapi.resources.announcement_banner import AnnouncementBanner

        return AnnouncementBanner(self)

    @cached_property
    def app_data_policies(self) -> AppDataPolicies:
        from jirapi.resources.app_data_policies import AppDataPolicies

        return AppDataPolicies(self)

    @cached_property
    def app_migration(self) -> AppMigration:
        from jirapi.resources.app_migration import AppMigration

        return AppMigration(self)

    @cached_property
    def app_properties(self) -> AppProperties:
        from jirapi.resources.app_properties import AppProperties

        return AppProperties(self)

    @cached_property
    def application_roles(self) -> ApplicationRoles:
        from jirapi.resources.application_roles import ApplicationRoles

        return ApplicationRoles(self)

    @cached_property
    def audit_records(self) -> AuditRecords:
        from jirapi.resources.audit_records import AuditRecords

        return AuditRecords(self)

    @cached_property
    def avatars(self) -> Avatars:
        from jirapi.resources.avatars import Avatars

        return Avatars(self)

    @cached_property
    def classification_levels(self) -> ClassificationLevels:
        from jirapi.resources.classification_levels import ClassificationLevels

        return ClassificationLevels(self)

    @cached_property
    def dashboards(self) -> Dashboards:
        from jirapi.resources.dashboards import Dashboards

        return Dashboards(self)

    @cached_property
    def dynamic_modules(self) -> DynamicModules:
        from jirapi.resources.dynamic_modules import DynamicModules

        return DynamicModules(self)

    @cached_property
    def field_schemes(self) -> FieldSchemes:
        from jirapi.resources.field_schemes import FieldSchemes

        return FieldSchemes(self)

    @cached_property
    def filter_sharing(self) -> FilterSharing:
        from jirapi.resources.filter_sharing import FilterSharing

        return FilterSharing(self)

    @cached_property
    def filters(self) -> Filters:
        from jirapi.resources.filters import Filters

        return Filters(self)

    @cached_property
    def group_and_user_picker(self) -> GroupAndUserPicker:
        from jirapi.resources.group_and_user_picker import GroupAndUserPicker

        return GroupAndUserPicker(self)

    @cached_property
    def groups(self) -> Groups:
        from jirapi.resources.groups import Groups

        return Groups(self)

    @cached_property
    def issue_attachments(self) -> IssueAttachments:
        from jirapi.resources.issue_attachments import IssueAttachments

        return IssueAttachments(self)

    @cached_property
    def issue_bulk_operations(self) -> IssueBulkOperations:
        from jirapi.resources.issue_bulk_operations import IssueBulkOperations

        return IssueBulkOperations(self)

    @cached_property
    def issue_comment_properties(self) -> IssueCommentProperties:
        from jirapi.resources.issue_comment_properties import IssueCommentProperties

        return IssueCommentProperties(self)

    @cached_property
    def issue_comments(self) -> IssueComments:
        from jirapi.resources.issue_comments import IssueComments

        return IssueComments(self)

    @cached_property
    def issue_custom_field_associations(self) -> IssueCustomFieldAssociations:
        from jirapi.resources.issue_custom_field_associations import IssueCustomFieldAssociations

        return IssueCustomFieldAssociations(self)

    @cached_property
    def issue_custom_field_configuration_apps(self) -> IssueCustomFieldConfigurationApps:
        from jirapi.resources.issue_custom_field_configuration_apps import (
            IssueCustomFieldConfigurationApps,
        )

        return IssueCustomFieldConfigurationApps(self)

    @cached_property
    def issue_custom_field_contexts(self) -> IssueCustomFieldContexts:
        from jirapi.resources.issue_custom_field_contexts import IssueCustomFieldContexts

        return IssueCustomFieldContexts(self)

    @cached_property
    def issue_custom_field_options(self) -> IssueCustomFieldOptions:
        from jirapi.resources.issue_custom_field_options import IssueCustomFieldOptions

        return IssueCustomFieldOptions(self)

    @cached_property
    def issue_custom_field_options_apps(self) -> IssueCustomFieldOptionsApps:
        from jirapi.resources.issue_custom_field_options_apps import IssueCustomFieldOptionsApps

        return IssueCustomFieldOptionsApps(self)

    @cached_property
    def issue_custom_field_values_apps(self) -> IssueCustomFieldValuesApps:
        from jirapi.resources.issue_custom_field_values_apps import IssueCustomFieldValuesApps

        return IssueCustomFieldValuesApps(self)

    @cached_property
    def issue_fields(self) -> IssueFields:
        from jirapi.resources.issue_fields import IssueFields

        return IssueFields(self)

    @cached_property
    def issue_link_types(self) -> IssueLinkTypes:
        from jirapi.resources.issue_link_types import IssueLinkTypes

        return IssueLinkTypes(self)

    @cached_property
    def issue_links(self) -> IssueLinks:
        from jirapi.resources.issue_links import IssueLinks

        return IssueLinks(self)

    @cached_property
    def issue_navigator_settings(self) -> IssueNavigatorSettings:
        from jirapi.resources.issue_navigator_settings import IssueNavigatorSettings

        return IssueNavigatorSettings(self)

    @cached_property
    def issue_notification_schemes(self) -> IssueNotificationSchemes:
        from jirapi.resources.issue_notification_schemes import IssueNotificationSchemes

        return IssueNotificationSchemes(self)

    @cached_property
    def issue_priorities(self) -> IssuePriorities:
        from jirapi.resources.issue_priorities import IssuePriorities

        return IssuePriorities(self)

    @cached_property
    def issue_properties(self) -> IssueProperties:
        from jirapi.resources.issue_properties import IssueProperties

        return IssueProperties(self)

    @cached_property
    def issue_redaction(self) -> IssueRedaction:
        from jirapi.resources.issue_redaction import IssueRedaction

        return IssueRedaction(self)

    @cached_property
    def issue_remote_links(self) -> IssueRemoteLinks:
        from jirapi.resources.issue_remote_links import IssueRemoteLinks

        return IssueRemoteLinks(self)

    @cached_property
    def issue_resolutions(self) -> IssueResolutions:
        from jirapi.resources.issue_resolutions import IssueResolutions

        return IssueResolutions(self)

    @cached_property
    def issue_search(self) -> IssueSearch:
        from jirapi.resources.issue_search import IssueSearch

        return IssueSearch(self)

    @cached_property
    def issue_security_level(self) -> IssueSecurityLevel:
        from jirapi.resources.issue_security_level import IssueSecurityLevel

        return IssueSecurityLevel(self)

    @cached_property
    def issue_security_schemes(self) -> IssueSecuritySchemes:
        from jirapi.resources.issue_security_schemes import IssueSecuritySchemes

        return IssueSecuritySchemes(self)

    @cached_property
    def issue_type_properties(self) -> IssueTypeProperties:
        from jirapi.resources.issue_type_properties import IssueTypeProperties

        return IssueTypeProperties(self)

    @cached_property
    def issue_type_schemes(self) -> IssueTypeSchemes:
        from jirapi.resources.issue_type_schemes import IssueTypeSchemes

        return IssueTypeSchemes(self)

    @cached_property
    def issue_type_screen_schemes(self) -> IssueTypeScreenSchemes:
        from jirapi.resources.issue_type_screen_schemes import IssueTypeScreenSchemes

        return IssueTypeScreenSchemes(self)

    @cached_property
    def issue_types(self) -> IssueTypes:
        from jirapi.resources.issue_types import IssueTypes

        return IssueTypes(self)

    @cached_property
    def issue_votes(self) -> IssueVotes:
        from jirapi.resources.issue_votes import IssueVotes

        return IssueVotes(self)

    @cached_property
    def issue_watchers(self) -> IssueWatchers:
        from jirapi.resources.issue_watchers import IssueWatchers

        return IssueWatchers(self)

    @cached_property
    def issue_worklog_properties(self) -> IssueWorklogProperties:
        from jirapi.resources.issue_worklog_properties import IssueWorklogProperties

        return IssueWorklogProperties(self)

    @cached_property
    def issue_worklogs(self) -> IssueWorklogs:
        from jirapi.resources.issue_worklogs import IssueWorklogs

        return IssueWorklogs(self)

    @cached_property
    def issues(self) -> Issues:
        from jirapi.resources.issues import Issues

        return Issues(self)

    @cached_property
    def jql(self) -> Jql:
        from jirapi.resources.jql import Jql

        return Jql(self)

    @cached_property
    def jql_functions_apps(self) -> JqlFunctionsApps:
        from jirapi.resources.jql_functions_apps import JqlFunctionsApps

        return JqlFunctionsApps(self)

    @cached_property
    def jira_expressions(self) -> JiraExpressions:
        from jirapi.resources.jira_expressions import JiraExpressions

        return JiraExpressions(self)

    @cached_property
    def jira_settings(self) -> JiraSettings:
        from jirapi.resources.jira_settings import JiraSettings

        return JiraSettings(self)

    @cached_property
    def labels(self) -> Labels:
        from jirapi.resources.labels import Labels

        return Labels(self)

    @cached_property
    def license_metrics(self) -> LicenseMetrics:
        from jirapi.resources.license_metrics import LicenseMetrics

        return LicenseMetrics(self)

    @cached_property
    def migration_of_connect_modules_to_forge(self) -> MigrationOfConnectModulesToForge:
        from jirapi.resources.migration_of_connect_modules_to_forge import (
            MigrationOfConnectModulesToForge,
        )

        return MigrationOfConnectModulesToForge(self)

    @cached_property
    def myself(self) -> Myself:
        from jirapi.resources.myself import Myself

        return Myself(self)

    @cached_property
    def permission_schemes(self) -> PermissionSchemes:
        from jirapi.resources.permission_schemes import PermissionSchemes

        return PermissionSchemes(self)

    @cached_property
    def permissions(self) -> Permissions:
        from jirapi.resources.permissions import Permissions

        return Permissions(self)

    @cached_property
    def plans(self) -> Plans:
        from jirapi.resources.plans import Plans

        return Plans(self)

    @cached_property
    def priority_schemes(self) -> PrioritySchemes:
        from jirapi.resources.priority_schemes import PrioritySchemes

        return PrioritySchemes(self)

    @cached_property
    def project_avatars(self) -> ProjectAvatars:
        from jirapi.resources.project_avatars import ProjectAvatars

        return ProjectAvatars(self)

    @cached_property
    def project_categories(self) -> ProjectCategories:
        from jirapi.resources.project_categories import ProjectCategories

        return ProjectCategories(self)

    @cached_property
    def project_classification_levels(self) -> ProjectClassificationLevels:
        from jirapi.resources.project_classification_levels import ProjectClassificationLevels

        return ProjectClassificationLevels(self)

    @cached_property
    def project_components(self) -> ProjectComponents:
        from jirapi.resources.project_components import ProjectComponents

        return ProjectComponents(self)

    @cached_property
    def project_email(self) -> ProjectEmail:
        from jirapi.resources.project_email import ProjectEmail

        return ProjectEmail(self)

    @cached_property
    def project_features(self) -> ProjectFeatures:
        from jirapi.resources.project_features import ProjectFeatures

        return ProjectFeatures(self)

    @cached_property
    def project_key_and_name_validation(self) -> ProjectKeyAndNameValidation:
        from jirapi.resources.project_key_and_name_validation import ProjectKeyAndNameValidation

        return ProjectKeyAndNameValidation(self)

    @cached_property
    def project_permission_schemes(self) -> ProjectPermissionSchemes:
        from jirapi.resources.project_permission_schemes import ProjectPermissionSchemes

        return ProjectPermissionSchemes(self)

    @cached_property
    def project_properties(self) -> ProjectProperties:
        from jirapi.resources.project_properties import ProjectProperties

        return ProjectProperties(self)

    @cached_property
    def project_role_actors(self) -> ProjectRoleActors:
        from jirapi.resources.project_role_actors import ProjectRoleActors

        return ProjectRoleActors(self)

    @cached_property
    def project_roles(self) -> ProjectRoles:
        from jirapi.resources.project_roles import ProjectRoles

        return ProjectRoles(self)

    @cached_property
    def project_templates(self) -> ProjectTemplates:
        from jirapi.resources.project_templates import ProjectTemplates

        return ProjectTemplates(self)

    @cached_property
    def project_types(self) -> ProjectTypes:
        from jirapi.resources.project_types import ProjectTypes

        return ProjectTypes(self)

    @cached_property
    def project_versions(self) -> ProjectVersions:
        from jirapi.resources.project_versions import ProjectVersions

        return ProjectVersions(self)

    @cached_property
    def projects(self) -> Projects:
        from jirapi.resources.projects import Projects

        return Projects(self)

    @cached_property
    def screen_schemes(self) -> ScreenSchemes:
        from jirapi.resources.screen_schemes import ScreenSchemes

        return ScreenSchemes(self)

    @cached_property
    def screen_tab_fields(self) -> ScreenTabFields:
        from jirapi.resources.screen_tab_fields import ScreenTabFields

        return ScreenTabFields(self)

    @cached_property
    def screen_tabs(self) -> ScreenTabs:
        from jirapi.resources.screen_tabs import ScreenTabs

        return ScreenTabs(self)

    @cached_property
    def screens(self) -> Screens:
        from jirapi.resources.screens import Screens

        return Screens(self)

    @cached_property
    def server_info(self) -> ServerInfo:
        from jirapi.resources.server_info import ServerInfo

        return ServerInfo(self)

    @cached_property
    def service_registry(self) -> ServiceRegistry:
        from jirapi.resources.service_registry import ServiceRegistry

        return ServiceRegistry(self)

    @cached_property
    def status(self) -> Status:
        from jirapi.resources.status import Status

        return Status(self)

    @cached_property
    def tasks(self) -> Tasks:
        from jirapi.resources.tasks import Tasks

        return Tasks(self)

    @cached_property
    def teams_in_plan(self) -> TeamsInPlan:
        from jirapi.resources.teams_in_plan import TeamsInPlan

        return TeamsInPlan(self)

    @cached_property
    def time_tracking(self) -> TimeTracking:
        from jirapi.resources.time_tracking import TimeTracking

        return TimeTracking(self)

    @cached_property
    def ui_modifications_apps(self) -> UiModificationsApps:
        from jirapi.resources.ui_modifications_apps import UiModificationsApps

        return UiModificationsApps(self)

    @cached_property
    def user_properties(self) -> UserProperties:
        from jirapi.resources.user_properties import UserProperties

        return UserProperties(self)

    @cached_property
    def user_search(self) -> UserSearch:
        from jirapi.resources.user_search import UserSearch

        return UserSearch(self)

    @cached_property
    def users(self) -> Users:
        from jirapi.resources.users import Users

        return Users(self)

    @cached_property
    def webhooks(self) -> Webhooks:
        from jirapi.resources.webhooks import Webhooks

        return Webhooks(self)

    @cached_property
    def workflow_scheme_drafts(self) -> WorkflowSchemeDrafts:
        from jirapi.resources.workflow_scheme_drafts import WorkflowSchemeDrafts

        return WorkflowSchemeDrafts(self)

    @cached_property
    def workflow_scheme_project_associations(self) -> WorkflowSchemeProjectAssociations:
        from jirapi.resources.workflow_scheme_project_associations import (
            WorkflowSchemeProjectAssociations,
        )

        return WorkflowSchemeProjectAssociations(self)

    @cached_property
    def workflow_schemes(self) -> WorkflowSchemes:
        from jirapi.resources.workflow_schemes import WorkflowSchemes

        return WorkflowSchemes(self)

    @cached_property
    def workflow_status_categories(self) -> WorkflowStatusCategories:
        from jirapi.resources.workflow_status_categories import WorkflowStatusCategories

        return WorkflowStatusCategories(self)

    @cached_property
    def workflow_statuses(self) -> WorkflowStatuses:
        from jirapi.resources.workflow_statuses import WorkflowStatuses

        return WorkflowStatuses(self)

    @cached_property
    def workflow_transition_rules(self) -> WorkflowTransitionRules:
        from jirapi.resources.workflow_transition_rules import WorkflowTransitionRules

        return WorkflowTransitionRules(self)

    @cached_property
    def workflows(self) -> Workflows:
        from jirapi.resources.workflows import Workflows

        return Workflows(self)

    @cached_property
    def untagged(self) -> Untagged:
        from jirapi.resources.untagged import Untagged

        return Untagged(self)


class AsyncJira(AsyncAPIClient):
    """Asynchronous Jira Cloud REST API client.

    Usage::

        from jirapi import AsyncJira

        async with AsyncJira(
            url="https://acme.atlassian.net", email="me@acme.com", api_token="..."
        ) as jira:
            issue = await jira.issues.get_issue("PROJ-123")
    """

    def __init__(  # noqa: D107
        self,
        *,
        url: str,
        email: str,
        api_token: str,
        timeout: float = _DEFAULT_TIMEOUT,
        **httpx_client_kwargs: Any,
    ) -> None:
        super().__init__(
            url=url,
            email=email,
            api_token=api_token,
            timeout=timeout,
            **httpx_client_kwargs,
        )

    @cached_property
    def announcement_banner(self) -> AsyncAnnouncementBanner:
        from jirapi.resources.announcement_banner import AsyncAnnouncementBanner

        return AsyncAnnouncementBanner(self)

    @cached_property
    def app_data_policies(self) -> AsyncAppDataPolicies:
        from jirapi.resources.app_data_policies import AsyncAppDataPolicies

        return AsyncAppDataPolicies(self)

    @cached_property
    def app_migration(self) -> AsyncAppMigration:
        from jirapi.resources.app_migration import AsyncAppMigration

        return AsyncAppMigration(self)

    @cached_property
    def app_properties(self) -> AsyncAppProperties:
        from jirapi.resources.app_properties import AsyncAppProperties

        return AsyncAppProperties(self)

    @cached_property
    def application_roles(self) -> AsyncApplicationRoles:
        from jirapi.resources.application_roles import AsyncApplicationRoles

        return AsyncApplicationRoles(self)

    @cached_property
    def audit_records(self) -> AsyncAuditRecords:
        from jirapi.resources.audit_records import AsyncAuditRecords

        return AsyncAuditRecords(self)

    @cached_property
    def avatars(self) -> AsyncAvatars:
        from jirapi.resources.avatars import AsyncAvatars

        return AsyncAvatars(self)

    @cached_property
    def classification_levels(self) -> AsyncClassificationLevels:
        from jirapi.resources.classification_levels import AsyncClassificationLevels

        return AsyncClassificationLevels(self)

    @cached_property
    def dashboards(self) -> AsyncDashboards:
        from jirapi.resources.dashboards import AsyncDashboards

        return AsyncDashboards(self)

    @cached_property
    def dynamic_modules(self) -> AsyncDynamicModules:
        from jirapi.resources.dynamic_modules import AsyncDynamicModules

        return AsyncDynamicModules(self)

    @cached_property
    def field_schemes(self) -> AsyncFieldSchemes:
        from jirapi.resources.field_schemes import AsyncFieldSchemes

        return AsyncFieldSchemes(self)

    @cached_property
    def filter_sharing(self) -> AsyncFilterSharing:
        from jirapi.resources.filter_sharing import AsyncFilterSharing

        return AsyncFilterSharing(self)

    @cached_property
    def filters(self) -> AsyncFilters:
        from jirapi.resources.filters import AsyncFilters

        return AsyncFilters(self)

    @cached_property
    def group_and_user_picker(self) -> AsyncGroupAndUserPicker:
        from jirapi.resources.group_and_user_picker import AsyncGroupAndUserPicker

        return AsyncGroupAndUserPicker(self)

    @cached_property
    def groups(self) -> AsyncGroups:
        from jirapi.resources.groups import AsyncGroups

        return AsyncGroups(self)

    @cached_property
    def issue_attachments(self) -> AsyncIssueAttachments:
        from jirapi.resources.issue_attachments import AsyncIssueAttachments

        return AsyncIssueAttachments(self)

    @cached_property
    def issue_bulk_operations(self) -> AsyncIssueBulkOperations:
        from jirapi.resources.issue_bulk_operations import AsyncIssueBulkOperations

        return AsyncIssueBulkOperations(self)

    @cached_property
    def issue_comment_properties(self) -> AsyncIssueCommentProperties:
        from jirapi.resources.issue_comment_properties import AsyncIssueCommentProperties

        return AsyncIssueCommentProperties(self)

    @cached_property
    def issue_comments(self) -> AsyncIssueComments:
        from jirapi.resources.issue_comments import AsyncIssueComments

        return AsyncIssueComments(self)

    @cached_property
    def issue_custom_field_associations(self) -> AsyncIssueCustomFieldAssociations:
        from jirapi.resources.issue_custom_field_associations import (
            AsyncIssueCustomFieldAssociations,
        )

        return AsyncIssueCustomFieldAssociations(self)

    @cached_property
    def issue_custom_field_configuration_apps(self) -> AsyncIssueCustomFieldConfigurationApps:
        from jirapi.resources.issue_custom_field_configuration_apps import (
            AsyncIssueCustomFieldConfigurationApps,
        )

        return AsyncIssueCustomFieldConfigurationApps(self)

    @cached_property
    def issue_custom_field_contexts(self) -> AsyncIssueCustomFieldContexts:
        from jirapi.resources.issue_custom_field_contexts import AsyncIssueCustomFieldContexts

        return AsyncIssueCustomFieldContexts(self)

    @cached_property
    def issue_custom_field_options(self) -> AsyncIssueCustomFieldOptions:
        from jirapi.resources.issue_custom_field_options import AsyncIssueCustomFieldOptions

        return AsyncIssueCustomFieldOptions(self)

    @cached_property
    def issue_custom_field_options_apps(self) -> AsyncIssueCustomFieldOptionsApps:
        from jirapi.resources.issue_custom_field_options_apps import (
            AsyncIssueCustomFieldOptionsApps,
        )

        return AsyncIssueCustomFieldOptionsApps(self)

    @cached_property
    def issue_custom_field_values_apps(self) -> AsyncIssueCustomFieldValuesApps:
        from jirapi.resources.issue_custom_field_values_apps import AsyncIssueCustomFieldValuesApps

        return AsyncIssueCustomFieldValuesApps(self)

    @cached_property
    def issue_fields(self) -> AsyncIssueFields:
        from jirapi.resources.issue_fields import AsyncIssueFields

        return AsyncIssueFields(self)

    @cached_property
    def issue_link_types(self) -> AsyncIssueLinkTypes:
        from jirapi.resources.issue_link_types import AsyncIssueLinkTypes

        return AsyncIssueLinkTypes(self)

    @cached_property
    def issue_links(self) -> AsyncIssueLinks:
        from jirapi.resources.issue_links import AsyncIssueLinks

        return AsyncIssueLinks(self)

    @cached_property
    def issue_navigator_settings(self) -> AsyncIssueNavigatorSettings:
        from jirapi.resources.issue_navigator_settings import AsyncIssueNavigatorSettings

        return AsyncIssueNavigatorSettings(self)

    @cached_property
    def issue_notification_schemes(self) -> AsyncIssueNotificationSchemes:
        from jirapi.resources.issue_notification_schemes import AsyncIssueNotificationSchemes

        return AsyncIssueNotificationSchemes(self)

    @cached_property
    def issue_priorities(self) -> AsyncIssuePriorities:
        from jirapi.resources.issue_priorities import AsyncIssuePriorities

        return AsyncIssuePriorities(self)

    @cached_property
    def issue_properties(self) -> AsyncIssueProperties:
        from jirapi.resources.issue_properties import AsyncIssueProperties

        return AsyncIssueProperties(self)

    @cached_property
    def issue_redaction(self) -> AsyncIssueRedaction:
        from jirapi.resources.issue_redaction import AsyncIssueRedaction

        return AsyncIssueRedaction(self)

    @cached_property
    def issue_remote_links(self) -> AsyncIssueRemoteLinks:
        from jirapi.resources.issue_remote_links import AsyncIssueRemoteLinks

        return AsyncIssueRemoteLinks(self)

    @cached_property
    def issue_resolutions(self) -> AsyncIssueResolutions:
        from jirapi.resources.issue_resolutions import AsyncIssueResolutions

        return AsyncIssueResolutions(self)

    @cached_property
    def issue_search(self) -> AsyncIssueSearch:
        from jirapi.resources.issue_search import AsyncIssueSearch

        return AsyncIssueSearch(self)

    @cached_property
    def issue_security_level(self) -> AsyncIssueSecurityLevel:
        from jirapi.resources.issue_security_level import AsyncIssueSecurityLevel

        return AsyncIssueSecurityLevel(self)

    @cached_property
    def issue_security_schemes(self) -> AsyncIssueSecuritySchemes:
        from jirapi.resources.issue_security_schemes import AsyncIssueSecuritySchemes

        return AsyncIssueSecuritySchemes(self)

    @cached_property
    def issue_type_properties(self) -> AsyncIssueTypeProperties:
        from jirapi.resources.issue_type_properties import AsyncIssueTypeProperties

        return AsyncIssueTypeProperties(self)

    @cached_property
    def issue_type_schemes(self) -> AsyncIssueTypeSchemes:
        from jirapi.resources.issue_type_schemes import AsyncIssueTypeSchemes

        return AsyncIssueTypeSchemes(self)

    @cached_property
    def issue_type_screen_schemes(self) -> AsyncIssueTypeScreenSchemes:
        from jirapi.resources.issue_type_screen_schemes import AsyncIssueTypeScreenSchemes

        return AsyncIssueTypeScreenSchemes(self)

    @cached_property
    def issue_types(self) -> AsyncIssueTypes:
        from jirapi.resources.issue_types import AsyncIssueTypes

        return AsyncIssueTypes(self)

    @cached_property
    def issue_votes(self) -> AsyncIssueVotes:
        from jirapi.resources.issue_votes import AsyncIssueVotes

        return AsyncIssueVotes(self)

    @cached_property
    def issue_watchers(self) -> AsyncIssueWatchers:
        from jirapi.resources.issue_watchers import AsyncIssueWatchers

        return AsyncIssueWatchers(self)

    @cached_property
    def issue_worklog_properties(self) -> AsyncIssueWorklogProperties:
        from jirapi.resources.issue_worklog_properties import AsyncIssueWorklogProperties

        return AsyncIssueWorklogProperties(self)

    @cached_property
    def issue_worklogs(self) -> AsyncIssueWorklogs:
        from jirapi.resources.issue_worklogs import AsyncIssueWorklogs

        return AsyncIssueWorklogs(self)

    @cached_property
    def issues(self) -> AsyncIssues:
        from jirapi.resources.issues import AsyncIssues

        return AsyncIssues(self)

    @cached_property
    def jql(self) -> AsyncJql:
        from jirapi.resources.jql import AsyncJql

        return AsyncJql(self)

    @cached_property
    def jql_functions_apps(self) -> AsyncJqlFunctionsApps:
        from jirapi.resources.jql_functions_apps import AsyncJqlFunctionsApps

        return AsyncJqlFunctionsApps(self)

    @cached_property
    def jira_expressions(self) -> AsyncJiraExpressions:
        from jirapi.resources.jira_expressions import AsyncJiraExpressions

        return AsyncJiraExpressions(self)

    @cached_property
    def jira_settings(self) -> AsyncJiraSettings:
        from jirapi.resources.jira_settings import AsyncJiraSettings

        return AsyncJiraSettings(self)

    @cached_property
    def labels(self) -> AsyncLabels:
        from jirapi.resources.labels import AsyncLabels

        return AsyncLabels(self)

    @cached_property
    def license_metrics(self) -> AsyncLicenseMetrics:
        from jirapi.resources.license_metrics import AsyncLicenseMetrics

        return AsyncLicenseMetrics(self)

    @cached_property
    def migration_of_connect_modules_to_forge(self) -> AsyncMigrationOfConnectModulesToForge:
        from jirapi.resources.migration_of_connect_modules_to_forge import (
            AsyncMigrationOfConnectModulesToForge,
        )

        return AsyncMigrationOfConnectModulesToForge(self)

    @cached_property
    def myself(self) -> AsyncMyself:
        from jirapi.resources.myself import AsyncMyself

        return AsyncMyself(self)

    @cached_property
    def permission_schemes(self) -> AsyncPermissionSchemes:
        from jirapi.resources.permission_schemes import AsyncPermissionSchemes

        return AsyncPermissionSchemes(self)

    @cached_property
    def permissions(self) -> AsyncPermissions:
        from jirapi.resources.permissions import AsyncPermissions

        return AsyncPermissions(self)

    @cached_property
    def plans(self) -> AsyncPlans:
        from jirapi.resources.plans import AsyncPlans

        return AsyncPlans(self)

    @cached_property
    def priority_schemes(self) -> AsyncPrioritySchemes:
        from jirapi.resources.priority_schemes import AsyncPrioritySchemes

        return AsyncPrioritySchemes(self)

    @cached_property
    def project_avatars(self) -> AsyncProjectAvatars:
        from jirapi.resources.project_avatars import AsyncProjectAvatars

        return AsyncProjectAvatars(self)

    @cached_property
    def project_categories(self) -> AsyncProjectCategories:
        from jirapi.resources.project_categories import AsyncProjectCategories

        return AsyncProjectCategories(self)

    @cached_property
    def project_classification_levels(self) -> AsyncProjectClassificationLevels:
        from jirapi.resources.project_classification_levels import AsyncProjectClassificationLevels

        return AsyncProjectClassificationLevels(self)

    @cached_property
    def project_components(self) -> AsyncProjectComponents:
        from jirapi.resources.project_components import AsyncProjectComponents

        return AsyncProjectComponents(self)

    @cached_property
    def project_email(self) -> AsyncProjectEmail:
        from jirapi.resources.project_email import AsyncProjectEmail

        return AsyncProjectEmail(self)

    @cached_property
    def project_features(self) -> AsyncProjectFeatures:
        from jirapi.resources.project_features import AsyncProjectFeatures

        return AsyncProjectFeatures(self)

    @cached_property
    def project_key_and_name_validation(self) -> AsyncProjectKeyAndNameValidation:
        from jirapi.resources.project_key_and_name_validation import (
            AsyncProjectKeyAndNameValidation,
        )

        return AsyncProjectKeyAndNameValidation(self)

    @cached_property
    def project_permission_schemes(self) -> AsyncProjectPermissionSchemes:
        from jirapi.resources.project_permission_schemes import AsyncProjectPermissionSchemes

        return AsyncProjectPermissionSchemes(self)

    @cached_property
    def project_properties(self) -> AsyncProjectProperties:
        from jirapi.resources.project_properties import AsyncProjectProperties

        return AsyncProjectProperties(self)

    @cached_property
    def project_role_actors(self) -> AsyncProjectRoleActors:
        from jirapi.resources.project_role_actors import AsyncProjectRoleActors

        return AsyncProjectRoleActors(self)

    @cached_property
    def project_roles(self) -> AsyncProjectRoles:
        from jirapi.resources.project_roles import AsyncProjectRoles

        return AsyncProjectRoles(self)

    @cached_property
    def project_templates(self) -> AsyncProjectTemplates:
        from jirapi.resources.project_templates import AsyncProjectTemplates

        return AsyncProjectTemplates(self)

    @cached_property
    def project_types(self) -> AsyncProjectTypes:
        from jirapi.resources.project_types import AsyncProjectTypes

        return AsyncProjectTypes(self)

    @cached_property
    def project_versions(self) -> AsyncProjectVersions:
        from jirapi.resources.project_versions import AsyncProjectVersions

        return AsyncProjectVersions(self)

    @cached_property
    def projects(self) -> AsyncProjects:
        from jirapi.resources.projects import AsyncProjects

        return AsyncProjects(self)

    @cached_property
    def screen_schemes(self) -> AsyncScreenSchemes:
        from jirapi.resources.screen_schemes import AsyncScreenSchemes

        return AsyncScreenSchemes(self)

    @cached_property
    def screen_tab_fields(self) -> AsyncScreenTabFields:
        from jirapi.resources.screen_tab_fields import AsyncScreenTabFields

        return AsyncScreenTabFields(self)

    @cached_property
    def screen_tabs(self) -> AsyncScreenTabs:
        from jirapi.resources.screen_tabs import AsyncScreenTabs

        return AsyncScreenTabs(self)

    @cached_property
    def screens(self) -> AsyncScreens:
        from jirapi.resources.screens import AsyncScreens

        return AsyncScreens(self)

    @cached_property
    def server_info(self) -> AsyncServerInfo:
        from jirapi.resources.server_info import AsyncServerInfo

        return AsyncServerInfo(self)

    @cached_property
    def service_registry(self) -> AsyncServiceRegistry:
        from jirapi.resources.service_registry import AsyncServiceRegistry

        return AsyncServiceRegistry(self)

    @cached_property
    def status(self) -> AsyncStatus:
        from jirapi.resources.status import AsyncStatus

        return AsyncStatus(self)

    @cached_property
    def tasks(self) -> AsyncTasks:
        from jirapi.resources.tasks import AsyncTasks

        return AsyncTasks(self)

    @cached_property
    def teams_in_plan(self) -> AsyncTeamsInPlan:
        from jirapi.resources.teams_in_plan import AsyncTeamsInPlan

        return AsyncTeamsInPlan(self)

    @cached_property
    def time_tracking(self) -> AsyncTimeTracking:
        from jirapi.resources.time_tracking import AsyncTimeTracking

        return AsyncTimeTracking(self)

    @cached_property
    def ui_modifications_apps(self) -> AsyncUiModificationsApps:
        from jirapi.resources.ui_modifications_apps import AsyncUiModificationsApps

        return AsyncUiModificationsApps(self)

    @cached_property
    def user_properties(self) -> AsyncUserProperties:
        from jirapi.resources.user_properties import AsyncUserProperties

        return AsyncUserProperties(self)

    @cached_property
    def user_search(self) -> AsyncUserSearch:
        from jirapi.resources.user_search import AsyncUserSearch

        return AsyncUserSearch(self)

    @cached_property
    def users(self) -> AsyncUsers:
        from jirapi.resources.users import AsyncUsers

        return AsyncUsers(self)

    @cached_property
    def webhooks(self) -> AsyncWebhooks:
        from jirapi.resources.webhooks import AsyncWebhooks

        return AsyncWebhooks(self)

    @cached_property
    def workflow_scheme_drafts(self) -> AsyncWorkflowSchemeDrafts:
        from jirapi.resources.workflow_scheme_drafts import AsyncWorkflowSchemeDrafts

        return AsyncWorkflowSchemeDrafts(self)

    @cached_property
    def workflow_scheme_project_associations(self) -> AsyncWorkflowSchemeProjectAssociations:
        from jirapi.resources.workflow_scheme_project_associations import (
            AsyncWorkflowSchemeProjectAssociations,
        )

        return AsyncWorkflowSchemeProjectAssociations(self)

    @cached_property
    def workflow_schemes(self) -> AsyncWorkflowSchemes:
        from jirapi.resources.workflow_schemes import AsyncWorkflowSchemes

        return AsyncWorkflowSchemes(self)

    @cached_property
    def workflow_status_categories(self) -> AsyncWorkflowStatusCategories:
        from jirapi.resources.workflow_status_categories import AsyncWorkflowStatusCategories

        return AsyncWorkflowStatusCategories(self)

    @cached_property
    def workflow_statuses(self) -> AsyncWorkflowStatuses:
        from jirapi.resources.workflow_statuses import AsyncWorkflowStatuses

        return AsyncWorkflowStatuses(self)

    @cached_property
    def workflow_transition_rules(self) -> AsyncWorkflowTransitionRules:
        from jirapi.resources.workflow_transition_rules import AsyncWorkflowTransitionRules

        return AsyncWorkflowTransitionRules(self)

    @cached_property
    def workflows(self) -> AsyncWorkflows:
        from jirapi.resources.workflows import AsyncWorkflows

        return AsyncWorkflows(self)

    @cached_property
    def untagged(self) -> AsyncUntagged:
        from jirapi.resources.untagged import AsyncUntagged

        return AsyncUntagged(self)
