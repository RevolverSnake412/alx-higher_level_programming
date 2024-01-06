#!/usr/bin/python3
'''sends a request to the URL and displays the body of the response'''

if __name__ == "__main__":
    import sys
    import requests

    url = sys.argv[1]
    value = {"email": sys.argv[2]}

    request = requests.post(url, data=value)
    print(request.text)
