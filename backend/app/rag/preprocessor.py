# from pathlib import Path
# from typing import List
# from langchain_community.document_loaders import PyPDFLoader
# from langchain_core.documents import Document
# from langchain_text_splitters import RecursiveCharacterTextSplitter
# from ..config import CHUNK_SIZE, CHUNK_OVERLAP


# def load_and_split_pdfs(folder_path: str) -> List[Document]:
#     """
#     Loads all PDF files from a folder and splits them into chunked LangChain Documents.
#     Args:
#         folder_path (str): Path to the folder with PDF files.
#     Returns:
#         List[Document]: List of chunked documents with metadata.
#     """
    
#     folder = Path(folder_path)
#     all_chunks: List[Document] = []
    
#     splitter = RecursiveCharacterTextSplitter(
#         chunk_size=CHUNK_SIZE,
#         chunk_overlap=CHUNK_OVERLAP,
#         separators=["\n\n", "\n", " ", ""],
#     )
    
#     for pdf_file in folder.glob("*.pdf"):
#         try:
#             loader = PyPDFLoader(str(pdf_file))
#             docs = loader.load()
            
#             full_text = "\n".join([d.page_content for d in docs]).strip()
#             if not full_text:
#                 print(f"No text extracted from {pdf_file}")
#                 continue
            
#             base_doc = Document(
#                 page_content=full_text,
#                 metadata={"source": str(pdf_file)}
#             )
#             chunks = splitter.split_documents([base_doc])
#             for i, ch in enumerate(chunks):
#                 ch.metadata["chunk_index"] = i
            
#             all_chunks.extend(chunks)
        
#         except Exception as e:
#             print(f"Error loading {pdf_file}: {e}")
#             continue
    
#     return all_chunks




#MarkDown Migration File



from pathlib import Path
from typing import List
from langchain_community.document_loaders import TextLoader
from langchain_core.documents import Document
from langchain_text_splitters import (
    MarkdownHeaderTextSplitter,
    RecursiveCharacterTextSplitter,
)
from ..config import CHUNK_SIZE, CHUNK_OVERLAP


def load_and_split_markdown(folder_path: str) -> List[Document]:
    """
    Loads Markdown (.md) files, splits them by headers for structure,
    then applies recursive chunking for optimal RAG performance.

    Args:
        folder_path (str): Path to folder containing Markdown files.

    Returns:
        List[Document]: Chunked LangChain documents with rich metadata.
    """

    folder = Path(folder_path)
    all_chunks: List[Document] = []

    header_splitter = MarkdownHeaderTextSplitter(
        headers_to_split_on=[
            ("##", "section"),
            ("###", "subsection"),
        ]
    )

    chunk_splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
        separators=["\n\n", "\n", " ", ""],
    )

    for md_file in folder.glob("*.md"):
        try:
            loader = TextLoader(
                file_path=str(md_file),
                encoding="utf-8"
            )
            docs = loader.load()

            full_text = "\n".join(d.page_content for d in docs).strip()
            if not full_text:
                print(f"[WARN] No text extracted from {md_file}")
                continue

            header_docs = header_splitter.split_text(full_text)


            for doc in header_docs:
                doc.metadata.update({
                    "source": str(md_file),
                    "document": md_file.stem,
                    "file_type": "markdown",
                })


            chunks = chunk_splitter.split_documents(header_docs)


            for idx, chunk in enumerate(chunks):
                chunk.metadata["chunk_index"] = idx

            all_chunks.extend(chunks)

        except Exception as e:
            print(f"[ERROR] Failed to process {md_file}: {e}")
            continue

    return all_chunks
