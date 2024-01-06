#!/usr/bin/python3
'''sends a POST request to the passed URL with email par'''

if __name__ == "__main__":
    import urllib.request
    import sys
    url = sys.argv[1]

    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        print(dict(response.headers).get("X-Request-Id"))
