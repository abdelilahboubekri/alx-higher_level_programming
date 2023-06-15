#!/usr/bin/python3
"""function that returns the number of keys in a dictionary."""


def number_keys(a_dictionary):
    number = 0
    list_keys = list(a_dictionary.keys())

    for i in list_keys:
        number = number + 1

    return (number)
