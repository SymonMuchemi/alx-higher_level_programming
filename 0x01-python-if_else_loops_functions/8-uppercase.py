#!/usr/bin/python3

# uppercase - checks if a character is in uppercase
# @c: the character to be checked
# return: true or false

def uppercase(c):
    if (ord(c) >= 65) and (ord(c) <= 90):
        return True
    else:
        return False
