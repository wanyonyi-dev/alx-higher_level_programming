#!/usr/bin/python3
"""a module with functions that Defines a rectangle"""


class Rectangle:
    """The __init__ method initialize the value passed to tghe object
        Attributes:
            width: its a private attribute
            height: its a private attribute
    """

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    @property
    def height(self):
        """The height property"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    @property
    def width(self):
        """The width property"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value
