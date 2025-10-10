/**
 * Quick Sort - JavaScript Implementation
 *
 * Description:
 * This module provides a recursive implementation of the Quick Sort algorithm,
 * an efficient divide-and-conquer sorting algorithm.
 *
 * Approach:
 * - Choose a pivot element (here, we use the last element of the subarray).
 * - Partition the array such that elements smaller than the pivot are on the left,
 *   and elements greater than the pivot are on the right.
 * - Recursively apply Quick Sort to the left and right subarrays.
 *
 * Time Complexity:
 * - Best/Average Case: O(n log n)
 * - Worst Case: O(n^2) (occurs when the pivot selection is poor, e.g., already sorted array)
 * Space Complexity:
 * - O(log n) due to recursive call stack
 */

function quickSort(arr, low = 0, high = arr.length - 1) {
  if (low < high) {
    // Partition the array and get the pivot index
    const pivotIndex = partition(arr, low, high);

    // Recursively sort elements before and after partition
    quickSort(arr, low, pivotIndex - 1);
    quickSort(arr, pivotIndex + 1, high);
  }
  return arr;
}

// Helper function to partition the array
function partition(arr, low, high) {
  const pivot = arr[high]; // Choose the last element as pivot
  let i = low - 1;         // Index of smaller element

  for (let j = low; j < high; j++) {
    if (arr[j] <= pivot) {
      i++;
      [arr[i], arr[j]] = [arr[j], arr[i]]; // Swap elements
    }
  }

  // Place pivot in correct position
  [arr[i + 1], arr[high]] = [arr[high], arr[i + 1]];
  return i + 1;
}

// -------------------------------------------------------------
// Example usage (runnable block)
// -------------------------------------------------------------
if (require.main === module) {
  const array = [10, 7, 8, 9, 1, 5];

  console.log("Original Array:", array);

  const sortedArray = quickSort(array);

  console.log("Sorted Array:", sortedArray);
}

/*
Expected Output:
Original Array: [10, 7, 8, 9, 1, 5]
Sorted Array: [1, 5, 7, 8, 9, 10]
*/
