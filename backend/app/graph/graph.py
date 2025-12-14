# from langgraph.graph import StateGraph, START, END
# from langgraph.prebuilt import ToolNode, tools_condition

# from .state import AgentState
# from .nodes.agent_node import agent_node as chatbot
# from .tools.rag_tool import scholarship_tool as scholarship_rag

# def build_graph():
#     builder = StateGraph(AgentState)

#     # Nodes
#     builder.add_node("chatbot", chatbot)
#     builder.add_node("tools", ToolNode([scholarship_rag]))

#     # Flow
#     builder.add_edge(START, "chatbot")
#     builder.add_conditional_edges("chatbot", tools_condition)
#     builder.add_edge("tools", "chatbot")
#     builder.add_edge("chatbot", END)

#     return builder.compile()


from typing import Literal
from langchain_core.messages import AIMessage
from langgraph.graph import StateGraph, START, END

from .state import AgentState
from .nodes.agent_node import agent_router
from .nodes.tool_node import execute_tools

def should_continue(state: AgentState) -> Literal["tools", "END"]:
    last = state["messages"][-1]
    return "tools" if isinstance(last, AIMessage) and last.tool_calls else END

def build_graph():
    graph = StateGraph(AgentState)

    graph.add_node("agent", agent_router)
    graph.add_node("tools", execute_tools)

    graph.add_edge(START, "agent")
    graph.add_conditional_edges("agent", should_continue, ["tools", END])
    graph.add_edge("tools", "agent")

    return graph.compile()
