def extract_filenames_with_directory(data_list):
    try:
        extracted_filenames = [item.split('Directory:')[-1].strip() for item in data_list if 'Directory:' in item]
        return extracted_filenames
    except Exception as e:
        print("Error:", e)
        return []

# Example list
data_list = ['prflpic.jpg  Directory:/bypy/ONDUP/prflpic.jpg', 'leftpic1.jpg  Directory:leftpic1.jpg', 'banner3.jpg  Directory:/bypy/ONDUP/new/banner3.jpg']

result = extract_filenames_with_directory(data_list)
print(result)  #