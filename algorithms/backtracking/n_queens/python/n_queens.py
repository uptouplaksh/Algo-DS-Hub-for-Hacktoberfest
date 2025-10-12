def solve_n_queens(n):
    """
    Solve the N-Queens problem using the Backtracking algorithm.

    Problem Overview:
    ------------------
    Place N queens on an N×N chessboard such that no two queens threaten each other.
    Threats occur when queens share the same row, column, or diagonal.

    Backtracking Approach:
    ----------------------
    1. Place one queen in each row (starting from row 0).
    2. For each row, try every column to find a safe position.
    3. If a column is safe:
        a. Place the queen.
        b. Recurse to the next row to place the next queen.
    4. If no valid column exists for the current row, backtrack:
        a. Remove the last placed queen.
        b. Try the next column in the previous row.
    5. Continue until all queens are placed (base case), then record the solution.

    Parameters:
    -----------
    n : int
        The size of the chessboard and number of queens.

    Returns:
    --------
    List[List[str]]
        A list of all valid solutions.
        Each solution is a list of strings where 'Q' denotes a queen and '.' an empty cell.

    Time Complexity: O(N!)
        - Each row has at most N choices, with pruning via the is_safe check.
    Space Complexity: O(N^2)
        - Board storage and recursion stack.
    """

    def is_safe(board, row, col):
        """
        Determine if it's safe to place a queen at board[row][col].

        Checks performed:
        1. Column: Ensure no queen exists in the same column in previous rows.
        2. Upper-left diagonal: Ensure no queen exists in the diagonal running from top-left to bottom-right.
        3. Upper-right diagonal: Ensure no queen exists in the diagonal running from top-right to bottom-left.

        Returns True if all checks pass, False otherwise.
        """

        # Check column for existing queen
        for i in range(row):
            if board[i][col] == 'Q':
                # Conflict found in same column
                return False

        # Check upper-left diagonal
        i, j = row - 1, col - 1
        while i >= 0 and j >= 0:
            if board[i][j] == 'Q':
                # Conflict found on upper-left diagonal
                return False
            i -= 1
            j -= 1

        # Check upper-right diagonal
        i, j = row - 1, col + 1
        while i >= 0 and j < n:
            if board[i][j] == 'Q':
                # Conflict found on upper-right diagonal
                return False
            i -= 1
            j += 1

        # No conflicts found, position is safe
        return True

    def solve(board, row):
        """
        Recursive function to place queens row by row.

        Recursive Logic:
        ----------------
        - Base Case: All rows are filled successfully.
          Append current board configuration to results.
        - Recursive Case:
            1. Loop through each column in current row.
            2. Check if position is safe using is_safe.
            3. If safe:
                a. Place queen.
                b. Recurse to next row.
                c. Backtrack by removing the queen.

        Comments explain both the recursion and backtracking mechanism.
        """

        # Base Case: all queens are placed
        if row == n:
            # Convert board rows to strings and store solution
            result.append([''.join(r) for r in board])
            return

        # Attempt to place queen in every column for current row
        for col in range(n):
            if is_safe(board, row, col):
                # Place queen at current position
                board[row][col] = 'Q'

                # Recursive call to place next queen in the next row
                solve(board, row + 1)

                # Backtrack: remove queen to try next possible column
                board[row][col] = '.'

    # Initialize empty chessboard with all '.' (empty cells)
    board = [['.' for _ in range(n)] for _ in range(n)]

    # List to store all valid board configurations
    result = []

    # Begin backtracking from row 0
    solve(board, 0)

    return result


if __name__ == "__main__":
    # Prompt user for board size (N)
    n = int(input("Enter the value of N: "))

    # Solve the N-Queens problem
    solutions = solve_n_queens(n)

    # Print total number of valid solutions
    print(f"\nTotal solutions for {n}-Queens: {len(solutions)}\n")

    # Print each solution with clear formatting
    for idx, sol in enumerate(solutions, 1):
        print(f"Solution {idx}:")
        for row in sol:
            print(row)
        print()