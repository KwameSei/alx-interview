#!/usr/bin/env python3
""" Creating a function that returns minimum number
    of operations needed to result in exactly n H characters.
"""


def prime_factorization(n):
    """ Returning prime factors of n """
    list_factors = []
    num = n

    for item in range(2, num // 2):
        if (num % item) == 0:
            list_factors.append(item)
            num = num // item
            item = 2
    list_factors.append(num)
    return list_factors


def minOperations(n):
    """ Returning minimum number of operations needed to result in
        exactly n H characters.
    """
    if n <= 1:
        return 0

    list_factors = prime_factorization(n)
    return sum(list_factors)