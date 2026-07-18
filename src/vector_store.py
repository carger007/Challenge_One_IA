from langchain_community.vectorstores import FAISS


def create_vector_store(chunks, embeddings):
    """
    Crea una base vectorial FAISS a partir de los chunks del documento.
    """

    vector_store = FAISS.from_documents(
        documents=chunks,
        embedding=embeddings
    )

    return vector_store