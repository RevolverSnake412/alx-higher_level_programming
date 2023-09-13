#!/usr/bin/python3
def roman_to_int(roman_string):
    dict_roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    flag = 0
    decimal = 0

    for i in range(len(roman_string)):
        cur_num = dict_roman.get(roman_string[i])
        if i != (len(roman_string) - 1):
            if flag == 1:
                flag = 0
                continue
            next_num = dict_roman.get(roman_string[i + 1])
            if next_num > cur_num:
                decimal += (next_num - cur_num)
                flag = 1
            else:
                decimal += cur_num
        else:
            if flag == 0:
                decimal += cur_num
    return decimal
