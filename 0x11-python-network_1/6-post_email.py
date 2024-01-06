#!/usr/bin/python3
'''sends a POST request to the passed URL with email par'''

if __name__ == "__main__":
    import requests
    import sys

    url = sys.argv[1]
    value = {"email": sys.argv[2]}

    request = requests.post(url, data=value)
    print(request.text)
