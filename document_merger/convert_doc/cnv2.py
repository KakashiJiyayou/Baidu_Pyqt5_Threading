import os
import tempfile
import win32com.client

def convert_doc_to_docx(doc_path, output_folder, index):
    temp_name = f"temp{index}.docx"
    temp_docx_path = os.path.join(output_folder, temp_name)

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
doc_path = 'E:\Project\Job\GQ\Python\Baidu_downlaod_upload\Baidu_Pyqt5_Threading\document_merger\convert_doc\doc4.doc'
output_folder = r'E:\Project\Job\GQ\Python\Baidu_downlaod_upload\Baidu_Pyqt5_Threading\document_merger\convert_doc\temp'
index = 4  # Adjust the index as needed

temp_docx_path = convert_doc_to_docx(doc_path, output_folder, index)
if temp_docx_path:
    print(f"Temporary DOCX file saved as: {temp_docx_path}")
