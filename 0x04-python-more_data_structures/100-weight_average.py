#!/usr/bin/python3
"""Function that returns the weighted average of all
integers tuple (<score>, <weight>)"""


def weight_average(my_list=[]):

    if not my_list:
        return 0

    num = 0
    d = 0

    for i in my_list:
        num += i[0] * i[1]
        d += i[1]

    return (num / d)
