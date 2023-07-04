from bypy import ByPy
bp = ByPy()

bp.upload(
  r"E:/Project/Job/GQ/Python/Baidu_downlaod_upload/软件 安排 编辑.rar",
  "PythonTest1.jpg"
)
print(bp.list())