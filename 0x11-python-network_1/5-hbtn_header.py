#!/usr/bin/python3
'''sends a request and displays the values of x-Request-ID'''

if __name__ == "__main__":
    import requests
    import sys

    url = sys.argv[1]

    req = requests.get(url)
    print(req.headers.get("X-Request-Id"))
