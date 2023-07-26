import os
def Test2(rootDir):
    for path, subdirs, files in os.walk(rootDir):
        for name in files:
            print(os.path.join(path, name))

path = r"软件 安排 编辑"
Test2(path)