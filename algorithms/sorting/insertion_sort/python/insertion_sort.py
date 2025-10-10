"""Insertion sort implementation."""

def insertion_sort(arr):
    """Sort a list in-place using insertion sort and return it.

    Args:
        arr (list): List of comparable elements.

    Returns:
        list: The same list object, sorted in non-decreasing order.
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr