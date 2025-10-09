package algorithms.sorting.insertion_sort.java;
/*
 * insertion_sort.java
 * File location: /algorithms/sorting/insertion_sort/java/insertion_sort.java
 *
 * Insertion Sort implementation (ascending order)
 *
 * Time Complexity:
 *   Best case:    O(n)   - when the array is already sorted (only one comparison per element)
 *   Average case: O(n^2)
 *   Worst case:   O(n^2) - when array is sorted in reverse order
 *
 * Space Complexity: O(1) - in-place sorting (constant extra space)
 * Stable: Yes
 *
 * Description:
 *   Insertion sort builds the final sorted array one element at a time. For every
 *   index i (starting from 1) it removes the element at i (the "key") and inserts it
 *   into the correct position among the elements to its left (which are already sorted),
 *   by shifting larger elements to the right.
 */

public class insertion_sort {

    /**
     * Sorts the given integer array in ascending order using insertion sort.
     * This implementation modifies the array in-place.
     *
     * @param arr the array to sort. If null or length &lt; 2, the method returns immediately.
     */
    public static void insertionSort(int[] arr) {
        if (arr == null || arr.length < 2) {
            // Nothing to sort for null or single-element arrays
            return;
        }

        int n = arr.length;

        // Iterate from the second element to the end
        for (int i = 1; i < n; i++) {
            int key = arr[i]; // The element we want to insert into the sorted left side
            int j = i - 1;

            // Shift elements of arr[0..i-1], that are greater than key, to one position ahead
            // of their current position. This makes room to insert 'key' in the correct spot.
            while (j >= 0 && arr[j] > key) {
                arr[j + 1] = arr[j];
                j--;
            }

            // Place key at the position after the last element greater than it.
            arr[j + 1] = key;
        }
    }

    /**
     * Utility method to print an array to stdout in a single line.
     */
    public static void printArray(int[] arr) {
        if (arr == null) {
            System.out.println("null");
            return;
        }
        for (int i = 0; i < arr.length; i++) {
            if (i > 0) System.out.print(" ");
            System.out.print(arr[i]);
        }
        System.out.println();
    }

    /**
     * Small demo of insertion sort. You can modify the sample array to test other cases.
     */
    public static void main(String[] args) {
        int[] arr = {12, 11, 13, 5, 6};

        System.out.println("Original array:");
        printArray(arr);

        insertionSort(arr);

        System.out.println("Sorted array:");
        printArray(arr);
    }
}
