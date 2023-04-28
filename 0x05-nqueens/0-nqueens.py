#!/usr/bin/python3
""" Solving the N-queens puzzle """
import sys


def printBoard(board):
    """ Print the board """
    array = []

    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == 1:
                array.append([row, col])
    print(array)

# printBoard([[0, 1, 0, 0], [0, 0, 0, 1], [1, 0, 0, 0], [0, 0, 1, 0]])
# printBoard([[0, 0], [1, 0]])


def isValidMove(board, row, col):
    """ Check if the move is valid and queen can be placed at the position """

    # Check the row on the left side to see if there is a queen i.e. 1
    # Return False if there is a queen
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check the upper diagonal on the left side to see if there is a queen
    # Return False if there is a queen
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check the lower diagonal on the left side to see if there is a queen
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

# print(isValidMove([[0, 0, 0, 0], [0, 0, 0, 0], [1, 0, 0, 0],
# [0, 0, 1, 0]], 2, 1))


def nQueen(board, col):
    """ Solve the N-queens puzzle """
    # Base case: If all queens are placed, return True
    if col >= len(board):
        return True

    # Consider this column and try placing this queen in all rows one by one
    for row in range(len(board)):
        if isValidMove(board, row, col):
            # Place this queen in board[row][col]
            board[row][col] = 1

            # recur to place rest of the queens
            if nQueen(board, col + 1) is True:
                return True

            # If placing queen in board[row][col] doesn't lead to a solution
            # then remove queen from board[row][col]
            # board[row][col] = 0
            board.pop()

    # If the queen can not be placed in any row in the column, return False
    return False

# print(nQueen([[0, 0, 0, 0], [0, 0, 0, 0], [1, 0, 0, 0],
# [0, 0, 1, 0]], 0))


if __name__ == "__main__":
    # Check if the number of arguments is correct
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    # Check if the argument is a number
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    # Check if N is less than 4
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Create an NxN matrix filled with 0's
    board = [[0 for i in range(N)] for j in range(N)]

    # Call the function to solve the N-queens puzzle
    nQueen(board, 0)

    # Print the solution
    printBoard(board)
