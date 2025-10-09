"""
Time Complexity: O(2^n)
- Each element has two choices: include or exclude.
- Total number of subsets for a set of size n is 2^n.

Space Complexity: O(n)
- The recursion call stack can go as deep as n.
- Additional space is used to build subsets during recursion.
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
