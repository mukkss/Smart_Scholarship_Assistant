from fastapi import APIRouter, HTTPException
from app.graph import runtime
from app.config import DEFAULT_THREAD_ID

router = APIRouter(prefix="/agent", tags=["Agent"])


@router.get("/history")
def get_history():
    if runtime.agent is None:
        raise HTTPException(status_code=503, detail="Graph not initialized")

    config = {
        "configurable": {
            "thread_id": DEFAULT_THREAD_ID
        }
    }

    state = runtime.agent.get_state(config)

    messages = []
    for m in state.values.get("messages", []):
        messages.append({
            "role": "user" if m.type == "human" else "assistant",
            "content": m.content
        })

    return {
        "thread_id": DEFAULT_THREAD_ID,
        "messages": messages
    }


# @router.delete("/clear")
# def clear_memory():
#     result = collection.delete_many(
#         {"thread_id": "default_user_thread"}
#     )
#     return {"deleted": result.deleted_count}
