#!/usr/bin/env python3
"""Generate sync + async resource classes from the Jira Cloud OpenAPI spec.

Reads the OpenAPI JSON, groups operations by consolidated resource groups, and
emits per-group packages under ``jirapi/<group>/`` with core ``_resource.py``
and optional sub-resource modules.  Also regenerates ``jirapi/client.py``.

Usage::

    uv run python scripts/generate_resources.py
"""

from __future__ import annotations

from collections import Counter, defaultdict
import json
import logging
from pathlib import Path
import re
import shutil
import subprocess
import textwrap
from typing import Any


logger = logging.getLogger(__name__)


REPO_ROOT = Path(__file__).resolve().parent.parent
OPENAPI_SPEC = REPO_ROOT / "docs" / "jira-cloud-api-openapi.json"
JIRAPI_DIR = REPO_ROOT / "jirapi"
CLIENT_FILE = JIRAPI_DIR / "client.py"

# ──────────────────────────────────────────────────────────────────────
# Tag consolidation map
#
# Maps each OpenAPI tag → (group, sub_resource | None).
# Tags with sub_resource=None merge into the group's core _resource.py.
# Tags with a sub_resource value become a separate file in the group package.
# ──────────────────────────────────────────────────────────────────────

TAG_CONSOLIDATION: dict[str, tuple[str, str | None]] = {
    # ── issues (core) ──
    "Issues": ("issues", None),
    "Issue search": ("issues", None),
    "Issue bulk operations": ("issues", None),
    "Issue navigator settings": ("issues", None),
    "Issue redaction": ("issues", None),
    # ── issues (sub-resources) ──
    "Issue comments": ("issues", "comments"),
    "Issue comment properties": ("issues", "comment_properties"),
    "Issue attachments": ("issues", "attachments"),
    "Issue worklogs": ("issues", "worklogs"),
    "Issue worklog properties": ("issues", "worklog_properties"),
    "Issue votes": ("issues", "votes"),
    "Issue watchers": ("issues", "watchers"),
    "Issue links": ("issues", "links"),
    "Issue remote links": ("issues", "remote_links"),
    "Issue properties": ("issues", "properties"),
    "untagged": ("issues", "worklogs"),
    # ── projects (core — includes email/features/classification/validation) ──
    "Projects": ("projects", None),
    "Project email": ("projects", None),
    "Project features": ("projects", None),
    "Project classification levels": ("projects", None),
    "Project key and name validation": ("projects", None),
    # ── projects (sub-resources) ──
    "Project avatars": ("projects", "avatars"),
    "Project components": ("projects", "components"),
    "Project versions": ("projects", "versions"),
    "Project properties": ("projects", "properties"),
    "Project roles": ("projects", "roles"),
    "Project role actors": ("projects", "roles"),
    "Project categories": ("projects", "categories"),
    "Project templates": ("projects", "templates"),
    "Project types": ("projects", "types"),
    "Project permission schemes": ("projects", "permission_schemes"),
    # ── fields ──
    "Issue fields": ("fields", None),
    "Field schemes": ("fields", None),
    "Issue custom field contexts": ("fields", "custom_field_contexts"),
    "Issue custom field options": ("fields", "custom_field_options"),
    "Issue custom field options (apps)": ("fields", "custom_field_options_apps"),
    "Issue custom field values (apps)": ("fields", "custom_field_values_apps"),
    "Issue custom field configuration (apps)": ("fields", "custom_field_config_apps"),
    "Issue custom field associations": ("fields", "custom_field_associations"),
    # ── screens ──
    "Screens": ("screens", None),
    "Screen schemes": ("screens", "schemes"),
    "Screen tabs": ("screens", "tabs"),
    "Screen tab fields": ("screens", "tab_fields"),
    "Issue type screen schemes": ("screens", "issue_type_screen_schemes"),
    # ── workflows ──
    "Workflows": ("workflows", None),
    "Workflow schemes": ("workflows", "schemes"),
    "Workflow scheme drafts": ("workflows", "scheme_drafts"),
    "Workflow scheme project associations": ("workflows", "scheme_project_associations"),
    "Workflow transition rules": ("workflows", "transition_rules"),
    "Workflow statuses": ("workflows", "statuses"),
    "Workflow status categories": ("workflows", "status_categories"),
    # ── users ──
    "Users": ("users", None),
    "User search": ("users", None),
    "Group and user picker": ("users", None),
    "Myself": ("users", None),
    "User properties": ("users", "properties"),
    # ── permissions ──
    "Permissions": ("permissions", None),
    "Permission schemes": ("permissions", None),
    # ── issue_types ──
    "Issue types": ("issue_types", None),
    "Issue type schemes": ("issue_types", None),
    "Issue type properties": ("issue_types", None),
    # ── priorities ──
    "Issue priorities": ("priorities", None),
    "Priority schemes": ("priorities", None),
    # ── security_schemes ──
    "Issue security level": ("security_schemes", None),
    "Issue security schemes": ("security_schemes", None),
    # ── jql ──
    "JQL": ("jql", None),
    "JQL functions (apps)": ("jql", None),
    # ── plans ──
    "Plans": ("plans", None),
    "Teams in plan": ("plans", "teams"),
    # ── standalone groups ──
    "Filters": ("filters", None),
    "Filter sharing": ("filters", None),
    "Dashboards": ("dashboards", None),
    "Groups": ("groups", None),
    "Issue resolutions": ("resolutions", None),
    "Status": ("statuses", None),
    "Issue notification schemes": ("notification_schemes", None),
    "Webhooks": ("webhooks", None),
    "Server info": ("server_info", None),
    "Jira settings": ("settings", None),
    "Labels": ("labels", None),
    "Tasks": ("tasks", None),
    "Time tracking": ("time_tracking", None),
    "License metrics": ("license_metrics", None),
    "Audit records": ("audit_records", None),
    "Avatars": ("avatars", None),
    "Application roles": ("application_roles", None),
    "Classification levels": ("classification_levels", None),
    "Announcement banner": ("announcement_banner", None),
    "Issue link types": ("issue_link_types", None),
    "Jira expressions": ("jira_expressions", None),
    "App properties": ("app_properties", None),
    "App migration": ("app_migration", None),
    "App data policies": ("app_data_policies", None),
    "Dynamic modules": ("dynamic_modules", None),
    "UI modifications (apps)": ("ui_modifications", None),
    "Service Registry": ("service_registry", None),
    "Migration of Connect modules to Forge": ("connect_migration", None),
}

