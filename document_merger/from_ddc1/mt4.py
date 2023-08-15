import os
import comtypes.client
from PyPDF2 import PdfMerger, PdfReader


def docxs_to_pdf(doc_paths):
    """Converts Word files to PDFs and appends them to pdfslist"""
    word = comtypes.client.CreateObject('Word.Application')
    temp_pdf_paths = []  # Store the paths of temporary PDFs
    for doc_path in doc_paths:
        input_file = os.path.abspath(doc_path)
        output_file = os.path.abspath("demo.pdf")

        # Load each Word document
        doc = word.Documents.Open(input_file)
        doc.SaveAs(output_file, FileFormat=16 + 1)
        doc.Close()  # Closes the document, not the application
        temp_pdf_paths.append(output_file)
    word.Quit()



    return temp_pdf_paths


def merge_pdfs(input_pdf_paths, output_pdf_path):
    """Merge all PDFs and save the result"""
    pdf_merger = PdfMerger()
    for pdf_path in input_pdf_paths:
        pdf_merger.append(pdf_path)

    with open(output_pdf_path, "wb") as result_pdf:
        pdf_merger.write(result_pdf)
    pdf_merger.close()

def main():
    """Convert Word docs to PDFs, merge PDFs, clean up"""
    input_docx_paths = [
        'E:\Project\Job\GQ\Python\Baidu_downlaod_upload\Baidu_Pyqt5_Threading\document_merger\\from_ddc1\\temp\\temp_doc_0.docx',
        'E:\Project\Job\GQ\Python\Baidu_downlaod_upload\Baidu_Pyqt5_Threading\document_merger\\from_ddc1\\temp\\temp_doc_1.docx',
        'E:\Project\Job\GQ\Python\Baidu_downlaod_upload\Baidu_Pyqt5_Threading\document_merger\\from_ddc1\\temp\\temp_doc_2.docx',
        # Add more paths as needed
    ]

    output_pdf_path = 'E:\Project\Job\GQ\Python\Baidu_downlaod_upload\Baidu_Pyqt5_Threading\document_merger\\from_ddc1\gen\\new5.pdf'

    temp_pdf_paths = docxs_to_pdf(input_docx_paths)
    merge_pdfs(temp_pdf_paths, output_pdf_path)

    try:
        # # Clean up temporary PDFs
        for temp_pdf in temp_pdf_paths:
            os.remove(temp_pdf)
    except:
        print ("")


if __name__ == "__main__":
    main()
