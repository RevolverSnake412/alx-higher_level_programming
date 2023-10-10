#!/usr/bin/python3
"""1"""


def write_file(filename="", text=""):
    """writes in a file"""
    with open(filename, "w", encoding="UTF8") as fhand:
        return fhand.write(text)
