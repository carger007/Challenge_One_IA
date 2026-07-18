from langchain_google_genai import GoogleGenerativeAIEmbeddings

from src.config import GOOGLE_API_KEY


def get_embeddings():
    """
    Crea y devuelve el modelo de embeddings de Google Gemini.
    """

    embeddings = GoogleGenerativeAIEmbeddings(
        model="gemini-embedding-2-preview",
        google_api_key=GOOGLE_API_KEY,
        task_type="RETRIEVAL_DOCUMENT"
    )

    return embeddings