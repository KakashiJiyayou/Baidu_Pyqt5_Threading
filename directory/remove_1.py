import os
import glob
import shutil

cwd = os.path.dirname(os.path.abspath(__file__))

print(" Current, Workig Directory ", cwd)
files = glob.glob(cwd + "/rr")

print(files)
for root, dirs, files in os.walk(cwd + "/rr"):
    for name in files:
        shutil.rmtree( os.path.join( root, name ) )
    for name in dirs:
        shutil.rmtree( os.path.join( root, name ) )

