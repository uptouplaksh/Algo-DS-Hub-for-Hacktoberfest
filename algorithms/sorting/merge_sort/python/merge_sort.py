"""
Merge Sort Algorithm Implementation

Time Complexity: O(n log n)
Space Complexity: O(n)
"""


def merge_sort(arr):
    """
    Sorts an array using the merge sort algorithm.
    
    Args:
        arr: List of comparable elements to be sorted
        
    Returns:
        Sorted list in ascending order
    """
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)


def merge(left, right):
    """
    Merges two sorted arrays into a single sorted array.
    
    Args:
        left: First sorted list
        right: Second sorted list
        
    Returns:
        Merged sorted list
    """
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result
