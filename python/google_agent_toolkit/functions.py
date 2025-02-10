from typing import Dict, Any

from .configuration import Context
import googlemaps


def search_places(
    context: Context,
    client: googlemaps.Client,
    text_query: str,
) -> Dict[str, Any]:
    """Searches for the places given a text query

    Parameters:
        text_query:text string on which to search, for example: restaurants in Kormangla, best events happening in Bangalore.

    Returns:
        A dictionary containing the places or an error dictionary.
    """

    try:
        response = client.places(query=text_query)
        return response
    except Exception as e:
        print(f"An error occurred: {e}")
        return {
            "error": "An unexpected error occurred",
            "type": "UnexpectedError",
        }
