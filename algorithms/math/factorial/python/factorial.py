#
# Factorial function using recursion in Python
#

# Time Complexity: O(n)
# Space Complexity: O(n) - Due to the recursion stack depth.
#

def factorial(n):
    """
    Calculates the factorial of a non-negative integer using recursion.

    Args:
        n: The integer to calculate the factorial of.

    Returns:
        The factorial of n. Raises a ValueError for negative numbers.
    """
    # Base case 1: Error for negative numbers
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    # Base case 2: Factorial of 0 is 1
    elif n == 0:
        return 1
    # Recursive step: n * factorial of (n-1)
    else:
        return n * factorial(n - 1)


# Example Usage:
if __name__ == "__main__":
    number = 5
    print(f"The factorial of {number} is {factorial(number)}")  # Output: 120

    number = 0
    print(f"The factorial of {number} is {factorial(number)}")  # Output: 1