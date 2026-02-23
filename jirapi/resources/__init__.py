"""Generated resource classes for the Jira Cloud REST API."""

from jirapi.resources.announcement_banner import AnnouncementBanner, AsyncAnnouncementBanner
from jirapi.resources.app_data_policies import AppDataPolicies, AsyncAppDataPolicies
from jirapi.resources.app_migration import AppMigration, AsyncAppMigration
from jirapi.resources.app_properties import AppProperties, AsyncAppProperties
from jirapi.resources.application_roles import ApplicationRoles, AsyncApplicationRoles
from jirapi.resources.audit_records import AsyncAuditRecords, AuditRecords
from jirapi.resources.avatars import AsyncAvatars, Avatars
from jirapi.resources.classification_levels import AsyncClassificationLevels, ClassificationLevels
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
from jirapi.resources.issue_security_schemes import AsyncIssueSecuritySchemes, IssueSecuritySchemes
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
from jirapi.resources.workflow_scheme_drafts import AsyncWorkflowSchemeDrafts, WorkflowSchemeDrafts
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
