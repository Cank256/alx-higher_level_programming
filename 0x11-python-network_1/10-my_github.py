#!/usr/bin/python3
"""
Takes GitHub credentials (username and password) and
uses the GitHub API to display the user id.
Uses Basic Authentication with a personal access token.
"""

import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    url = "https://api.github.com/user"

    response = requests.get(url, auth=(username, password))
    print(response.json().get('id'))
