import subprocess, time, os, sys
# cmd = ["bypy", "quota"]

cmd = [ "bypy", "search", "chat.wxss" ]



p = subprocess.Popen(cmd,
                     stdout=subprocess.PIPE,
                     stderr=subprocess.STDOUT)

for line in iter(p.stdout.readline, b''):
    print(">>> " , line.rstrip() )