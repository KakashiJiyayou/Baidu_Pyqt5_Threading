import os


file_path = r"E:\Project\Job\GQ\Python\Baidu_downlaod_upload\Baidu_Pyqt5_Threading\document_merger\doc_docx_merger\docx\CCTV.docx"
file_base, file_extension = os.path.splitext(file_path)
file_path = file_base + '.html'

print( "File path ", file_path )