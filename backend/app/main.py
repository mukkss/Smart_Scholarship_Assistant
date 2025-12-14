from fastapi import FastAPI
from .api.test_retriever import router as retriever_router
from .api.agent_api import router as agent_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # React dev server
    allow_credentials=True,
    allow_methods=["*"],  # POST, GET, OPTIONS, etc.
    allow_headers=["*"],
)

app.include_router(retriever_router)
app.include_router(agent_router)
