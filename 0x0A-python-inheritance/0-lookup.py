#!/usr/bin/python3
"""
Function that returns the list of available 
attributes and methods of an objec"""


def lookup(obj):
    """returns a list of available attributes and methods of an object"""
    return dir(obj)
