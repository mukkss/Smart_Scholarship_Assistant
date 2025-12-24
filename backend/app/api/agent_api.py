from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import uuid

from ..graph.router import run_agent

router = APIRouter(prefix="/agent", tags=["Agent"])


class AgentRequest(BaseModel):
    query: str
    thread_id: str | None = None


@router.post("/run")
def run_agent_api(request: AgentRequest):
    try:
        thread_id = request.thread_id or str(uuid.uuid4())

        result = run_agent(
            user_input=request.query,
            thread_id=thread_id
        )

        return {
            "answer": result
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))