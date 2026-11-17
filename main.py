from dotenv import load_dotenv

load_dotenv()

from langchain.messages import HumanMessage
from langchain_core.runnables import RunnableConfig
from langchain_core.utils.uuid import uuid7
from rich import print as rprint

from agents import philosopher_agent

philosopher_question = HumanMessage(content="What is life?")
philosopher_config: RunnableConfig = {"configurable": {"thread_id": str(uuid7())}}

philosopher_response = philosopher_agent.invoke(
    {"messages": [philosopher_question]}, config=philosopher_config
)

rprint(philosopher_response["messages"][-1].content)
