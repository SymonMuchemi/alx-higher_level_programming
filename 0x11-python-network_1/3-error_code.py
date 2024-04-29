#!/usr/bin/python3
""" sends a request to a url and displays the body of the response
    decode in utf-8.
    it also handles the HTTPError exception
"""
import sys
import urllib
import urllib.error
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    req = urllib.request.Request(url)

    try:
        with urllib.request.urlopen(req) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
