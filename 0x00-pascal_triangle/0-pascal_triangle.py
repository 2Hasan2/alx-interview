#!/usr/bin/python3
"""this module contains the pascal_triangle function 
    that returns a list of lists of integers representing the Pascal’s triangle of n
"""

def pascal_triangle(n):
    """returns a list of lists of integers representing the Pascal’s triangle of n
    """
    t = [[1] * (i + 1) for i in range(n)]
    print(t)
    for i in range(2, n):
        for j in range(1, i):
            t[i][j] = t[i - 1][j - 1] + t[i - 1][j]
        print(t[i])
    return t
