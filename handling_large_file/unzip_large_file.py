import os
import glob
import time
import shutil
import _thread
from zipfile import ZipFile
from bypy import ByPy
from pyunpack import Archive
import traceback

root_path = os.path.dirname(__file__)

path = os.path.join ( root_path, "temp" )

zip_file_path = "E:\\Downloads\\wechat\\another.zip"

Archive( zip_file_path ).extractall( path )
