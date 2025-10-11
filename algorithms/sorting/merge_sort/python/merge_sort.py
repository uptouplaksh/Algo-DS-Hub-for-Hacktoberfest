"""
Merge Sort Algorithm Implementation

Description:
Merge Sort is an efficient, stable, comparison-based,
divide-and-conquer sorting algorithm. It works by recursively
dividing the unsorted list into n sub-lists, each containing
one element, and then repeatedly merging the sub-lists to
produce new sorted sub-lists until there is only one remaining.

Time Complexity: O(n log n) in all cases (best, average, worst)
Space Complexity: O(n) - requires additional space for temporary arrays

Author: Kartikeya Nainkhwal
"""


def merge_sort(arr):
    """
    Sorts an array using merge sort (divide-and-conquer approach).

    Args:
        arr (list): The list of comparable elements to be sorted

    Returns:
        list: A new sorted list in ascending order
    """
    # Base case: if array has 1 or 0 elements, it's already sorted
    if len(arr) <= 1:
        return arr

    # DIVIDE: Split the array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursively sort both halves
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    # CONQUER: Merge the sorted halves
    return merge(left_sorted, right_sorted)


def merge(left, right):
    """
    Merges two sorted arrays into a single sorted array.

    Args:
        left (list): First sorted sub-array
        right (list): Second sorted sub-array

    Returns:
        list: Merged sorted array with all elements from both inputs
    """
    result = []
    i = j = 0

    # Compare elements from left and right, add smaller to result
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Add any remaining elements from left array
    while i < len(left):
        result.append(left[i])
        i += 1

    # Add any remaining elements from right array
    while j < len(right):
        result.append(right[j])
        j += 1

    return result


if __name__ == "__main__":
    # Example usage with a sample unsorted array
    unsorted_array = [38, 27, 43, 3, 9, 82, 10]

    print("Original Array:", unsorted_array)
    sorted_array = merge_sort(unsorted_array)
    print("Sorted Array:  ", sorted_array)

    # Additional test cases
    print("\n--- Additional Test Cases ---")

    # Test with already sorted array
    sorted_test = [1, 2, 3, 4, 5]
    print(f"Sorted input:    {sorted_test} -> {merge_sort(sorted_test)}")

    # Test with reverse sorted array
    reverse_test = [5, 4, 3, 2, 1]
    print(f"Reverse input:   {reverse_test} -> {merge_sort(reverse_test)}")

    # Test with duplicates
    duplicates_test = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    print(f"With duplicates: {duplicates_test} -> " f"{merge_sort(duplicates_test)}")

    # Test with single element
    single_test = [42]
    print(f"Single element:  {single_test} -> {merge_sort(single_test)}")

    # Test with empty array
    empty_test = []
    print(f"Empty array:     {empty_test} -> {merge_sort(empty_test)}")
