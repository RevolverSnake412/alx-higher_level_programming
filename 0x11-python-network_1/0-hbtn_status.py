#!/usr/bin/python3
'''Fetches the URL below'''

if __name__ == '__main__':
    import urllib.request

    req = urllib.request.urlopen('https://alx-intranet.hbtn.io/status')
    answer = req.read()
    print("Body response:")
    print("\t- type: {}".format(type(answer)))
    print("\t- content: {}".format(answer))
    print("\t- utf8 content: {}".format(answer.decode('utf-8')))
