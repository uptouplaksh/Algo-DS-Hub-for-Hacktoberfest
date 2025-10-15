/**
 * N-Queens Problem (Bitmask Optimization)
 *
 * Description:
 * Solves the classic N-Queens problem using backtracking with bitmask optimization.
 * The goal is to place N queens on an N×N chessboard such that no two queens attack each other.
 * This optimized version uses bit manipulation to efficiently track column and diagonal attacks.
 *
 * Time Complexity: O(N!) — each row has up to N choices, but pruning reduces it significantly.
 * Space Complexity: O(N) — for recursion stack and the array tracking queen positions.
 */

public class NQueensBitmask {

    // Board size (N)
    private int size;

    // Counts total number of valid solutions
    private int solutionCount = 0;

    // Stores the column index of the queen placed in each row
    private int[] queens;

    /**
     * Entry point of the program.
     * You can modify the value of n to test with different board sizes.
     */
    public static void main(String[] args) {
        int n = 4; // Example: Solve for 4x4 board
        NQueensBitmask solver = new NQueensBitmask();
        solver.solveNQueens(n);
    }

    /**
     * Initializes board size and begins solving.
     *
     * @param n size of the board (N)
     */
    public void solveNQueens(int n) {
        this.size = n;
        this.queens = new int[n];
        backtrack(0, 0, 0, 0); // Start from row 0 with empty bitmasks
        System.out.println("Total solutions found: " + solutionCount);
    }

    /**
     * Recursive backtracking function using bitmask optimization.
     *
     * Logic:
     * - cols tracks which columns are under attack.
     * - d1 (main diagonals '\') tracks attacks diagonally down-left.
     * - d2 (anti-diagonals '/') tracks attacks diagonally down-right.
     * - availablePositions = all positions in the current row that are safe to place a queen.
     *
     * @param row  current row index
     * @param cols bitmask for columns under attack
     * @param d1   bitmask for '\' diagonals under attack
     * @param d2   bitmask for '/' diagonals under attack
     */
    private void backtrack(int row, int cols, int d1, int d2) {
        // Base case: All queens are placed
        if (row == size) {
            printSolution();
            solutionCount++;
            return;
        }

        // Bitmask of available (safe) positions for this row
        int availablePositions = ((1 << size) - 1) & ~(cols | d1 | d2);

        // Try placing a queen in each available position
        while (availablePositions != 0) {
            // Extract the rightmost available bit (LSB)
            int position = availablePositions & -availablePositions;

            // Remove this position from available positions
            availablePositions -= position;

            // Store the column where the queen is placed
            queens[row] = Integer.numberOfTrailingZeros(position);

            // Recurse to next row with updated attack bitmasks
            backtrack(
                row + 1,
                cols | position,        // Mark this column as attacked
                (d1 | position) << 1,   // Mark next diagonal ('\')
                (d2 | position) >> 1    // Mark next diagonal ('/')
            );
        }
    }

    /**
     * Prints one valid board configuration.
     * Example output for N=4:
     * . Q . .
     * . . . Q
     * Q . . .
     * . . Q .
     */
    private void printSolution() {
        System.out.println("Solution " + (solutionCount + 1) + ":");
        for (int i = 0; i < size; i++) {
            StringBuilder row = new StringBuilder();
            for (int j = 0; j < size; j++) {
                row.append(queens[i] == j ? "Q " : ". ");
            }
            System.out.println(row.toString());
        }
        System.out.println();
    }
}
