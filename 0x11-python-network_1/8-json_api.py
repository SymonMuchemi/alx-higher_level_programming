#!/usr/bin/python3
""" takes a letter and sends a POST request to a URL
    with the letter as a parameter
"""
import sys
import requests


if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    if len(sys.argv) == 2:
        letter = sys.argv[1]
    else:
        letter = ""

    value = {'q' : letter}
    # send a request
    response = requests.post(url, value)

    # convert response to json using
    try:
        response = response.json()
        if response == {}:
            print("No result")
        else:
            print(f"[{response.get('id')}] {response.get('name')}")
    except ValueError:
        print("Not a valid JSON")
