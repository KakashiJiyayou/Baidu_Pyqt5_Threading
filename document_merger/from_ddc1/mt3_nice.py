import os
import comtypes.client
from PyPDF2 import PdfMerger

temp_list = []

def docxs_to_pdf(doc_paths):
    global  temp_list
    """Converts Word files to PDFs and appends them to pdfslist"""
    word = comtypes.client.CreateObject('Word.Application')
    pdfslist = PdfMerger()

    x = 0
    for doc_path in doc_paths:
        input_file = os.path.abspath(doc_path)
        output_file = os.path.abspath("demo" + str(x) + ".pdf")

        # Load each Word document
        doc = word.Documents.Open(input_file)
        doc.SaveAs(output_file, FileFormat=16 + 1)
        doc.Close()  # Closes the document, not the application
        pdfslist.append(output_file)
        temp_list.append ( output_file )
        x += 1
    word.Quit()
    return pdfslist


def joinpdf(pdfs, output_pdf_path):
    """Unite all PDFs"""
    with open(output_pdf_path, "wb") as result_pdf:
        pdfs.write(result_pdf)



def main():
    """Convert Word docs to PDFs, unite PDFs"""
    input_docx_paths = [
        'E:\Project\Job\GQ\Python\Baidu_downlaod_upload\Baidu_Pyqt5_Threading\document_merger\\from_ddc1\\temp\\temp_doc_0.docx',
        'E:\Project\Job\GQ\Python\Baidu_downlaod_upload\Baidu_Pyqt5_Threading\document_merger\\from_ddc1\\temp\\temp_doc_1.docx',
        'E:\Project\Job\GQ\Python\Baidu_downlaod_upload\Baidu_Pyqt5_Threading\document_merger\\from_ddc1\\temp\\temp_doc_2.docx',
        # Add more paths as needed
    ]

    output_pdf_path = 'E:\Project\Job\GQ\Python\Baidu_downlaod_upload\Baidu_Pyqt5_Threading\document_merger\\from_ddc1\gen\\new8.pdf'

    pdfs = docxs_to_pdf(input_docx_paths)
    joinpdf(pdfs, output_pdf_path)
    pdfs.close()

    try:
        # # Clean up temporary PDFs
        for temp_pdf in temp_list:
            os.remove(temp_pdf)
    except:
        print ("")


if __name__ == "__main__":
    main()
