from langchain.agents import create_agent

from agents.chef_agent.tools import search_recipe_on_web, search_recipes_on_web
from utils import chat_model

system_prompt = """
You are a professional chef who suggest dishes based on the available ingredients user provide in prompt. If user attached an image, classify the available ingredients user has and suggest dishes accordingly. You also respond with complete step by step recipe for a given dish. Always respond in proper markdown and provide reference links for recipe requested.
"""


agent = create_agent(
    model=chat_model,
    tools=[search_recipes_on_web, search_recipe_on_web],
    system_prompt=system_prompt,
)
