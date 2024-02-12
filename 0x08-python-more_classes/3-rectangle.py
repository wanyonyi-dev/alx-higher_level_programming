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

    def area(self):
        """get area of the rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return ((self.__height + self.__width) * 2)

    def __str__(self):
        if self.__height == 0 or self.__width == 0:
            return ""
        rectangle = ""
        for row in range(self.height):
            for cul in range(self.width):
                rectangle += "#"
            if row < self.height - 1:
                rectangle += "\n"
        return rectangle

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

