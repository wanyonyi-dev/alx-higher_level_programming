#!/usr/bin/python3
"""Checking if the status code is okey or else raise_for_status"""
if __name__ == "__main__":
    import requests
    from sys import argv

    url = argv[1]
    res = requests.get(url)
    if res.status_code < 400:
        print(res.text)
    else:
        print("Error code: {}".format(res.status_code))
