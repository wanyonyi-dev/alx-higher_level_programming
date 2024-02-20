#!/usr/bin/python3
"""Student to JSON"""


class Student:
    """Class student"""
    def __init__(self, first_name, last_name, age):
        """
        Instantiation

        Args:
            first_name: student's first name (str)
            last_name: student's last name (str)
            age: student's age int
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves a dictionary representation"""
        return self.__dict__

