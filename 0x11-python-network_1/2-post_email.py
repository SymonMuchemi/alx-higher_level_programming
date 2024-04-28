#!/usr/bin/python3
""" Takes in a url and an email, sends a POST request to the
    the url with the email as a parameter and displays the body of
    the response decoded in utf-8
"""
import sys
import urllib.request
import urllib.parse


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    values = {'email': email}
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data=data)

    with urllib.request.urlopen(req) as response:
        body = response.read().decode('utf-8')
        print(body)
