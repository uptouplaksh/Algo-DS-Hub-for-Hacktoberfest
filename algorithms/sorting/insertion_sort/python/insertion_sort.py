#
# Insertion Sort Algorithm in Python
#

# Time Complexity:
#   - Best Case: O(n) - When the array is already sorted.
#   - Average Case: O(n^2) - When the array is randomly ordered.
#   - Worst Case: O(n^2) - When the array is sorted in reverse.
#
# Space Complexity: O(1) - It's an in-place sorting algorithm.
#

def insertion_sort(arr):
    """
    Sorts an array using the Insertion Sort algorithm.
#
# Insertion Sort Algorithm in Python
#
# Time Complexity:
#   - Best Case: O(n) - When the array is already sorted.
#   - Average Case: O(n^2) - When the array is randomly ordered.
#   - Worst Case: O(n^2) - When the array is sorted in reverse.
#
# Space Complexity: O(1) - It's an in-place sorting algorithm.
#

def insertion_sort(arr):
    """
    Sorts an array using the Insertion Sort algorithm.

    Args:
        arr: A list of comparable elements.

    Returns:
        The sorted list.
    """
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]

        # Move elements of arr[0..i-1], that are greater than key,
        # to one position ahead of their current position
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


# Example Usage:
if __name__ == "__main__":
    sample_array = [12, 11, 13, 5, 6]
    print("Unsorted array:", sample_array)
    sorted_array = insertion_sort(sample_array.copy())
    print("Sorted array:  ", sorted_array)