#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    llis = sorted(list(a_dictionary.keys()))
    for i in llis:
        print("{}: {}".format(i, a_dictionary.get(i)))
