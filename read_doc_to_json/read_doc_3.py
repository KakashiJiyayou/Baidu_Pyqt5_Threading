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

print("Key ", value.keys())

def get_paths(source):
    paths = []
    if isinstance(source, collections.abc.MutableMapping):
        # print("SOurce items ", source.items())
        for k, v  in source.items():
            if k not in paths:
                paths.append(k)
            for x in get_paths(v):
                if k + '.' + x not in paths:
                    paths.append(k + '.' + x)
    elif isinstance(source, collections.abc.Sequence) and not isinstance(source, str):

        for x in source:
            for y in get_paths(x):
                if '[].' + y not in paths:
                    paths.append('[].' + y)
    return paths


paths = get_paths(value)



print("all paths\n\t::",paths)