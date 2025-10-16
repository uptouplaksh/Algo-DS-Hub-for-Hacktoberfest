"""
Module: power_of_two
Description:
    This module provides a function to check if a given integer is a power of two
    using efficient bit manipulation. A number n is a power of two if it has
    exactly one bit set in its binary representation.

Bit Manipulation Logic:
    For any positive integer n:
        n & (n - 1) == 0  → True if n is a power of two
    Example:
        8 (0b1000)
        7 (0b0111)
        8 & 7 = 0  → True

Complexity Analysis:
    Time Complexity: O(1)
    Space Complexity: O(1)
"""

def is_power_of_two(n: int) -> bool:
    """
    Check whether a given integer n is a power of two.

    Args:
        n (int): The integer to check.

    Returns:
        bool: True if n is a power of two, False otherwise.
    """
    return n > 0 and (n & (n - 1)) == 0


# Example usage
if __name__ == "__main__":
    test_numbers = [0, 1, 2, 3, 4, 8, 16, 18, 32]
    print("Power of Two Check:")
    for num in test_numbers:
        print(f"{num}: {is_power_of_two(num)}")
