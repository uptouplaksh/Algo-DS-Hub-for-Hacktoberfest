/**
 * Binary Search (Recursive) - JavaScript Implementation
 *
 * Description:
 * This module provides a recursive implementation of the Binary Search algorithm
 * for sorted arrays. It returns the index of the target element if found, or -1 if not found.
 *
 * Approach:
 * - Binary Search works by repeatedly dividing the search interval in half.
 * - Check the middle element:
 *     * If it matches the target, return its index.
 *     * If target < middle, recursively search the left subarray.
 *     * If target > middle, recursively search the right subarray.
 *
 * Time Complexity:
 * - O(log n) — each recursive call halves the search interval
 * Space Complexity:
 * - O(log n) — due to recursive call stack
 */

function binarySearchRecursive(arr, target, left = 0, right = arr.length - 1) {
  if (left > right) {
    return -1; // Base case: target not found
  }

  const mid = Math.floor((left + right) / 2);

  if (arr[mid] === target) {
    return mid; // Target found
  } else if (arr[mid] > target) {
    // Search in the left subarray
    return binarySearchRecursive(arr, target, left, mid - 1);
  } else {
    // Search in the right subarray
    return binarySearchRecursive(arr, target, mid + 1, right);
  }
}

// -------------------------------------------------------------
// Example usage (runnable block)
// -------------------------------------------------------------
if (require.main === module) {
  const sortedArray = [1, 3, 5, 7, 9, 11, 13];
  const target = 7;

  const index = binarySearchRecursive(sortedArray, target);

  console.log("Sorted Array:", sortedArray);
  console.log("Target:", target);
  console.log("Index of Target:", index);
}

/*
Expected Output:
Sorted Array: [1, 3, 5, 7, 9, 11, 13]
Target: 7
Index of Target: 3
*/
