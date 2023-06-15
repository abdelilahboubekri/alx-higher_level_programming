#!/usr/bin/python3
"""Function that prints a dictionary by ordered keys"""


def print_sorted_dictionary(a_dictionary):
    list_by_ord = list(a_dictionary.keys())
    list_by_ord.sort()
    for i in list_by_ord:
        print("{}: {}".format(i, a_dictionary.get(i)))
