#!/usr/bin/python3
"""101"""


def add_attribute(obj, att, value):
    """add attribute"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
