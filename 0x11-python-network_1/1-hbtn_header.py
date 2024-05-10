#!/usr/bin/python3
"""Display the value of X-Request-Id from url request"""
if __name__ == "__main__":
    import urllib.request as request
    from sys import argv as argv

    url = argv[1]
    with request.urlopen(url) as res:
        print(res.headers.get("X-Request-Id"))
