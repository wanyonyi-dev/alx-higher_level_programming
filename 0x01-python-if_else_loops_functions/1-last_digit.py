#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
str = "and is less than 6 and not 0"
if (number < 0):
    last = (number * -1) % 10
    last = last * -1
    if (last == 0):
        print(f"Last digit of {number} is {last} and is 0")
    elif (last < 6 and last != 9):
        print(f"Last digit of {number} is {last} " + str)
    else:
        print(f"Last digit of {number} is {last}")
elif (number >= 0):
    last = number % 10
    if (last == 0):
        print(f"Last digit of {number} is {last} and is 0")
    elif (last < 6 and last != 9):
        print(f"Last digit of {number} is {last} " + str)
    elif (last > 5):
        print(f"Last digit of {number} is {last} and is greater than 5")
    else:
        print(f"Last digit of {number} is {last}")
else:
    print("Generated number is 0")
