#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    panga = sorted(a_dictionary)
    for i in panga:
        print("{}: {}".format(i, a_dictionary[i]))
