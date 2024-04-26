#!/usr/bin/python3
"""A script that takes in a URL and an email, sends a POST request
to the passed URL with the email as a parameter, and displays
the body of the response (decoded in utf-8)"""
from urllib import request, parse
from sys import argv


if __name__ == "__main__":
    value = {"email": argv[2]}
    data = parse.urlencode(value).encode("utf-8")
    request = request.Request(argv[1], data)
    with request.urlopen(request) as x:
        print(x.read().decode("utf-8"))