# ──────────────────────────────────────────────────────────────────────
# Method name overrides  (operationId → desired method name)
#
# Applied BEFORE auto-stripping.  Use for names that auto-strip can't
# produce or where the OpenAPI operationId is misleading.
# ──────────────────────────────────────────────────────────────────────

METHOD_NAME_OVERRIDES: dict[str, str] = {
    # ── Issues core ──
    "searchAndReconsileIssuesUsingJql": "search",
    "searchAndReconsileIssuesUsingJqlPost": "search_post",
    "doTransition": "transition",
    "getIssuePickerResource": "picker_suggestions",
    "createIssues": "create_bulk",
    "getCreateIssueMeta": "get_create_meta",
    # ── Issue comments ──
    "getComments": "list",
    "getComment": "get",
    "getCommentsByIds": "get_by_ids",
    # ── Issue attachments ──
    "addAttachment": "add",
    # ── Issue worklogs ──
    "getIssueWorklog": "list",
    "getWorklogsForIds": "get_by_ids",
    "getIdsOfWorklogsDeletedSince": "get_deleted_ids",
    "getIdsOfWorklogsModifiedSince": "get_modified_ids",
    "getWorklogsByIssueIdAndWorklogId": "get_by_ids_legacy",
    # ── Issue votes ──
    "getVotes": "list",
    # ── Issue watchers ──
    "getIsWatchingIssueBulk": "is_watching_bulk",
    "getIssueWatchers": "list",
    # ── Issue links ──
    "linkIssues": "create",
    "getIssueLink": "get",
    "deleteIssueLink": "delete",
    # ── Issue remote links ──
    "getRemoteIssueLinks": "list",
    "createOrUpdateRemoteIssueLink": "create_or_update",
    "deleteRemoteIssueLinkByGlobalId": "delete_by_global_id",
    "getRemoteIssueLinkById": "get_by_id",
    "deleteRemoteIssueLinkById": "delete_by_id",
    "updateRemoteIssueLink": "update",
    # ── Issue properties ──
    "bulkSetIssuesPropertiesList": "bulk_set_by_list",
    "bulkSetIssuePropertiesByIssue": "bulk_set_by_issue",
    # ── Issue comment properties ──
    "getCommentPropertyKeys": "get_keys",
    "getCommentProperty": "get",
    "setCommentProperty": "set",
    "deleteCommentProperty": "delete",
    # ── Issue worklog properties ──
    "getWorklogPropertyKeys": "get_keys",
    "getWorklogProperty": "get",
    "setWorklogProperty": "set",
    "deleteWorklogProperty": "delete",
    # ── Projects core ──
    "searchProjects": "search",
    "deleteProjectAsynchronously": "delete_async",
    "getAllStatuses": "get_all_statuses",
    "getHierarchy": "get_hierarchy",
    "getNotificationSchemeForProject": "get_notification_scheme",
    "getFeaturesForProject": "get_features",
    "toggleFeatureForProject": "toggle_feature",
    "getProjectEmail": "get_email",
    "updateProjectEmail": "update_email",
    "removeDefaultProjectClassification": "remove_default_classification",
    "getDefaultProjectClassification": "get_default_classification",
    "updateDefaultProjectClassification": "update_default_classification",
    "validateProjectKey": "validate_key",
    "getValidProjectKey": "get_valid_key",
    "getValidProjectName": "get_valid_name",
    # ── Project roles (merges roles + role actors) ──
    "getProjectRoles": "list",
    "getProjectRole": "get",
    "getProjectRoleDetails": "get_details",
    "getAllProjectRoles": "get_all",
    "createProjectRole": "create",
    "deleteProjectRole": "delete",
    "getProjectRoleById": "get_by_id",
    "partialUpdateProjectRole": "partial_update",
    "fullyUpdateProjectRole": "full_update",
    "deleteActor": "delete_actor",
    "addActorUsers": "add_actors",
    "setActors": "set_actors",
    "deleteProjectRoleActorsFromRole": "delete_actors_from_role",
    "getProjectRoleActorsForRole": "get_actors_for_role",
    "addProjectRoleActorsToRole": "add_actors_to_role",
    # ── Project versions ──
    "getProjectVersionsPaginated": "list",
    "getProjectVersions": "list_all",
    "getVersionRelatedIssues": "get_related_issues",
    "getRelatedWork": "get_related_work",
    "createRelatedWork": "create_related_work",
    "updateRelatedWork": "update_related_work",
    "deleteAndReplaceVersion": "delete_and_replace",
    "getVersionUnresolvedIssues": "get_unresolved_issues",
    "deleteRelatedWork": "delete_related_work",
    # ── Project components ──
    "findComponentsForProjects": "find_for_projects",
    "getComponentRelatedIssues": "get_related_issues",
    "getProjectComponentsPaginated": "list",
    "getProjectComponents": "list_all",
    # ── Project avatars ──
    "updateProjectAvatar": "update",
    "deleteProjectAvatar": "delete",
    "createProjectAvatar": "create",
    "getAllProjectAvatars": "list",
    # ── Project properties ──
    "getProjectPropertyKeys": "get_keys",
    "deleteProjectProperty": "delete",
    "getProjectProperty": "get",
    "setProjectProperty": "set",
    # ── Project categories ──
    "getAllProjectCategories": "list",
    "createProjectCategory": "create",
    "removeProjectCategory": "remove",
    "getProjectCategoryById": "get_by_id",
    "updateProjectCategory": "update",
    # ── Project templates ──
    "createProjectWithCustomTemplate": "create_with_template",
    "editTemplate": "edit",
    "liveTemplate": "go_live",
    "removeTemplate": "remove",
    "saveTemplate": "save",
    # ── Project types ──
    "getAllProjectTypes": "list",
    "getAllAccessibleProjectTypes": "list_accessible",
    "getProjectTypeByKey": "get_by_key",
    "getAccessibleProjectTypeByKey": "get_accessible_by_key",
    # ── Project permission schemes ──
    "getProjectIssueSecurityScheme": "get_issue_security_scheme",
    "getAssignedPermissionScheme": "get_assigned",
    "assignPermissionScheme": "assign",
    "getSecurityLevelsForProject": "get_security_levels",
    # ── Users core ──
    "getAllUsersDefault": "list",
    "getAllUsers": "list_all",
    "findBulkAssignableUsers": "find_bulk_assignable",
    "findAssignableUsers": "find_assignable",
    "findUsersWithAllPermissions": "find_with_permissions",
    "findUsersForPicker": "find_for_picker",
    "findUsers": "find",
    "findUsersByQuery": "find_by_query",
    "findUserKeysByQuery": "find_keys_by_query",
    "findUsersWithBrowsePermission": "find_with_browse_permission",
    "findUsersAndGroups": "find_users_and_groups",
    "removePreference": "remove_preference",
    "getPreference": "get_preference",
    "setPreference": "set_preference",
    "getLocale": "get_locale",
    "getCurrentUser": "get_current_user",
    # ── User properties ──
    "getUserPropertyKeys": "get_keys",
    "deleteUserProperty": "delete",
    "getUserProperty": "get",
    "setUserProperty": "set",
    # ── Filters ──
    "getFiltersPaginated": "list",
    "getFavouriteFilters": "get_favourites",
    "getMyFilters": "get_mine",
    "deleteFavouriteForFilter": "remove_favourite",
    "setFavouriteForFilter": "add_favourite",
    "changeFilterOwner": "change_owner",
    "resetColumns": "reset_columns",
    "getColumns": "get_columns",
    "setColumns": "set_columns",
    "getDefaultShareScope": "get_default_share_scope",
    "setDefaultShareScope": "set_default_share_scope",
    "getSharePermissions": "get_share_permissions",
    "addSharePermission": "add_share_permission",
    "deleteSharePermission": "delete_share_permission",
    "getSharePermission": "get_share_permission",
    # ── Workflows core ──
    "readWorkflowFromHistory": "read_from_history",
    "listWorkflowHistory": "list_history",
    "deleteInactiveWorkflow": "delete_inactive",
    "getWorkflowProjectIssueTypeUsages": "get_project_issue_type_usages",
    "getProjectUsagesForWorkflow": "get_project_usages",
    "getWorkflowSchemeUsagesForWorkflow": "get_scheme_usages",
    "readWorkflows": "read",
    "workflowCapabilities": "get_capabilities",
    "createWorkflows": "create",
    "validateCreateWorkflows": "validate_create",
    "getDefaultEditor": "get_default_editor",
    "readWorkflowPreviews": "read_previews",
    "searchWorkflows": "search",
    "updateWorkflows": "update",
    "validateUpdateWorkflows": "validate_update",
    # ── Workflow schemes ──
    "getAllWorkflowSchemes": "list",
    "createWorkflowScheme": "create",
    "switchWorkflowSchemeForProject": "switch_for_project",
    "readWorkflowSchemes": "read",
    "updateSchemes": "update_bulk",
    "getRequiredWorkflowSchemeMappings": "get_required_mappings",
    "deleteWorkflowScheme": "delete",
    "getWorkflowScheme": "get",
    "updateWorkflowScheme": "update",
    "deleteDefaultWorkflow": "delete_default_workflow",
    "getDefaultWorkflow": "get_default_workflow",
    "updateDefaultWorkflow": "update_default_workflow",
    "deleteWorkflowSchemeIssueType": "delete_issue_type",
    "getWorkflowSchemeIssueType": "get_issue_type",
    "setWorkflowSchemeIssueType": "set_issue_type",
    "deleteWorkflowMapping": "delete_mapping",
    "getWorkflow": "get_workflow",
    "updateWorkflowMapping": "update_mapping",
    "getProjectUsagesForWorkflowScheme": "get_project_usages",
    # ── Workflow scheme drafts ──
    "createWorkflowSchemeDraftFromParent": "create_from_parent",
    "deleteWorkflowSchemeDraft": "delete",
    "getWorkflowSchemeDraft": "get",
    "updateWorkflowSchemeDraft": "update",
    "deleteDraftDefaultWorkflow": "delete_default_workflow",
    "getDraftDefaultWorkflow": "get_default_workflow",
    "updateDraftDefaultWorkflow": "update_default_workflow",
    "deleteWorkflowSchemeDraftIssueType": "delete_issue_type",
    "getWorkflowSchemeDraftIssueType": "get_issue_type",
    "setWorkflowSchemeDraftIssueType": "set_issue_type",
    "publishDraftWorkflowScheme": "publish",
    "deleteDraftWorkflowMapping": "delete_mapping",
    "getDraftWorkflow": "get_workflow",
    "updateDraftWorkflowMapping": "update_mapping",
    # ── Workflow scheme project associations ──
    "getWorkflowSchemeProjectAssociations": "list",
    "assignSchemeToProject": "assign",
    # ── Workflow transition rules ──
    "getWorkflowTransitionRuleConfigurations": "list",
    "updateWorkflowTransitionRuleConfigurations": "update",
    "deleteWorkflowTransitionRuleConfigurations": "delete",
    # ── Workflow statuses ──
    "getStatuses": "list",
    "getStatus": "get",
    # ── Workflow status categories ──
    "getStatusCategories": "list",
    "getStatusCategory": "get",
    # ── Status (standalone) ──
    "deleteStatusesById": "delete_by_id",
    "getStatusesById": "get_by_id",
    "createStatuses": "create",
    "updateStatuses": "update",
    "getStatusesByName": "get_by_name",
    "search": "search",
    "getProjectIssueTypeUsagesForStatus": "get_project_issue_type_usages",
    "getProjectUsagesForStatus": "get_project_usages",
    "getWorkflowUsagesForStatus": "get_workflow_usages",
    # ── App properties ──
    "AddonPropertiesResource.getAddonProperties_get": "list",
    "AddonPropertiesResource.deleteAddonProperty_delete": "delete",
    "AddonPropertiesResource.getAddonProperty_get": "get",
    "AddonPropertiesResource.putAddonProperty_put": "set",
    "getForgeAppPropertyKeys": "get_forge_keys",
    "deleteForgeAppProperty": "delete_forge",
    "getForgeAppProperty": "get_forge",
    "putForgeAppProperty": "set_forge",
    # ── App migration ──
    "AppIssueFieldValueUpdateResource.updateIssueFields_put": "update_issue_fields",
    "MigrationResource.updateEntityPropertiesValue_put": "update_entity_properties",
    "MigrationResource.workflowRuleSearch_post": "workflow_rule_search",
    # ── Dynamic modules ──
    "DynamicModulesResource.removeModules_delete": "remove",
    "DynamicModulesResource.getModules_get": "get",
    "DynamicModulesResource.registerModules_post": "register",
    # ── Service registry ──
    "ServiceRegistryResource.services_get": "list",
    # ── Connect migration ──
    "ConnectToForgeMigrationFetchTaskResource.fetchMigrationTask_get": "fetch_task",
    # ── Dashboards ──
    "getAllDashboards": "list",
    "getDashboardsPaginated": "list_paginated",
    "getAllAvailableDashboardGadgets": "list_available_gadgets",
    "getDashboardItemPropertyKeys": "get_item_property_keys",
    "deleteDashboardItemProperty": "delete_item_property",
    "getDashboardItemProperty": "get_item_property",
    "setDashboardItemProperty": "set_item_property",
    # ── Permissions ──
    "getAllPermissions": "list",
    "getMyPermissions": "get_my",
    "getBulkPermissions": "get_bulk",
    "getPermittedProjects": "get_permitted_projects",
    "getAllPermissionSchemes": "list_schemes",
    "createPermissionScheme": "create_scheme",
    "deletePermissionScheme": "delete_scheme",
    "getPermissionScheme": "get_scheme",
    "updatePermissionScheme": "update_scheme",
    "getPermissionSchemeGrants": "list_grants",
    "createPermissionGrant": "create_grant",
    "deletePermissionSchemeEntity": "delete_grant",
    "getPermissionSchemeGrant": "get_grant",
    # ── Issue types ──
    "getIssueAllTypes": "list",
    "getIssueTypesForProject": "list_for_project",
    "getAlternativeIssueTypes": "get_alternatives",
    "createIssueTypeAvatar": "create_avatar",
    "getAllIssueTypeSchemes": "list_schemes",
    "createIssueTypeScheme": "create_scheme",
    "getIssueTypeSchemesMapping": "get_scheme_mappings",
    "getIssueTypeSchemeForProjects": "get_schemes_for_projects",
    "assignIssueTypeSchemeToProject": "assign_scheme_to_project",
    "deleteIssueTypeScheme": "delete_scheme",
    "updateIssueTypeScheme": "update_scheme",
    "addIssueTypesToIssueTypeScheme": "add_to_scheme",
    "reorderIssueTypesInIssueTypeScheme": "reorder_in_scheme",
    "removeIssueTypeFromIssueTypeScheme": "remove_from_scheme",
    "getIssueTypePropertyKeys": "get_property_keys",
    "deleteIssueTypeProperty": "delete_property",
    "getIssueTypeProperty": "get_property",
    "setIssueTypeProperty": "set_property",
    # ── Priorities ──
    "setDefaultPriority": "set_default",
    "movePriorities": "move",
    "deletePriority": "delete",
    "getPriority": "get",
    "getPrioritySchemes": "list_schemes",
    "createPriorityScheme": "create_scheme",
    "suggestedPrioritiesForMappings": "get_suggested_for_mappings",
    "getAvailablePrioritiesByPriorityScheme": "get_available_by_scheme",
    "deletePriorityScheme": "delete_scheme",
    "updatePriorityScheme": "update_scheme",
    "getPrioritiesByPriorityScheme": "get_by_scheme",
    "getProjectsByPriorityScheme": "get_projects_by_scheme",
    # ── Security schemes ──
    "getIssueSecuritySchemes": "list",
    "createIssueSecurityScheme": "create",
    "getSecurityLevels": "get_levels",
    "setDefaultLevels": "set_default_levels",
    "getSecurityLevelMembers": "get_level_members",
    "searchProjectsUsingSecuritySchemes": "search_projects",
    "associateSchemesToProjects": "associate_to_projects",
    "searchSecuritySchemes": "search",
    "getIssueSecurityScheme": "get",
    "updateIssueSecurityScheme": "update",
    "deleteSecurityScheme": "delete",
    "addSecurityLevel": "add_level",
    "removeLevel": "remove_level",
    "updateSecurityLevel": "update_level",
    "addSecurityLevelMembers": "add_level_members",
    "removeMemberFromSecurityLevel": "remove_level_member",
    "getIssueSecurityLevelMembers": "get_security_level_members",
    "getIssueSecurityLevel": "get_security_level",
    # ── Issue resolutions ──
    "createResolution": "create",
    "setDefaultResolution": "set_default",
    "moveResolutions": "move",
    "searchResolutions": "search",
    "deleteResolution": "delete",
    "getResolution": "get",
    "updateResolution": "update",
    # ── Notification schemes ──
    "getNotificationSchemes": "list",
    "createNotificationScheme": "create",
    "getNotificationSchemeToProjectMappings": "get_project_mappings",
    "getNotificationScheme": "get",
    "updateNotificationScheme": "update",
    "addNotifications": "add_notifications",
    "deleteNotificationScheme": "delete",
    "removeNotificationFromNotificationScheme": "remove_notification",
    # ── Screen schemes (sub-resource of screens) ──
    "getScreenSchemes": "list",
    "createScreenScheme": "create",
    "deleteScreenScheme": "delete",
    "updateScreenScheme": "update",
    # ── Screen tabs (sub-resource of screens) ──
    "getBulkScreenTabs": "list_bulk",
    "getAllScreenTabs": "list",
    "addScreenTab": "add",
    "deleteScreenTab": "delete",
    "renameScreenTab": "rename",
    "moveScreenTab": "move",
    # ── Screen tab fields (sub-resource of screens) ──
    "getAllScreenTabFields": "list",
    "addScreenTabField": "add",
    "removeScreenTabField": "remove",
    "moveScreenTabField": "move",
    # ── Issue type screen schemes (sub-resource of screens) ──
    "getIssueTypeScreenSchemes": "list",
    "createIssueTypeScreenScheme": "create",
    "getIssueTypeScreenSchemeMappings": "get_mappings",
    "getIssueTypeScreenSchemeProjectAssociations": "get_project_associations",
    "assignIssueTypeScreenSchemeToProject": "assign_to_project",
    "deleteIssueTypeScreenScheme": "delete",
    "updateIssueTypeScreenScheme": "update",
    "appendMappingsForIssueTypeScreenScheme": "append_mappings",
    "updateDefaultScreenScheme": "update_default",
    "removeMappingsFromIssueTypeScreenScheme": "remove_mappings",
    "getProjectsForIssueTypeScreenScheme": "get_projects",
    # ── Plans teams (sub-resource) ──
    "getTeams": "list",
    "addAtlassianTeam": "add_atlassian",
    "removeAtlassianTeam": "remove_atlassian",
    "getAtlassianTeam": "get_atlassian",
    "updateAtlassianTeam": "update_atlassian",
    "createPlanOnlyTeam": "create_plan_only",
    "deletePlanOnlyTeam": "delete_plan_only",
    "getPlanOnlyTeam": "get_plan_only",
    "updatePlanOnlyTeam": "update_plan_only",
    # ── Fields (core) ──
    "getFields": "list",
    "getFieldsPaginated": "list_paginated",
    "getTrashedFieldsPaginated": "list_trashed",
    # ── Field schemes ──
    "getFieldAssociationSchemes": "list_schemes",
    "createFieldAssociationScheme": "create_scheme",
    "removeFieldsAssociatedWithSchemes": "remove_fields_from_schemes",
    "updateFieldsAssociatedWithSchemes": "update_fields_in_schemes",
    "removeFieldAssociationSchemeItemParameters": "remove_scheme_item_params",
    "updateFieldAssociationSchemeItemParameters": "update_scheme_item_params",
    "getProjectsWithFieldSchemes": "get_projects_with_schemes",
    "associateProjectsToFieldAssociationSchemes": "associate_projects_to_schemes",
    "deleteFieldAssociationScheme": "delete_scheme",
    "getFieldAssociationSchemeById": "get_scheme",
    "updateFieldAssociationScheme": "update_scheme",
    "cloneFieldAssociationScheme": "clone_scheme",
    "searchFieldAssociationSchemeFields": "search_scheme_fields",
    "getFieldAssociationSchemeItemParameters": "get_scheme_item_params",
    "searchFieldAssociationSchemeProjects": "search_scheme_projects",
}

