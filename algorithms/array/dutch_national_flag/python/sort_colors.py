"""
sort_colors.py

This module provides a function to solve the Dutch National Flag Problem.

Given an array containing only 0s, 1s, and 2s, the goal is to sort the array
in-place such that all 0s come first, followed by all 1s, then all 2s.

Algorithm Used:
    Dutch National Flag Algorithm (Three-pointer approach)

Time Complexity: O(n)
Space Complexity: O(1)
"""

def sort_colors(nums):
    """
    Sorts an array containing only 0s, 1s, and 2s in-place using the
    Dutch National Flag algorithm.

    Args:
        nums (list[int]): The list of numbers to be sorted. It is modified in-place.
    """
    low, mid, high = 0, 0, len(nums) - 1

    # Traverse the list and arrange elements in a single pass
    while mid <= high:
        if nums[mid] == 0:
            # Swap 0 to the beginning
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            # Leave 1 in the middle
            mid += 1
        else:  # nums[mid] == 2
            # Swap 2 to the end
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1


# Example usage
if __name__ == "__main__":
    nums = [2, 0, 2, 1, 1, 0]
    print("Before sorting:", nums)
    sort_colors(nums)
    print("After sorting: ", nums)
