#!/usr/bin/python3
"""
 Python script that takes in a URL and an email, sends a POST request to the passed 
 URL with the email as a parameter, and displays the body of the response (decoded in utf-8)
"""


import sys
from urllib import request, parse


if __name__ == "__main__":
    values = {'email': sys.argv[2]}
    data = parse.urlencode(values)
    data = data.encode('utf-8')
    reqt = request.Request(sys.argv[1], data)
    with request.urlopen(reqt) as resp:
        print(resp.read().decode('utf-8'))
