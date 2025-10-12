/**
 * Jump Search Implementation in Java
 * 
 * Description:
 * This class demonstrates the Jump Search algorithm for searching an element
 * in a sorted array. Jump Search works by jumping ahead by fixed steps and
 * then performing linear search in the identified block.
 * 
 * Time Complexity: O(√n)
 * Space Complexity: O(1)
 */

public class JumpSearch {

    /**
     * Performs Jump Search on a sorted array.
     *
     * @param arr   Sorted array of integers
     * @param x     Element to search for
     * @return      Index of x if found; -1 otherwise
     */
    public static int jumpSearch(int[] arr, int x) {
        int n = arr.length;
        
        // Handle empty array
        if (n == 0) {
            return -1;
        }
        
        int step = (int)Math.floor(Math.sqrt(n)); // Optimal block size
        int prev = 0;

        // Finding the block where element may be present
        while (arr[Math.min(step, n)-1] < x) {
            prev = step;
            step += (int)Math.floor(Math.sqrt(n));
            if (prev >= n) {
                return -1; // Element not found
            }
        }

        // Linear search within the block
        for (int i = prev; i < Math.min(step, n); i++) {
            if (arr[i] == x) {
                return i;
            }
        }

        return -1; // Element not found
    }

    // ------------------------- MAIN METHOD -------------------------
    public static void main(String[] args) {
        int[] arr = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
        int x = 7;

        System.out.println("Jump Search Example\n");
        System.out.println("Array: ");
        for (int num : arr) {
            System.out.print(num + " ");
        }
        System.out.println("\nElement to search: " + x);

        int index = jumpSearch(arr, x);

        if (index != -1) {
            System.out.println("Element found at index: " + index);
        } else {
            System.out.println("Element not found in the array.");
        }
    }
}
