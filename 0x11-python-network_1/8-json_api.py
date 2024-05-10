#!/usr/bin/python3
"""Checking if the status code is okey or else raise_for_status"""
if __name__ == "__main__":
    import requests
    from sys import argv

    url = "http://0.0.0.0:5000/search_user"
    value = argv[1] if len(argv) > 1 else ""
    res = requests.post(url, data={"q": value})
    if res.status_code == 200:
        r_dict = res.json()
        if r_dict:
            print("[{}] {}".format(r_dict["id"], r_dict["name"]))
        elif r_dict == {}:
            print("No result")
        else:
            print("Not a valid JSON")
