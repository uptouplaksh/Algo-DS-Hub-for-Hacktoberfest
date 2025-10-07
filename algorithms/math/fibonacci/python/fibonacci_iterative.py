"""
Generates the nth number in the Fibonacci Sequence using an iterative approach.
"""
def fibonacci_iterative(n):
    """
    Calculates the nth Fibonacci number.

    Args:
        n (int): The position in the Fibonacci sequence.

    Returns:
        int: The nth Fibonacci number.
    """
    if n <= 1:
        return n

    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return b

"""
Complexity Analysis:
Time Complexity: O(n) - We loop from 2 to n, performing constant time operations.
Space Complexity: O(1) - We only use a few variables to store the state, regardless of the input size.
"""

if __name__ == "__main__":
    """
    Runnable Example Block
    """
    num = 10
    print(f"The {num}th Fibonacci number is: {fibonacci_iterative(num)}") # Expected output: 55

    num = 1
    print(f"The {num}st Fibonacci number is: {fibonacci_iterative(num)}") # Expected output: 1
