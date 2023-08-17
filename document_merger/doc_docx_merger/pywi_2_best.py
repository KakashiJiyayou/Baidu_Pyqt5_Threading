import os
import win32com.client

def insert_image(doc, image_path, width, height):
    shape = doc.InlineShapes.AddPicture(FileName=image_path, LinkToFile=False, SaveWithDocument=True)
    # shape.Width = width
    # shape.Height = height



def merge_and_insert_images(input_files, output_path, output_filename):
    word = win32com.client.Dispatch("Word.Application")
    word.Visible = False
    merged_doc = word.Documents.Add()

    for input_file in input_files:
        # Check if the input file is an image (based on file extension)
        if input_file.lower().endswith(('.png', '.jpg', '.jpeg')):
            insert_image(merged_doc, input_file, width=300, height=200)
        else:
            merged_doc.Application.Selection.Range.InsertFile(input_file)

    # Save the merged document
    output_path = os.path.join(output_path, output_filename)
    merged_doc.SaveAs(output_path)
    merged_doc.Close()
    word.Quit()

if __name__ == "__main__":
    input_files = [
        r'E:\Project\Job\GQ\Python\Baidu_downlaod_upload\Baidu_Pyqt5_Threading\document_merger\doc_docx_merger\docx\1.营业执照.doc',
        r'E:\Project\Job\GQ\Python\Baidu_downlaod_upload\Baidu_Pyqt5_Threading\document_merger\doc_docx_merger\docx\2.市政资质.doc',
        r'E:\Project\Job\GQ\Python\Baidu_downlaod_upload\Baidu_Pyqt5_Threading\document_merger\doc_docx_merger\docx\CCTV检测技术文件10页.doc',
        # r'E:\Project\Job\GQ\Python\Baidu_downlaod_upload\Baidu_Pyqt5_Threading\document_merger\doc_docx_merger\docx\CCTV检测文件5页.doc',
        # r'E:\Project\Job\GQ\Python\Baidu_downlaod_upload\Baidu_Pyqt5_Threading\document_merger\doc_docx_merger\docx\下水管道养护工 张明华.doc',
        # r'E:\Project\Job\GQ\Python\Baidu_downlaod_upload\Baidu_Pyqt5_Threading\document_merger\doc_docx_merger\docx\安全员于娜娜0725.docx',
        # r'E:\Project\Job\GQ\Python\Baidu_downlaod_upload\Baidu_Pyqt5_Threading\document_merger\doc_docx_merger\docx\附件2：2023 宁波市国际学生汉语口语大赛报名表.docx',
        # r'E:\Project\Job\GQ\Python\Baidu_downlaod_upload\Baidu_Pyqt5_Threading\document_merger\doc_docx_merger\docx\管道检测标应急预案.doc',
        # r'E:\Project\Job\GQ\Python\Baidu_downlaod_upload\Baidu_Pyqt5_Threading\document_merger\doc_docx_merger\docx\组织安全方案.doc',
        # r'E:\Project\Job\GQ\Python\Baidu_downlaod_upload\Baidu_Pyqt5_Threading\document_merger\doc_docx_merger\docx\安全员谢延杰0725.docx',
        # r'E:\Project\Job\GQ\Python\Baidu_downlaod_upload\Baidu_Pyqt5_Threading\document_merger\doc_docx_merger\docx\组织安全方案.doc',
        # r'E:\Project\Job\GQ\Python\Baidu_downlaod_upload\Baidu_Pyqt5_Threading\document_merger\doc_docx_merger\docx\质量员程礼海(1).docx',
        # r'E:\Project\Job\GQ\Python\Baidu_downlaod_upload\Baidu_Pyqt5_Threading\document_merger\doc_docx_merger\docx\2.市政资质.doc',
        # r'E:\Project\Job\GQ\Python\Baidu_downlaod_upload\Baidu_Pyqt5_Threading\document_merger\doc_docx_merger\docx\质量员程礼海0725.docx',
        # r'E:\Project\Job\GQ\Python\Baidu_downlaod_upload\Baidu_Pyqt5_Threading\document_merger\doc_docx_merger\docx\资料员谢延莉(1).docx',
        # r'E:\Project\Job\GQ\Python\Baidu_downlaod_upload\Baidu_Pyqt5_Threading\document_merger\doc_docx_merger\docx\2.市政资质.doc',
        # r'E:\Project\Job\GQ\Python\Baidu_downlaod_upload\Baidu_Pyqt5_Threading\document_merger\doc_docx_merger\docx\资料员谢延莉0725.docx',
        # r'E:\Project\Job\GQ\Python\Baidu_downlaod_upload\Baidu_Pyqt5_Threading\document_merger\doc_docx_merger\docx\2.市政资质.doc',
        # r'E:\Project\Job\GQ\Python\Baidu_downlaod_upload\Baidu_Pyqt5_Threading\document_merger\doc_docx_merger\docx\During 4th and 5th Competition.jpg',
        # r'E:\Project\Job\GQ\Python\Baidu_downlaod_upload\Baidu_Pyqt5_Threading\document_merger\doc_docx_merger\docx\InternationalCompetition in Wuxi.jpg',
        # r'E:\Project\Job\GQ\Python\Baidu_downlaod_upload\Baidu_Pyqt5_Threading\document_merger\doc_docx_merger\docx\Published Paper.jpg',
        # r'E:\Project\Job\GQ\Python\Baidu_downlaod_upload\Baidu_Pyqt5_Threading\document_merger\doc_docx_merger\docx\screen v6.png',
        # r'E:\Project\Job\GQ\Python\Baidu_downlaod_upload\Baidu_Pyqt5_Threading\document_merger\doc_docx_merger\docx\BildschirmÂ_foto 2022-11-16 um 16.12.00.png',
        # r'E:\Project\Job\GQ\Python\Baidu_downlaod_upload\Baidu_Pyqt5_Threading\document_merger\doc_docx_merger\docx\附件2：2023 宁波市国际学生汉语口语大赛报名表.docx',
        # # Add more paths as needed
    ]

    output_dir = r'E:\Project\Job\GQ\Python\Baidu_downlaod_upload\Baidu_Pyqt5_Threading\document_merger\doc_docx_merger\temp'
    output_filename = 'f01.docx'

    merge_and_insert_images(input_files, output_dir, output_filename)
