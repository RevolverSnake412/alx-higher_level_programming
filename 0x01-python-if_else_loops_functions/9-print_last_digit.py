#!/usr/bin/python3
def print_last_digit(number):
    last_dig = abs(number) % 10
    print(last_dig, end="")
    return last_dig
