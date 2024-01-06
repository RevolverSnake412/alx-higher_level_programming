#!/usr/bin/python3
'''sends a request to the URL and displays the body of the response'''

if __name__ == "__main__":
    import sys
    import requests

    url = sys.argv[1]
    request = requests.get(url)

    if request.status_code >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        print(request.text)