# ──────────────────────────────────────────────────────────────────────
# Helpers
# ──────────────────────────────────────────────────────────────────────

PYTHON_KEYWORDS = frozenset(
    {
        "False",
        "None",
        "True",
        "and",
        "as",
        "assert",
        "async",
        "await",
        "break",
        "class",
        "continue",
        "def",
        "del",
        "elif",
        "else",
        "except",
        "finally",
        "for",
        "from",
        "global",
        "if",
        "import",
        "in",
        "is",
        "lambda",
        "nonlocal",
        "not",
        "or",
        "pass",
        "raise",
        "return",
        "try",
        "while",
        "with",
        "yield",
        "type",
    }
)

PYTHON_BUILTINS = frozenset(
    {
        "filter",
        "format",
        "id",
        "input",
        "list",
        "map",
        "max",
        "min",
        "next",
        "object",
        "open",
        "print",
        "range",
        "set",
        "super",
        "type",
        "vars",
        "zip",
    }
)

RESERVED = PYTHON_KEYWORDS | PYTHON_BUILTINS


def _camel_to_snake(name: str) -> str:
    if "." in name:
        name = name.rsplit(".", 1)[-1]
    s1 = re.sub(r"([A-Z]+)([A-Z][a-z])", r"\1_\2", name)
    result = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", s1).lower()
    result = re.sub(r"[^a-z0-9_]", "_", result)
    result = re.sub(r"_+", "_", result).strip("_")
    return result


