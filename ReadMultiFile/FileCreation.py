import time
import random

startTime = time.time()

count = 0

for i in range(100):
    rand = random.randint(1, 3)
    if rand % 3 == 0:
        count += 1
        with open("./Files/Sample_File_{}.txt".format(str(count)), "w") as f:
            f.write('This file doesn\'t have the "t-e-x-t" string to be extracted.')
            f.write("\nBut this will still be included to the files to be read since this has the same file name to be considered by the program.")
    else:
        count += 1
        with open("./Files/Sample_File_{}.txt".format(str(count)), "w") as f:
            f.write('This file has the "text" to be counted by the program.')
            f.write("\nOutput the count number to a new .txt file or to the console.")

print("Successfully created " + str(count) + " files")
print("--- Program takes %.4f seconds to finished ---" % (time.time() - startTime))
