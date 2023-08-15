import subprocess
import locale

# # Set the desired locale
# desired_locale = 'zh_CN.UTF-8'  # Change to the desired locale name
#
# try:
#     locale.setlocale(locale.LC_ALL, desired_locale)
#     print("Locale set to:", locale.getlocale())
# except locale.Error as e:
#     print("Error setting locale:", e)

# Run the subprocess with UTF-8 encoding

# output = subprocess.check_output( ["bypy", "search", "老师老师老师老师老师老师老师老师老师.docx", "ONDUP"],universal_newlines=True)
# output = subprocess.check_output( ["bypy", "search", "老123456789012345678901234567890.docx", "ONDUP"],universal_newlines=True)
output = subprocess.check_output( ["bypy", "search", "2022年舟山国家远洋渔业基地.docx", "ONDUP"],universal_newlines=True)

# output = subprocess.check_output( ["bypy", "search", "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabc.docx", "ONDUP"],universal_newlines=True)

print(output)  # Print the output from the subprocess

# # Reset the locale to the default system locale
# try:
#     locale.setlocale(locale.LC_ALL, "")
#     print("Locale reset to the default system locale:", locale.getlocale())
# except locale.Error as e:
#     print("Error resetting locale:", e)