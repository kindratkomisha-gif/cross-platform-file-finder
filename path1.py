import os
import sys
import time

is_windows = sys.platform.startswith("win")
is_mac = sys.platform.startswith('darwin')
is_linux = sys.platform.startswith('linux')

if is_windows:
    path_main = "C:\\Users"
elif is_linux or is_mac:
    path_main = "/" 
else:
    print("Unknown OS. Supported: Linux, macOS, Windows.")

exclude_dirs = ("AppData", "NTUSER.DAT", ".ssh", "Searches", "Links")

input_User = input("Enter name of file: ")
time_input = int(input("Time: ") or 0) *60*60
matches = []

for path, directiry, files in os.walk(path_main):

    for exc in exclude_dirs:
        if exc in directiry:
            directiry.remove(exc)

    for file in files:
        if input_User.lower() in file.lower():
            full_path = os.path.join(path, file)

            if os.path.islink(full_path):
                continue
            if time_input:
                if time.time() - os.path.getctime(full_path) < time_input:
                    matches.append(full_path)
            else:
                matches.append(full_path)

print(matches)

