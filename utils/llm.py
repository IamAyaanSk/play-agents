from langchain.chat_models import init_chat_model

model = init_chat_model(
    model="openai:nvidia/nemotron-3-nano-4b", use_responses_api=True
)
