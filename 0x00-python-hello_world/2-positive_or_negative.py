#!/usr/bin/python3

from random import randint
number = randint(-10, 10)
if number > 0:
    print("The number", number, "is positive\n")
elif number == 0:
    print("The number", number, "is zero\n")
else:
    print("The number", number, "is negative\n")
