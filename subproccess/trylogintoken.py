import subprocess
from subprocess import Popen, CREATE_NEW_CONSOLE
# from bypy import ByPy
# bp = ByPy()
# result = subprocess.run(["bypy", "list"], shell=True, capture_output=True, text=True)

# result = subprocess.run( ["bypy" , "search", "chat.wxss"], shell=True,  capture_output=True, text=True)

# result = subprocess.run( ["bypy" , "ls", "ONDUP"],  capture_output=True, text=True)

# result = subprocess.run(["bypy", "info"], shell=True, capture_output=True, text=True)

# result = subprocess.run(["bypy", "quota"], shell=True, capture_output=True, text=True)

# result = subprocess.run(["bypy", "-c"], shell=True, capture_output=True, text=True)
# print("result ",result.stdout)


# proc  = subprocess.Popen([ "bypy", "list"], stdout=subprocess.PIPE,
#                          stdin=subprocess.PIPE,shell=True, capture_output=True, text=True)

# proc  = subprocess.Popen([ "bypy", "list"],  shell=True, capture_output=True, text=True )


#
proc   = subprocess.Popen([ "bypy", "list"],shell=False,creationflags=CREATE_NEW_CONSOLE, stdout=subprocess.PIPE,stdin=subprocess.PIPE,)

def is_url( link ):
    if "https://openapi.baidu.com/oauth"in link:
        return True
    else :
        return False


while True:
    line = proc.stdout.readline()
    if not line:
        break
    #the real code does filtering here
    # print ( "test:", line.rstrip() )
    # print("test:", str ( line, "utf-8") )
    value = str(line, "utf-8").rstrip( )
    print ( value )
    if is_url( value ):
        print ( "*"*8, "Given link is an url ",value )

