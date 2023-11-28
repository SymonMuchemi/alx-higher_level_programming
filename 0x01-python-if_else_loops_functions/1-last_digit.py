#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

# get the last digit number and state whether
# it is zero, greater than 6 and not 0
# or is greater than 5


def get_last_digit(parent_number):
    if parent_number < 0:
        parent_number *= -1
        return -1 * (parent_number % 10)
    last_digit = parent_number % 10
    return last_digit


last = get_last_digit(number)

if last == 0:
    print("Last digit of {} is {} and is 0".format(number, last))
elif last > 5:
    print(f"Last digit of {number} is {last} and is greater than 5")
else:
    print(f"Last digit of {number} is {last} and is less than 6 and not 0")
