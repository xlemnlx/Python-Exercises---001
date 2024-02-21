import time
import random
import os

start_time = time.time()
# udpate with the use of os to make the file path cross-platform.
base_path = os.path.dirname(__file__)
folder_path = os.path.join(base_path, "Files")

count = 0

for i in range(100):
    rand = random.randint(1, 3)
    if rand % 3 == 0:
        count += 1
        with open(f"{folder_path}/Sample_File_{count}.txt", "w") as f:
            f.write('This file doesn\'t have the "t-e-x-t" string to be extracted.')
            f.write("\nBut this will still be included to the files to be read since this has the same file name to be considered by the program.")
    else:
        count += 1
        with open(f"{folder_path}/Sample_File_{count}.txt", "w") as f:
            f.write('This file has the "text" to be counted by the program.')
            f.write("\nOutput the count number to a new .txt file or to the console.")

print("Successfully created " + str(count) + " files")
print(f"--- Program takes {round(time.time() - start_time, 4)} seconds to finished ---")
