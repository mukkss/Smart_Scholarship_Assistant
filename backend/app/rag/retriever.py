import os
from pinecone import Pinecone
from langchain_pinecone import PineconeVectorStore
from functools import lru_cache

from .embed import get_embedding_model
from ..config import PINECONE_API_KEY, PINECONE_INDEX_NAME


# Cache the embedding model to avoid reloading
@lru_cache
def _get_embeddings():
    return get_embedding_model()


def get_vector_store():
    pc = Pinecone(api_key=PINECONE_API_KEY)

    available_indexes = pc.list_indexes().names()
    if PINECONE_INDEX_NAME not in available_indexes:
        raise ValueError(f"Pinecone index '{PINECONE_INDEX_NAME}' not found")

    index = pc.Index(PINECONE_INDEX_NAME)

    return PineconeVectorStore(
        index=index,
        embedding=_get_embeddings()
    )


def get_retriever():
    """
    Creates a similarity_score_threshold-based retriever.
    Recommended settings for Scholarship RAG.
    """

    vector_store = get_vector_store()
    retriever = vector_store.as_retriever(
        search_type="similarity_score_threshold",
        search_kwargs={
            "k": 3,                # return top 3 docs
            "score_threshold": 0.4 # minimum similarity
        }
    )
    return retriever
