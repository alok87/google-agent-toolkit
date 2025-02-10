"""
This tool allows agents to interact with the Google API.
"""

from __future__ import annotations

from typing import Any, Optional, Type

from langchain.tools import BaseTool
from pydantic import BaseModel

from ..api import GoogleAPI


class GoogleTool(BaseTool):
    """Tool for interacting with the Google API."""

    google_api: GoogleAPI
    method: str
    name: str = ""
    description: str = ""
    args_schema: Optional[Type[BaseModel]] = None

    def _run(
        self,
        *args: Any,
        **kwargs: Any,
    ) -> str:
        """Use the google API to run an operation."""
        return self.google_api.run(self.method, *args, **kwargs)
