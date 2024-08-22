#!/usr/bin/python3
"""Module for the make change problem using dynamic programming"""


def makeChange(coins, total):
    """Using the bottom-up method"""
    if total <= 0:
        return 0

    coins = list(set(coins))

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for amt in range(1, total + 1):
        for coin in coins:
            if coin <= amt:
                dp[amt] = min(dp[amt], dp[amt - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
