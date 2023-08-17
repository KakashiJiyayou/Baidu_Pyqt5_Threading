from bs4 import BeautifulSoup

def merge_html_files(html_paths, output_path):
    combined_html = ""

    # Read the content of each HTML file, extract the body content, and append to the combined_html string
    for html_path in html_paths:
        with open(html_path, "r", encoding="utf-8") as file:
            html_content = file.read()
            soup = BeautifulSoup(html_content, "html.parser")
            body_content = str(soup.body)
            combined_html += body_content

    # Wrap the combined body content in a complete HTML structure
    full_html = (
        '<!DOCTYPE html><html><head><meta charset="utf-8"/></head><body>'
        + combined_html
        + "</body></html>"
    )

    # Write the combined content to the output file
    with open(output_path, "w", encoding="utf-8") as file:
        file.write(full_html)

# List of paths to the HTML files you want to merge
input_files = [
    r"E:\Project\Job\GQ\Python\Baidu_downlaod_upload\Baidu_Pyqt5_Threading\document_merger\doc_to_html\libre\temp\CCTV.html",
    r"E:\Project\Job\GQ\Python\Baidu_downlaod_upload\Baidu_Pyqt5_Threading\document_merger\doc_to_html\libre\temp\CCTV检测文件5页.html",
    r"E:\Project\Job\GQ\Python\Baidu_downlaod_upload\Baidu_Pyqt5_Threading\document_merger\doc_to_html\libre\temp\下水管道养护工 张明华.html",
    r"E:\Project\Job\GQ\Python\Baidu_downlaod_upload\Baidu_Pyqt5_Threading\document_merger\doc_to_html\libre\temp\doc3.html",
    # Add more files as needed
]

# Output file name for the merged HTML document
output_file = r"E:\Project\Job\GQ\Python\Baidu_downlaod_upload\Baidu_Pyqt5_Threading\document_merger\doc_to_html\libre\temp\merged.html"

merge_html_files(input_files, output_file)
