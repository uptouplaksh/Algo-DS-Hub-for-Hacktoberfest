package algorithms.sorting.bubble_sort.java;

import java.util.Arrays; // Needed for printing the array easily

/**
 * Implements the Bubble Sort algorithm in Java.
 *
 * Bubble Sort is a simple sorting algorithm that repeatedly steps through the list,
 * compares adjacent elements and swaps them if they are in the wrong order.
 * The pass through the list is repeated until no swaps are needed, which indicates
 * that the list is sorted.
 *
 * Time Complexity: O(n^2) in average and worst cases.
 * Space Complexity: O(1)
 */
public class BubbleSort {

    /**
     * Sorts an integer array using the Bubble Sort algorithm.
     *
     * @param arr The array of integers to be sorted.
     */
    public void sort(int[] arr) {
        int n = arr.length;
        boolean swapped; // Flag to optimize: if no elements were swapped in an inner loop, the array is sorted.

        // Outer loop for passes
        for (int i = 0; i < n - 1; i++) {
            swapped = false; // Reset swapped flag for each pass

            // Inner loop for comparisons and swaps
            // The largest element "bubbles up" to its correct position in each pass,
            // so we don't need to check the last 'i' elements in subsequent passes.
            for (int j = 0; j < n - 1 - i; j++) {
                // Compare adjacent elements
                if (arr[j] > arr[j + 1]) {
                    // Swap arr[j] and arr[j+1]
                    int temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                    swapped = true; // Mark that a swap occurred
                }
            }

            // If no two elements were swapped by inner loop, then break
            // because the array is already sorted.
            if (!swapped) {
                break;
            }
        }
    }

    /**
     * Main method to demonstrate the Bubble Sort algorithm.
     * This acts as an example of how to use the sort method.
     * @param args Command line arguments (not used here).
     */
    public static void main(String[] args) {
        // Create an instance of BubbleSort
        BubbleSort sorter = new BubbleSort();

        // Test array 1
        int[] arr1 = {64, 34, 25, 12, 22, 11, 90};
        System.out.println("Original array 1: " + Arrays.toString(arr1));
        sorter.sort(arr1); // Sort the array
        System.out.println("Sorted array 1: " + Arrays.toString(arr1)); // Print sorted array

        System.out.println("\n----------------------------------\n");

        // Test array 2
        int[] arr2 = {5, 1, 4, 2, 8};
        System.out.println("Original array 2: " + Arrays.toString(arr2));
        sorter.sort(arr2);
        System.out.println("Sorted array 2: " + Arrays.toString(arr2));

        System.out.println("\n----------------------------------\n");

        // Test already sorted array
        int[] arr3 = {1, 2, 3, 4, 5};
        System.out.println("Original array 3 (already sorted): " + Arrays.toString(arr3));
        sorter.sort(arr3);
        System.out.println("Sorted array 3: " + Arrays.toString(arr3));
    }
}