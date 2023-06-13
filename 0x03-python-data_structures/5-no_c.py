#!/usr/bin/python3
"""function that removes all characters c and C from a string"""


def no_c(my_string):
    
    copy = [i for i in my_string if i != 'c' and i != 'C']
    return ("".join(copy))
