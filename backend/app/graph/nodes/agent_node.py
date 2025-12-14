from ...llm.model import get_llm
from ..tools import TOOLS
from ..state import AgentState
from langchain_core.messages import AIMessage, SystemMessage

llm = get_llm()
llm_with_tools = llm.bind_tools(TOOLS)


RAG_KEYWORDS = [
    "scholarship", "scholarships", "award", "grant",
    "funding", "apply", "deadline", "eligibility", "requirements"
]

def agent_router(state: AgentState):
    messages = state["messages"]
    user_query = messages[-1].content.lower()
    is_rag_query = any(k in user_query for k in RAG_KEYWORDS)

    system_prompt = f"""
        You are a scholarship assistant.

        TOOLS:
        1. scholarship_tool → internal scholarship database (RAG)
        2. google_search_tool → external web search

        RULES:
        - ALWAYS try scholarship_tool first for scholarship queries
        - ONLY use google_search_tool if RAG returns no results
        - Use web search for latest/current scholarships

        Current query type: {"RAG-first" if is_rag_query else "Web-first"}
    """
    response = llm_with_tools.invoke(
        [SystemMessage(content=system_prompt)] + messages
    )

    return {"messages": [response]}
