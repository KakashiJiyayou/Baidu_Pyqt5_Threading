from bypy import ByPy
import  _thread

bp = ByPy()

# value = bp.list()

# ls = bp.ls()
searc_result = bp.search("ONDUP")

# print(value)
# print("type " , type(value))

# print("Directory ",ls)
print("Search result ", searc_result)