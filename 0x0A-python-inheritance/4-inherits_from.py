#!/usr/bin/python3
"""
Contains the inherits_from function
"""


def inherits_from(obj, a_class):
    """returns true if obj is a subclass of a_class, otherwise false"""
    if type(obj) != a_class:
        return issubclass(type(obj), a_class)
    else:
        return False
