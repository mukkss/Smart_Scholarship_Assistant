from typing import Literal
from langchain_core.messages import AIMessage
from langgraph.graph import StateGraph, START, END

from .state import AgentState
from .nodes.agent_node import agent_node
from .nodes.tool_node import execute_tools



def should_continue(state: AgentState) -> Literal["tools", "END"]:
    last = state["messages"][-1]
    return "tools" if isinstance(last, AIMessage) and last.tool_calls else END

def build_graph(checkpointer):
    graph = StateGraph(AgentState)

    graph.add_node("agent", agent_node)
    graph.add_node("tools", execute_tools)

    graph.add_edge(START, "agent")
    graph.add_conditional_edges("agent", should_continue, ["tools", END])
    graph.add_edge("tools", "agent")

    return graph.compile(checkpointer=checkpointer)
