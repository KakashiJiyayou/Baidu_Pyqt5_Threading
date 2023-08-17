import os
import re
import base64
from bs4 import BeautifulSoup
from shutil import copy
from urllib.parse import unquote
import requests

def is_url_encoded(path):
    return re.search(r'%[0-9a-fA-F]{2}', path) is not None




def save_base64_image(base64_data, output_folder, img_count):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

        # Extract image type and data from the base64 string
    img_match = re.match(r'data:image/(?P<ext>.*?);base64,(?P<data>.*)', base64_data)
    if img_match:
        img_ext = img_match.group('ext')
        img_data = img_match.group('data').encode('utf-8')
        img_filename = f'Image_{img_count}.{img_ext}'
        img_path = os.path.join(output_folder, img_filename)

        with open(img_path, 'wb') as img_file:
            img_file.write(base64.b64decode(img_data))

        print(f"Saved: {img_filename}")
        return img_path  # Return the path of the saved image
    else:
        print("Invalid base64 image data")
        return None

def extract_and_replace_images(html_content, output_folder):
    soup = BeautifulSoup(html_content, 'html.parser')
    img_tags = soup.find_all('img')

    img_count = 0
    for img_tag in img_tags:
        img_src = img_tag.get('src')

        # got null
        if not img_src:
            return None

        # judge wheher it is base-64 or not
        if  img_src.startswith('data:image'):
            img_count += 1
            img_path = save_base64_image(img_src, output_folder, img_count)
            if img_path:
                img_tag.replace_with(f'IMAG_SRC_{img_count}@@@{img_path}')
            else:
                img_tag.replace_with(f'IMAG_SRC_{img_count}@@@Error')

        # not base 64
        else:
            img_count += 1
            img_src = unquote(img_src)
            img_filename = os.path.basename( img_src )
            dest_path = os.path.join ( output_folder, img_filename )
            path_exists = os.path.exists( img_src )
            print("copy from ", img_src)
            if not path_exists:
                temp_path = r"E:\Project\Job\GQ\Python\Baidu_downlaod_upload\Baidu_Pyqt5_Threading\document_merger\doc_to_html\libre\temp"
                img_src = os.path.join( temp_path, img_src )
            print("copy from ", img_src)
            copy(img_src, dest_path)
            img_tag.replace_with(f'IMAG_SRC_{img_count}@@@{dest_path}')


    modified_html = str(soup)
    return modified_html


# Read HTML content from file
html_file_path = r'E:\Project\Job\GQ\Python\Baidu_downlaod_upload\Baidu_Pyqt5_Threading\document_merger\doc_to_html\libre\temp\doc3.html'
with open(html_file_path, 'r', encoding='utf-8') as html_file:
    html_content = html_file.read()

# Output folder for saving images
output_folder = 'E:\Project\Job\GQ\Python\Baidu_downlaod_upload\Baidu_Pyqt5_Threading\document_merger\doc_to_html\libre\libre_html_image'

# Call the function to replace <img> tags and save images
modified_html = extract_and_replace_images(html_content, output_folder)

# Write the modified HTML content back to the file
with open(html_file_path, 'w', encoding='utf-8') as html_file:
    html_file.write(modified_html)

# print(modified_html)
