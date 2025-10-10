"""
--------------------------------------------------------
    Sudoku Solver using Backtracking (Python)
--------------------------------------------------------

    Time Complexity:
        Worst Case: O(9^(N))
        - For each empty cell (N), there can be up to 9 possible numbers.
        - In the worst case (when the board is mostly empty),
          the solver may explore 9^N possibilities.
        - However, due to pruning (validity checks),
          actual performance is much faster in practice.

    Space Complexity:
        O(N)
        - Due to recursive backtracking stack depth (N = number of empty cells).
        - The grid is modified in place, so no extra data structures are used.
--------------------------------------------------------
"""


def print_grid(grid):
    """Helper function to print the Sudoku grid neatly."""
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-" * 21)
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            print(grid[i][j] if grid[i][j] != 0 else ".", end=" ")
        print()


def is_valid(grid, row, col, num):
    """
    Check if placing 'num' in grid[row][col] is valid.
    - Checks the row, column, and 3x3 subgrid for conflicts.
    """
    # Check row
    for x in range(9):
        if grid[row][x] == num:
            return False

    # Check column
    for x in range(9):
        if grid[x][col] == num:
            return False

    # Check 3x3 subgrid
    start_row = row - row % 3
    start_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[i + start_row][j + start_col] == num:
                return False

    return True


def solve_sudoku(grid):
    """
    Solves the Sudoku puzzle using backtracking.
    Returns True if solved successfully, else False.
    """
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:  # Empty cell found
                for num in range(1, 10):  # Try digits 1-9
                    if is_valid(grid, row, col, num):
                        grid[row][col] = num  # Tentatively assign

                        if solve_sudoku(grid):  # Recursive call
                            return True

                        grid[row][col] = 0  # Backtrack

                return False  # No valid number found
    return True  # All cells filled → solved


if __name__ == "__main__":
    # Example Sudoku puzzle (0 represents an empty cell)
    sudoku_grid = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

    print("Original Sudoku Puzzle:\n")
    print_grid(sudoku_grid)

    if solve_sudoku(sudoku_grid):
        print("\nSolved Sudoku Puzzle:\n")
        print_grid(sudoku_grid)
    else:
        print("\nNo solution exists for the given Sudoku puzzle.")
