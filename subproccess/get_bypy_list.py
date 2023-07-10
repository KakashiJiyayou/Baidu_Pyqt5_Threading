import subprocess

# result = subprocess.run(["bypy", "list"], shell=True, capture_output=True, text=True)

# result = subprocess.run( ["bypy" , "search", "chat.wxss"], shell=True,  capture_output=True, text=True)

# result = subprocess.run( ["bypy" , "ls", "ONDUP"],  capture_output=True, text=True)

# result = subprocess.run(["bypy", "info"], shell=True, capture_output=True, text=True)

result = subprocess.run(["bypy", "quota"], shell=True, capture_output=True, text=True)
print("result ",result.stdout)