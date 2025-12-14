from langchain_core.messages import HumanMessage, AIMessage
from .graph import build_graph

agent  = build_graph()

def run_agent(user_input:str):
    initial_state = {
        "messages": [HumanMessage(content=user_input)],
    }
    result_state = agent.invoke(initial_state)
    
    for msg in reversed(result_state["messages"]):
        if isinstance(msg, AIMessage):
            # Gemini sometimes returns list of chunks
            if isinstance(msg.content, list):
                return "\n".join(
                    chunk["text"]
                    for chunk in msg.content
                    if chunk.get("type") == "text"
                )
            return msg.content

    return "No answer generated."





