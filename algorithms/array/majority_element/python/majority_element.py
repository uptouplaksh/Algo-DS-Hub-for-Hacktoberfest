"""
Module: majority_element.py

Description:
    This module provides an efficient implementation of the Boyer-Moore Voting Algorithm
    to find the majority element in an array. The majority element is the element that 
    appears more than ⌊n / 2⌋ times.

Algorithm Steps:
    1. Phase 1 – Find a candidate element that could be the majority.
    2. Phase 2 – Verify that the candidate actually appears more than ⌊n / 2⌋ times.

Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List

class Solution:
    """
    A class to represent the Boyer-Moore Voting Algorithm implementation.
    """

    def majorityElement(self, nums: List[int]) -> int:
        """
        Finds the majority element in the list using the Boyer-Moore Voting Algorithm.

        Parameters:
            nums (List[int]): A list of integers.

        Returns:
            int or None: The majority element if it exists, otherwise None.
        """

        # ------------------------
        # Phase 1: Find Candidate
        # ------------------------
        candidate = None
        count = 0

        for num in nums:
            if count == 0:
                candidate = num  # Choose new candidate
            count += 1 if num == candidate else -1

        # ------------------------
        # Phase 2: Verify Candidate
        # ------------------------
        if candidate is not None and nums.count(candidate) > len(nums) // 2:
            return candidate
        else:
            return None  # No majority element found


# ------------------------
# Example Usage
# ------------------------
if __name__ == "__main__":
    solver = Solution()

    # Example 1: Has a majority element
    nums1 = [3, 2, 3]
    print("Input:", nums1)
    print("Majority Element:", solver.majorityElement(nums1))  # Expected Output: 3

    # Example 2: Has a majority element
    nums2 = [2, 2, 1, 1, 1, 2, 2]
    print("\nInput:", nums2)
    print("Majority Element:", solver.majorityElement(nums2))  # Expected Output: 2

    # Example 3: No majority element (edge case)
    nums3 = [1, 2, 3, 4]
    print("\nInput:", nums3)
    print("Majority Element:", solver.majorityElement(nums3))  # Expected Output: None

    print("Input array:", nums)
    majority = find_majority_element(nums)
    if majority is not None:
        print("Majority Element:", majority)
    else:
        print("No majority element found.")
