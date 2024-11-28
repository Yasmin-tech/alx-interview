#!/usr/bin/python3
""" Solve the Alx Making Change problem
"""


def makeChange(coins, total):
    """Given a pile of coins of different values,
        determine the fewest number of coins needed
        to meet a given total tota"""
    # Initialize a list with a value larger than the maximum total
    dp = [float('inf')] * (total + 1)
    # Zero coins needed to make zero total
    dp[0] = 0

    # Iterate through all the totals up to the given total
    for i in range(1, total + 1):
        # Check each coin
        for coin in coins:
            if i - coin >= 0:
                # Update the dp list with the minimum coins needed
                dp[i] = min(dp[i], dp[i - coin] + 1)

    # If the value at dp[total] is still float('inf'),
    # return -1 indicating no solution
    return dp[total] if dp[total] != float('inf') else -1
