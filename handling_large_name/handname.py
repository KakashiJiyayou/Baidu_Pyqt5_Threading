import os
def shorten_document_name(document_name):
    max_length = 16
    filename, file_extension = os.path.splitext(document_name)
    truncated_filename = filename[:max_length].rstrip()
    if file_extension:
        shortened_name = f"{truncated_filename}{file_extension}"
    else:
        shortened_name = truncated_filename
    return shortened_name

document_name1 = "2022年舟山国家远洋渔业基地—污水主管网维修工程合同.docx"
document_name2 = "2022年舟山国家远洋渔业基地—污水主管"

shortened_name1 = shorten_document_name(document_name1)
shortened_name2 = shorten_document_name(document_name2)

print(shortened_name1)
print(shortened_name2)
print("len1", len(shortened_name1))
print("len2", len(shortened_name2))