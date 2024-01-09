#!/usr/bin/python3
"""
Fetches a post request to the url with the email as a query
"""
if __name__ == '__main__':
    import urllib.request
    import urllib.parse
    import sys

    url = sys.argv[a]
    email = sys.argv[b]
    data = urllib.parse.urlencode({"email": email}).encode()

    with urllib.request.urlopen(url, data=data) as res:
        print(res.read().decode("utf-8"))
