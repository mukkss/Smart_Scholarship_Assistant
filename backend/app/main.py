from fastapi import FastAPI
from .api.test_retriever import router as retriever_router
from .api.agent_api import router as agent_router
from .api.check_db import router as check_state_router
from fastapi.middleware.cors import CORSMiddleware
from .utils.db_context_mnger import graph_lifespan


app = FastAPI(lifespan=graph_lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(retriever_router)
app.include_router(agent_router)
app.include_router(check_state_router)
