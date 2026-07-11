from pypdf import PdfReader


def load_pdf(pdf_path):
    """
    Lee un archivo PDF y devuelve todo su contenido como un único texto.

    Parámetros:
        pdf_path (str): Ruta del archivo PDF.

    Retorna:
        str: Texto completo del documento.
    """

    # Abrimos el PDF
    reader = PdfReader(pdf_path)

    # Variable donde iremos almacenando el texto
    text = ""

    # Recorremos todas las páginas del documento
    for page in reader.pages:

        # Extraemos el texto de la página
        page_text = page.extract_text()

        # Algunas páginas pueden no contener texto
        if page_text:
            text += page_text + "\n"

    return text