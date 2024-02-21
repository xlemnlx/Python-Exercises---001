from glob import glob
import time
import os

start_time = time.time()
# udpate with the use of os to make the file path cross-platform.
base_path = os.path.dirname(__file__)
folder_path = os.path.join(base_path, "Files")

count = 0
file_count = 0

path_list = glob(f"{folder_path}/Sample*.txt")
# *NAME* - means that the string to be find can be in the start, end or middle.
# NAME* - means that the string to be find is at the start of the file name.
# *NAME - means that the string to be find is at the end of the file name.

for per_path in path_list:
    with open (per_path, "r") as perFile:
        if "text" in perFile.read():
            count += 1
    file_count += 1

print("Number of files that has been tested:", len(path_list))
print("Number of occurence:", count)
print(f"--- Program takes {round(time.time() - start_time, 4)} seconds to finished ---")
