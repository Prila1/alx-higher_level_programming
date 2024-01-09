#!/usr/bin/python3
"""
Fetchess a post request to the url with the email as a query
"""

if __name__ == '__main__':
    import requests
    import sys

    url = sys.argv[1]
    email = sys.argv[2]
    data = {"email": email}

    res = requests.post(
        url,
        data=data,
    )
    print(res.text)
