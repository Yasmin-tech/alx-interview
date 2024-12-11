#!/usr/bin/python3
"""The Prime game.
"""


def isWinner(x, nums):
    """ determine the winner of each round x of the game.
     Assuming Maria always goes first and both players play optimally.
    """
    if x < 1 or not nums:
        return None
    Maria_win, Ben_win = 0, 0
    n = max(nums)
    primes = [True for _ in range(1, n + 1, 1)]
    primes[0] = False
    for i, is_prime in enumerate(primes, 1):
        if i == 1 or not is_prime:
            continue
        for j in range(i + i, n + 1, i):
            primes[j - 1] = False
    for _, n in zip(range(x), nums):
        primes_count = len(list(filter(lambda x: x, primes[0: n])))
        Ben_win += primes_count % 2 == 0
        Maria_win += primes_count % 2 == 1
    if Maria_win == Ben_win:
        return None
    return 'Maria' if Maria_win > Ben_win else 'Ben'
