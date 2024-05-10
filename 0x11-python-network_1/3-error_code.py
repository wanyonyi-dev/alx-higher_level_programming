#!/usr/bin/python3
"""handling HTTPError and displaying the status code"""
if __name__ == "__main__":
    import sys
    import urllib.request as request
    from urllib.error import HTTPError

    try:
        url = sys.argv[1]
        with request.urlopen(url) as res:
            res = res.read().decode("utf-8")
            print("{}".format(res))
    except HTTPError as err:
        print("Error code: {}".format(err.code))
