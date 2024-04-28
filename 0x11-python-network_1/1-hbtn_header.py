#!/usr/bin/python3
""" send request to a url and displays the """
import sys
import urllib.request


if __name__ == "__main__":
    req = urllib.request.Request(sys.argv[1])

    with urllib.request.urlopen(req) as response:
        print(response.info()['X-Request-Id'])
