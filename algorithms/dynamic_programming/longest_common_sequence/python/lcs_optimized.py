"""
Longest Common Subsequence (LCS) - Optimized Dynamic Programming Implementation
-------------------------------------------------------------------------------

This implementation reduces space complexity from O(m*n) to O(min(m, n))
by only keeping two rows (previous and current) of the DP table.

Time Complexity: O(m * n)
Space Complexity: O(min(m, n))

"""

def lcs_optimized(X: str, Y: str) -> int:
    """
    Function to find the length of the Longest Common Subsequence (LCS)
    between two strings X and Y using O(min(m, n)) space.
    
    Args:
        X (str): First string
        Y (str): Second string

    Returns:
        int: Length of the longest common subsequence
    """

    # Ensure that Y is the shorter string to minimize space usage
    if len(X) < len(Y):
        X, Y = Y, X

    m, n = len(X), len(Y)

    # Two rows for DP - previous and current
    previous = [0] * (n + 1)
    current = [0] * (n + 1)

    # Build the DP table row by row
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                current[j] = 1 + previous[j - 1]
            else:
                current[j] = max(previous[j], current[j - 1])
        # Move current row to previous for next iteration
        previous, current = current, [0] * (n + 1)

    # The last processed row (previous) contains the result
    return previous[n]


# ---------------- Example Execution ----------------
if __name__ == "__main__":
    str1 = "AGGTAB"
    str2 = "GXTXAYB"
    
    print("String 1:", str1)
    print("String 2:", str2)
    print("Length of LCS:", lcs_optimized(str1, str2))

"""
Example Output:
---------------
String 1: AGGTAB
String 2: GXTXAYB
Length of LCS: 4
Explanation: The LCS is "GTAB"
"""
