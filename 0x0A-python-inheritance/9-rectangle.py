#!/usr/bin/python3
"""Module Rectangle
Createsa Rectangle class
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represents a rectangle that inherits from rectangle"""

    def __init__(self, width, height):
        """constructor
        Args:
            width: rectangle Width
            height: rectangle height
        """
        self.integer_validator("width", width)
        self.integer_validator("Height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """Returns a formatted string"""

        return str("[Rectangle] {}/{}".format(self.__width, self.__height))

    def area(self):
        """
        Function that calculates the area of a rectangle
        overwritting the same function in BaseGeometry
        """

        self.A = self.__height * self.__width
        return self.A

