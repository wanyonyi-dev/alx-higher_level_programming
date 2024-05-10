#!/usr/bin/python3
"""Getting a specific header and displaying its value"""
if __name__ == "__main__":
    import requests
    from sys import argv

    url = argv[1]
    res = requests.get(url)
    print(res.headers["X-Request-Id"])
