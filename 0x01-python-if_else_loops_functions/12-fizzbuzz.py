#!/usr/bin/python3

def fizzbuzz():
    """Function to perform the FizzBuzz game for numbers from 1 to 100.

    The function iterates through numbers from 1 to 100 and prints:
    - "Fizz" for numbers divisible by 3,
    - "Buzz" for numbers divisible by 5, and
    - "FizzBuzz" for numbers divisible by both 3 and 5.
    If a number is not divisible by either 3 or 5, it prints the number itself.

    The function does not return any value.
    """
    for i in range(1, 101):
        if (i % 3 == 0) and (i % 5 != 0):
            print("Fizz", end=" ")
        elif (i % 3 != 0) and (i % 5 == 0):
            print("Buzz", end=" ")
        elif (i % 3 == 0) and (i % 5 == 0):
            print("FizzBuzz", end=" ")
        else:
            print(i, end=" ")
