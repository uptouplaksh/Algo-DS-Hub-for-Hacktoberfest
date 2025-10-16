/**
 * Heap Sort Implementation in Java
 *
 * Description:
 * This module provides a Java implementation of the Heap Sort algorithm,
 * which is a comparison-based sorting algorithm using a Binary Heap data structure.
 * It sorts an array in ascending order by first building a max heap and then
 * repeatedly extracting the maximum element and placing it at the end of the array.
 *
 * Time Complexity:
 * - O(n log n) for all cases (best, average, worst)
 * Space Complexity:
 * - O(1) (in-place sorting)
 *
 */

public class HeapSort {

    // Function to heapify a subtree rooted at index i
    private static void heapify(int[] arr, int n, int i) {
        int largest = i;       // Initialize largest as root
        int left = 2 * i + 1;  // left child index
        int right = 2 * i + 2; // right child index

        // If left child exists and is greater than root
        if (left < n && arr[left] > arr[largest]) {
            largest = left;
        }

        // If right child exists and is greater than current largest
        if (right < n && arr[right] > arr[largest]) {
            largest = right;
        }

        // If largest is not root, swap and continue heapifying
        if (largest != i) {
            int swap = arr[i];
            arr[i] = arr[largest];
            arr[largest] = swap;

            // Recursively heapify the affected subtree
            heapify(arr, n, largest);
        }
    }

    // Main function to perform Heap Sort
    public static void heapSort(int[] arr) {
        int n = arr.length;

        // Build max heap
        for (int i = n / 2 - 1; i >= 0; i--) {
            heapify(arr, n, i);
        }

        // Extract elements from heap one by one
        for (int i = n - 1; i >= 0; i--) {
            // Move current root (largest) to end
            int temp = arr[0];
            arr[0] = arr[i];
            arr[i] = temp;

            // Call heapify on the reduced heap
            heapify(arr, i, 0);
        }
    }

    // -------------------------------------------------------------
    // Example usage (runnable block)
    // -------------------------------------------------------------
    public static void main(String[] args) {
        int[] arr = {12, 11, 13, 5, 6, 7};

        System.out.println("Original Array:");
        for (int num : arr) {
            System.out.print(num + " ");
        }
        System.out.println();

        heapSort(arr);

        System.out.println("Sorted Array:");
        for (int num : arr) {
            System.out.print(num + " ");
        }
        System.out.println();
    }
}

/*
Expected Output:
Original Array:
12 11 13 5 6 7
Sorted Array:
5 6 7 11 12 13
*/
