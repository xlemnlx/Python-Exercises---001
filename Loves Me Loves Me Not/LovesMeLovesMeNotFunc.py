def LMLMN(testVariable):
    holderList = []
    count = 1
    
    while count <= testVariable:
        if count == testVariable:
            if count % 2 == 0:
                holderList.append("LOVES ME NOT")
                break
            else:
                holderList.append("LOVES ME")
                break
        else:
            if count % 2 == 0:
                holderList.append("Loves me not, ")
                count += 1
            else:
                holderList.append("Loves me, ")
                count += 1
    
    strList = "".join(holderList)
    
    return strList