# rotate_array.py

def rotate_array(nums, k):
    """
    Rotates the array `nums` to the right by `k` steps in-place.
    
    Parameters:
        nums (List[int]): The array to rotate.
        k (int): The number of positions to rotate the array.
    
    Returns:
        None: The array is modified in place.
    
    Time Complexity:
        O(n) where n is the number of elements in the array. This is because we are
        performing a series of operations that each take linear time.
    
    Space Complexity:
        O(1) because the solution uses constant extra space (in-place rotation).
    """
    
    # If k is larger than the length of the array, we can take advantage of modulo
    k = k % len(nums)
    
    # Helper function to reverse a portion of the array
    def reverse(start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
    
    # Reverse the entire array
    reverse(0, len(nums) - 1)
    
    # Reverse the first k elements
    reverse(0, k - 1)
    
    # Reverse the remaining elements
    reverse(k, len(nums) - 1)

# Example block for running the function
if __name__ == "__main__":
    # Example array and rotation step
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    
    print("Original array:", nums)
    
    rotate_array(nums, k)
    
    print("Array after rotating {} steps:".format(k), nums)
