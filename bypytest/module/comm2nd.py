import subprocess

# Set the UTF-8 encoding for the subprocess
env = {"PYTHONIOENCODING": "utf-8"}
command = ["bypy", "search", "2022年舟山国家远洋渔业基地—污水主管网维修工程合同.docx", "ONDUP"]

# Run the subprocess and capture the output
completed_process = subprocess.run(
    command,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True,
    env=env
)

# Print the captured stdout and stderr
print("Standard Output:")
print(completed_process.stdout)

print("Standard Error:")
print(completed_process.stderr)

# Check the return code
if completed_process.returncode == 0:
    print("Subprocess completed successfully.")
else:
    print("Subprocess returned non-zero exit status:", completed_process.returncode)
