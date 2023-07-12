#!/usr/bin/python3
"""
Module writes an Object to a text file
"""

import json


def save_to_json_file(my_obj, filename):
    """Object to a text file, using a JSON representation"""
    with open(filename, 'w', encoding='utf-8') as File:
        json.dump(my_obj, File)
