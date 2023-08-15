import os
import win32com.client
import tempfile

def convert_doc_to_docx(doc_path, output_folder):
    temp_fd, temp_docx_path = tempfile.mkstemp(suffix='.docx', dir=output_folder)
    os.close(temp_fd)

    # Use pywin32 to interact with Word for DOC to DOCX conversion
    try:
        word = win32com.client.Dispatch("Word.Application")
        doc = word.Documents.Open(doc_path)
        doc.SaveAs2(temp_docx_path, FileFormat=16)  # 16 represents DOCX format
        doc.Close()
        word.Quit()
    except Exception as e:
        print(f"Error converting {doc_path} to DOCX: {e}")
        return None

    return temp_docx_path
# Example usage
doc_path = 'E:\Project\Job\GQ\Python\Baidu_downlaod_upload\Baidu_Pyqt5_Threading\document_merger\convert_doc\CCTV.doc'
output_folder = 'E:\Project\Job\GQ\Python\Baidu_downlaod_upload\Baidu_Pyqt5_Threading\document_merger\convert_doc'
docx_path = convert_doc_to_docx(doc_path, output_folder)
if docx_path:
    print(f"Conversion successful. DOCX file saved at: {docx_path}")
else:
    print("Conversion failed.")