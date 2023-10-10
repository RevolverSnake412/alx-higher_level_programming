#!/usr/bin/python3
"""100"""


def append_after(filename="", search_string="", new_string=""):
    """append after"""
    text = ""
    with open(filename) as fhand:
        for line in fhand:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as fhand_:
        fhand_.write(text)
