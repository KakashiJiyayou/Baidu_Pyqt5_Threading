import pypandoc
output = pypandoc.convert(
    source=r"E:\Project\Job\GQ\Python\Baidu_downlaod_upload\Baidu_Pyqt5_Threading\document_merger\doc_to_html\libre\temp\安全员于娜娜0725.html",
    format='html',
    to='docx',
    outputfile=r"E:\Project\Job\GQ\Python\Baidu_downlaod_upload\Baidu_Pyqt5_Threading\document_merger\doc_to_html\libre\docx_from_html\安全员于娜娜0725.docx",
    extra_args=['-RTS'])

from htmldocx import HtmlToDocx

# new_parser = HtmlToDocx()
# new_parser.parse_html_file(
#     r"E:\Project\Job\GQ\Python\Baidu_downlaod_upload\Baidu_Pyqt5_Threading\document_merger\doc_to_html\libre\temp\big.html",
#     r"E:\Project\Job\GQ\Python\Baidu_downlaod_upload\Baidu_Pyqt5_Threading\document_merger\doc_to_html\libre\docx_from_html\big")
# #Files extensions not needed, but tolerated