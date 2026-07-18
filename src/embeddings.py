from langchain_google_genai import GoogleGenerativeAIEmbeddings

from src.config import GOOGLE_API_KEY


def get_embeddings():
    """
    Crea y devuelve el modelo de embeddings de Google Gemini.
    """

    embeddings = GoogleGenerativeAIEmbeddings(
        model="models/embedding-001",
        google_api_key=GOOGLE_API_KEY
    )

    return embeddings