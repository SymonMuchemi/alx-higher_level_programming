#!/usr/bin/python3
# This program emulates a simple calculator
from calculator_1 import add, sub, mul, div

def calculate(a, op, b):
    """handles simple calculations

    Args:
        a (int): first operand
        op (char): operator
        b (int): second operand
    """
    a = int(a)
    b = int(b)
    match op:
        case "+":
            print("{:d} {} {:d} = {:d}".format(a, op, b, add(a, b)))
        case "-":
            print("{:d} {} {:d} = {:d}".format(a, op, b, sub(a, b)))
        case "*":
            print("{:d} {} {:d} = {:d}".format(a, op, b, mul(a, b)))
        case "/":
            print("{:d} {} {:d} = {:d}".format(a, op, b, div(a, b)))
        case _:
            print("Unknown operator. Available operators: +, -, * and /")

if __name__ == "__main__":
    import sys
    from sys import argv
    argc = len(argv)
    if argc != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    else:
        a = argv[1]
        b = argv[3]
        op = argv[2]
        calculate(a, op, b)
