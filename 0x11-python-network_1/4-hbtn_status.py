#!/usr/bin/python3
"""
requests model
"""

import requests


if __name__ == '__main__':
    reqst = requests.get('https://alx-intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(reqst.text.__class__))
    print("\t- content: {}".format(reqst.text))
