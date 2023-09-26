#!/usr/bin/python3
"""class Square"""


class Square:
    """square"""

    def __init__(self, size=0, position=(0, 0)):
        """Init"""
        self.size = size
        self.position = position

    @property
    def position(self):
        """Pos property"""
        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    @property
    def size(self):
        """size property"""
        return self.__size

    @size.setter
    def size(self, value):
        """size setter"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """returns current square area"""
        return self.__size * self.__size

    def my_print(self):
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__position[1]):
                print("")
            for j in range(self.__size):
                for k in range(self.__position[0]):
                    print(" ", end="")
                for x in range(self.__size):
                    print("#", end="")
                print("")
