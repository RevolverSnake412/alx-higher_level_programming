#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    rev_list = reversed(my_list)
    for element in rev_list:
        print("{:d}".format(element))
