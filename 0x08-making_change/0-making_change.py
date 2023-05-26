#!/usr/bin/python3
""" Making Change """


def makeChange(coins, total):
    """ Return fewest number of coins needed to meet total
    """
    if total <= 0:
        return 0

    coins.sort(reverse=True)  # sort coins in descending order

    fewest_coins = 0  # fewest number of coins needed to meet total
    for coin in coins:
        if total <= 0:
            break
        if coin <= total:  # if coin is less than total
            fewest_coins += total // coin  # add quotient to fewest
            total = total % coin  # remainder is new total

    if total > 0:  # if total is not met
        return -1

    return fewest_coins
