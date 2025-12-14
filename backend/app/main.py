from fastapi import FastAPI
from .api.test_retriever import router as retriever_router
from .api.agent_api import router as agent_router

app = FastAPI()

app.include_router(retriever_router)
app.include_router(agent_router)
