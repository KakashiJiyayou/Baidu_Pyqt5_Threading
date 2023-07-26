import os
def Test2(rootDir):
    for lists in os.walk(rootDir):
        path = os.path.join(rootDir, lists)

        if(os.path.isfile(path)):
            print("File: ", path ,"  Name: ", lists  )

        if os.path.isdir(path):

            print("Dir: ", path ,"  Name: ", lists  )
            Test2(path)

path = r"软件 安排 编辑"
Test2(path)