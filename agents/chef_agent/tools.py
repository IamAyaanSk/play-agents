from typing import Any

from langchain.tools import tool

from utils import web_search_client


@tool
def search_recipes_on_web(ingredients: str) -> dict[str, Any]:
    """Search information for all possible recipes over the web by providing comma seperated ingredients string"""

    search_query = f"Suggest recipes with {ingredients}"

    response = web_search_client.search(
        query=search_query, search_depth="basic", topic="general", max_results=3
    )

    return response


@tool
def search_recipe_on_web(dish: str) -> dict[str, Any]:
    """Search for complete recipes for a dish on the web"""

    search_query = f"Recipe for {dish}"

    response = web_search_client.search(
        query=search_query, search_depth="basic", topic="general", max_results=1
    )

    return response
