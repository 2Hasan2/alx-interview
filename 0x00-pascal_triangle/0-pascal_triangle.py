#!/usr/bin/python3
'''A module for working with Pascal's triangle.
'''

def pascal_triangle(n):
    '''returns a list of lists of integers
    representing the Pascal’s triangle of n
    '''
    tr = []
    if type(n) is not int or n <= 0:
        return tr
    for i in range(n):
        line = []
        for j in range(i + 1):
            if j == 0 or j == i:
                line.append(1)
            elif i > 0 and j > 0:
                line.append(tr[i - 1][j - 1] + tr[i - 1][j])
        tr.append(line)
    return tr
