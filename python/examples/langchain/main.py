import os

from dotenv import load_dotenv
from langchain_openai import AzureChatOpenAI
from langgraph.prebuilt import create_react_agent

from google_agent_toolkit.langchain.toolkit import GoogleAgentToolkit

load_dotenv()

llm = AzureChatOpenAI(
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    openai_api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    model=os.getenv("AZURE_OPENAI_MODEL_NAME"),
    openai_api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
    azure_deployment=os.getenv("AZURE_OPENAI_CHAT_DEPLOYMENT_NAME"),
)

google_agent_toolkit = GoogleAgentToolkit(
    client_id=os.getenv("GOOGLE_CLIENT_ID"),
    client_secret=os.getenv("GOOGLE_CLIENT_SECRET"),
    configuration={
        "actions": {
            "places": {
                "search": True,
            },
        }
    },
)

tools = []
tools.extend(google_agent_toolkit.get_tools())

langgraph_agent_executor = create_react_agent(llm, tools)

input_state = {
    "messages": """
        Search some happening events in Bangalore this weekend
    """,
}

print("result")
output_state = langgraph_agent_executor.invoke(input_state)

print(output_state)

print(output_state["messages"][-1].content)
