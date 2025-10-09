"""
majority_element.py

This module provides a function to find the Majority Element in an array 
using the Boyer-Moore Voting Algorithm.

The majority element is the element that appears more than ⌊n / 2⌋ times.

Time Complexity: O(n)
Space Complexity: O(1)
"""

def find_majority_element(nums):
    candidate = None
    count = 0

    # Phase 1: Find the candidate
    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)

    # Phase 2: Verify if candidate is actually the majority element
    if nums.count(candidate) > len(nums) // 2:
        return candidate
    return None


# Example usage
if __name__ == "__main__":
    # Example array
    nums = [2, 2, 1, 1, 1, 2, 2]

    print("Input array:", nums)
    majority = find_majority_element(nums)
    if majority is not None:
        print("Majority Element:", majority)
    else:
        print("No majority element found.")
