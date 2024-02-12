from glob import glob
import os
import time

startTime = time.time()

count = 0

pathList = glob("./Files/Sample*.txt")

for perPath in pathList:
    os.remove(perPath)
    count += 1

print("Successfully deleted " + str(count) + " files.")
print("--- Program takes %.4f seconds to finished ---" % (time.time() - startTime))
