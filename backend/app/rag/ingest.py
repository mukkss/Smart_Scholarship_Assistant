from typing import List
from pathlib import Path
from langchain_core.documents import Document
from .preprocessor import load_and_split_pdfs
from .embed import get_embedding_model
from .vectorstore import get_vector_store
from ..config import PINECONE_INDEX_NAME, PINECONE_API_KEY, GOOGLE_API_KEY


def build_pinecone_index(folder_path: str, index_name: str):
    """
    Loads PDFs → splits → embeds → stores in Pinecone.
    """


    folder = Path(folder_path)

    # -----------------------------------
    # 1. PATH VALIDATION
    # -----------------------------------
    if not folder.exists():
        raise FileNotFoundError(f"Path does not exist: {folder.resolve()}")

    # If input is a file, convert to parent folder
    if folder.is_file():
        print(f"⚠️ Provided path is a FILE. Using parent folder instead: {folder.parent}")
        folder = folder.parent
        

    
    print("Loading & splitting PDFs...")
    documents: List[Document] = load_and_split_pdfs(folder_path)

    if not documents:
        raise ValueError("No valid documents found to index")

    print(f"Total chunks created: {len(documents)}")

    print("Initializing embedding model...")
    embedding_model = get_embedding_model()

    print("Connecting to Pinecone vector store...")
    vectorstore = get_vector_store(index_name)

    print("Uploading chunks to Pinecone...")
    vectorstore.add_documents(documents)

    print("Indexing complete!")
    return f"Indexed {len(documents)} chunks into Pinecone '{index_name}'"


# Example usage:
build_pinecone_index(
    folder_path="data/",
    index_name=PINECONE_INDEX_NAME
)
