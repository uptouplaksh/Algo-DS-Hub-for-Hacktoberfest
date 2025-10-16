#
# Missing Number Finder in Python
#

# Time Complexity:
#   - Best Case: O(n)
#   - Average Case: O(n)
#   - Worst Case: O(n)
#   We traverse the array once to compute the sum, so it’s linear time.
#
# Space Complexity: O(1)
#   - Only a few extra variables are used, making it constant space.
#

def find_missing_number(nums):
    """
    Finds the missing number from an array containing n distinct numbers 
    taken from 0, 1, 2, ..., n.

    Args:
        nums (list[int]): List of n distinct integers from the range [0, n].

    Returns:
        int: The missing number.
    """

    # Formula for the sum of first n natural numbers: n * (n + 1) / 2
    n = len(nums)
    expected_sum = n * (n + 1) // 2

    # Actual sum of all elements in the given array
    actual_sum = sum(nums)

    # The difference gives the missing number
    return expected_sum - actual_sum


# Example Usage:
if __name__ == "__main__":
    sample_array = [3, 0, 5, 2, 1]
    print("Array:", sample_array)
    missing = find_missing_number(sample_array)
    print("Missing Number:", missing)
