"""Google Agent Toolkit."""

from typing import List, Optional

from pydantic import PrivateAttr

from ..api import GoogleAPI
from ..configuration import Configuration, is_tool_allowed
from ..tools import tools
from .tool import GoogleTool


class GoogleAgentToolkit:
    _tools: List["GoogleTool"] = PrivateAttr(default_factory=list)

    def __init__(
        self,
        api_key: str,
        configuration: Optional[Configuration] = None
    ):
        super().__init__()

        context = configuration.get("context") if configuration else None

        google_api = GoogleAPI(
            api_key=api_key,
            context=context)

        filtered_tools = [
            tool for tool in tools if is_tool_allowed(tool, configuration)
        ]

        self._tools = [
            GoogleTool(
                name=tool["method"],
                description=tool["description"],
                method=tool["method"],
                google_api=google_api,
                args_schema=tool.get("args_schema", None),
            )
            for tool in filtered_tools
        ]

    def get_tools(self) -> List["GoogleTool"]:
        """Get the tools in the toolkit."""
        return self._tools
