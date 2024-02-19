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

    def integer_validator(self, name, value):
        """Validate values
        Args:
            name: name to me checked
            value: value to be checked
        """
        self.name = name
        self.value = value
        if type(self.value) is not int:
            raise TypeError("{} must be an integer".format(self.name))
        elif self.value <= 0:
            raise ValueError("{} must be greater than 0".format(self.name))

