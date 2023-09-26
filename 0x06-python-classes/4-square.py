#!/usr/bin/python3
"""class Square"""


class Square:
    """square"""

    def __init__(self, size=0):
        """Init"""
        self.size = size

    @property
    def size(self):
        """property"""
        return self.__size

    @size.setter
    def size(self, value):
        """setter"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """returns current square area"""
        return self.__size * self.__size
