#!/usr/bin/python3
"""A script that takes in a letter and sends a POST request"""
from sys import argv
import requests


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    value = {'q': argv[1] if len(argv) == 2 else ""}
    try:
        response = requests.post(url, data=value).json()
        if response:
            print(f"[{response.get('id')}] {response.get('name')}")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
