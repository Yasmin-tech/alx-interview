#!/usr/bin/python3
""" Solve the Alx Making Change problem
"""


def makeChange(coins, total):
    """Given a pile of coins of different values,
        determine the fewest number of coins needed
        to meet a given amount tota"""
    if total <= 0:
        return 0
    r = total
    coins_count = 0
    coin_index = 0
    sorted_coins = sorted(coins, reverse=True)
    n = len(coins)
    while r > 0:
        if coin_idx >= n:
            return -1
        if r - sorted_coins[coin_idx] >= 0:
            r -= sorted_coins[coin_idx]
            coins_count += 1
        else:
            coin_idx += 1
    return coins_countn
