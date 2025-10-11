"""
Product of Array Except Self

This module provides a function to solve the "Product of Array Except Self"
problem without using division and in O(n) time.

Time Complexity: O(n)
- The array is traversed three times in separate, non-nested loops.

Space Complexity: O(n)
- Two additional arrays of size n are used to store prefix and suffix products.
"""

def product_except_self(nums):
    """
    Given an array of integers, returns an array where the output at each index
    is the product of all elements of the original array except the one at that index.

    Args:
        nums (list[int]): List of integers.

    Returns:
        list[int]: List of products.
    """
    n = len(nums)
    if n == 0:
        return []

    # Step 1: Create arrays for left and right products
    left_products = [1] * n
    right_products = [1] * n
    result = [1] * n

    # Step 2: Populate the left_products array
    for i in range(1, n):
        left_products[i] = left_products[i - 1] * nums[i - 1]

    # Step 3: Populate the right_products array in reverse
    for i in range(n - 2, -1, -1):
        right_products[i] = right_products[i + 1] * nums[i + 1]

    # Step 4: Construct the result array
    for i in range(n):
        result[i] = left_products[i] * right_products[i]

    return result

# Example usage
if __name__ == "__main__":
    nums = [1, 2, 3, 4]
    print("Input:", nums)
    print("Product Except Self:", product_except_self(nums)) # Expected: [24, 12, 8, 6]
