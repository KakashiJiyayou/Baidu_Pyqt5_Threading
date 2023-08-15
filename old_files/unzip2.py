# import zipfile

# # 指定需要解压的zip文件路径
# zip_file = zipfile.ZipFile("软件 安排 编辑.rar")

# # 指定解压后的目录路径
# extract_path = './module/temp01'

# # 解压全部文件到指定目录
# zip_file.extractall(extract_path)

# # 关闭zip文件
# zip_file.close()



import rarfile
import os

def un_rar(file_name):
    rar = rarfile.RarFile(file_name)
    if os.path.isdir(file_name + "_files"):
        pass
    else:
        os.mkdir(file_name + "_files")
    os.chdir(file_name + "_files")
    rar.extractall()
    rar.close()

un_rar(r"E:\Project\Job\GQ\Python\Baidu_downlaod_upload\test\testing.rar")