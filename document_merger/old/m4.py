from docx import Document
import os
import win32com.client
import tempfile
import shutil

def convert_to_docx(doc_path):
    temp_docx_path = tempfile.mktemp(suffix='.docx')

    try:
        word = win32com.client.Dispatch("Word.Application")
        doc = word.Documents.Open(doc_path)
        doc.SaveAs2(temp_docx_path, FileFormat=16)  # 16 represents DOCX format
        doc.Close()
        word.Quit()
    except Exception as e:
        print(f"Error converting {doc_path} to DOCX: {e}")
        return None

    return temp_docx_path

def extract_and_copy_images(doc, image_dir):
    rels = doc.part.rels
    for rel in rels:
        if "image" in rels[rel].target_ref:
            img_part = rels[rel].target_part
            img_data = img_part.blob
            img_name = img_part.partname.split("/")[-1]
            img_path = os.path.join(image_dir, img_name)
            with open(img_path, "wb") as img_file:
                img_file.write(img_data)

def merge_documents(file_list, output_path):
    doc = Document()

    temp_image_dir = tempfile.mkdtemp()

    for filename in file_list:
        if filename.lower().endswith(('.doc', '.docx')):
            file_path = os.path.join(folder_path, filename)
            try:
                if filename.lower().endswith('.doc'):
                    file_path = convert_to_docx(file_path)
                    if not file_path:
                        continue

                docx_content = Document(file_path)
                for element in docx_content.element.body:
                    doc.element.body.append(element)

                extract_and_copy_images(docx_content, temp_image_dir)
            except Exception as e:
                print(f"Error processing {filename}: {e}")

    doc.save(output_path)
    shutil.rmtree(temp_image_dir)




file_list = ['Asif Coder.doc', 'ok0.docx' , "CCTV.doc"]
folder_path = 'E:\Project\Job\GQ\Python\Baidu_downlaod_upload\Baidu_Pyqt5_Threading\document_merger'
output_filename = 'merge_doc2.docx'
output_folder = 'E:\Project\Job\GQ\Python\Baidu_downlaod_upload\Baidu_Pyqt5_Threading\document_merger\est'


output_path = os.path.join( output_folder, output_filename)
merge_documents(file_list, output_path)
print(f"Document '{output_filename}' saved successfully in '{folder_path}'.")
