#!/usr/bin/python3
"""class Square"""


class Square:
    """square"""

    def __init__(self, size=0):
        """Init"""
        self.__size = size
        if isinstance(size, int):
            raise TypeError ("size must be an integer")
        if size < 0:
            raise ValueError ("size must be >= 0")
