"""
Reverses the bits of a given 32-bit unsigned integer.

Time Complexity: O(1)
- The number of iterations is fixed at 32, regardless of the input value.

Space Complexity: O(1)
- Only a constant amount of extra space is used for intermediate variables.
"""

def reverse_bits(n: int) -> int:
    """
    Reverses the bits of a 32-bit unsigned integer.

    Args:
        n (int): The 32-bit unsigned integer to reverse.

    Returns:
        int: The integer with its bits reversed.
    """
    result = 0
    # Ensure n is treated as a 32-bit unsigned integer
    n = n & 0xFFFFFFFF

    for _ in range(32):
        # Left shift result to make space for the next bit
        result <<= 1
        # Extract the least significant bit of n
        lsb = n & 1
        # Add the extracted bit to the result
        result |= lsb
        # Right shift n to process the next bit
        n >>= 1

    return result

if __name__ == "__main__":
    test_value = 43261596  
    reversed_value = reverse_bits(test_value)

    print(f"Original Number: {test_value}")
    print("Original Binary:  {:032b}".format(test_value))
    print("Reversed Binary:  {:032b}".format(reversed_value))
    print(f"Reversed Number: {reversed_value}")  
