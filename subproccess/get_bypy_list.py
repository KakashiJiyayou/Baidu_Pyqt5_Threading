import subprocess

# result = subprocess.run(["bypy", "list"], shell=True, capture_output=True, text=True)

result = subprocess.run( ["bypy" , "search", "chat.wxss"],  capture_output=True, text=True)

result = subprocess.run( ["bypy" , "ls", "ONDUP"],  capture_output=True, text=True)
print("result ",result.stdout)