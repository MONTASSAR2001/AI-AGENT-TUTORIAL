import os
import sys
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langgraph.prebuilt import create_react_agent
from langchain_core.messages import HumanMessage
from tools import ALL_TOOLS

load_dotenv()
groq_key = os.getenv("GROQ_API_KEY")

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=groq_key,
    temperature=0
)

agent_executor = create_react_agent(llm, ALL_TOOLS)

def ask_agent(query):
    try:
        response = agent_executor.invoke({"messages": [HumanMessage(content=query)]})
        return response["messages"][-1].content
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    print(ask_agent("Hello"))