"""
Generates all subsets (the power set) of a given set of distinct integers.

Time Complexity: O(n * 2^n)
- There are 2^n possible subsets.
- For each subset, we create a copy of it to add to the result list.
  In the worst case, this copy operation takes O(n) time.

Space Complexity: O(n)
- The recursion call stack can go as deep as n. This does not include the
  space required for the output list itself, which would be O(n * 2^n).
"""

def generate_subsets(nums):

    result = []

    def backtrack(start, current_subset):

        # Add a copy of the current subset to the result
        result.append(current_subset[:])

        # Try including each element one by one
        for i in range(start, len(nums)):
            # Include nums[i]
            current_subset.append(nums[i])

            # Recurse with the next index
            backtrack(i + 1, current_subset)

            # Backtrack: remove the last element added
            current_subset.pop()

    # Start recursion with an empty subset
    backtrack(0, [])

    return result


# 🧪 Runnable Example Block
def main():
    nums = [1, 2, 3]
    subsets = generate_subsets(nums)

    print(f"Input: {nums}")
    print("All Subsets (Power Set):")
    for subset in subsets:
        print(subset)


if __name__ == "__main__":
    main()
