#!/usr/bin/python3
"""
  Python script that takes in a URL, sends a request to the URL and
  displays the body of the response.
"""


import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    R = requests.get(url)
    try:
        R.raise_for_status()
        print(R.text)
    except Exception as e:
        print("Error code: {}".format(R.status_code))
