import os
import sys
from document_merger.xfinal_version.module import merge_docs as MGD

folder_structure = "module/temp"

cwd = os.path.dirname( os.path.abspath( __file__ ) )

output_folder = os.path.join ( cwd, folder_structure )

print (output_folder)

file_paths = []
for item in os.listdir(output_folder):
    item_path = os.path.join(output_folder, item)
    if os.path.isfile(item_path):
        file_paths.append(item_path)

print( "file list ", file_paths )

MGD.Merge( file_paths, output_folder )