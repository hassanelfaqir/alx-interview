#!/usr/bin/python3
"""
0-pascal_triangle
"""

def pascal_triangle(n):
    """
    Returns a list of integers
    representing the Pascal Triangle of n
    returns empty list if n <= 0
    """
    l = []
    if n <= 0:
        return l
    l = [[1]]
    for o in range(1, n):
        temp = [1]
        for m in range(len(k[i - 1]) - 1):
            curr = l[o - 1]
            temp.append(l[o - 1][m] + l[m - 1][m + 1])
        temp.append(1)
        l.append(temp)
    return l
