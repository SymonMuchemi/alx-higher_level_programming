#!/usr/bin/python3
""" script that takes in a URL, sends a request to the URL and
    display the value of the variable `X-Request-Id` in the
    response header
"""
import sys
import requests


if __name__ == "__main__":
    response = requests.get(sys.argv[1])
    print(response.headers['X-Request-Id'])
