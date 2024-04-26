#!/usr/bin/python3
"""A script that fetches https://alx-intranet.hbtn.io/status"""
from urllib import request


if __name__ == "__main__":
    with request.urlopen('https://alx-intranet.hbtn.io/status') as x:
        reads = x.read()
        print("Body response:")
        print("\t- type: {}".format(type(reads)))
        print("\t- content: {}".format(reads))
        print("\t- utf8 content: {}".format(reads.decode("utf-8")))
