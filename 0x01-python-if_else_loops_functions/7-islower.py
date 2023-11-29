#!/usr/bin/python3

# isLower - checks if a character is in lowercase
# @c: the character to be checked
# return: true or false

def islower(c):
    if (ord(c) >= 97) and (ord(c) <= 122):
        return True
    else:
        return False
