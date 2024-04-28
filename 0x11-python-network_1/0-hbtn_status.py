#!/usr/bin/python3
""" uses urllib to fetch https://alx-intranet.hbtn.io/status """
import urllib
import urllib.request


location = 'https://alx-intranet.hbtn.io/status'
# create request body
req = urllib.request.Request(location)

with urllib.request.urlopen(req) as response:
    data = response.read()
    print("Body response:")
    print("\t- type: {}".format(type(data)))
    print("\t- content: {}".format(data))
