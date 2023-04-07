#!/usr/bin/python3
""" Creating a function that returns minimum number
    of operations needed to result in exactly n H characters.
"""


def prime_factorization(n):
    """ Returning prime factors of n """
    list_factors = []
    mul_num = (n // 2) + 1

    for item in range(2, int(mul_num)):
        if (n % item) == 0:
            list_factors.append(item)
            n = n // item
            item = 2
    list_factors.append(n)
    return list_factors


def minOperations(n):
    """ Returning minimum number of operations needed to result in
        exactly n H characters.
    """
    if n <= 1:
        return 0

    list_factors = prime_factorization(n)
    return sum(list_factors)
