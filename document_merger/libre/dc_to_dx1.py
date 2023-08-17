import os
import subprocess


def convert_doc_to_docx(input_docs, output_dir):
    new_docx = []
    try:
        # Create the output directory if it doesn't exist
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        for input_doc in input_docs:
            output_docx = os.path.join(output_dir, os.path.splitext(os.path.basename(input_doc))[0] + ".docx")

            # Replace this with the actual path to soffice executable on your system
            soffice_path = r"E:\Installed\LibreOffice\program\soffice.exe"

            # Run the LibreOffice command to convert the document to DOCX
            subprocess.run([soffice_path, "--headless", "--convert-to", "docx", input_doc, "--outdir", output_dir],
                           check=True)

            print(f"Conversion successful: {input_doc} -> {output_docx}")

            new_docx.append( output_docx )
    except subprocess.CalledProcessError as e:
        print("Conversion failed:", e)

    return  new_docx


# Replace these with actual paths
input_docs_list = [
    r"E:\Project\Job\GQ\Python\Baidu_downlaod_upload\Baidu_Pyqt5_Threading\document_merger\libre\docx\CCTV.doc",
    r"E:\Project\Job\GQ\Python\Baidu_downlaod_upload\Baidu_Pyqt5_Threading\document_merger\libre\docx\doc2.doc",
    r"E:\Project\Job\GQ\Python\Baidu_downlaod_upload\Baidu_Pyqt5_Threading\document_merger\libre\docx\doc3.doc"
]
output_docx_dir = r"E:\Project\Job\GQ\Python\Baidu_downlaod_upload\Baidu_Pyqt5_Threading\document_merger\libre\temp"

convert_doc_to_docx(input_docs_list, output_docx_dir)
