from fastapi import APIRouter
from pydantic import BaseModel
from ..rag.retriever import get_retriever

router = APIRouter()


class QueryRequest(BaseModel):
    query: str


@router.post("/test_retriever")
async def test_retriever(request: QueryRequest):
    retriever = get_retriever()
    try:
        docs = retriever.invoke(request.query)
        if not docs:
            return {
                "status": "success",
                "message": "No documents found for this query.",
                "results": []
            }

        return {
            "status": "success",
            "results": [
                {
                    "content": doc.page_content,
                    "metadata": doc.metadata
                }
                for doc in docs
            ]
        }

    except Exception as e:
        return {"status": "error","message": str(e)}
