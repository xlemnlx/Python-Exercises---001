def love_me_loves_me_not(test_variable):
    handler_list = []
    count = 1
    
    while count <= test_variable:
        if count == test_variable:
            if count % 2 == 0:
                handler_list.append("LOVES ME NOT")
                break
            else:
                handler_list.append("LOVES ME")
                break
        else:
            if count % 2 == 0:
                handler_list.append("Loves me not, ")
                count += 1
            else:
                handler_list.append("Loves me, ")
                count += 1
    
    str_list = "".join(handler_list)
    
    return str_list