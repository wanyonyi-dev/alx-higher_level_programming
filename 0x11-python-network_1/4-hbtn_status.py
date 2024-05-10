#!/usr/bin/python3
"""Fetching url responce with requests module"""
if __name__ == "__main__":
    import requests

    url = "https://intranet.hbtn.io/status"
    req = requests.get(url)
    print("Body response:")
    print("\t- type: {}".format(type(req.text)))
    print("\t- content: {}".format(req.text))
