#!/usr/bin/python3
"""Module for the make change problem using dynamic programming"""


def makeChange(coins, total):
    """Using the bottom-up method"""
    if total <= 0:
        return 0

    check = 0
    temp = 0

    coins.sort(reverse=True)
    for i in coins:
        while check < total:
            check += i
            temp += 1

        if check == total:
            return temp
        check -= i
        temp -= 1

    return -1
