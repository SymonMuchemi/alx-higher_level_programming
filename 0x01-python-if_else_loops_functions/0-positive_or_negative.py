#!/usr/bin/python3
import random
number = random.randint(-10, 10)

# check if the number is positive, negative or zero

if number < 0:
    print("{} is negative".format(number))
elif number == 0:
    print("{} is zero".format(number))
else:
    print("{} is positive".format(number))
