from glob import glob
import time
import os

startTime = time.time()
# udpate with the use of os to make the file path cross-platform.
base_path = os.path.dirname(__file__)
folder_path = os.path.join(base_path, "Files")

count = 0
fileCount = 0

pathList = glob(f"{folder_path}/Sample*.txt")
# *NAME* - means that the string to be find can be in the start, end or middle.
# NAME* - means that the string to be find is at the start of the file name.
# *NAME - means that the string to be find is at the end of the file name.

for perPath in pathList:
    with open (perPath, "r") as perFile:
        if "text" in perFile.read():
            count += 1
    fileCount += 1

print("Number of files that has been tested:", len(pathList))
print("Number of occurence:", count)
print("--- Program takes %.4f seconds to finished ---" % (time.time() - startTime))
