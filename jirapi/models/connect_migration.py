"""Pydantic models for the connect migration domain."""

from __future__ import annotations

from typing import Annotated, Any

from pydantic import AnyUrl, AwareDatetime, BaseModel, Field


class TaskProgress(BaseModel):
    description: Annotated[str | None, Field(description="The description of the task.")] = None
    elapsed_runtime: Annotated[
        int,
        Field(
            alias="elapsedRuntime",
            description="The execution time of the task, in milliseconds.",
        ),
    ]
    finished: Annotated[
        AwareDatetime | None, Field(description="A timestamp recording when the task was finished.")
    ] = None
    id: Annotated[str, Field(description="The ID of the task.")]
    last_update: Annotated[
        AwareDatetime,
        Field(
            alias="lastUpdate",
            description="A timestamp recording when the task progress was last updated.",
        ),
    ]
    message: Annotated[
        str | None, Field(description="Information about the progress of the task.")
    ] = None
    progress: Annotated[
        int, Field(description="The progress of the task, as a percentage complete.")
    ]
    result: Annotated[Any | None, Field(description="The result of the task execution.")] = None
    self: Annotated[AnyUrl, Field(description="The URL of the task.")]
    started: Annotated[
        AwareDatetime | None, Field(description="A timestamp recording when the task was started.")
    ] = None
    status: Annotated[Status3, Field(description="The status of the task.")]
    submitted: Annotated[
        AwareDatetime | None,
        Field(description="A timestamp recording when the task was submitted."),
    ] = None
    submitted_by: Annotated[
        int,
        Field(
            alias="submittedBy",
            description="The ID of the user who submitted the task.",
        ),
    ]


__all__ = [
    "TaskProgress",
]
