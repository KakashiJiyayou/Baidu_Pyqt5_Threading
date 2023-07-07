import os
import glob
import shutil

cwd = os.path.dirname(os.path.abspath(__file__))

print(" Current, Workig Directory ", cwd)
files = glob.glob(cwd + "/rr")

print(files)
# os.chmod(cwd+"/rr",0o777)
for root, dir, files in os.walk(cwd + "/rr"):
    for name in file:
        os.remove(os.path.join())

# shutil.rmtree(cwd + "/rr/")