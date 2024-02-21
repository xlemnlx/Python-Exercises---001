def censored_string(test_variable):
    str_as_list = list(test_variable[0].split())
    to_be_censored = test_variable[1]
    censored_char = test_variable[2]
    
    censored_word = None
    
    for indx, per_word in enumerate(str_as_list):
        for i in to_be_censored:
            if per_word.lower() == i.lower():
                censored_word = censored_char * len(per_word)
                str_as_list.insert(indx, censored_word)
                str_as_list.remove(per_word)
    
    censored_string = " ".join(str_as_list)
    
    return censored_string