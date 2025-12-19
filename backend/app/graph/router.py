from langchain_core.messages import HumanMessage, AIMessage
# from .graph import build_graph
from ..config import DEFAULT_THREAD_ID
from ..graph import runtime



def run_agent(user_input:str):
    if runtime.agent is None:
        raise RuntimeError("Graph not initialized")
    
    config = {
        "configurable": {
            "thread_id": DEFAULT_THREAD_ID
        }
    }
    result_state = runtime.agent.invoke(
        {
            "messages": [HumanMessage(content=user_input)],
        },
        config
    )

    for msg in reversed(result_state["messages"]):
        if isinstance(msg, AIMessage):
            if isinstance(msg.content, list):
                return "\n".join(
                    chunk["text"]
                    for chunk in msg.content
                    if chunk.get("type") == "text"
                )
            return msg.content

    return "No answer generated."





