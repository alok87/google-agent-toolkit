from typing import Dict, List, Any

from .prompts import (
    SEARCH_PLACES_PROMPT,
)
from .schema import SearchPlaces


tools: List[Dict[str, Any]] = [
    {
        "method": "search_places",
        "name": "Search Places",
        "description": SEARCH_PLACES_PROMPT,
        "args_schema": SearchPlaces,
        "actions": {
            "places": {
                "search": True,
            }
        },
    },
]
