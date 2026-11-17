import os
from typing import Any

from langchain.tools import tool
from tavily import TavilyClient

tavily_api_key = os.getenv("TAVILY_API_KEY")

if not tavily_api_key:
    raise ValueError("Web search is not configured.")

tavily_client = TavilyClient(api_key=tavily_api_key)


@tool
def search_news_on_web(query: str) -> dict[str, Any]:
    """Search any news query over the web to get upto date information. Keep the query short and do not exceed the 400 character limit for query"""
    response = tavily_client.search(
        query=query, search_depth="fast", topic="news", max_results=3
    )

    return response
