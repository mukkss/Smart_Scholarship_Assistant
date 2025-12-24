from ...llm.model import get_llm
from ..tools import TOOLS
from ..state import AgentState
from langchain_core.messages import AIMessage, SystemMessage
from ...utils.summarize_db_context import summarize_messages

llm = get_llm()
llm_with_tools = llm.bind_tools(TOOLS)


RAG_KEYWORDS = [
    "scholarship", "scholarships", "award", "grant",
    "funding", "apply", "deadline", "eligibility", "requirements"
]


MAX_RECENT_MESSAGES = 6
SUMMARIZE_AFTER = 10


def agent_node(state: AgentState):
    messages = state["messages"]
    summary = state.get("summary")

    if len(messages) > SUMMARIZE_AFTER:
        old_messages = messages[:-MAX_RECENT_MESSAGES]
        recent_messages = messages[-MAX_RECENT_MESSAGES:]

        new_summary = summarize_messages(
            old_messages=old_messages,
            existing_summary=summary
        )

        messages = [
            SystemMessage(content=f"Conversation summary:\n{new_summary}")
        ] + recent_messages

        summary = new_summary

    user_query = messages[-1].content.lower()
    is_rag_query = any(k in user_query for k in RAG_KEYWORDS)

    system_prompt = f"""
        You are a scholarship assistant.

        You MUST follow this process exactly:

        STEP 1: Decide if the query is about scholarships.
        STEP 2: If yes, CALL `scholarship_tool` first.
        STEP 3: AFTER receiving the tool result:
            - If the result says "no results" or "not found",
            THEN call `google_search_tool`.
            - Otherwise, use the RAG result.
        STEP 4: Produce a FINAL ANSWER for the user.
            - Do NOT mention tools
            - Do NOT explain your reasoning
            - Do NOT say "according to the tool"

        TOOLS AVAILABLE:
        - scholarship_tool → internal scholarship database
        - google_search_tool → external web search

        Current routing decision: {"RAG-first" if is_rag_query else "Web-first"}
    """

    response = llm_with_tools.invoke(
        [SystemMessage(content=system_prompt)] + messages
    )


    return {
        "messages": [response],
        "summary": summary,
        "final_answer": response.content
    }
