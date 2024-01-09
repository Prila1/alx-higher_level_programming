#!/usr/bin/python3
"""
Fetches and prints out the value of the X-Request-Id
"""

if __name__ == '__main__':
    import urllib.request
    import sys

    url = sys.argv[1]

    with urllib.request.urlopen(url) as res:
        header = res.headers
        print(header.get("X-Request-Id"))
