from langchain_core.messages import AIMessage, ToolMessage
from ..state import AgentState
from ..tools import scholarship_tool, google_search_tool

def execute_tools(state: AgentState):
    messages = state["messages"]
    last_message = messages[-1]

    if not isinstance(last_message, AIMessage) or not last_message.tool_calls:
        return {"messages": []}

    results = []
    rag_success = state.get("rag_success", False)

    for call in last_message.tool_calls:
        name = call["name"]
        args = call["args"]

        if name == "scholarship_tool":
            rag_result = scholarship_tool.invoke(args)

            if "no results" in rag_result.lower() or "not found" in rag_result.lower():
                results.append(
                    ToolMessage(
                        content="NO_RAG_RESULTS",
                        tool_call_id=call["id"]
                    )
                )
            else:
                rag_success = True
                results.append(
                    ToolMessage(
                        content=rag_result,
                        tool_call_id=call["id"]
                    )
                )

        elif name == "google_search_tool":
            web_query = args.get("query", "")
            web_result = google_search_tool.invoke(web_query)
            results.append(
                ToolMessage(
                    content=web_result,
                    tool_call_id=call["id"]
                )
            )

    return {
        "messages": results,
        "rag_success": rag_success
    }
