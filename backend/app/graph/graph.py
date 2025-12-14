from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import ToolNode, tools_condition

from .state import AgentState
from .nodes.agent_node import chatbot
from .tools.rag_tool import scholarship_tool as scholarship_rag

def build_graph():
    builder = StateGraph(AgentState)

    # Nodes
    builder.add_node("chatbot", chatbot)
    builder.add_node("tools", ToolNode([scholarship_rag]))

    # Flow
    builder.add_edge(START, "chatbot")
    builder.add_conditional_edges("chatbot", tools_condition)
    builder.add_edge("tools", "chatbot")
    builder.add_edge("chatbot", END)

    return builder.compile()
