import mammoth

with open("E:\Project\Job\GQ\Python\Baidu_downlaod_upload\Baidu_Pyqt5_Threading\document_merger\doc_to_html\\doc2.docx", "rb") as docx_file:
    result = mammoth.convert_to_html(docx_file)
    html = result.value  # The generated HTML
    messages = result.messages  # Any messages,

    full_html = (
        '<!DOCTYPE html><html><head><meta charset="utf-8"/></head><body>'
        + html
        + "</body></html>"
    )

    with open("E:\Project\Job\GQ\Python\Baidu_downlaod_upload\Baidu_Pyqt5_Threading\document_merger\doc_to_html\\doc2.html", "w", encoding="utf-8") as f:
        f.write(full_html)
