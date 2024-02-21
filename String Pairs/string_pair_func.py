def string_pairs(test_variable):
    for per_word in test_variable:
        
        count = 0
        per_word_list = list(per_word)
        new_list = []
        
        if len(per_word_list) == 0: # Return [] if the given string is empty.
            new_list = per_word_list
        elif len(per_word_list) % 2 != 0: # If the string has an odd number of characters, add an asterisk * in the final pair.
            while count < len(per_word_list):
                if count > len(per_word_list) - 1:
                    break
                elif count == len(per_word_list) - 1:
                    new_list.append(per_word_list[count] + "*")
                    break
                else:
                    pair_string = per_word_list[count] + per_word_list[count + 1]
                    new_list.append(pair_string)
                    count += 2
        else: # For the even count
            while count < len(per_word_list):
                if count > len(per_word_list) - 1:
                    break
                else:
                    pair_string = per_word_list[count] + per_word_list[count + 1]
                    new_list.append(pair_string)
                    count += 2
        
        if len(per_word_list) == 0:
            print("Empty list:", new_list)
        elif len(per_word_list) % 2 != 0:
            print("Odd count list:", new_list)
        else:
            print("Even count list:", new_list)