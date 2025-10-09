"""
Time Complexity: O(n * target)
- n = number of elements in the input set
- target = required sum
- We fill a 2D DP table of size (n+1) x (target+1)

Space Complexity: O(n * target)
- A 2D boolean table is used to store intermediate results.
"""

def is_subset_sum(nums, target):


    n = len(nums)

    # dp[i][j] will be True if a subset of the first i elements has sum j
    dp = [[False] * (target + 1) for _ in range(n + 1)]

    # A sum of 0 is always possible — by taking an empty subset
    for i in range(n + 1):
        dp[i][0] = True

    # Fill the DP table
    for i in range(1, n + 1):
        for j in range(1, target + 1):
            if nums[i - 1] <= j:
                # Include the current element or exclude it
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]
            else:
                # Cannot include the current element
                dp[i][j] = dp[i - 1][j]

    return dp[n][target]


# 🧪 Runnable Example Block
def main():
    nums = [3, 34, 4, 12, 5, 2]
    target = 9
    print(f"Input set: {nums}")
    print(f"Target sum: {target}")
    if is_subset_sum(nums, target):
        print("Result: A subset with the given sum exists.")
    else:
        print("Result: No subset with the given sum exists.")

if __name__ == "__main__":
    main()
