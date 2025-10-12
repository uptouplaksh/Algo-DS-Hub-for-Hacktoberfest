"""
rotate_array.py

This module provides a function to solve the "Rotate Array" problem in-place
using the three-reversal algorithm.

Time Complexity: O(n), where n is the number of elements in the array.
- The array is reversed three times, each taking O(n) time.

Space Complexity: O(1)
- The rotation is performed in-place with constant extra space.
"""


def rotate_array(nums, k):
    """
    Rotates the array `nums` to the right by `k` steps in-place.

    Args:
        nums (list[int]): The array to rotate.
        k (int): The number of positions to rotate the array.
    """
    if not nums:
        return

    n = len(nums)
    # If k is larger than the length of the array, handle the wraparound
    k = k % n

    # Helper function to reverse a portion of the array
    def reverse(start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    # Step 1: Reverse the entire array
    reverse(0, n - 1)

    # Step 2: Reverse the first k elements
    reverse(0, k - 1)

    # Step 3: Reverse the remaining n-k elements
    reverse(k, n - 1)


# --- Runnable Example Block ---
if __name__ == "__main__":
    # Example array and rotation step
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3

    print("Original array:", nums)
    rotate_array(nums, k)
    print(f"Array after rotating {k} steps:", nums)
    # Expected: [5, 6, 7, 1, 2, 3, 4]
