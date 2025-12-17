from langchain_huggingface.embeddings import HuggingFaceEmbeddings


def get_embedding_model():
    return HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")


# Ollama Migration File
# from langchain_ollama import OllamaEmbeddings
# def get_embedding_model():
#     return OllamaEmbeddings(model="nomic-embed-text")