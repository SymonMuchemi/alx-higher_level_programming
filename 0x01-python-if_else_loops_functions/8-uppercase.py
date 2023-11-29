#!/usr/bin/python3

# uppercase - prints the uppercase version of a string
# @str: the string to be converted

def uppercase(str):
    upper_case_string = ""
    for char in str:
        if 'a' <= char <= 'z':
            upper_case_string += chr(ord(char) - 32)
        else:
            upper_case_string += char
    print("{}".format(upper_case_string))
