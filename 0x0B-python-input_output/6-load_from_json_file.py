#!/usr/bin/python3
"""
Module creates an Object from a “JSON file”
"""

import json


def load_from_json_file(filename):
    """create and object from a "JSON file" """
    with open(filename, 'r', encoding='utf-8') as File:
        return json.load(File)
