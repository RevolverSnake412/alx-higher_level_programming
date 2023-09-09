#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    size = len(my_list)
    if idx >= size or idx < 0:
        return my_list
    copy_list = [element for element in my_list]
    copy_list[idx] = element
    return copy_list
