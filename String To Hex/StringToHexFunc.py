def StringToHex(testVariable):
    hexList = []
    
    for i in list(testVariable):
        valueHandler = format(ord(i), "x")
        hexList.append(valueHandler)
    
    return hexList