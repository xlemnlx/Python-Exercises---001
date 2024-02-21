from glob import glob
import os
import time

startTime = time.time()
# udpate with the use of os to make the file path cross-platform.
base_path = os.path.dirname(__file__)
file_path = os.path.join(base_path, "Files")

count = 0

pathList = glob(f"{file_path}/Sample*.txt")

for perPath in pathList:
    os.remove(perPath)
    count += 1

print("Successfully deleted " + str(count) + " files.")
print("--- Program takes %.4f seconds to finished ---" % (time.time() - startTime))
