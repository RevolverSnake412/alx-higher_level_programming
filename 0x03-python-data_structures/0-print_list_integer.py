#!/usr/bin/python3
def print_list_integer(my_list=[]):
    for element in my_list:
        if element is str:
            print(str.format(element))
        else:
            print(element)
