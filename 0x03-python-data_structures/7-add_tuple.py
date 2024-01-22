#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    j = ()
    for i in range(2):
        if len(tuple_a) < 2:
            tuple_a += 0,
        if len(tuple_b) < 2:
            tuple_b += 0,
        k = (tuple_a[i] + tuple_b[i])
        j += k,
    return j
