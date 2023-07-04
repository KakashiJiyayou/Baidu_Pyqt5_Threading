import os

path = r"E:\Project\Job\GQ\Python\Baidu_downlaod_upload\test\directory\软件 安排 编辑"


files = folders = 0
folder_list = []

print(os.walk( ))
print("\n\n")
for _, dirnames, filenames in os.walk(path):
  # ^ this idiom means "we won't be using this value"
    files += len(filenames)
    folders += len(dirnames)
    print( "Dir name ", dirnames )

print( "{:,} files, {:,} folders".format(files, folders))