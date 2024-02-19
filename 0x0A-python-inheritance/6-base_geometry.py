#!/usr/bin/python3
"""
Module BaseGeometry
Creates a class with a method that raises an exception
"""


class BaseGeometry:
    """class with a public instance"""

    def area(self):
        """Function that raises an exception"""

        raise Exception("area() is not implemented")

