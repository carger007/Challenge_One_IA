from src.loader import load_pdf


def main():

    pdf_path = "data/politica_de_reembolsos_y_devoluciones_de_BimBam_Buy.pdf"

    document = load_pdf(pdf_path)

    print("=" * 50)
    print("PDF leído correctamente")
    print("=" * 50)

    print(f"Cantidad de caracteres: {len(document)}")

    print("\nPrimeros 1000 caracteres:\n")

    print(document[:1000])


if __name__ == "__main__":
    main()