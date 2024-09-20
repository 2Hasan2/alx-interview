#!/usr/bin/python3
"""Making Change with optimizations.
"""


def makeChange(coins, total):
    """This function calculates the minimum number
    of coins needed to make change for a given total."""

    if total <= 0:
        return 0

    coins.sort(reverse=True)

    dp = [float("inf")] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for t in range(coin, total + 1):
            dp[t] = min(dp[t], dp[t - coin] + 1)

            if dp[total] != float("inf"):
                break

    return dp[total] if dp[total] != float("inf") else -1
