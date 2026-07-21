import os

from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if not GOOGLE_API_KEY:
    GOOGLE_API_KEY = st.secrets.get("GOOGLE_API_KEY")

print("ENV:", os.getenv("GOOGLE_API_KEY"))
print("SECRETS:", st.secrets.get("GOOGLE_API_KEY", None))

if not GOOGLE_API_KEY:
    raise ValueError(
        "No se encontró GOOGLE_API_KEY."
    )