#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    a = []
    for i in my_list:
        if i % 2 == 0:
            a += True,
        else:
            a += False,
    return (a)
