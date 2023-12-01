#!/usr/bin/python3
"""
Script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id.
"""

import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]

    url = 'https://api.github.com/user'
    auth = (username, password)
    response = requests.get(url, auth=auth)

    try:
        json_response = response.json()
        print(json_response.get('id', 'None'))
    except ValueError:
        print("None")

