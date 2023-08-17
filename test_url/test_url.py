from urllib.parse import unquote

# URL-encoded src attribute
img_src = "%E5%AE%89%E5%85%A8%E5%91%98%E8%B0%A2%E5%BB%B6%E6%9D%B00725_html_9f5b2df2de087314.png"

# img_src= "file:///E:/Project/Job/GQ/Python/Baidu_downlaod_upload/Baidu_Pyqt5_Threading/document_merger/doc_to_html/libre/temp/%E5%AE%89%E5%85%A8%E5%91%98%E8%B0%A2%E5%BB%B6%E6%9D%B00725_html_9f5b2df2de087314.png"
img_src= "E:\Installed\Anaconda\python.exe E:/Project/Job/GQ/Python/Baidu_downlaod_upload/Baidu_Pyqt5_Threading/test_url/test_url.py"

img_src = r"E:\Project\Job\GQ\Python\Baidu_downlaod_upload\Baidu_Pyqt5_Threading\document_merger\xfinal_version\module/temp\Bloomsy site.png"

# Decode the URL-encoded string to get the actual filename
decoded_img_filename = unquote(img_src)
print(decoded_img_filename)  #