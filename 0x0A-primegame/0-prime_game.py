#!/usr/bin/python3
"""Prime game module.
"""
from math import sqrt


def isWinner(x: int, nums: list[int]) -> str:
    """Determine the winner of the prime game.

    Args:
        x (int): The number of rounds.
        nums (List[int]): A list of integers representing the upper limit for each round.

    Returns:
        str: The name of the winner, either "Ben" or "Maria".
    """
    rounds = [
        [i for i in range(1, nums[round] + 1) if is_prime(i)] for round in range(x)
    ]
    ben, maria = 0, 0
    for round in rounds:
        ben += len(round) == 0 or len(round) % 2 == 0
        maria += len(round) % 2 == 1
    return "Ben" if ben > maria else "Maria"


def is_prime(num: int) -> bool:
    """Check if a number is prime.

    Args:
        num (int): The number to check for primality.

    Returns:
        bool: True if num is prime, False otherwise.
    """
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    for i in range(5, int(sqrt(num) + 1)):
        if num % i == 0 or num % (i + 2) == 0:
            return False
    return True
