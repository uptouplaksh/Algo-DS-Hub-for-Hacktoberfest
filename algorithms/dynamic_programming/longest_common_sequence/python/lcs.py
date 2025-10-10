"""
Longest Common Subsequence (LCS) - Dynamic Programming Implementation

This module provides a function to find the length of the Longest Common Subsequence (LCS)
between two strings using a bottom-up Dynamic Programming approach.

Author: Your Name
Date: 2025-10-10
"""

def longest_common_subsequence(X: str, Y: str) -> int:
    """
    Compute the length of the Longest Common Subsequence (LCS) between two strings.

    Parameters:
        X (str): First input string.
        Y (str): Second input string.

    Returns:
        int: Length of the longest common subsequence.

    Approach:
        - We use a 2D DP table where dp[i][j] represents the LCS length
          between X[:i] and Y[:j].
        - If characters match: dp[i][j] = 1 + dp[i-1][j-1]
        - Otherwise: dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    Time Complexity:
        O(m * n) — where m = len(X), n = len(Y)
    Space Complexity:
        O(m * n) — for the 2D DP table
    """

    m, n = len(X), len(Y)

    # Initialize a 2D DP table with dimensions (m+1) x (n+1)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Build the DP table in bottom-up manner
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]


# ---------------------- Example Usage ----------------------
if __name__ == "__main__":
    # Example strings
    str1 = "AGGTAB"
    str2 = "GXTXAYB"

    # Compute LCS length
    result = longest_common_subsequence(str1, str2)

    print(f"String 1: {str1}")
    print(f"String 2: {str2}")
    print(f"Length of Longest Common Subsequence: {result}")
