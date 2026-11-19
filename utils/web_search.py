import os

from tavily import TavilyClient

tavily_api_key = os.getenv("TAVILY_API_KEY")

if not tavily_api_key:
    raise ValueError("Web search is not configured.")

tavily_client = TavilyClient(api_key=tavily_api_key)
