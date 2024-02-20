#!/usr/bin/python3
"""Student to JSON with filter"""


class Student:
    """class Student"""
    def __init__(self, first_name, last_name, age):
        """Instantiation

        Args:
          first_name: student's first name (str)
          last_name: student's last name (str)
          age: student's age (int)
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves the dict representation of the instance

        Args:
          attrs: list (None default)
        """
        result = {}

        if attrs is None:
            return self.__dict__

        for attr in attrs:
            value = self.__dict__.get(attr)
            if value is not None:
                result[attr] = value

        return result

