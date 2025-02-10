"""Abstraction above Google APIs."""

from __future__ import annotations

import json
from typing import Optional

import googlemaps
from pydantic import BaseModel

from .configuration import Context
from .functions import search_places


class GoogleAPI(BaseModel):
    """ "Wrapper for Google API"""

    _context: Context
    _client: googlemaps.Client

    def __init__(
        self,
        api_key: str,
        context: Optional[Context],
    ):

        super().__init__()

        self._context = context if context is not None else Context()
        self._client = googlemaps.Client(
            key=api_key,
        )

    def run(self, method: str, *args, **kwargs) -> str:
        if method == "search_flights":
            return json.dumps(
                search_places(
                    self._context,
                    self._client,
                    *args,
                    **kwargs
                )
            )
        else:
            raise ValueError("Invalid method " + method)
