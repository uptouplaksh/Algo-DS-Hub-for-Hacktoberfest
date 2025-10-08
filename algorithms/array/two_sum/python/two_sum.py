"""
# Time Complexity: O(n)
- We iterate through the list of n elements only once. Each lookup and
- insertion in the hash map takes constant time on average, O(1).

# Space Complexity: O(n)
- In the worst-case scenario, we might store all n elements in the
- hash map if the solution pair is found at the very end or not at all.
"""



def two_sum(nums, target):
    """
    Finds two numbers in a list that add up to a specific target.

    This function uses a hash map to achieve an optimal time complexity.
    It iterates through the list, and for each element, it checks if the
    complement (target - current element) is already in the hash map.
    """
    
    # Create a hash map to store numbers we've seen and their indices.
    # Key: number, Value: index
    num_map = {}

    # Iterate through the list with both index and value.
    for i, num in enumerate(nums):
        # Calculate the complement needed to reach the target.
        complement = target - num

        # Check if the complement exists in our hash map.
        if complement in num_map:
            # If it exists, we found our pair.
            # Return the index of the complement and the current index.
            return [num_map[complement], i]
        
        # If the complement is not found, add the current number and its
        # index to the map for future lookups.
        num_map[num] = i
    
    # If no solution is found after checking all elements, return an empty list.
    return []



# Runnable example block.
def main():
    # Example 1: Basic case
    nums1 = [2, 7, 11, 15]
    target1 = 9
    result1 = two_sum(nums1, target1)
    print(f"Input: nums = {nums1}, target = {target1}")
    print(f"Output: {result1}") # Expected: [0, 1]
    print("-" * 20)

    # Example 2: Numbers are further apart
    nums2 = [3, 2, 4]
    target2 = 6
    result2 = two_sum(nums2, target2)
    print(f"Input: nums = {nums2}, target = {target2}")
    print(f"Output: {result2}") # Expected: [1, 2]
    print("-" * 20)
    
    # Example 3: Case with duplicate numbers
    nums3 = [3, 3]
    target3 = 6
    result3 = two_sum(nums3, target3)
    print(f"Input: nums = {nums3}, target = {target3}")
    print(f"Output: {result3}") # Expected: [0, 1]
    print("-" * 20)


if __name__ == "__main__":
    main()