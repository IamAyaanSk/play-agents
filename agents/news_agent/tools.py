from typing import Any

from langchain.tools import tool

from utils import web_search_client


@tool
def search_news_on_web(query: str) -> dict[str, Any]:
    """Search any news query over the web to get upto date information. Keep the query short and do not exceed the 400 character limit for query"""
    response = web_search_client.search(
        query=query, search_depth="fast", topic="news", max_results=3
    )

    return response
