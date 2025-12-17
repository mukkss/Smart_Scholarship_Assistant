import os
from pinecone import Pinecone
from langchain_pinecone import PineconeVectorStore
from .embed import get_embedding_model
from ..config import PINECONE_API_KEY

def get_vector_store(index_name: str):
    pc = Pinecone(PINECONE_API_KEY)
    index = pc.Index(index_name)

    return PineconeVectorStore(
        index=index,
        embedding=get_embedding_model()
    )
