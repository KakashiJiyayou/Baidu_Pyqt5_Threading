import win32com.client as win32
import time

def combine_documents(output_path, *input_paths):
    word_app = win32.gencache.EnsureDispatch('Word.Application')
    word_app.Visible = False

    # Create a new Word document to combine the input documents
    new_doc = word_app.Documents.Add()

    for input_path in input_paths:
        if input_path.lower().endswith('.doc') or input_path.lower().endswith('.docx'):
            input_doc = word_app.Documents.Open(input_path)
            input_doc.Content.Copy()
            new_doc.Content.Paste()
            input_doc.Close()

            # Introduce a delay to prevent the com_error
            time.sleep(1)

    new_doc.SaveAs(output_path)
    new_doc.Close()

    word_app.Quit()
# Example usage
input_files = ["E:\Project\Job\GQ\Python\Baidu_downlaod_upload\Baidu_Pyqt5_Threading\document_merger\CCTV.doc",
               "E:\Project\Job\GQ\Python\Baidu_downlaod_upload\Baidu_Pyqt5_Threading\document_merger\老师协议.docx"]
output_file = "E:\Project\Job\GQ\Python\Baidu_downlaod_upload\Baidu_Pyqt5_Threading\document_merger\combined_output.docx"

combine_documents(output_file, *input_files)