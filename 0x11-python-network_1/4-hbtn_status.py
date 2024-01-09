#!/usr/bin/python3
"""
Fetches https://alx-intranet.hbtn.io/status
"""

if __name__ == '__main__':
    import requests

    res = requests.get("https://alx-intranet.hbtn.io/status")
    body = res.text
    print("Body response:")
    print("\t- type: {}".format(type(body)))
    print("\t- content: {}".format(body))
