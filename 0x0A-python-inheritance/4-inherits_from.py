#!/usr/bin/python3
"""4"""


def inherits_from(obj, a_class):
    """inherits from"""
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
