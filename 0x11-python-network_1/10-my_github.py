#!/usr/bin/python3
'''
a script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
'''

if __name__ == "__main__":
    import requests
    from requests.auth import HTTPBasicAuth
    import sys

    user = sys.argv[1]
    passwd = sys.argv[2]

    auth = HTTPBasicAuth(user, passwd)
    req = requests.get("https://api.github.com/user", auth=auth)
    print(req.json().get("id"))
