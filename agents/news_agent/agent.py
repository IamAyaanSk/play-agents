from langchain.agents import create_agent

from utils import chat_model

from .tools import search_news_on_web

system_prompt = """
    You are a professional news fact verifier who takes a query and respond with a brief about the news, shares recent news related to the query. You can use the search_news_on_web tool to obtain recent information regarding the user query. Respond a proper helpful markdown with referred urls too.
"""

agent = create_agent(
    model=chat_model, tools=[search_news_on_web], system_prompt=system_prompt
)
