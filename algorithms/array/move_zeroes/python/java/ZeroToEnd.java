import java.util.Arrays;

/**
 * Moves all zeros in an array to the end while maintaining the relative order of non-zero elements.
 * This implementation uses the two-pointer approach for optimal in-place modification.
 *
 * Time Complexity: O(n) – single pass through the array
 * Space Complexity: O(1) – in-place swap, no extra array
 */
class Solution {

    /**
     * Moves zeros to the end of the given array.
     *
     *  nums Input array of integers
     */
    public void moveZeroes(int[] nums) {
        int i = 0; // Pointer for the position to place the next non-zero element

        // Iterate through the array
        for (int j = 0; j < nums.length; j++) {
            if (nums[j] != 0) {
                swap(nums, i, j); // Swap non-zero element to the correct position
                i++;
            }
        }

        // Print the final array (optional)
        System.out.println("Array after moving zeros to the end: " + Arrays.toString(nums));
    }

    /**
     * Helper method to swap two elements in the array
     */
    private void swap(int[] arr, int i, int j) {
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }
}

/**
 * Runnable example to test moveZeroes method
 */
public class ZeroToEnd {

    public static void main(String[] args) {
        int[] arr = {10, 0, 20, 0};

        // Move zeros to the end
        new Solution().moveZeroes(arr);
    }
}
