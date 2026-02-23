"""Shared type aliases used across jirapi internals."""

from __future__ import annotations

from typing import Any, TypeVar


__all__: list[str] = []

JSON = dict[str, Any]
"""A JSON-serialisable dictionary."""

Params = dict[str, str | int | bool | list[str] | None]
"""Query-parameter mapping accepted by request helpers."""

T = TypeVar("T")
"""Generic type variable for response model parsing."""
