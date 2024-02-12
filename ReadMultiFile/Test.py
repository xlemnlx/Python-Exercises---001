from glob import glob
import time

startTime = time.time()

count = 0
fileCount = 0

pathList = glob("./Files/Sample*.txt")
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