def _safe_param_name(name: str) -> str:
    """Ensure a parameter name isn't a Python keyword or builtin."""
    snake = _camel_to_snake(name)
    return snake + "_" if snake in RESERVED else snake


def _to_singular(word: str) -> str:
    """Best-effort English singular form."""
    overrides = {
        "statuses": "status",
        "categories": "category",
        "priorities": "priority",
        "properties": "property",
        "entries": "entry",
        "activities": "activity",
        "strategies": "strategy",
        "policies": "policy",
    }
    if word in overrides:
        return overrides[word]
    if word.endswith("ies"):
        return word[:-3] + "y"
    if word.endswith("sses") or word.endswith("xes") or word.endswith("zes"):
        return word[:-2]
    if word.endswith("ses"):
        return word[:-2]
    if word.endswith("s") and not word.endswith("ss"):
        return word[:-1]
    return word


def _build_strip_words(group: str, sub_resource: str | None) -> set[str]:
    """Build the set of tokens to strip from method names."""
    words: set[str] = set()
    for part in group.split("_"):
        words.add(part)
        words.add(_to_singular(part))
    if sub_resource:
        for part in sub_resource.split("_"):
            words.add(part)
            words.add(_to_singular(part))
    return words


def _simplify_method_name(
    method_name: str,
    operation_id: str,
    strip_words: set[str],
) -> str:
    """Simplify method name by removing redundant resource-context tokens."""
    if operation_id in METHOD_NAME_OVERRIDES:
        return METHOD_NAME_OVERRIDES[operation_id]

    tokens = method_name.split("_")
    filtered = [t for t in tokens if t not in strip_words]

    if not filtered:
        return method_name
    return "_".join(filtered)


