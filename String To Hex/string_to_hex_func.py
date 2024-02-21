def string_to_hex(test_variable):
    hex_list = []
    
    for i in list(test_variable):
        value_handler = format(ord(i), "x")
        hex_list.append(value_handler)
    
    hex_str = " ".join(hex_list)
    
    return hex_str