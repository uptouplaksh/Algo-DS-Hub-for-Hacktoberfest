"""
Quick Sort Algorithm Implementation

Quick Sort is a highly efficient, comparison-based sorting algorithm that uses a divide-and-conquer strategy.
It works by selecting a 'pivot' element from the array and partitioning the other elements into two sub-arrays,
according to whether they are less than or greater than the pivot.

Time Complexity:
- Best Case: O(n log n)
- Average Case: O(n log n)
- Worst Case: O(n²) - occurs when the pivot is always the smallest or largest element

Space Complexity:
- O(log n) - due to the recursive call stack

Key Features:
- In-place sorting algorithm
- Unstable sort (doesn't preserve the relative order of equal elements)
- Efficient for large datasets
- Can be optimized for different types of input data
"""

def quick_sort(arr):
    """
    Sort an array using the Quick Sort algorithm.
    
    Args:
        arr (list): The input array to be sorted
        
    Returns:
        list: The sorted array
        
    Example:
        >>> arr = [64, 34, 25, 12, 22, 11, 90]
        >>> quick_sort(arr)
        [11, 12, 22, 25, 34, 64, 90]
    """
    # Base case: arrays of length 0 or 1 are already sorted
    if len(arr) <= 1:
        return arr
    
    # Choose the pivot (here we use the last element)
    pivot = arr[-1]
    left = []
    right = []
    
    # Partition elements into left and right subarrays
    for element in arr[:-1]:
        if element <= pivot:
            left.append(element)
        else:
            right.append(element)
    
    # Recursively sort the partitions and combine them
    return quick_sort(left) + [pivot] + quick_sort(right)


def quick_sort_in_place(arr, low, high):
    """
    In-place version of Quick Sort algorithm.
    
    Args:
        arr (list): The input array to be sorted
        low (int): Starting index of the partition
        high (int): Ending index of the partition
        
    Returns:
        None (sorts the array in-place)
        
    Example:
        >>> arr = [64, 34, 25, 12, 22, 11, 90]
        >>> quick_sort_in_place(arr, 0, len(arr)-1)
        >>> print(arr)
        [11, 12, 22, 25, 34, 64, 90]
    """
    def partition(arr, low, high):
        """Helper function to partition the array."""
        pivot = arr[high]
        i = low - 1
        
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1
    
    if low < high:
        # Find the partition index
        pi = partition(arr, low, high)
        
        # Recursively sort the left partition
        quick_sort_in_place(arr, low, pi - 1)
        # Recursively sort the right partition
        quick_sort_in_place(arr, pi + 1, high)


# Example usage and testing
if __name__ == "__main__":
    # Test the regular quick sort
    test_arr1 = [64, 34, 25, 12, 22, 11, 90]
    sorted_arr = quick_sort(test_arr1)
    print(f"Regular Quick Sort: {sorted_arr}")
    
    # Test the in-place quick sort
    test_arr2 = [64, 34, 25, 12, 22, 11, 90]
    quick_sort_in_place(test_arr2, 0, len(test_arr2)-1)
    print(f"In-place Quick Sort: {test_arr2}")