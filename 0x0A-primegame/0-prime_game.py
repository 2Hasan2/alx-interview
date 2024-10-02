#!/usr/bin/python3
"""Prime game module."""


def sieve_of_eratosthenes(n):
    """Generate a list of prime numbers up to n using the Sieve of Eratosthenes."""
    is_prime = [True] * (n + 1)
    p = 2
    while p * p <= n:
        if is_prime[p]:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1
    return [p for p in range(2, n + 1) if is_prime[p]]


def isWinner(x: int, nums: list[int]) -> str:
    """Determine the winner of the prime game.

    Args:
        x (int): The number of rounds.
        nums (list[int]): A list of integers representing the upper limit for each round.

    Returns:
        str: The name of the player that won the most rounds or None if the winner cannot be determined.
    """
    if x <= 0 or not nums:
        return None

    max_n = max(nums)
    primes = sieve_of_eratosthenes(max_n)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        count_primes = len([p for p in primes if p <= n])
        if count_primes % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
