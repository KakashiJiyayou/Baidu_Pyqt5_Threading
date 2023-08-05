import subprocess
# proc =  subprocess.Popen(["bypy", "info"], stdout=subprocess.PIPE)
proc =  subprocess.Popen([ "bypy", "upload",
                           "C:\\Users\\rafib\Desktop\\年舟山国家远洋渔业基地—污水主管网维修工程合同.docx" ,
                           "ONDUP" ], stdout=subprocess.PIPE)

# proc  = subprocess.Popen([ "bypy", "search", "r.jpeg"], stdout=subprocess.PIPE)

while True:
  line = proc.stdout.readline()
  if not line:
    break
  #the real code does filtering here
  # print ( "test:", line.rstrip() )
  print("test:", str ( line, "utf-8") )
