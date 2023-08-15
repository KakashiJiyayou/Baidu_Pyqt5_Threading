import zipfile, sys, os

zip_file_path = ".\\temp01\\软件编制 资料.zip"

zf = zipfile.ZipFile(zip_file_path )
for m in zf.infolist():
    data = zf.read(m) # extract zipped data into memory
    # convert unicode file path to utf8
    disk_file_name = m.filename.encode('utf8')
    dir_name = os.path.dirname(disk_file_name)
    try:
        os.makedirs(dir_name)
    except OSError as e:
        if e.errno == os.errno.EEXIST:
            pass
        else:
            raise
    except Exception as e:
        raise
    print ("disk fiel name ", disk_file_name)
    with open(disk_file_name, 'wb') as fd:
        fd.write(data)
zf.close()