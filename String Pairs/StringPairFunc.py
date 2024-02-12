def StringPairs(testVariable):
    for perword in testVariable:
        
        count = 0
        perwordList = list(perword)
        newList = []
        
        if len(perwordList) == 0: # Return [] if the given string is empty.
            newList = perwordList
        elif len(perwordList) % 2 != 0: # If the string has an odd number of characters, add an asterisk * in the final pair.
            while count < len(perwordList):
                if count > len(perwordList) - 1:
                    break
                elif count == len(perwordList) - 1:
                    newList.append(perwordList[count] + "*")
                    break
                else:
                    pairStr = perwordList[count] + perwordList[count + 1]
                    newList.append(pairStr)
                    count += 2
        else: # For the even count
            while count < len(perwordList):
                if count > len(perwordList) - 1:
                    break
                else:
                    pairStr = perwordList[count] + perwordList[count + 1]
                    newList.append(pairStr)
                    count += 2
        
        if len(perwordList) == 0:
            print("Empty list:", newList)
        elif len(perwordList) % 2 != 0:
            print("Odd count list:", newList)
        else:
            print("Even count list:", newList)