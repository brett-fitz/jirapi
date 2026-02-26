"""Pydantic models for the dynamic modules domain."""

from __future__ import annotations

from typing import Annotated

from pydantic import BaseModel, Field


class ConnectModule(BaseModel):
    pass


class ConnectModules(BaseModel):
    modules: Annotated[
        list[ConnectModule],
        Field(
            description="A list of app modules in the same format as the `modules` property in the\n[app descriptor](https://developer.atlassian.com/cloud/jira/platform/app-descriptor/)."
        ),
    ]


__all__ = [
    "ConnectModule",
    "ConnectModules",
]
