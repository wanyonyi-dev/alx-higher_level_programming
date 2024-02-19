#!/usr/bin/python3
"""
Module 1-list
Creates a classs that inherits from list
"""


class MyList(list):
    """class that inherits list"""

    def print_sorted(self):
        """Prints the list in ascending order"""

        list1 = self[:]
        list1.sort()
        print("{}".format(list1))