def _resolve_method_conflicts(operations: list[dict[str, Any]]) -> None:
    """If two ops in the same class got the same simplified name, revert both."""
    counts = Counter(op["method_name"] for op in operations)
    for op in operations:
        if counts[op["method_name"]] > 1:
            op["method_name"] = op["original_method_name"]


def _group_to_class(group: str) -> str:
    return "".join(w.capitalize() for w in group.split("_"))


def _sub_to_class(group: str, sub: str) -> str:
    singular = "_".join(_to_singular(p) for p in group.split("_"))
    return _group_to_class(f"{singular}_{sub}")


_BEAN_RENAME_MAP: dict[str, str] | None = None


def _bean_rename_map() -> dict[str, str]:
    """Build a rename map for Bean-suffixed schema names.

    Mirrors the logic in ``generate_models._strip_bean_suffix`` so that
    resource classes import the renamed model names.
    """
    global _BEAN_RENAME_MAP  # noqa: PLW0603
    if _BEAN_RENAME_MAP is not None:
        return _BEAN_RENAME_MAP

    spec = json.loads(OPENAPI_SPEC.read_text())
    all_schemas = set(spec.get("components", {}).get("schemas", {}).keys())
    bean_schemas = sorted(n for n in all_schemas if n.endswith("Bean"))

    rename: dict[str, str] = {}
    for name in bean_schemas:
        rename[name] = name[:-4]

    # Also rename compound helper types (e.g. UserBeanAvatarUrls -> UserAvatarUrls)
    for bean_name in list(rename):
        for schema in all_schemas:
            if schema.startswith(bean_name) and schema != bean_name:
                suffix = schema[len(bean_name) :]
                rename[schema] = rename[bean_name] + suffix

    _BEAN_RENAME_MAP = rename
    return _BEAN_RENAME_MAP


