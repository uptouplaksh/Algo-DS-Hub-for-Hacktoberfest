"""
Selection Sort Algorithm in Python

Selection Sort works by repeatedly finding the minimum element
from the unsorted portion of the array and swapping it with
the first element of the unsorted portion.

-------------------------------------------------------------
Time Complexity:
    Best Case:    O(n^2)
    Average Case: O(n^2)
    Worst Case:   O(n^2)

    - Selection Sort always performs n*(n-1)/2 comparisons,
      regardless of the input order.

Space Complexity:
    O(1) – Sorting is done in-place with no extra data structures.

Stability:
    Not a stable sorting algorithm (relative order of equal
    elements may not be preserved).
-------------------------------------------------------------
"""

def selection_sort(arr):
    """
    Sorts an array in ascending order using Selection Sort.

    Args:
        arr (list): List of elements to be sorted.

    Returns:
        list: Sorted list.
    """
    n = len(arr)

    # Traverse through all array elements
    for i in range(n):
        min_index = i

        # Find the index of the minimum element in the remaining unsorted array
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the found minimum element with the first element of unsorted part
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


# Runnable example block
    # Example array
    def selection_sort(arr):
        """
        Sorts an array in ascending order using Selection Sort.

        Args:
            arr (list): List of elements to be sorted.

        Returns:
            list: Sorted list.
        """
        n = len(arr)

        # Traverse through all array elements
        for i in range(n):
            # Assume the current element is the minimum
            min_index = i

            # Find the index of the minimum element in the remaining unsorted array
            for j in range(i + 1, n):
                if arr[j] < arr[min_index]:
                    min_index = j

            # Swap the found minimum element with the first element of unsorted part
            arr[i], arr[min_index] = arr[min_index], arr[i]

        return arr


    # Runnable example block
    if __name__ == "__main__":
        # Example array
        example_array = [64, 25, 12, 22, 11]

        print("Original array:", example_array)

        sorted_array = selection_sort(example_array)

        print("Sorted array:", sorted_array)

    print("Original array:", example_array)

    sorted_array = selection_sort(example_array)

    print("Sorted array:", sorted_array)
