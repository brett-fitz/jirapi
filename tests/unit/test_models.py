"""Tests for jirapi.models package organization.

Verifies that the domain-themed submodule split works correctly:
backward-compatible imports, domain-specific imports, cross-module
Pydantic annotation resolution, and __all__ completeness.
"""

from __future__ import annotations

import importlib
import pkgutil

import jirapi.models
from jirapi.models import Issue, Project


class TestBackwardCompatImports:
    """Models can be imported from jirapi.models (the public API)."""

    def test_import_issue_model(self) -> None:
        from jirapi.models import Issue

        assert Issue is not None

    def test_import_project_model(self) -> None:
        from jirapi.models import Project

        assert Project is not None

    def test_import_shared_enum(self) -> None:
        from jirapi.models import PlanningStyle

        assert PlanningStyle.scrum == "Scrum"

    def test_import_shared_model(self) -> None:
        from jirapi.models import UserDetails

        assert UserDetails is not None


class TestDomainSubmoduleImports:
    """Models can be imported directly from their domain submodule."""

    def test_issues_submodule(self) -> None:
        from jirapi.models.issues import Issue

        assert Issue is not None

    def test_projects_submodule(self) -> None:
        from jirapi.models.projects import Project

        assert Project is not None

    def test_shared_submodule(self) -> None:
        from jirapi.models._shared import UserDetails

        assert UserDetails is not None

    def test_workflows_submodule(self) -> None:
        from jirapi.models.workflows import Workflow

        assert Workflow is not None

    def test_identity_preserved(self) -> None:
        """Same class object whether imported from __init__ or submodule."""
        from jirapi.models import Issue as FromInit
        from jirapi.models.issues import Issue as FromSub

        assert FromInit is FromSub


class TestCrossModuleResolution:
    """Pydantic can resolve type annotations that reference models in other submodules."""

    def test_project_with_user_lead(self) -> None:
        project = Project.model_validate(
            {
                "id": "10000",
                "key": "PROJ",
                "name": "Test",
                "lead": {"accountId": "123", "displayName": "Alice"},
            }
        )
        assert project.lead is not None
        assert project.lead.display_name == "Alice"

    def test_issue_model_fields_resolve(self) -> None:
        fields = Issue.model_fields
        assert len(fields) > 0

    def test_recursive_model_rebuild(self) -> None:
        from jirapi.models import CreateWorkflowCondition

        cond = CreateWorkflowCondition.model_validate(
            {
                "type": "CompoundCondition",
                "conditions": [{"type": "AllowOnlyAssignee"}],
            }
        )
        assert len(cond.conditions) == 1


class TestSubmodulesComplete:
    """Every submodule is importable and defines __all__."""

    def test_all_submodules_importable(self) -> None:
        pkg_path = jirapi.models.__path__
        for _importer, mod_name, _ispkg in pkgutil.iter_modules(pkg_path):
            mod = importlib.import_module(f"jirapi.models.{mod_name}")
            assert hasattr(mod, "__all__"), f"{mod_name} missing __all__"
            assert len(mod.__all__) > 0, f"{mod_name} has empty __all__"

    def test_init_all_covers_submodules(self) -> None:
        """__init__.__all__ includes every name from every submodule."""
        init_all = set(jirapi.models.__all__)
        pkg_path = jirapi.models.__path__
        submodule_names: set[str] = set()
        for _importer, mod_name, _ispkg in pkgutil.iter_modules(pkg_path):
            mod = importlib.import_module(f"jirapi.models.{mod_name}")
            submodule_names.update(mod.__all__)
        missing = submodule_names - init_all
        assert not missing, f"Names in submodules but not in __init__.__all__: {missing}"
