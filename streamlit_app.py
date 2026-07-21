import streamlit as st

from src.loader import load_pdf
from src.splitter import split_text
from src.embeddings import get_embeddings
from src.vector_store import (
    create_vector_store,
    load_vector_store
)
from src.chatbot import (
    create_chat_model,
    answer_question
)


st.set_page_config(
    page_title="BimBam Buy AI",
    page_icon="🤖"
)

st.title("🤖 Agente IA - BimBam Buy")

st.write(
    "Haz preguntas sobre la política de reembolsos y devoluciones."
)


@st.cache_resource
def load_resources():

    pdf_path = "Data/politica_de_reembolsos_y_devoluciones_de_BimBam_Buy.pdf"

    document = load_pdf(pdf_path)

    chunks = split_text(document)

    embeddings = get_embeddings()

    vector_store = load_vector_store(embeddings)

    if vector_store is None:

        vector_store = create_vector_store(
            chunks,
            embeddings
        )

    llm = create_chat_model()

    return vector_store, llm


vector_store, llm = load_resources()


question = st.text_input(
    "Escribe tu pregunta:"
)

if st.button("Preguntar"):

    if question.strip():

        with st.spinner("Pensando..."):

            answer = answer_question(
                vector_store,
                llm,
                question
            )

        st.success(answer)