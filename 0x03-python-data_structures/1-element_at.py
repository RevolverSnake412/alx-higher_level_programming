#!/usr/bin/python3
def element_at(my_list, idx):
    size = len(my_list)
    if idx >= size or my_list[idx] < 0:
        return None
    else:
        return my_list[idx]
