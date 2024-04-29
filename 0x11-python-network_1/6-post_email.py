#!/usr/bin/python3
""" sends a post request to the passed URL wiht the email
    as a parameter and display th body of the response
"""
import sys
import requests


if __name__ == "__main__":
    data = {'email': sys.argv[2]}
    # making a POST request
    response = requests.post(sys.argv[1], data=data)
    print(response.text)