def _ref_to_model(ref: str | None) -> str | None:
    if not ref:
        return None
    name = ref.rsplit("/", 1)[-1]
    return _bean_rename_map().get(name, name)


def _resolve_schema_ref(schema: dict[str, Any]) -> str | None:
    if "$ref" in schema:
        return _ref_to_model(schema["$ref"])
    if "items" in schema and "$ref" in schema.get("items", {}):
        return _ref_to_model(schema["items"]["$ref"])
    if "oneOf" in schema:
        for variant in schema["oneOf"]:
            ref = _ref_to_model(variant.get("$ref"))
            if ref:
                return ref
    return None


def _openapi_type_to_python(param: dict[str, Any]) -> str:
    schema = param.get("schema", {})
    t = schema.get("type", "str")
    mapping = {
        "string": "str",
        "integer": "int",
        "boolean": "bool",
        "number": "float",
        "array": "list[str]",
    }
    py = mapping.get(t, "str")
    return py if param.get("required", False) else f"{py} | None"


_PRIMITIVE_TYPE_MAP: dict[str, str] = {
    "string": "str",
    "integer": "int",
    "number": "float",
    "boolean": "bool",
}
_NON_MODEL_TYPES: set[str] = {"str", "int", "float", "bool", "dict[str, Any]"}

_MODELS_DIR = JIRAPI_DIR / "models"


def _discover_enum_models() -> set[str]:
    """Scan generated model files and return the set of enum class names.

    These classes inherit from ``StrEnum`` or ``Enum`` and do NOT have
    ``model_validate`` — the resource generator must not emit
    ``.model_validate()`` calls for them.
    """
    enum_names: set[str] = set()
    if not _MODELS_DIR.is_dir():
        return enum_names
    for path in _MODELS_DIR.glob("*.py"):
        for match in re.finditer(r"^class (\w+)\((StrEnum|Enum)\)", path.read_text(), re.MULTILINE):
            enum_names.add(match.group(1))
    return enum_names


def _get_success_response(op: dict[str, Any]) -> tuple[str | None, str]:
    """Return (response_type, status_code) for the first 2xx response."""
    for code in ("200", "201", "202", "204"):
        resp = op.get("responses", {}).get(code)
        if not resp:
            continue
        if code == "204":
            return None, code
        content = resp.get("content", {})
        json_ct = content.get("application/json", {})
        schema = json_ct.get("schema", {})
        model = _resolve_schema_ref(schema)
        if model:
            return model, code
        schema_type = schema.get("type")
        if schema_type in _PRIMITIVE_TYPE_MAP:
            return _PRIMITIVE_TYPE_MAP[schema_type], code
        if schema_type == "object" and ("additionalProperties" in schema or "properties" in schema):
            return "dict[str, Any]", code
        return None, code
    return None, "200"


def _get_request_body(op: dict[str, Any]) -> str | None:
    body = op.get("requestBody", {})
    content = body.get("content", {})
    json_ct = content.get("application/json", {})
    schema = json_ct.get("schema", {})
    return _resolve_schema_ref(schema)


# ──────────────────────────────────────────────────────────────────────
# Parsing & consolidation
# ──────────────────────────────────────────────────────────────────────

GroupKey = tuple[str, str | None]  # (group, sub_resource)


def parse_and_consolidate(
    spec: dict[str, Any],
) -> dict[GroupKey, list[dict[str, Any]]]:
    """Parse ops from OpenAPI spec and consolidate by group/sub-resource."""
    by_group: dict[GroupKey, list[dict[str, Any]]] = defaultdict(list)

    for path, methods in spec.get("paths", {}).items():
        for http_method, op in methods.items():
            if http_method not in ("get", "post", "put", "delete", "patch"):
                continue
            if op.get("deprecated"):
                continue

            tag = op.get("tags", ["untagged"])[0]
            if tag not in TAG_CONSOLIDATION:
                print(f"  WARNING: unmapped tag {tag!r}, skipping")
                continue

            group, sub = TAG_CONSOLIDATION[tag]
            operation_id = op.get("operationId", "")
            raw_method = _camel_to_snake(operation_id)

            path_params = []
            query_params = []
            for p in op.get("parameters", []):
                if p.get("in") == "path":
                    path_params.append(
                        {
                            "name": _safe_param_name(p["name"]),
                            "original": p["name"],
                            "type": "str",
                            "required": True,
                        }
                    )
                elif p.get("in") == "query":
                    query_params.append(
                        {
                            "name": _safe_param_name(p["name"]),
                            "original": p["name"],
                            "type": _openapi_type_to_python(p),
                            "required": p.get("required", False),
                        }
                    )

            request_model = _get_request_body(op)
            response_model, status_code = _get_success_response(op)

            strip_words = _build_strip_words(group, sub)
            simplified = _simplify_method_name(raw_method, operation_id, strip_words)

            by_group[(group, sub)].append(
                {
                    "operation_id": operation_id,
                    "method_name": simplified,
                    "original_method_name": raw_method,
                    "http_method": http_method.upper(),
                    "path": path,
                    "summary": op.get("summary", ""),
                    "path_params": path_params,
                    "query_params": query_params,
                    "request_model": request_model,
                    "response_model": response_model,
                    "status_code": status_code,
                }
            )

    for _key, ops in by_group.items():
        _resolve_method_conflicts(ops)

    return dict(by_group)


# ──────────────────────────────────────────────────────────────────────
# Code generation
# ──────────────────────────────────────────────────────────────────────


def _build_method_sig(
    op: dict[str, Any],
    *,
    is_async: bool,
    renames: dict[str, str],
) -> str:
    parts = ["self"]
    for p in op["path_params"]:
        parts.append(f"{p['name']}: str")
    if op["request_model"]:
        model = renames.get(op["request_model"], op["request_model"])
        parts.append(f"body: {model}")
    kw_only = False
    for p in op["query_params"]:
        if not kw_only:
            parts.append("*")
            kw_only = True
        if p["required"]:
            parts.append(f"{p['name']}: {p['type']}")
        else:
            parts.append(f"{p['name']}: {p['type']} = None")
    args = ", ".join(parts)
    ret_model = op["response_model"]
    ret = renames.get(ret_model, ret_model) if ret_model else "None"
    prefix = "async def" if is_async else "def"
    return f"    {prefix} {op['method_name']}({args}) -> {ret}:"


