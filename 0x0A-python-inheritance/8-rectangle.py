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

