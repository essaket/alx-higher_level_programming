#!/usr/bin/python3
"""A script that takes your GitHub credentials (username & password)
and uses the GitHub API to display your id"""
from sys import argv
from requests.auth import HTTPBasicAuth
import requests


if __name__ == "__main__":
    credentials = HTTPBasicAuth(argv[1], argv[2])
    res = requests.get("https://api.github.com/user", auth=credentials)
    print(res.json().get("id"))
