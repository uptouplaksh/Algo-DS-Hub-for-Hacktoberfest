"""
Binary Search Algorithm in Python

Time Complexity: O(log n)
Space Complexity: O(1)

This implementation assumes the input array is sorted in ascending order.
"""

def binary_search(arr, target):
    """
    Performs binary search on a sorted array.
    
    Parameters:
        arr (list): Sorted list of elements
        target : Element to search for
    
    Returns:
        int: Index of target in arr if found, else -1
    """
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2  # Prevents overflow in other languages
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1  # Target not found


# Example usage
if __name__ == "__main__":
    sorted_array = [1, 3, 5, 7, 9, 11, 13]
    target = 7
    result = binary_search(sorted_array, target)
    if result != -1:
        print(f"Element {target} found at index {result}")
    else:
        print(f"Element {target} not found in the array")
