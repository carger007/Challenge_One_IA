import os

from dotenv import load_dotenv

load_dotenv()

print("GOOGLE_API_KEY encontrada:", os.getenv("GOOGLE_API_KEY") is not None)

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if not GOOGLE_API_KEY:
    raise ValueError(
        "No se encontró GOOGLE_API_KEY. Configúrala en el archivo .env o en los Secrets de Streamlit."
    )