from fastapi import FastAPI
from .api.test_retriever import router as retriever_router

app = FastAPI()

app.include_router(retriever_router)
