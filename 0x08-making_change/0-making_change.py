#!/usr/bin/python3
""" Making changes """


def makeChange(coins, total):
    """ Generate changes needed to reach total

    Args:
        coins ([List]): [List of Coins available]
        total ([int]): [total amount needed]
    """
    if total <= 0:
        return 0
    check = 0
    tem = 0
    coins.sort(reverse=True)
    for j in coins:
        while check < total:
            check += j
            tem += 1
        if check == total:
            return tem
        check -= j
        tem -= 1
    return -1
