# from langchain_google_genai import ChatGoogleGenerativeAI
# from ..config import GOOGLE_API_KEY

# def get_llm():
#     return ChatGoogleGenerativeAI(
#         model="gemini-2.5-flash",
#         temperature=0.2,
#         google_api_key=GOOGLE_API_KEY,
#     )



from langchain_groq import ChatGroq
from ..config import GROQ_API_KEY

def get_llm():
    return ChatGroq(
        model="llama-3.1-8b-instant",
        temperature=0.2,
        api_key=GROQ_API_KEY
    )