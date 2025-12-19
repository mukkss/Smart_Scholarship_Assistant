from langchain_tavily import TavilySearch
from ...config import TAVILY_API_KEY
import os
from langchain_core.tools import tool


os.environ["TAVILY_API_KEY"] = TAVILY_API_KEY

search_engine = TavilySearch(
        max_results=5,
        topic="general",
        include_raw_content=False,
        include_answer=True
    )
    
@tool
def google_search_tool(query: str) -> str:
    """Search scholarships on the web."""
    return search_engine.invoke(query) 