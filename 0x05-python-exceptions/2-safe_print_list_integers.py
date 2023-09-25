#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    dig_count = 0
    for idx in range(x):
        try:
            print("{:d}".format(my_list[idx]), end="")
            dig_count += 1
        except (TypeError, ValueError):
            continue
    print("")
    return dig_count
