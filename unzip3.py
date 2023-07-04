import gzip
import os
# import tarfile , zipfile, rarfile


# import lib
# from library.utils.file import get_filetype
# from library.utils.path import make_dir
# from library.utils.type_conv import random_str

# def uncompress(src_file, dest_dir):
#     rar = rarfile.RarFile(src_file)  
#     os.chdir(dest_dir)
#     rar.extractall()  
#     rar.close()  


# uncompress("E:\\Project\\\Job\\GQ\\Python\\Baidu_downlaod_upload\\test\\软件 安排 编辑.rar","./module/temp")

directory = os.getcwd()

print(directory)

from unrar import rarfile
file = rarfile.RarFile("E:\\Project\\\Job\\GQ\\Python\\Baidu_downlaod_upload\\test\\testing.rar")  #这里写入的是需要解压的文件，别忘了加路径
file.extractall("./module/temp")  #这里写入的是你想要解压到的文件夹