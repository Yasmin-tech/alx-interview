#!/usr/bin/python3
""" Solve the Alx Making Change problem
"""


def makeChange(coins, total):
    """Given a pile of coins of different values,
        determine the fewest number of coins needed
        to meet a given amount tota"""
    # Initialize a list with a value larger than the maximum amount
    dp = [float('inf')] * (amount + 1)
    # Zero coins needed to make zero amount
    dp[0] = 0

    # Iterate through all the amounts up to the given amount
    for i in range(1, amount + 1):
        # Check each coin
        for coin in coins:
            if i - coin >= 0:
                # Update the dp list with the minimum coins needed
                dp[i] = min(dp[i], dp[i - coin] + 1)

    # If the value at dp[amount] is still float('inf'),
    # return -1 indicating no solution
    return dp[amount] if dp[amount] != float('inf') else -1
