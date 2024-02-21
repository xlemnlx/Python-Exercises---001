import os
import time
import random
from glob import glob

def file_create_read_delete(range_):
    file_create_time = time.time()
    
    base_path = os.path.dirname(__file__)
    folder_path = os.path.join(base_path, "Files")
    
    count = 0
    
    for i in range(range_):
        rand = random.randint(1, 3)
        if rand % 3 == 0:
            count = i
            with open(f"{folder_path}/Sample_File_{count}.txt", "w") as f:
                f.write('This file doesn\'t have the "t-e-x-t" string to be extracted.')
                f.write("\nBut this will still be included to the files to be read since this has the same file name to be considered by the program.")
        else:
            count = i
            with open(f"{folder_path}/Sample_File_{count}.txt", "w") as f:
                f.write('This file has the "text" to be counted by the program.')
                f.write("\nOutput the count number to a new .txt file or to the console.")

    print("Successfully created " + str(count) + " files")
    print(f"--- Program takes {round(time.time() - file_create_time, 4)} seconds to finished ---\n\n")
    
    
    
    file_read_time = time.time()
    
    count = 0
    file_count = 0
    
    path_list = glob(f"{folder_path}/Sample*.txt")
    
    for per_path in path_list:
        with open (per_path, "r") as perFile:
            if "text" in perFile.read():
                count += 1
        file_count += 1

    print("Number of files that has been tested:", len(path_list))
    print("Number of occurence:", count)
    print(f"--- Program takes {round(time.time() - file_read_time, 4)} seconds to finished ---\n\n")
    
    
    
    file_delete_time = time.time()
    
    count = 0

    path_list = glob(f"{folder_path}/Sample*.txt")

    for per_path in path_list:
        os.remove(per_path)
        count += 1

    print("Successfully deleted " + str(count) + " files.")
    print(f"--- Program takes {round(time.time() - file_delete_time, 4)} seconds to finished ---\n\n")