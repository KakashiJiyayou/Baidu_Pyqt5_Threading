import os
import glob
import time
import shutil
import _thread
from zipfile import ZipFile
from bypy import ByPy
from pyunpack import Archive
import traceback
import zipfile
import locale




root_path = os.path.dirname(__file__)
path = os.path.join ( root_path, "temp" )

shutil.rmtree ( path )
os.mkdir(path)
zip_file_path = r"E:\Downloads\wechat\15.柴桥一期二期检测.zip"

# Archive(zip_file_path).extractall(path)
# shutil.unpack_archive(zip_file_path, path)
shutil.unpack_cp437_or_unicode(zip_file_path, path)
#
#
# zipfile


# temp_zip_path = zip_file_path
# target_loc = path
# temp_zip_path = r"" + zip_file_path
#
# def unpack_cp437_or_unicode(archive_path):
#     with zipfile.ZipFile(archive_path) as zz:
#         for zipped_name in zz.namelist():
#             try:
#                 print ("real name ", zipped_name)
#                 real_name = zipped_name.decode('cp437')
#             except UnicodeEncodeError:
#                 real_name = zipped_name
#
#             with zz.open(zipped_name) as archived:
#                 contents = archived.read()
#             if zipped_name.endswith('/'):
#                 dirname = os.path.join(target_loc, real_name)
#                 if not os.path.isdir(dirname):
#                     os.makedirs(dirname)
#             else:
#                 with open(os.path.join(target_loc, real_name), 'wb') as target:
#                     target.write(contents)
#
#
# unpack_cp437_or_unicode(temp_zip_path)