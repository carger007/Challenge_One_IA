from google import genai

from src.config import GOOGLE_API_KEY


def create_chat_model():
    """
    Crea el modelo de chat de Gemini.
    """

    client = genai.Client(api_key=GOOGLE_API_KEY)

    return client

def answer_question(vector_store, client, question):

    # Buscar los 3 fragmentos más relevantes
    docs = vector_store.similarity_search(
        question,
        k=3
    )

    # Unimos el contenido encontrado
    context = "\n\n".join(
        doc.page_content
        for doc in docs
    )

    # Construimos el prompt
    prompt = f"""
Eres un asistente que responde únicamente utilizando la información del contexto.

Si la respuesta no aparece en el contexto responde exactamente:

"No encontré esa información en el documento."

====================

CONTEXTO

{context}

====================

PREGUNTA

{question}

====================

RESPUESTA
"""

    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt
    )

    return response.text