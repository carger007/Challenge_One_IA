import os

from langchain_community.vectorstores import FAISS


VECTOR_DB_PATH = "vectorstore"


def create_vector_store(chunks, embeddings):
    """
    Crea una base vectorial FAISS y la guarda en disco.
    """

    vector_store = FAISS.from_documents(
        documents=chunks,
        embedding=embeddings
    )

    vector_store.save_local(VECTOR_DB_PATH)

    return vector_store


def load_vector_store(embeddings):
    """
    Carga una base vectorial FAISS existente.
    """

    if not os.path.exists(VECTOR_DB_PATH):
        return None

    return FAISS.load_local(
        VECTOR_DB_PATH,
        embeddings,
        allow_dangerous_deserialization=True
    )