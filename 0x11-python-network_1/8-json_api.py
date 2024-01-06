#!/usr/bin/python3
'''sends a POST request to the URL with the letter as a parameter'''

if __name__ == "__main__":
    import requests
    import sys

    letter = "" if len(sys.argv) == 1 else sys.argv[1]
    payload = {"q": letter}
    request = requests.post("http://0.0.0.0:5000/search_user", data=payload)

    try:
        response = request.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")
