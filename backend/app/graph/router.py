from langchain_core.messages import HumanMessage, AIMessage
from ..graph import runtime


def run_agent(user_input: str, thread_id: str):
    if runtime.agent is None:
        raise RuntimeError("Graph not initialized")

    config = {
        "configurable": {
            "thread_id": thread_id
        }
    }

    result_state = runtime.agent.invoke(
        {
            "messages": [HumanMessage(content=user_input)],
        },
        config
    )

    for msg in reversed(result_state.get("messages", [])):
            if isinstance(msg, AIMessage):
                if msg.tool_calls:
                    continue
                if isinstance(msg.content, list):
                    return "\n".join(
                        chunk.get("text", "")
                        for chunk in msg.content
                        if chunk.get("type") == "text"
                    ).strip()

                return msg.content.strip()

    return "No answer generated."
