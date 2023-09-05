#!/usr/bin/python3
import sys


def is_safe(board, row, col, N):
    """
    Check if it's safe to place a queen at a specific position on the board.

    Args:
        board (list): The chessboard represented as a 2D list.
        row (int): The row index to check.
        col (int): The column index to check.
        N (int): The size of the chessboard.

    Returns:
        bool: True if it's safe to place a queen, False otherwise.
    """
    # Check this row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on the left side
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens(N):
    """
    Solve the N queens problem and print all possible solutions.

    Args:
        N (int): The size of the chessboard.

    Prints:
        All possible solutions to the N queens problem, one solution per line.
    """
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0 for _ in range(N)] for _ in range(N)]
    solutions = []

    def solve(col):
        if col >= N:
            solution = []
            for i in range(N):
                row_str = "".join(
                    ["Q" if board[i][j] == 1 else "." for j in range(N)]
                )
                solution.append(row_str)
            solutions.append(solution)
            return

        for i in range(N):
            if is_safe(board, i, col, N):
                board[i][col] = 1
                solve(col + 1)
                board[i][col] = 0  # Backtrack

    solve(0)

    for solution in solutions:
        for row in solution:
            print(row)
        print()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
        solve_nqueens(N)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
