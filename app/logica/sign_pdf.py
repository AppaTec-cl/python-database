import PyPDF2
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import io
import os

output_pdf_path = os.path.join(os.path.expanduser('~'), 'Downloads', 'output.pdf')


def add_signature_to_pdf(pdf_path, signature_image_path, output_pdf_path):
    # Leer el PDF original
    input_pdf = PyPDF2.PdfReader(pdf_path)
    num_pages = len(input_pdf.pages)

    # Crear un PDF temporal para la firma
    packet = io.BytesIO()
    c = canvas.Canvas(packet, pagesize=letter)
    # Asumiendo que la firma debe estar a 100, 50 (x, y) desde la esquina inferior derecha
    x_position = 500  # Ajusta estas coordenadas según tus necesidades
    y_position = 50
    c.drawImage(signature_image_path, x_position, y_position, width=100,
                height=50)  # Ajusta el tamaño según sea necesario
    c.save()

    # Mover al principio del StringIO buffer
    packet.seek(0)
    new_pdf = PyPDF2.PdfReader(packet)
    output_pdf = PyPDF2.PdfWriter()

    # Copiar todas las páginas del PDF original y añadir la firma a la última página
    for i in range(num_pages):
        page = input_pdf.pages[i]
        if i == num_pages - 1:  # Solo añadir la firma a la última página
            page.merge_page(new_pdf.pages[0])
        output_pdf.add_page(page)

    # Escribir el PDF modificado a un archivo
    with open(output_pdf_path, 'wb') as f_out:
        output_pdf.write(f_out)


# Uso de la función
pdf_original_path = 'path_to_original.pdf'
signature_img_path = 'path_to_signature_image.png'
output_pdf_path = 'path_to_output.pdf'

add_signature_to_pdf(pdf_original_path, signature_img_path, output_pdf_path)
