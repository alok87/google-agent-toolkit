from pydantic import BaseModel, Field


class SearchPlaces(BaseModel):
    """Schema for the `search_places` operation."""

    text_query: str = Field(
        ...,
        description="text string on which to search, for example: restaurants "
        "in Kormangla, best events happening in Bangalore.",
    )
