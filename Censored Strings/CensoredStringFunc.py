def CensoredString(testVariable):
    strAsList = list(testVariable[0].split())
    toBeCensored = testVariable[1]
    censoreChar = testVariable[2]
    
    censoredWord = None
    
    for indx, perword in enumerate(strAsList):
        for i in toBeCensored:
            if perword.lower() == i.lower():
                censoredWord = censoreChar * len(perword)
                strAsList.insert(indx, censoredWord)
                strAsList.remove(perword)
    
    censoredString = " ".join(strAsList)
    
    return censoredString