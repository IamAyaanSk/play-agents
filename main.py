from dotenv import load_dotenv

load_dotenv()

from langchain.messages import AIMessage, HumanMessage
from langchain_core.runnables import RunnableConfig
from langchain_core.utils.uuid import uuid7
from rich import print as rprint

from agents import news_agent

# from agents import philosopher_agent

# philosopher_question = HumanMessage(content="What is life?")
# philosopher_config: RunnableConfig = {"configurable": {"thread_id": str(uuid7())}}

# philosopher_response = philosopher_agent.invoke(
#     {"messages": [philosopher_question]}, config=philosopher_config
# )

# rprint(philosopher_response["messages"][-1].content)


news_question = HumanMessage(content="Tell me something recent about NVIDIA corp.")

news_resposne_stream = news_agent.stream_events(
    {"messages": [news_question]}, version="v3"
)

for snapshot in news_resposne_stream.values:
    latest_message = snapshot["messages"][-1]

    if latest_message.content:
        if isinstance(latest_message, HumanMessage):
            rprint(f"User: {latest_message.content}")

        elif isinstance(latest_message, AIMessage):
            rprint(f"Agent: {latest_message.content}")

    elif latest_message.tool_calls:
        rprint(f"Calling tools: {[tc['name'] for tc in latest_message.tool_calls]}")
