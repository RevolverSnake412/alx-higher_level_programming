#!/usr/bin/python3
"""100"""


class MyInt(int):
    """My int"""
    def __eq__(self, value):
        """eq"""
        return self.real != value

    def __ne__(self, value):
        """ne"""
        return self.real == value
