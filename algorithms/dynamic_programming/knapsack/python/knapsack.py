"""
0/1 Knapsack Problem - Standard & Optimized Dynamic Programming Implementation
------------------------------------------------------------------------------

We first implement the standard 2D DP approach with O(n * W) time and space.
Then, we optimize it to O(W) space by observing that we only need the previous
row of the DP table at each step.

Time Complexity: O(n * W)
Space Complexity:
    - Standard DP: O(n * W)
    - Optimized DP: O(W)
"""


def knapsack_dp(weights: list[int], values: list[int], capacity: int) -> int:
    """
    Find the maximum value achievable with 0/1 Knapsack using
    standard 2D Dynamic Programming.

    Args:
        weights (list[int]): List of item weights.
        values (list[int]): List of item values.
        capacity (int): Total capacity of the knapsack.

    Returns:
        int: Maximum total value achievable.
    """
    n = len(weights)

    # DP table: dp[i][w] = max value using first i items and capacity w
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    # Build the table bottom-up
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] > w:
                # Current item can't be included
                dp[i][w] = dp[i - 1][w]
            else:
                # Max of excluding or including current item
                dp[i][w] = max(
                    dp[i - 1][w],  # Exclude
                    values[i - 1] + dp[i - 1][w - weights[i - 1]]  # Include
                )

    return dp[n][capacity]


def knapsack_optimized(weights: list[int], values: list[int], capacity: int) -> int:
    """
    Find the maximum value achievable with 0/1 Knapsack using
    space-optimized Dynamic Programming (1D array).

    Args:
        weights (list[int]): List of item weights.
        values (list[int]): List of item values.
        capacity (int): Total capacity of the knapsack.

    Returns:
        int: Maximum total value achievable.
    """
    n = len(weights)

    # 1D DP array: dp[w] = max value achievable for capacity w
    dp = [0] * (capacity + 1)

    for i in range(n):
        # Traverse backward to prevent overwriting needed values
        for w in range(capacity, weights[i] - 1, -1):
            dp[w] = max(dp[w], values[i] + dp[w - weights[i]])

    return dp[capacity]


# ---------------- Example Execution ----------------
if __name__ == "__main__":
    weights_list = [1, 3, 4, 5]
    values_list = [1, 4, 5, 7]
    max_capacity = 7

    print("Weights :", weights_list)
    print("Values  :", values_list)
    print("Capacity:", max_capacity)
    print("Maximum value:", knapsack_dp(weights_list, values_list, max_capacity))
    print("Max value:", knapsack_optimized(weights_list, values_list, max_capacity))


# Example Output:
# ---------------
# Weights : [1, 3, 4, 5]
# Values  : [1, 4, 5, 7]
# Capacity: 7
# Maximum value (Standard 2D DP): 9
# Maximum value (Optimized 1D DP): 9
#
# Explanation:
# ------------
# The optimal set of items has weights 3 and 4 (total = 7)
# and values 4 + 5 = 9.

