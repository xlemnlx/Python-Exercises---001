def uncensored_string(test_variable):
    censored_list = list(test_variable[0])
    answer_list = list(test_variable[1])
    count = 0

    for indx, i in enumerate(censored_list):
        if i == "*":
            censored_list.insert(indx, answer_list[count])
            censored_list.remove(i)
            count += 1

    string_out = "".join(censored_list)

    return string_out