#!/usr/bin/python3
"""2"""


def append_write(filename="", text=""):
    """appends to a file"""
    with open(filename, "a", encoding="UTF8") as fhand:
        return fhand.write(text)
