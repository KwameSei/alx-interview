#!/usr/bin/python3
"""Rotate two dimensions matrix ninety degrees"""


def all(matrix):
    """ Rotate 2D matrix 90 degrees clockwise """
    n = len(matrix[0])  # n = 3

    for x in range(n):   # x = 0, 1, 2
        for j in range(x, n):  # j = 1, 2, 3
            matrix[x][j], matrix[j][x] = matrix[j][x], matrix[x][j]

    for x in range(n):   # x = 0, 1, 2
        matrix[x].reverse()


def rotate_2d_matrix(matrix):
    """Function that rotates 2D matrix"""
    all(matrix)
