"""
Module: power_of_two
Description: Check if a given integer is a power of two using bit manipulation.

An integer n is a power of two if and only if it has exactly one bit set in its binary representation.
For example:
- 1 (0b0001) → True
- 2 (0b0010) → True
- 3 (0b0011) → False
- 16 (0b10000) → True
"""

def is_power_of_two(n: int) -> bool:
    """
    Check whether a given integer n is a power of two using bit manipulation.

    Approach:
    - A positive integer n is a power of two if n & (n - 1) == 0.
      This works because powers of two have only one set bit in binary.

    Example:
        n = 8 (1000)
        n - 1 = 7 (0111)
        n & (n - 1) = 0 → True

    Args:
        n (int): The integer to check.

    Returns:
        bool: True if n is a power of two, False otherwise.

    Time Complexity: O(1)
    Space Complexity: O(1)
    """
    return n > 0 and (n & (n - 1)) == 0

# Example usage
if __name__ == "__main__":
    test_numbers = [0, 1, 2, 3, 4, 8, 16, 18, 32]
    print("Power of Two Check:")
    for num in test_numbers:
        print(f"{num}: {is_power_of_two(num)}")
