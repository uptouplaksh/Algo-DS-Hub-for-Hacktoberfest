"""
Shell Sort Algorithm (Python Implementation)
---------------------------------------------
Shell Sort is an in-place comparison sort and an extension of insertion sort
that allows the exchange of items that are far apart.

Time Complexity:
    Best Case: O(n log n)
    Average Case: O((n log n)^2)
    Worst Case: O(n^2)
Space Complexity: O(1)
Stable: No
"""

def shell_sort(arr):
    """
    Sorts a list using Shell Sort algorithm.

    Parameters:
        arr (list): The list to be sorted.

    Returns:
        None: The list is sorted in place.
    """
    n = len(arr)
    gap = n // 2  # Initial gap size

    # Start with a big gap, then reduce it
    while gap > 0:
        # Perform a gapped insertion sort
        for i in range(gap, n):
            temp = arr[i]
            j = i
            # Shift earlier gap-sorted elements up until correct position found
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        # Reduce the gap for next iteration
        gap //= 2


if __name__ == "__main__":
    # Example usage
    arr = [12, 34, 54, 2, 3]
    print("Unsorted array:", arr)
    shell_sort(arr)
    print("Sorted array:  ", arr)
