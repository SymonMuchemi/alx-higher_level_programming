#!/usr/bin/python3
""" Takes Github credentials and uses GitHub api to display
    id
"""
import sys
import requests


if __name__ == "__main__":
    auth = (sys.argv[1], sys.argv[2])
    response = requests.get('https://api.github.com/user', auth=auth)

    if response.status_code == 200:
        data = response.json()
        print(data.get('id'))
