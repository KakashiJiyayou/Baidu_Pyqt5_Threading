import pypandoc
output = pypandoc.convert(
    source='E:\Project\Job\GQ\Python\Baidu_downlaod_upload\Baidu_Pyqt5_Threading\document_merger\html_to_docx\CCTV.html',
    format='html',
    to='docx',
    outputfile='E:\Project\Job\GQ\Python\Baidu_downlaod_upload\Baidu_Pyqt5_Threading\document_merger\html_to_docx\CCTV.docx',
    extra_args=['-RTS'])

# from htmldocx import HtmlToDocx
#
# new_parser = HtmlToDocx()
# new_parser.parse_html_file(
#     "E:\Project\Job\GQ\Python\Baidu_downlaod_upload\Baidu_Pyqt5_Threading\document_merger\html_to_docx\CCTV.html",
#     "E:\Project\Job\GQ\Python\Baidu_downlaod_upload\Baidu_Pyqt5_Threading\document_merger\html_to_docx\CCTV")
# #Files extensions not needed, but tolerated