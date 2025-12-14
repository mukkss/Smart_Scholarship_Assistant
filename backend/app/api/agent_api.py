from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from ..graph.router import run_agent

router = APIRouter(prefix="/agent", tags=["Agent"])

class AgentRequest(BaseModel):
    query: str


@router.post("/run")
def run_agent_api(request: AgentRequest):
    try:
        result = run_agent(request.query)
        return {"answer": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    