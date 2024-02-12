def UncensoredString(testVariable):
    censoredList = list(testVariable[0])
    answerList = list(testVariable[1])
    count = 0

    for indx, i in enumerate(censoredList):
        if i == "*":
            censoredList.insert(indx, answerList[count])
            #censoredList.remove(censoredList[indx + 1])
            censoredList.remove(i)
            count += 1

    stringOut = "".join(censoredList)

    print(stringOut)