def string_reversal(str_input):
    input_as_list = list(str_input)  # Converting it to a list.

    str_list = []  # Will use to hold the characters only.
    for i in input_as_list:
        if i.isalpha():
            str_list.append(i)

    str_list.reverse()  # Reverses the characters.
    count_to_add = len(input_as_list) - len(str_list)  # Count how many index I need to extend the List.

    for i in range(count_to_add):  # Extends the list so that it won't throw an error about "out of index" for the next step.
        str_list.append("a")

    final_list = []
    for idx, i in enumerate(str_list):  # Enumerate wil get both the index and value.
        if i.isalpha() and input_as_list[idx].isalpha():  # Will just append the char.
            final_list.append(i)
        else:  # Will insert first the non-char then append the char.
            final_list.insert(idx, input_as_list[idx])
            final_list.append(i)

    max_count = len(final_list) - 1  # Will use to index the the last item of the list
    for i in range(count_to_add):
        final_list.pop(max_count)
        max_count -= 1  # Making sure to decrement so that it will remove the last index as long as the iteration goes.

    reversedStr = "".join(final_list)  # Finally, making it back to a string.

    return reversedStr