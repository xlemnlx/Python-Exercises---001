def StringReversal(strInput):
    inputAsList = list(strInput)  # Converting it to a list.

    strList = []  # Will use to hold the characters only.
    for i in inputAsList:
        if i.isalpha():
            strList.append(i)

    strList.reverse()  # Reverses the characters.
    countToAdd = len(inputAsList) - len(strList)  # Count how many index I need to extend the List.

    for i in range(countToAdd):  # Extends the list so that it won't throw an error about "out of index" for the next step.
        strList.append("a")

    finalList = []
    for idx, i in enumerate(strList):  # Enumerate wil get both the index and value.
        if i.isalpha() and inputAsList[idx].isalpha():  # Will just append the char.
            finalList.append(i)
        else:  # Will insert first the non-char then append the char.
            finalList.insert(idx, inputAsList[idx])
            finalList.append(i)

    maxCount = len(finalList) - 1  # Will use to index the the last item of the list
    for i in range(countToAdd):
        finalList.pop(maxCount)
        maxCount -= 1  # Making sure to decrement so that it will remove the last index as long as the iteration goes.

    reversedStr = "".join(finalList)  # Finally, making it back to a string.

    return reversedStr