import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class PascalTriangle {

    /**
     * Generates Pascal's Triangle up to the given number of rows.
     *
     * Each row is built based on the previous row:
     * - First and last elements of each row are always 1
     * - Middle elements are the sum of two adjacent elements from the previous row
     *
     * Time Complexity: O(numRows^2) – each element is computed once
     * Space Complexity: O(numRows^2) – storing all rows
     *
     * numRows Number of rows to generate
     * @return List of rows, each row is a list of integers
     */
    public List<List<Integer>> generate(int numRows) {
        // Initialize result list
        List<List<Integer>> result = new ArrayList<>();
        
        // Edge case: no rows requested
        if (numRows == 0) return result;

        // First row is always [1]
        result.add(new ArrayList<>(Arrays.asList(1)));
        
        // Build remaining rows
        for (int i = 1; i < numRows; i++) {
            List<Integer> prevRow = result.get(i - 1);  // Previous row
            List<Integer> currentRow = new ArrayList<>();

            // First element of each row is always 1
            currentRow.add(1);

            // Compute middle elements as sum of adjacent elements from previous row
            for (int j = 0; j < prevRow.size() - 1; j++) {
                currentRow.add(prevRow.get(j) + prevRow.get(j + 1));
            }

            // Last element of each row is always 1
            currentRow.add(1);

            // Add current row to result
            result.add(currentRow);
        }

        return result;
    }

    /**
     * Runnable example to test Pascal's Triangle generation.
     */
    public static void main(String[] args) {
        int numRows = 5;

        // Generate Pascal's Triangle
        List<List<Integer>> result = new PascalTriangle().generate(numRows);

        // Print the triangle
        System.out.println("Pascal's Triangle with " + numRows + " rows:");
        for (List<Integer> row : result) {
            System.out.println(row);
        }
    }
}
