#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for idx in range(x):
            print(my_list[idx], end="")
            if idx == x:
                print("\n")
        return x
    except IndexError:
        i = 0
        for idx in my_list:
            print(idx, end="")
            i += 1
        return i
