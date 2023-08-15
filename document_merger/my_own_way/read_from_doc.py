from docx import Document

import os

def extract_images_from_docx(docx_path, output_folder):
    doc = Document(docx_path)
    image_counter = 1

    for shape in doc.inline_shapes:
        if shape.type == 3:  # Check if it's an image
            image_data = shape._inline.graphic.graphicData.pic.blipFill.blip.embed
            image_path = os.path.join(output_folder, f'image{image_counter}.png')
            with open(image_path, 'wb') as img_file:
                img_file.write(doc.part.related_parts[image_data].blob)
            image_counter += 1


output_folder = r"E:\Project\Job\GQ\Python\Baidu_downlaod_upload\Baidu_Pyqt5_Threading\document_merger\my_own_way\temp"

doc_path = "E:\Project\Job\GQ\Python\Baidu_downlaod_upload\Baidu_Pyqt5_Threading\document_merger\my_own_way\doc1.doc"

extract_images_from_docx(doc_path, output_folder )