#!/usr/bin/python3
from collections import deque

"""Making Change with optimizations.
"""


def makeChange(coins, total):
    """This function calculates the minimum number
    of coins needed to make change for a given total."""

    if total <= 0:
        return 0

    queue, visited = deque([(0, 0)]), set([0])

    while queue:
        curr_sum, num_coins = queue.popleft()
        for coin in coins:
            new_sum = curr_sum + coin

            if new_sum == total:
                return num_coins + 1
            if new_sum < total and new_sum not in visited:
                visited.add(new_sum)
                queue.append((new_sum, num_coins + 1))

    return -1
