#!/usr/bin/python3
"""access my github account and display my id using basic authentication"""
if __name__ == "__main__":
    import requests
    from sys import argv

    username = argv[1]
    password = argv[2]
    header = {"X-GitHub-Api-Version": "2022-11-28"}
    url = "https://api.github.com/user"
    res = requests.get(url, auth=(username, password), headers=header)
    res_dict = res.json()
    if "id" in res_dict:
        print(res_dict["id"])
    else:
        print(None)
