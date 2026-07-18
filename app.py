from src.loader import load_pdf
from src.splitter import split_text
from src.embeddings import get_embeddings
from src.vector_store import create_vector_store, load_vector_store
from src.chatbot import (
    create_chat_model,
    answer_question
)

def main():

    pdf_path = "data/politica_de_reembolsos_y_devoluciones_de_BimBam_Buy.pdf"

    document = load_pdf(pdf_path)

    chunks = split_text(document)

    embeddings = get_embeddings()

    vector_store = load_vector_store(embeddings)

    if vector_store is None:

        print("Creando base vectorial...")

        vector_store = create_vector_store(
            chunks,
            embeddings
        )
    else:
        print("Base vectorial cargada correctamente.")

    llm = create_chat_model()

    while True:

        question = input("\nPregunta (o escribe 'salir'): ")

        if question.lower() == "salir":
            break

        answer = answer_question(
            vector_store,
            llm,
            question
        )

        print("\nRespuesta:\n")

        print(answer)

    # print("=" * 50)
    # print("PDF leído correctamente")
    # print("=" * 50)

    # print(f"Cantidad de chunks: {len(chunks)}")

    # print("\nPrimer chunk:\n")

    # print(chunks[0].page_content)

    # print("\nModelo de embeddings creado correctamente.")


if __name__ == "__main__":
    main()