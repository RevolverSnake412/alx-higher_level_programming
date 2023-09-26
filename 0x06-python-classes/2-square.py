#!/usr/bin/python3
"""class Square"""


class Square:
    """square"""

    def __init__(self, size=0):
        """Init"""
        self.__size = size
        try:
            if size.isdigit():
                pass
        except TypeError:
            print("size must be an integer")
        except ValueError:
            print("size must be >= 0")
