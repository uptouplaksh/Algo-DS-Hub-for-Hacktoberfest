"""
Perform binary search (iterative version) on a sorted array.

Time Complexity: O(log n)
Space Complexity: O(1)
"""

def binary_search_iterative(arr, target):
    """
    Parameters:
        arr (list): A sorted list of elements.
        target:     The element to search for.

    Returns:
        int: The index of the target element if found, else -1.
    """
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


# Example usage
if __name__ == "__main__":
    array = [2, 3, 6, 8, 9, 11, 15]
    target = 11
    result = binary_search_iterative(array, target)
    if result != -1:
        print(f"Target {target} found at index: {result}")
    else:
        print(f"Target {target} not found in the array")
