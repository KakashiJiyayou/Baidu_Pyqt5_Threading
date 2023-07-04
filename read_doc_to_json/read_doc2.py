import glob

from markdown_to_json.markdown_to_json import Renderer, CMarkASTNester
from markdown_to_json.vendor.CommonMark import CommonMark
from read_doc_to_json.utilss import locate_file
from collections import  *
import json
import re
import ast

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



def test_examples():
    absolute_file_paths = []

    sample_search_results_file: str = "menu.md"
    absolute_file_paths.append(sample_search_results_file)
    assert absolute_file_paths

    print(absolute_file_paths)

    for file_name in absolute_file_paths:
        with open(file_name, encoding="utf-8") as file:
            ast = CommonMark.DocParser().parse(file.read())
            dictionary = CMarkASTNester().nest(ast)
            stringified = Renderer().stringify_dict(dictionary)
            assert stringified


    value = json.loads(json.dumps(stringified))
    print("after converting ",value)
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(value, f, ensure_ascii=False, indent=4)

test_examples()