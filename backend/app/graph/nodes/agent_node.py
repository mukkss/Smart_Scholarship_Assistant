from ...llm.model import get_llm
from  ..tools.rag_tool import scholarship_tool

llm = get_llm()
llm_with_tools = llm.bind_tools([scholarship_tool])

def chatbot(state):
    return {
        "messages" : [
            llm_with_tools.invoke(state["messages"])
        ]
    }