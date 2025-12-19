import os 
from dotenv import load_dotenv


load_dotenv()

# Google API Key
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Pinecone serverless
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_INDEX_NAME = os.getenv("PINECONE_INDEX_NAME")
PINECONE_DIMENSION = int(os.getenv("PINECONE_DIMENSION"))

# Chunking
CHUNK_SIZE = int(os.getenv("CHUNK_SIZE", "1000"))
CHUNK_OVERLAP = int(os.getenv("CHUNK_OVERLAP", "200"))

# Tavily API Key
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

# Groq API Key
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# MongoDB URI
DB_URI = os.getenv("DB_URI")

# Langsmith Configuration
LANGSMITH_TRACING = os.getenv("LANGSMITH_TRACING")
LANGSMITH_ENDPOINT = os.getenv("LANGSMITH_ENDPOINT")
LANGSMITH_API_KEY = os.getenv("LANGSMITH_API_KEY")
LANGSMITH_PROJECT = os.getenv("LANGSMITH_PROJECT")

# Thread Configuration
DEFAULT_THREAD_ID = os.getenv("DEFAULT_THREAD_ID")