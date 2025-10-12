// Quick Sort Algorithm
// Pivot & Partition Method
/*
Problem Statement-> Sort an integer array in ascending order using the QuickSort algorithm.
Approach ->
- Algorithm Used: QuickSort (Divide and Conquer)
- Partitioning Strategy: Last element as pivot
- Steps:
  1. Select the last element as pivot.
  2. Rearrange elements so smaller elements are on the left, greater elements on the right.
  3. Recursively apply QuickSort to left and right subarrays.

 */

public class QuickSort {
    public static int partition(int arr[], int low, int high) {  
        int pivot = arr[high];
        int i = low - 1;

        for (int j = low; j < high; j++) {
            if (arr[j] < pivot) {
                i++;
                // Swap
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }
        i++;
        int temp = arr[i];
        arr[i] = pivot;
        arr[high] = temp;
        return i; // pivot index
    }

    public static void quickSort(int arr[], int low, int high) {
        if (low < high) {
            int pivotIdx = partition(arr, low, high);
            quickSort(arr, low, pivotIdx - 1);
            quickSort(arr, pivotIdx + 1, high);
        }
    }

    public static void main(String[] args) {
        int[] arr = {6, 3, 9, 5, 2, 8};
        int n = arr.length;
        quickSort(arr, 0, n - 1);

        // Print sorted array
        for (int i = 0; i < n; i++) {
            System.out.print(arr[i] + " ");
        }
        System.out.println();
    }
}
//output-> 2 3 5 6 8 9

/*
-Time Complexity:
  - Best/Average Case: O(n log n)
  - Worst Case: O(n²) (already sorted or reverse sorted array)
-Space Complexity: O(log n) due to recursion stack
-Stable: No
 */
