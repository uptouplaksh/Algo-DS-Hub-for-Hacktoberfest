"""
Time Complexity: O(1)
- The number of iterations is fixed (32 bits), regardless of the input value.

Space Complexity: O(1)
- Only a constant amount of space is used to store intermediate values.
"""


def reverse_bits(n: int) -> int:


    result = 0
    for i in range(32):
        # Get the least significant bit (LSB) of n
        lsb = n & 1

        # Shift result to the left to make space for the bit
        result <<= 1

        # Add the extracted bit to result
        result |= lsb

        # Shift input number to the right to process the next bit
        n >>= 1

    return result


# 🧪 Runnable example block
def main():
    test_value = 0b00000010100101000001111010011100  # 32-bit binary input
    reversed_value = reverse_bits(test_value)

    print("Original binary:  {:032b}".format(test_value))
    print("Reversed binary:  {:032b}".format(reversed_value))
    print("Reversed integer:", reversed_value)


if __name__ == "__main__":
    main()
