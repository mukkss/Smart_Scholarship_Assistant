from pathlib import Path
from typing import List
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from ..config import CHUNK_SIZE, CHUNK_OVERLAP


def load_and_split_pdfs(folder_path: str) -> List[Document]:
    """
    Loads all PDF files from a folder and splits them into chunked LangChain Documents.
    
    Args:
        folder_path (str): Path to the folder with PDF files.
    
    Returns:
        List[Document]: List of chunked documents with metadata.
    """
    
    folder = Path(folder_path)
    all_chunks: List[Document] = []
    
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
        separators=["\n\n", "\n", " ", ""],
    )
    
    for pdf_file in folder.glob("*.pdf"):
        try:
            loader = PyPDFLoader(str(pdf_file))
            docs = loader.load()
            
            full_text = "\n".join([d.page_content for d in docs]).strip()
            if not full_text:
                print(f"No text extracted from {pdf_file}")
                continue
            
            base_doc = Document(
                page_content=full_text,
                metadata={"source": str(pdf_file)}
            )
            chunks = splitter.split_documents([base_doc])
            for i, ch in enumerate(chunks):
                ch.metadata["chunk_index"] = i
            
            all_chunks.extend(chunks)
        
        except Exception as e:
            print(f"Error loading {pdf_file}: {e}")
            continue
    
    return all_chunks



