#!/usr/bin/python3
""" sends request to a url and displays the body of the
    response. Prints the status code in case of error
"""
import sys
import requests


if __name__ == "__main__":
    response = requests.get(sys.argv[1])

    if response.status_code > 400:
        print("Error code: {}".format(response.status_code))
    else:
        print(response.text)
