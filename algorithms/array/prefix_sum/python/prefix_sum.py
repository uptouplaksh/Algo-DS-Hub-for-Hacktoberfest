"""
Prefix Sum Array Implementation

Time Complexity: O(n) for building, O(1) for queries
Space Complexity: O(n)

"""


def build_prefix_sum(arr):
    """
    build a prefix sum array from the input array.
    
    the prefix sum array at index i contains the sum of all elements
    from index 0 to i in the original array.
    
    Args:
        arr (list): input array of integers
    
    Returns:
        list: prefix sum array
    
    Example:
        >>> build_prefix_sum([1, 2, 3, 4, 5])
        [1, 3, 6, 10, 15]
    
    Time Complexity: O(n) where n is the length of input array
    Space Complexity: O(n) for the prefix sum array
    """
    if not arr:
        return []
    
    prefix_sum = [0] * len(arr)
    prefix_sum[0] = arr[0]
    
    # Build prefix sum array
    for i in range(1, len(arr)):
        prefix_sum[i] = prefix_sum[i - 1] + arr[i]
    
    return prefix_sum


def range_sum(prefix_sum, left, right):
    """
    Calculate sum of elements in range [left, right] using prefix sum array.
    
    Uses the formula: sum[left:right+1] = prefix[right] - prefix[left-1]
    
    Args:
        prefix_sum (list): Prefix sum array
        left (int): Starting index (inclusive)
        right (int): Ending index (inclusive)
    
    Returns:
        int: Sum of elements in range [left, right]
    
    Example:
        >>> prefix = [1, 3, 6, 10, 15]  # From [1, 2, 3, 4, 5]
        >>> range_sum(prefix, 1, 3)  # Sum of elements at indices 1,2,3
        9  # (2 + 3 + 4)
    
    Time Complexity: O(1) - constant time query
    Space Complexity: O(1) - no extra space needed
    """
    if not prefix_sum or left > right or right >= len(prefix_sum):
        return 0
    
    # If range starts at 0, return prefix_sum[right]
    if left == 0:
        return prefix_sum[right]
    
    # Otherwise, subtract prefix_sum[left-1] from prefix_sum[right]
    return prefix_sum[right] - prefix_sum[left - 1]


def main():
    """demonstrate prefix sum array with examples"""
    
    print("=" * 50)
    print("prefix sum array - examples")
    print("=" * 50)
    
    # Example 1: Basic usage
    print("\nexample 1: basic array")
    arr1 = [1, 2, 3, 4, 5]
    prefix1 = build_prefix_sum(arr1)
    print(f"original array: {arr1}")
    print(f"prefix sum array: {prefix1}")
    print(f"sum of range [0, 2]: {range_sum(prefix1, 0, 2)}")  # 1+2+3 = 6
    print(f"sum of range [1, 3]: {range_sum(prefix1, 1, 3)}")  # 2+3+4 = 9
    print(f"sum of range [2, 4]: {range_sum(prefix1, 2, 4)}")  # 3+4+5 = 12
    
    # Example 2: Array with negative numbers
    print("\nexample 2: array with negatives")
    arr2 = [10, -5, 3, -2, 8]
    prefix2 = build_prefix_sum(arr2)
    print(f"original array: {arr2}")
    print(f"prefix sum array: {prefix2}")
    print(f"sum of range [0, 4]: {range_sum(prefix2, 0, 4)}")
    print(f"sum of range [1, 3]: {range_sum(prefix2, 1, 3)}")
    
    # Example 3: Single element
    print("\nexample 3: single element")
    arr3 = [42]
    prefix3 = build_prefix_sum(arr3)
    print(f"original array: {arr3}")
    print(f"prefix sum array: {prefix3}")
    print(f"sum of range [0, 0]: {range_sum(prefix3, 0, 0)}")
    
    # Example 4: Multiple queries
    print("\nexample 4: multiple range queries")
    arr4 = [2, 4, 6, 8, 10, 12]
    prefix4 = build_prefix_sum(arr4)
    print(f"original array: {arr4}")
    print(f"prefix sum array: {prefix4}")
    queries = [(0, 2), (1, 4), (3, 5), (0, 5)]
    for left, right in queries:
        result = range_sum(prefix4, left, right)
        print(f"sum of range [{left}, {right}]: {result}")
    
    # Example 5: Empty array
    print("\nexample 5: edge case - empty array")
    arr5 = []
    prefix5 = build_prefix_sum(arr5)
    print(f"original array: {arr5}")
    print(f"prefix sum array: {prefix5}")
    
    print("\n" + "=" * 50)
    print("complexity analysis:")
    print("- build prefix sum: O(n)")
    print("- range query: O(1)")
    print("- space: O(n)")
    print("=" * 50)


if __name__ == "__main__":
    main()
