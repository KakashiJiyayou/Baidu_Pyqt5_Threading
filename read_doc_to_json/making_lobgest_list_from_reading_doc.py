import collections

from markdown_to_json.markdown_to_json import Renderer, CMarkASTNester
from markdown_to_json.vendor.CommonMark import CommonMark
from read_doc_to_json.utilss import locate_file
from collections import  *
import json

def deep_convert_dict(layer):
    to_ret = layer
    if isinstance(layer, OrderedDict):
        to_ret = dict(layer)

    try:
        for key, value in to_ret.items():
            to_ret[key] = deep_convert_dict(value)
    except AttributeError:
        pass

    return to_ret


file_name = "menu.md"
with open(file_name, encoding="utf-8") as file:
    ast = CommonMark.DocParser().parse(file.read())
    dictionary = CMarkASTNester().nest(ast)
    stringfield = Renderer().stringify_dict(dictionary)
    file.close()

value = json.loads(json.dumps(stringfield))
print(" After converting ", value)

key = list(value.keys())[0]

print("Key ", key)
print("Source Item ", value.items())
print("Source  for value '",key ,"' ==" ,value[key])




def get_longest_path(source):
    source = json.loads(json.dumps(source))

    print("Source type ", type(source))
    if  isinstance(source, list):
        return source
    elif isinstance(source,dict) and len(list(source.items()))>0:

        items = source.items()

        print("source from here ", source, " \t\t Item ", items, "Lenght ", len(items))
        key = list(source.keys())[0]
        print("Key from here ", key , " new source ", source[key])

        result = key +"."+ str((get_longest_path(source[key])))
        return  result


# ## do something here
# L_path = get_longest_path(value)
# print("Longest path ", L_path)