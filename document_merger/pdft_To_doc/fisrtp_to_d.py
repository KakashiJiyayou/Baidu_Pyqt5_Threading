import os
from docx import Document
from PyPDF2 import PdfReader
import re

def clean_textf(text):
    # Remove invalid XML characters
    return re.sub(r'[^\x20-\x7E]', '', text)

def pdf_to_docx(pdf_path, docx_path):
    pdf_reader = PdfReader(pdf_path)

    doc = Document()
    for page_number in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_number]
        text = page.extract_text()
        clean_text = clean_textf(text)
        doc.add_paragraph(clean_text)

    doc.save(docx_path)

# Paths for input PDF, intermediate HTML, and final DOCX files
pdf_input = r'E:\Project\Job\GQ\Python\Baidu_downlaod_upload\Baidu_Pyqt5_Threading\document_merger\pdft_To_doc\Output.pdf'
docx_output = r'E:\Project\Job\GQ\Python\Baidu_downlaod_upload\Baidu_Pyqt5_Threading\document_merger\pdft_To_doc\new.docx'

# Convert PDF to DOCX
pdf_to_docx(pdf_input, docx_output)

print("Conversion completed successfully.")
