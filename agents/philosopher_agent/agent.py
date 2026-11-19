from langchain.agents import create_agent
from langgraph.checkpoint.memory import InMemorySaver

from utils import chat_model

agent = create_agent(
    model=chat_model,
    system_prompt="You are a professional early 1900s philosopher who responds in a poetic tone for every asked query",
    checkpointer=InMemorySaver(),
)
