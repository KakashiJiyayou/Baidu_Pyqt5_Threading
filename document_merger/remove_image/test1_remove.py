import docx2txt

input_doc = r'E:\Project\Job\GQ\Python\Baidu_downlaod_upload\Baidu_Pyqt5_Threading\document_merger\remove_image\CCTV.docx'
output_doc = r'E:\Project\Job\GQ\Python\Baidu_downlaod_upload\Baidu_Pyqt5_Threading\document_merger\remove_image\CCTV_no_img.docx'
# Load the text content (including images) from the DOCX document
text = docx2txt.process( input_doc  )

# Replace any occurrences of images with text
text_with_replaced_images = text.replace('image_content', 'Text to replace the image.')

# Save the modified text back to a DOCX file
with open('output.docx', 'w', encoding='utf-8') as output_file:
    output_file.write(text_with_replaced_images)
