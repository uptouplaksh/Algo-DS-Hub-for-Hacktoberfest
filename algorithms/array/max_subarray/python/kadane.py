#
# Kadane's Algorithm in Python
#

# Time Complexity:
#   - Best Case: O(n)
#   - Average Case: O(n)
#   - Worst Case: O(n)
#   Kadane’s algorithm always runs in linear time since it scans the array once.
#
# Space Complexity: O(1)
#   - Only a few extra variables are used, making it a constant space algorithm.
#

def kadane(arr):
    """
    Finds the maximum sum of a contiguous subarray using Kadane's Algorithm.

    Args:
        arr (list[int]): A list of integers (positive, negative, or zero).

    Returns:
        int: The maximum subarray sum.
    """

       # Handle empty array edge case
       # The sum of an empty subarray is 0
    if not arr:
        return 0 
    
    # Initialize max_current and max_global with the first element
    max_current = max_global = arr[0]

    # Traverse the array from the second element onward
    for x in arr[1:]:
        # Either extend the current subarray or start a new subarray at x
        max_current = max(x, max_current + x)

        # Update the global maximum if current sum is greater
        if max_current > max_global:
            max_global = max_current

    return max_global


# Example Usage:
if __name__ == "__main__":
    sample_array = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print("Array:", sample_array)
    max_sum = kadane(sample_array)
    print("Maximum Subarray Sum:", max_sum)
