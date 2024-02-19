#!/usr/bin/python3
"""Module 10-square
Creates a square class
"""


rectangle = __import__('9-rectangle').Rectangle


class Square(rectangle):
    """Represents a square
    Private instance attribute size
    Public method area()
    Inherits from Rectangle
    """

    def __init__(self, size):
        """Initializes a Square
        Args:
            - size: square size
        """

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        return super().__str__()

    def area(self):
        """Computes the area of a Square instance
        Ovewrites the area() method from Rectangle
        """

        return self.__size ** 2

