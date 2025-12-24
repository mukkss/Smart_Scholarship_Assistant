from contextlib import asynccontextmanager
from langgraph.checkpoint.mongodb import MongoDBSaver
from ..graph.graph import build_graph
from ..graph import runtime
from ..config import DB_URI


@asynccontextmanager
async def graph_lifespan(app):
    global agent

    with MongoDBSaver.from_conn_string(DB_URI) as saver:
        runtime.agent = build_graph(checkpointer=saver)
        print("LangGraph initialized with MongoDB")
        yield
    print("MongoDBSaver closed")
