#!/usr/bin/python3
"""Script tha:
- takes in a letter
- sends POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""


import sys
import requests


if __name__ == "__main__":
    letter = "" if len(sys.argv) == 1 else sys.argv[1]
    value = {"q": letter}

    R = requests.post("http://0.0.0.0:5000/search_user", data=value)
    try:
        response = R.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")
