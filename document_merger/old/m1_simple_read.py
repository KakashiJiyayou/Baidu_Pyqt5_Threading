from docx import Document
from shutil import copyfile


def copy_document(input_path, output_path):
    try:
        # Copy the original document to the output path
        copyfile(input_path, output_path)

        # Open the copied document
        doc = Document(output_path)

        # Add a new paragraph at the end
        doc.add_paragraph("This is a new paragraph added to the copied document.")

        # Save the changes
        doc.save(output_path)

        print("Document copied and modified successfully.")
    except Exception as e:
        print(f"Error: {e}")


# Example usage
input_files = "E:\Project\Job\GQ\Python\Baidu_downlaod_upload\Baidu_Pyqt5_Threading\document_merger\CCTV.doc"
output_file = "E:\Project\Job\GQ\Python\Baidu_downlaod_upload\Baidu_Pyqt5_Threading\document_merger\combined_output.doc"

copy_document(input_files , output_file)