def _build_method_body(
    op: dict[str, Any],
    *,
    is_async: bool,
    renames: dict[str, str],
    enum_models: set[str] | None = None,
) -> list[str]:
    lines: list[str] = []
    if op["summary"]:
        safe = op["summary"].replace('"', '\\"')
        lines.append(f'        """{safe}"""')

    path = op["path"]
    for p in op["path_params"]:
        path = path.replace("{" + p["original"] + "}", "{" + p["name"] + "}")

    if op["query_params"]:
        items = [f'"{p["original"]}": {p["name"]}' for p in op["query_params"]]
        lines.append(f"        params = self._client._build_params(**{{{', '.join(items)}}})")

    kwargs = []
    if op["query_params"]:
        kwargs.append("params=params")
    if op["request_model"]:
        kwargs.append("json=body.model_dump(by_alias=True, exclude_none=True)")
    kw = (", " + ", ".join(kwargs)) if kwargs else ""

    await_pfx = "await " if is_async else ""
    url = f'f"{path}"' if op["path_params"] else f'"{path}"'
    call = f'{await_pfx}self._client._request("{op["http_method"]}", {url}{kw})'

    resp_type = op["response_model"]
    if resp_type and resp_type not in _NON_MODEL_TYPES:
        model = renames.get(resp_type, resp_type)
        if enum_models and model in enum_models:
            logger.warning(
                "Response model %r for %s %s is an Enum (no model_validate). "
                "Falling back to raw resp.json(). Fix the model mapping.",
                model,
                op["http_method"],
                op["path"],
            )
            lines.append(f"        resp = {call}")
            lines.append("        return resp.json()")
        else:
            lines.append(f"        resp = {call}")
            lines.append(f"        return {model}.model_validate(resp.json())")
    elif resp_type in _NON_MODEL_TYPES:
        lines.append(f"        resp = {call}")
        lines.append("        return resp.json()")
    else:
        lines.append(f"        {call}")
        lines.append("        return None")
    return lines


def _generate_class(
    class_name: str,
    base_class: str,
    doc: str,
    operations: list[dict[str, Any]],
    renames: dict[str, str],
    *,
    is_async: bool,
    sub_resources: list[tuple[str, str, str]] | None = None,
    enum_models: set[str] | None = None,
) -> list[str]:
    """Generate lines for one resource class.

    sub_resources is a list of (prop_name, sync_class, async_class) tuples
    for @cached_property sub-resource wiring.
    """
    lines: list[str] = []
    lines.append(f"class {class_name}({base_class}):")
    lines.append(f'    """{doc}"""')
    lines.append("")

    if sub_resources:
        for prop_name, sync_cls, async_cls in sub_resources:
            cls = async_cls if is_async else sync_cls
            lines.append("    @cached_property")
            lines.append(f"    def {prop_name}(self) -> {cls}:")
            group = class_name.replace("Async", "") if is_async else class_name
            pkg = _class_to_package(group)
            lines.append(f"        from jirapi.{pkg}.{prop_name} import {cls}")
            lines.append("")
            lines.append(f"        return {cls}(self._client)")
            lines.append("")

    for op in operations:
        lines.append(_build_method_sig(op, is_async=is_async, renames=renames))
        lines.extend(
            _build_method_body(op, is_async=is_async, renames=renames, enum_models=enum_models)
        )
        lines.append("")

    return lines


# Map from PascalCase class name back to package name
_CLASS_TO_PKG: dict[str, str] = {}


def _class_to_package(class_name: str) -> str:
    return _CLASS_TO_PKG.get(class_name, class_name.lower())


def generate_resource_module(
    group: str,
    sub_resource: str | None,
    operations: list[dict[str, Any]],
    sub_resources_info: list[tuple[str, str, str]] | None = None,
    enum_models: set[str] | None = None,
) -> str:
    """Generate Python source for a resource module."""
    if sub_resource:
        sync_class = _sub_to_class(group, sub_resource)
        async_class = f"Async{sync_class}"
        label = f"{group}.{sub_resource}"
    else:
        sync_class = _group_to_class(group)
        async_class = f"Async{sync_class}"
        label = group

    _CLASS_TO_PKG[sync_class] = group

    models: set[str] = set()
    needs_any = False
    for op in operations:
        if op["request_model"]:
            models.add(op["request_model"])
        if op["response_model"] and op["response_model"] not in _NON_MODEL_TYPES:
            models.add(op["response_model"])
        if op["response_model"] == "dict[str, Any]":
            needs_any = True

    conflicting = models & {sync_class, async_class}
    safe_models = models - conflicting
    renames = {c: f"{c}Model" for c in conflicting}

    lines: list[str] = []
    lines.append(f'"""Resource classes for {label}."""')
    lines.append("")
    lines.append("from __future__ import annotations")
    lines.append("")

    need_cached_property = bool(sub_resources_info)
    extra_imports: list[str] = []
    if needs_any:
        extra_imports.append("Any")
    if need_cached_property:
        extra_imports.append("TYPE_CHECKING")
    if extra_imports:
        lines.append(f"from typing import {', '.join(sorted(extra_imports))}")
        lines.append("")
    if need_cached_property:
        lines.append("from functools import cached_property")
        lines.append("")

    lines.append("from jirapi._resource import AsyncAPIResource, SyncAPIResource")
    if safe_models:
        lines.append(f"from jirapi.models import {', '.join(sorted(safe_models))}")
    for c in sorted(conflicting):
        lines.append(f"from jirapi.models import {c} as {c}Model")

    if need_cached_property and sub_resources_info:
        lines.append("")
        lines.append("if TYPE_CHECKING:")
        for prop_name, sync_cls, async_cls in sub_resources_info:
            lines.append(f"    from jirapi.{group}.{prop_name} import {async_cls}, {sync_cls}")

    lines.append("")
    lines.append("")

    lines.extend(
        _generate_class(
            sync_class,
            "SyncAPIResource",
            f"Synchronous resource for {label}.",
            operations,
            renames,
            is_async=False,
            sub_resources=sub_resources_info,
            enum_models=enum_models,
        )
    )
    lines.append("")
    lines.extend(
        _generate_class(
            async_class,
            "AsyncAPIResource",
            f"Asynchronous resource for {label}.",
            operations,
            renames,
            is_async=True,
            sub_resources=sub_resources_info,
            enum_models=enum_models,
        )
    )

    return "\n".join(lines)


