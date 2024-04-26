#!/usr/bin/python3
"""A script that takes in a URL, sends a request to the URL
and displays the body of the response"""
from sys import argv
import requests


if __name__ == "__main__":
    res = requests.get(argv[1])
    try:
        res.raise_for_status()
        print(res.text)
    except Exception as err:
        print("Error code: {}".format(res.status_code))
