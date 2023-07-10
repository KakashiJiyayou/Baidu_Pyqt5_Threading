import subprocess
proc =  subprocess.Popen(["bypy", "info"], stdout=subprocess.PIPE)

while True:
  line = proc.stdout.readline()
  if not line:
    break
  #the real code does filtering here
  print ( "test:", line.rstrip() )
  print("test:", str ( line, "utf-8") )