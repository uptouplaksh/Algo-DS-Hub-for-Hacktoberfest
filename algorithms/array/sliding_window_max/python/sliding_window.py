"""
sliding_window.py

This module provides a function to solve the Sliding Window Maximum problem.

Given an array of integers and a window size k, the goal is to find the maximum
value in each contiguous subarray of size k.

Algorithm Used:
    Deque (double-ended queue) for maintaining maximum in O(n) time.

Time Complexity: O(n)
Space Complexity: O(k)
"""

from collections import deque

def sliding_window_max(nums, k):
    if not nums or k <= 0:
        return []

    n = len(nums)
    result = []
    dq = deque()  # Store indices of potential max elements

    for i in range(n):
        # Remove indices that are out of the current window
        while dq and dq[0] < i - k + 1:
            dq.popleft()

        # Remove elements smaller than current from the deque
        while dq and nums[i] >= nums[dq[-1]]:
            dq.pop()

        dq.append(i)

        # Append current max to result starting from the first full window
        if i >= k - 1:
            result.append(nums[dq[0]])

    return result


# Example usage
if __name__ == "__main__":
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    print("Input array:", nums)
    print(f"Sliding window maximum (k={k}):", sliding_window_max(nums, k))
