#!/usr/bin/python3
"""Fetching and displaying data from a URL."""
if __name__ == "__main__":
    import urllib.request as request

    url = "https://alx-intranet.hbtn.io/status"
    with request.urlopen(url) as res:
        res = res.read()
        print("Body response:")
        print("\t- type: {}".format(type(res)))
        print("\t- content: {}".format(res))
        print("\t- utf8 content: {}".format(res.decode("utf-8")))
