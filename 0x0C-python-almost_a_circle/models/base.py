#!/usr/bin/python3
"""base.py"""


class Base:
    """Base class"""
    def __init__(self, id=None):
        self.__nb_objects = 0
        if id == None:
            self.__nb_objects += 1
        else:
            self.__nb_objects = id
