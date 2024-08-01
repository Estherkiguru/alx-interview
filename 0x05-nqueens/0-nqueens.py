#!/usr/bin/python3
"""Script for implementing N queens puzzle challenge"""
import sys

"""Validate command-line arguments"""
if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

if not sys.argv[1].isdigit():
    print("N must be a number")
    sys.exit(1)

if int(sys.argv[1]) < 4:
    print("N must be at least 4")
    sys.exit(1)

N = int(sys.argv[1])


def Nqueens(n, i=0, a=[], b=[], c=[]):
    """ find possible positions to place a queen at board"""
    if i < N:
        for j in range(N):
            if j not in a and i + j not in b and i - j not in c:
                yield from Nqueens(N, i + 1, a + [j], b + [i + j], c + [i - j])
    else:
        yield a


def solve(N):
    """ solve """
    k = []
    i = 0
    for solution in Nqueens(N, 0):
        for s in solution:
            k.append([i, s])
            i += 1
        print(k)
        k = []
        i = 0


solve(N)
