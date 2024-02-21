from glob import glob
import os
import time

start_time = time.time()
# udpate with the use of os to make the file path cross-platform.
base_path = os.path.dirname(__file__)
folder_path = os.path.join(base_path, "Files")

count = 0

path_list = glob(f"{folder_path}/Sample*.txt")

for per_path in path_list:
    os.remove(per_path)
    count += 1

print("Successfully deleted " + str(count) + " files.")
print(f"--- Program takes {round(time.time() - start_time, 4)} seconds to finished ---")
