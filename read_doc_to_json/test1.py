import docx2txt, json, collections
# step 1 get docx text
text = docx2txt.process(r"E:\Project\Job\GQ\Python\Baidu_downlaod_upload\test\read_doc_to_json\file.docx")
# convert to list
li = [x for x in text.split('\n')]
# remove ''s i.e Nones
li = list(filter(None, li))
print(li)
# json list
json_li = []
# convert and store all values
for x in li:
    x = x[2:] # remove 1. 2. 3. ...
    y = x.split(',')
    print(y)
    d = collections.defaultdict()
    for m in y:
        z = m.split(':')
        z1 = [x.strip() for x in z]
        d[z1[0]] = z1[1]
    json_li.append(d)
# JSON conversion
print(json.dumps(json_li, indent=4))