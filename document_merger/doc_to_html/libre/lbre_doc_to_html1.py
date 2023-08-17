import subprocess

# Replace this with the actual path to soffice executable on your system
soffice_path = r"E:\Installed\LibreOffice\program\soffice.exe"

# input doc
input_doc = r"E:\Project\Job\GQ\Python\Baidu_downlaod_upload\Baidu_Pyqt5_Threading\document_merger\libre\docx\下水管道养护工 张明华.doc"

#output_dir
output_dir = r"E:\Project\Job\GQ\Python\Baidu_downlaod_upload\Baidu_Pyqt5_Threading\document_merger\doc_to_html\libre\temp"

# Run the LibreOffice command to convert the document to DOCX
subprocess.run(
    [soffice_path,
     "--headless",
     "--convert-to",
      'html',
     input_doc,
     "--outdir",
     output_dir],
    check=True)