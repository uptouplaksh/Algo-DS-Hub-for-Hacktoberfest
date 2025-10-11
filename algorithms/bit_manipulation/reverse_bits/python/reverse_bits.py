"""
Task: Reverse the bits of a given 32-bit unsigned integer.

Example:
    Input:  43261596 (binary 00000010100101000001111010011100)
    Output: 964176192 (binary 00111001011110000010100101000000)

Author: Contributor (Hacktoberfest 2025)
"""


def reverse_bits(n: int) -> int:
    """
    Reverse the bits of a 32-bit unsigned integer.

    Args:
        n (int): 32-bit unsigned integer.

    Returns:
        int: Integer with reversed bit order.

    Approach:
        - Initialize result = 0.
        - Loop 32 times:
            - Left shift result by 1 to make space for the next bit.
            - Extract the least significant bit (n & 1).
            - Add it to result.
            - Right shift n by 1 to process the next bit.
    """
    result = 0
    for _ in range(32):
        result = (result << 1) | (n & 1)
        n >>= 1
    return result


if __name__ == "__main__":
    # Example usage
    num = 43261596
    print(f"Input Number: {num}")
    print(f"Reversed Bits Output: {reverse_bits(num)}")
