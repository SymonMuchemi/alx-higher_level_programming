#!/usr/bin/python3
""" uses urllib to fetch https://alx-intranet.hbtn.io/status """
import urllib
import urllib.request


location = 'https://alx-intranet.hbtn.io/status'

with urllib.request.urlopen(location) as res:
    data = res.read()
    print("Body response:")
    print("\t- type: {}".format(type(data)))
    print("\t- content: {}".format(data))
