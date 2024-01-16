#!/usr/bin/python3
for i in range(48, 58):
    for j in range(48, 58):
        if j > i and i < 56:
            print("{}{}".format(chr(i), chr(j)), end=", ")
print("{}".format(89))
