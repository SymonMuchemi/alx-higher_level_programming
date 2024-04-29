#!/usr/bin/python3
""" Listing 10 most recent commits of a github repository """
import sys
import requests


if __name__ == "__main__":
    rname = sys.argv[1]
    uname = sys.argv[2]
    params = {'per_page': 10}

    # use get request to fetch data about commits
    r = requests.get("https://api.github.com/repos/{}/{}/commits"
                     .format(rname, uname), params=params)

    if r.status_code == 200:
        r_data = r.json()

        for data in r_data:
            print("{}: {}".format(
                data.get('sha'),
                data.get('commit').get('author').get('name')
            ))
