import sys
from subprocess import run
print("Type away: ", end="")
sys.stdout.flush()
r = run("bypy list", capture_output=True, shell=True, encoding="utf8")
# print(f"You entered {r.stdout}")