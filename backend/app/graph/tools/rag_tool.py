from langchain.tools import tool, ToolRuntime
from ...rag.retriever import get_retriever

retriever = get_retriever()   # this is a Runnable retriever

@tool
def scholarship_tool(query: str) -> str:
    """
    Search scholarship documents and return relevant content.
    """
    docs = retriever.invoke(query)

    if not docs:
        return "No relevant scholarship information found."

    return "\n\n".join(doc.page_content for doc in docs)
