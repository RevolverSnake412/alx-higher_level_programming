#!/usr/bin/python3
"""0"""


def read_file(filename=""):
    """reads a file"""
    with open(filename) as fhand:
        for line in fhand:
            print(line, end="")
