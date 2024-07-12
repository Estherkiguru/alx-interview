#!/usr/bin/env python3
"""module for Prototype: def minOperations(n)"""


def minOperations(n):
    """calculates the fewest number of operations needed"""
    if n < 2:
        return 0
    fac_list = []
    i = 1

    while n != 1:
        i += 1
        if n % i == 0:
            while n % i == 0:
                n /= i
                fac_list.append(i)
    return sum(fac_list)