def generate_group_init(group: str, sub_resources: list[str]) -> str:
    """Generate __init__.py for a group package."""
    sync_class = _group_to_class(group)
    async_class = f"Async{sync_class}"

    lines = [
        f'"""{sync_class} resource package."""',
        "",
        f"from jirapi.{group}._resource import {async_class}, {sync_class}",
        "",
        f'__all__ = ["{async_class}", "{sync_class}"]',
        "",
    ]
    return "\n".join(lines)


def generate_client_file(groups: list[str]) -> str:
    """Generate jirapi/client.py with @cached_property for each group."""
    sync_props: list[str] = []
    async_props: list[str] = []
    type_imports: list[str] = []

    for group in sorted(groups):
        sync_cls = _group_to_class(group)
        async_cls = f"Async{sync_cls}"

        type_imports.append(f"    from jirapi.{group} import {async_cls}, {sync_cls}")

        sync_props.append(
            f"    @cached_property\n"
            f"    def {group}(self) -> {sync_cls}:\n"
            f"        from jirapi.{group} import {sync_cls}\n"
            f"\n"
            f"        return {sync_cls}(self)\n"
        )
        async_props.append(
            f"    @cached_property\n"
            f"    def {group}(self) -> {async_cls}:\n"
            f"        from jirapi.{group} import {async_cls}\n"
            f"\n"
            f"        return {async_cls}(self)\n"
        )

    ti = "\n".join(type_imports)
    sp = "\n".join(sync_props)
    ap = "\n".join(async_props)

    return textwrap.dedent(f'''\
"""Public Jira client classes.

``Jira`` provides synchronous access and ``AsyncJira`` provides asynchronous
access to the Jira Cloud REST API.  Resource groups are exposed as
``@cached_property`` attributes (e.g. ``jira.issues``, ``jira.projects``).
"""

from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING, Any

from jirapi._base_client import AsyncAPIClient, SyncAPIClient, _DEFAULT_TIMEOUT


if TYPE_CHECKING:
{ti}

__all__ = ["Jira", "AsyncJira"]


class Jira(SyncAPIClient):
    """Synchronous Jira Cloud REST API client.

    Usage::

        from jirapi import Jira

        jira = Jira(url="https://acme.atlassian.net", email="me@acme.com", api_token="...")
        issue = jira.issues.get("PROJ-123")

    Or as a context manager::

        with Jira(url="...", email="...", api_token="...") as jira:
            issue = jira.issues.get("PROJ-123")
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

{sp}

class AsyncJira(AsyncAPIClient):
    """Asynchronous Jira Cloud REST API client.

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

{ap}''')


# ──────────────────────────────────────────────────────────────────────
# Main
# ──────────────────────────────────────────────────────────────────────


def main() -> None:
    """Parse the OpenAPI spec and generate resource packages + client."""
    print("Loading OpenAPI spec …")
    spec = json.loads(OPENAPI_SPEC.read_text())

    print("Parsing and consolidating operations …")
    by_group_key = parse_and_consolidate(spec)

    # Organise into {group: {None: [ops], "sub": [ops], ...}}
    groups: dict[str, dict[str | None, list[dict[str, Any]]]] = defaultdict(dict)
    for (group, sub), ops in by_group_key.items():
        if sub in groups[group]:
            groups[group][sub].extend(ops)
        else:
            groups[group][sub] = list(ops)

    total_ops = sum(len(ops) for bucket in groups.values() for ops in bucket.values())
    total_groups = len(groups)
    print(f"  {total_ops} operations across {total_groups} groups")

    # Discover enum model names so we can avoid emitting .model_validate() for them
    enum_models = _discover_enum_models()
    if enum_models:
        print(f"  {len(enum_models)} enum models detected (will guard against model_validate)")

    # Clean old resources/ directory
    old_resources = JIRAPI_DIR / "resources"
    if old_resources.exists():
        print("Removing old jirapi/resources/ …")
        shutil.rmtree(old_resources)

    # Generate each group package
    print("Generating group packages …")
    for group in sorted(groups):
        bucket = groups[group]
        group_dir = JIRAPI_DIR / group

        # Skip if the group name clashes with existing non-resource modules
        if group_dir.exists() and (group_dir / "__init__.py").exists():
            # Could be models/ etc — only overwrite if it's our resource package
            pass
        group_dir.mkdir(parents=True, exist_ok=True)

        core_ops = bucket.get(None, [])
        sub_keys = sorted(k for k in bucket if k is not None)

        # Build sub-resource info for @cached_property wiring on core class
        sub_info: list[tuple[str, str, str]] = []
        for sk in sub_keys:
            sync_cls = _sub_to_class(group, sk)
            async_cls = f"Async{sync_cls}"
            sub_info.append((sk, sync_cls, async_cls))

        # Write core _resource.py
        core_source = generate_resource_module(
            group,
            None,
            core_ops,
            sub_resources_info=sub_info or None,
            enum_models=enum_models,
        )
        (group_dir / "_resource.py").write_text(core_source)

        # Write sub-resource modules
        for sk in sub_keys:
            sub_source = generate_resource_module(group, sk, bucket[sk], enum_models=enum_models)
            (group_dir / f"{sk}.py").write_text(sub_source)

        # Write __init__.py
        init_source = generate_group_init(group, sub_keys)
        (group_dir / "__init__.py").write_text(init_source)

    # Generate client.py
    print("Generating client.py …")
    client_source = generate_client_file(sorted(groups.keys()))
    CLIENT_FILE.write_text(client_source)

    # Collect all generated paths for formatting
    gen_paths = [str(CLIENT_FILE)]
    for group in groups:
        gen_paths.append(str(JIRAPI_DIR / group))

    print("Running ruff format …")
    subprocess.run(["uv", "run", "ruff", "format", *gen_paths], check=False)

    print("Running ruff check --fix …")
    subprocess.run(
        ["uv", "run", "ruff", "check", *gen_paths, "--fix"],
        check=False,
    )

    sub_count = sum(len([k for k in bucket if k is not None]) for bucket in groups.values())
    print(
        f"Done. Generated {total_groups} group packages "
        f"({sub_count} sub-resources) with {total_ops} endpoint methods."
    )


if __name__ == "__main__":
    main()
