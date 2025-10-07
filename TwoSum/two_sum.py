"""
Title: Two Sum Problem
Author: Tathagat Gaikwad
Contribution: Hacktoberfest 2025
Repository: https://github.com/uptouplaksh/Open-Source-DS-Algo
Description:
    Given an array of integers `nums` and an integer `target`,
    return indices of the two numbers such that they add up to the target.
"""

def two_sum(nums, target):
    """
    Solve the Two Sum problem in O(n) time using a hash map.

    Parameters:
        nums (List[int]): List of integers.
        target (int): Target sum.

    Returns:
        List[int]: Indices of the two numbers adding up to target.
    """
    num_map = {}  # Stores number -> index

    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i

    # If no solution found (as per problem, it always exists)
    return []

# Example usage
if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    result = two_sum(nums, target)
    print(f"Input: nums = {nums}, target = {target}")
    print(f"Output indices: {result}")
    print(f"Numbers: {nums[result[0]]} + {nums[result[1]]} = {target}")
