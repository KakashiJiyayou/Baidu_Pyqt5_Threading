import os
import bypy
import time
import subprocess

# Get the parent directory that is shared by "module" and "DB" folders
parent_directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def download_file(baidu_path, local_file_path):
    try:
        bp = bypy.ByPy()
        temp_dir = os.path.join(parent_directory, "temp_folder")
        os.makedirs(temp_dir, exist_ok=True)

        temp_file_path = os.path.join(temp_dir, os.path.basename(local_file_path) + ".download")
        bp.download(baidu_path, temp_file_path)
        os.rename(temp_file_path, local_file_path)
        os.rmdir(temp_dir)
        return True
    except Exception as e:
        print(f"Error in download_file: {e}")
        return False

def upload_file(local_file_path, baidu_path):
    try:
        bp = bypy.ByPy()
        bp.upload(local_file_path, baidu_path)

        output = subprocess.check_output(["bypy", "list", baidu_path], universal_newlines=True)
        if "Found" in output or "found" in output:
            bp.remove(baidu_path)
            bp.copy(baidu_path.replace("backup/", ""), baidu_path)

            output = subprocess.check_output(["bypy", "list", baidu_path], universal_newlines=True)
            if "Found" in output or "found" in output:
                bp.remove(baidu_path.replace("backup/", ""))

        return True
    except Exception as e:
        print(f"Error in upload_file: {e}")
        return False

def download_db_file():
    baidu_path = "/DB/db.json"
    local_file_path = os.path.join(parent_directory, "DB", "db.json")
    print( "download db file to ", local_file_path )
    if download_file(baidu_path, local_file_path):
        return {"status": "Download done"}
    else:
        return {"status": "Download failed"}

def upload_db_file():
    baidu_path = "/DB/backup/db.json"
    local_file_path = os.path.join(parent_directory, "DB", "db.json")
    print( "upload db file from ", local_file_path )
    if upload_file(local_file_path, baidu_path):
        return {"status": "Upload done"}
    else:
        return {"status": "Upload failed"}

def download_db_running():
    baidu_path = "/DB/running.json"
    local_file_path = os.path.join(parent_directory, "DB", "running.json")
    print( "download db running  file to", local_file_path )
    if download_file(baidu_path, local_file_path):
        return {"status": "Download done"}
    else:
        return {"status": "Download failed"}

def upload_db_running():
    baidu_path = "/DB/backup/running.json"
    local_file_path = os.path.join(parent_directory, "DB", "running.json")
    print( "upload db running file from ", local_file_path )
    if upload_file(local_file_path, baidu_path):
        return {"status": "Upload done"}
    else:
        return {"status": "Upload failed"}

# Example usage
# print(download_db_file())
# time.sleep(3)
# print(upload_db_file())
# time.sleep(3)
# print(download_db_running())
# time.sleep(3)
# print(upload_db_running())
