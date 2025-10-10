"""
Climbing Stairs Problem
-----------------------
You are climbing a staircase with 'n' steps.
Each time, you can either climb 1 or 2 steps.
Your task is to determine how many distinct ways you can reach the top.

Approach:
---------
This problem is a classic example of Dynamic Programming (DP).
The number of ways to reach step 'n' is the sum of ways to reach:
- step 'n-1' (taking 1 step)
- step 'n-2' (taking 2 steps)

This forms a Fibonacci-like recurrence:
    ways(n) = ways(n-1) + ways(n-2)

Base Cases:
    ways(1) = 1  (only one way to climb 1 step)
    ways(2) = 2  (two ways: 1+1 or 2)

Time Complexity: O(n)
Space Complexity: O(1)
"""

def climb_stairs(n: int) -> int:
    """
    Compute the number of distinct ways to climb to the top.
    Parameters:
    -----------
    n : int    The total number of steps.
    Returns:
    --------
    int
        Number of distinct ways to climb to the top.
    """
    # Base cases
    if n <= 2:
        return n

    # Initialize first two Fibonacci numbers
    prev2, prev1 = 1, 2

    # Iteratively compute next numbers up to n
    for _ in range(3, n + 1):
        current = prev1 + prev2
        prev2, prev1 = prev1, current

    return prev1


# ------------------------------
# Example Usage (Runnable Block)
# ------------------------------
if __name__ == "__main__":
    n = 5  # Example: total steps
    result = climb_stairs(n)
    print(f"Number of distinct ways to climb {n} steps: {result}")
