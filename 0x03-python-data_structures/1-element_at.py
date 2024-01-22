#!/usr/bin/python3
def element_at(my_list, idx):
    length = len(my_list)
    for i in range(length):
        if idx < 0 or idx > length - 1:
            return ("None")
        if i == idx:
            return (my_list[i])
