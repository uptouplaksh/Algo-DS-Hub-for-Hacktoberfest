def product_except_self(nums):
    """
    Given an array of integers, return an array such that the output at each index is the product of all 
    elements of the original array except the one at that index. The solution must not use division and 
    must run in O(n) time.

    Parameters:
    nums (list): List of integers.

    Returns:
    list: List of products of all elements except the one at each index.

    Time Complexity: O(n)
        - The array is traversed three times: once for left products, once for right products, and once
          to construct the result array.

    Space Complexity: O(n)
        - Additional space is used for the left_products, right_products, and result arrays, each of size n.
    """
    n = len(nums)

    # Step 1: Create two arrays to hold the products from left and right
    left_products = [1] * n
    right_products = [1] * n
    result = [1] * n

    # Step 2: Populate the left_products array
    for i in range(1, n):
        left_products[i] = left_products[i - 1] * nums[i - 1]

    # Step 3: Populate the right_products array in reverse order
    for i in range(n - 2, -1, -1):
        right_products[i] = right_products[i + 1] * nums[i + 1]

    # Step 4: Populate the result array by multiplying corresponding left and right products
    for i in range(n):
        result[i] = left_products[i] * right_products[i]

    return result

# Example usage
if __name__ == "__main__":
    # Test case
    nums = [1, 2, 3, 4]
    print("Input:", nums)
    print("Product Except Self:", product_except_self(nums))
