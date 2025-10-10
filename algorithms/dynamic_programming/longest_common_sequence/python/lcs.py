"""
Longest Common Subsequence (LCS) - Dynamic Programming Implementation

This module provides a function to find the length of the Longest Common Subsequence (LCS)
between two strings using a bottom-up Dynamic Programming approach.

Time Complexity: O(m * n), where m and n are the lengths of the two strings.
Space Complexity: O(m * n), for the 2D DP table.
"""

def longest_common_subsequence(X: str, Y: str) -> int:
    """
    Computes the length of the LCS between two strings using a 2D DP table.

    Args:
        X (str): The first input string.
        Y (str): The second input string.

    Returns:
        int: The length of the longest common subsequence.
    """
    m, n = len(X), len(Y)

    # Initialize a 2D DP table with dimensions (m+1) x (n+1)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Build the DP table in a bottom-up manner
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # If the characters match, the LCS is 1 + LCS of the prefixes
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            # If they don't match, take the max of the two possibilities
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]


# ---------------------- Example Usage ----------------------
if __name__ == "__main__":
    str1 = "AGGTAB"
    str2 = "GXTXAYB"

    result = longest_common_subsequence(str1, str2)

    print(f"String 1: {str1}")
    print(f"String 2: {str2}")
    print(f"Length of Longest Common Subsequence: {result}") # Expected: 4 (for "GTAB")
