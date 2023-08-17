from bs4 import BeautifulSoup
import os

def merge_html_files(html_and_image_paths, output_path):
    combined_html = ""

    for path in html_and_image_paths:
        if path.lower().endswith(('.html', '.htm')):
            with open(path, "r", encoding="utf-8") as file:
                html_content = file.read()
                soup = BeautifulSoup(html_content, "html.parser")
                body_content = str(soup.body)
                combined_html += body_content
        elif path.lower().endswith(('.png', '.jpg', '.jpeg')):
            image_tag = f'<img src="{path}" alt="{os.path.basename(path)}">'
            combined_html += image_tag

    # Wrap the combined content in a complete HTML structure
    full_html = (
        '<!DOCTYPE html><html><head><meta charset="utf-8"/></head><body>'
        + combined_html
        + "</body></html>"
    )

    # Write the combined content to the output file
    with open(output_path, "w", encoding="utf-8") as file:
        file.write(full_html)

# List of paths to the HTML files and image files you want to merge (in desired order)
input_files = [
    r"E:\Project\Job\GQ\Python\Baidu_downlaod_upload\Baidu_Pyqt5_Threading\document_merger\doc_to_html\libre\temp\CCTV.html",
    r"E:\Project\Job\GQ\Python\Baidu_downlaod_upload\Baidu_Pyqt5_Threading\document_merger\doc_to_html\libre\temp\CCTV检测文件5页.html",
    r"E:\Project\Job\GQ\Python\Baidu_downlaod_upload\Baidu_Pyqt5_Threading\document_merger\doc_to_html\libre\temp\下水管道养护工 张明华.html",
    r"E:\Project\Job\GQ\Python\Baidu_downlaod_upload\Baidu_Pyqt5_Threading\document_merger\doc_to_html\libre\temp\gui.png",
    r"E:\Project\Job\GQ\Python\Baidu_downlaod_upload\Baidu_Pyqt5_Threading\document_merger\doc_to_html\libre\temp\BÂ.png",
    r"E:\Project\Job\GQ\Python\Baidu_downlaod_upload\Baidu_Pyqt5_Threading\document_merger\doc_to_html\libre\temp\doc3.html",
    r"E:\Project\Job\GQ\Python\Baidu_downlaod_upload\Baidu_Pyqt5_Threading\document_merger\doc_to_html\libre\temp\deetss.jpg",

    # Add more files and images as needed
]

# Output file name for the merged HTML document
output_file = r"E:\Project\Job\GQ\Python\Baidu_downlaod_upload\Baidu_Pyqt5_Threading\document_merger\doc_to_html\libre\temp\merged_img.html"

merge_html_files(input_files, output_file)
