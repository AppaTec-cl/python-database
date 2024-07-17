import os
import PyPDF2
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import io

from ..models import contract, user

def add_signature_to_pdf(pdf_path, signature_image_path):
    # Ruta en la carpeta de descargas
    output_pdf_path = os.path.join(os.path.expanduser('~'), 'Downloads', 'signed_contract.pdf')

    input_pdf = PyPDF2.PdfReader(pdf_path)
    num_pages = len(input_pdf.pages)

    # Crear un PDF temporal para la firma
    packet = io.BytesIO()
    c = canvas.Canvas(packet, pagesize=letter)
    x_position = 500
    y_position = 50
    c.drawImage(signature_image_path, x_position, y_position, width=100, height=50)
    c.save()

    packet.seek(0)
    new_pdf = PyPDF2.PdfReader(packet)
    output_pdf = PyPDF2.PdfWriter()

    for i in range(num_pages):
        page = input_pdf.pages[i]
        if i == num_pages - 1:
            page.merge_page(new_pdf.pages[0])
        output_pdf.add_page(page)

    with open(output_pdf_path, 'wb') as f_out:
        output_pdf.write(f_out)
    print(f"Archivo guardado en: {output_pdf_path}")

pdf_original_path = contract.contrato
signature_img_path = user.firma

add_signature_to_pdf(pdf_original_path, signature_img_path)
