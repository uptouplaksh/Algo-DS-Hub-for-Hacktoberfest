#
# Bubble Sort Algorithm in Python
#

# Time Complexity:
#   - Best Case: O(n) - When the array is already sorted.
#   - Average Case: O(n^2) - When the array is randomly ordered.
#   - Worst Case: O(n^2) - When the array is sorted in reverse.
#
# Space Complexity: O(1) - It's an in-place sorting algorithm.
#

def bubble_sort(arr):
    """
    Sorts an array using the Bubble Sort algorithm.

    Args:
        arr: A list of comparable elements.

    Returns:
        The sorted list.
    """
    n = len(arr)

    # Traverse through all array elements
    for i in range(n):
        # A flag to optimize the sort. If no swaps occur in a pass, the array is sorted.
        swapped = False

        # Last i elements are already in place, so we don't need to check them
        for j in range(0, n - i - 1):
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # If no two elements were swapped by inner loop, then break
        if not swapped:
            break
    return arr

# Example Usage:
if __name__ == "__main__":
    sample_array = [64, 34, 25, 12, 22, 11, 90]
    print("Unsorted array:", sample_array)
    sorted_array = bubble_sort(sample_array.copy()) # Use copy to keep original intact
    print("Sorted array:  ", sorted_array)