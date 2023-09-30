#!/usr/bin/python3
""" Python script that fetches https://alx-intranet.hbtn.io/status
"""

from urllib.request import Request, urlopen


if __name__ == "__main__":
    rqst = Request('https://alx-intranet.hbtn.io/status')

    with urlopen(rqst) as resp:
        content = resp.read()
        utf8_content = content.decode('utf-8')

        print('Body response:')
        print('\t- type: {_type}'.format(_type=type(content)))
        print('\t- content: {_content}'.format(_content=content))
        print('\t- utf8 content: {utf8_c}'.format(utf8_c=utf8_content))
