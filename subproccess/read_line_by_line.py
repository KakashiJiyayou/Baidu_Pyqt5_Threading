import subprocess
# proc =  subprocess.Popen(["bypy", "info"], stdout=subprocess.PIPE)
# proc =  subprocess.Popen([ "bypy", "upload",
#                            "E:\Project\Job\GQ\Python\Baidu_downlaod_upload\Baidu_Pyqt5_Threading\软件 安排 编辑" ,
#                            "ONDUP" ], stdout=subprocess.PIPE)

proc  = subprocess.Popen([ "bypy", "search", "r.jpeg"], stdout=subprocess.PIPE)

while True:
  line = proc.stdout.readline()
  if not line:
    break
  #the real code does filtering here
  # print ( "test:", line.rstrip() )
  print("test:", str ( line, "utf-8") )
