from genericpath import isdir
import os
# Console Colors Lol
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Refs
dir = f"{os.curdir}/EmojiFolder"

# Func
def End():
    print("Press Any Key To Exit...")
    os.system("pause >nul")
    exit()

# Checks
if not (isdir(dir)):
    os.mkdir("EmojiFolder")
    print(f"{bcolors.HEADER}Created EmojiFolder{bcolors.ENDC}")
    print(f"{bcolors.HEADER}Put ur files in then press any key to continue{bcolors.ENDC}")
    os.system("pause >nul")

os.system(f"echo.{bcolors.OKCYAN}Scanning {dir}... {bcolors.ENDC}")

if os.listdir(dir) == []: # Checks for files in dir
    print(f"{bcolors.FAIL}No files found in the directory.{bcolors.ENDC}")

for f in os.listdir(dir): # Does work
    check = f[0:5]
    if "-" in check:
        rename = f.split("-", 1)
        print(f"{bcolors.OKGREEN}File: {f} >> Renamed: {rename[1]}{bcolors.ENDC}")
        os.rename(os.path.join(dir, f), os.path.join(dir, rename[1]))
    else:
        print(f"{bcolors.WARNING}Already done {f}{bcolors.ENDC}")
End()
# CREATED BY IGNOREDSOUL#1973