from fastapi import APIRouter
from pydantic import BaseModel
from ..graph.router import run_agent

router = APIRouter()

class AgentRequest(BaseModel):
    query: str


@router.post("/agent")
async def agent_endpoint(request: AgentRequest):
    try:
        response = run_agent(request.query)
        return {
            "status": "success",
            "response": response
        }
    except Exception as e:
        return {"status": "error", "message": str(e)}
    