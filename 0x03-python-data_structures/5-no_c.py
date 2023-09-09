#!/usr/bin/python3
def no_c(my_string):
    size = len(my_string)
    new_string = ""
    j = 0
    for i in range(0, size):
        if my_string[i] == 'c' or my_string[i] == 'C':
            continue
        else:
            new_string += my_string[i]
            j += 1
    return new_string
