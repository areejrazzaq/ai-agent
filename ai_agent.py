import os
from dotenv import load_dotenv
load_dotenv()
# build agent
from langchain_groq import ChatGroq
from langgraph.prebuilt import create_react_agent
from langchain_tavily import TavilySearch


def fetch_response_from_ai(user_query, allow_search: bool, llm_id: str)->str:
    # "qwen-qwq-32b", "llama-3.3-70b-versatile"
    qroq_llm = ChatGroq(
        model=llm_id
    )

    tool = [TavilySearch(max_results=2)] if allow_search else []

    agent = create_react_agent(
        model=qroq_llm,
        tools = tool
    )

    query = {"messages": user_query}
    response = agent.invoke(query);

    return response["messages"][-1].content;

