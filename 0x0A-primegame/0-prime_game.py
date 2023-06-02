#!/usr/bin/python3

""" Game to find prime numbers """

def isprime(n):
    """
    Check if a number is prime.
    
    Args:
        n (int): Number to check for primality.
        
    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def delete_numbers(n, nums):
    """
    Delete numbers and assign a modified list.

    Args:
        n (int): Number to use as a divisor.
        nums (list): List of numbers to modify.

    Modifies:
        nums: Removes elements divisible by n and assigns the modified list.
    """
    nums_copy = []
    for num in nums:
        if num % n != 0:
            nums_copy.append(num)
    nums[:] = nums_copy


def isWinner(x, nums):
    """
    Determine the winner of the prime number game.

    Args:
        x (int): Number of game rounds.
        nums (list): List of integers representing the upper bounds for each round.

    Returns:
        str or None: Name of the player with the most wins ('Maria' or 'Ben'). 
                     If the winner cannot be determined, returns None.
    """
    winners = []
    for n in nums:
        nums2 = list(range(1, n + 1))
        turn = 0
        while True:
            change = False
            for i, num in enumerate(nums2):
                if num > 1 and isprime(num):
                    delete_numbers(num, nums2)
                    change = True
                    turn += 1
                    break
            if not change:
                break
        winners.append("Maria" if turn % 2 == 1 else "Ben")

    maria_wins = winners.count("Maria")
    ben_wins = winners.count("Ben")

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
