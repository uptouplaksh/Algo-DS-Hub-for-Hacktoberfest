"""
Single Number Problem
---------------------
Given a non-empty array of integers where every element appears twice except for one,
find that single one.

Approach:
---------
We use the XOR (^) bitwise operator. XOR has the following useful properties:
1. x ^ 0 = x
2. x ^ x = 0
3. XOR is commutative and associative, meaning order doesn’t matter.

By XORing all numbers together, all duplicate pairs cancel out (x ^ x = 0),
and we are left with the single number.

Complexity:
-----------
Time Complexity:  O(n)  → We traverse the array once.
Space Complexity: O(1)  → Only a single variable is used.
"""

def single_number(nums):
    
    result = 0
    for num in nums:
        result ^= num  # XOR all numbers
    return result

# -------------------------------
# Example Usage (for testing)
# -------------------------------
if __name__ == "__main__":
    example_nums = [4, 1, 2, 1, 2]
    print("Input:", example_nums)
    print("Single number is:", single_number(example_nums))
    # Expected Output: 4
