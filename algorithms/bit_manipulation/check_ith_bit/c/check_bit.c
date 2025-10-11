#include <stdio.h>
#include <stdbool.h>

/**
 * Function: isIthBitSet
 * ---------------------
 * Checks if the ith bit of a given integer n is set (i.e., 1) or not (i.e., 0)
 * using bitwise operators.
 *
 * Parameters:
 *   n - The integer number whose bit needs to be checked.
 *   i - The bit position to check (0-indexed, where 0 is the least significant bit).
 *
 * Returns:
 *   true  - if the ith bit is set (1)
 *   false - if the ith bit is not set (0)
 *
 * How it works:
 *   1. 1 << i : This shifts the number 1 left by i positions.
 *      - Example: i = 3 -> 1 << 3 = 00001000 (in binary)
 *   2. n & (1 << i) : Performs bitwise AND between n and the mask (1 << i).
 *      - If the ith bit in n is 1, the result is non-zero.
 *      - If the ith bit in n is 0, the result is zero.
 *
 * Time Complexity:
 *   O(1) - Bitwise operations are constant-time operations.
 *
 * Space Complexity:
 *   O(1) - Only a few variables are used; no extra memory allocation.
 */
bool isIthBitSet(int n, int i) {
    // Create a mask by left shifting 1 by i positions
    int mask = 1 << i;

    // Perform bitwise AND between n and mask
    int result = n & mask;

    // If result is non-zero, the ith bit is set; otherwise, it's not
    return result != 0;
}

int main() {
    // Example number to test
    int number = 42; // Binary: 00101010
    // Example bit position to check (0-indexed)
    int bitPosition = 3;

    // Display the number
    printf("Number: %d\n", number);

    // Display which bit we are checking
    printf("Checking if bit at position %d is set...\n", bitPosition);

    // Call the function and display result
    if (isIthBitSet(number, bitPosition)) {
        printf("The %dth bit is set (1).\n", bitPosition);
    } else {
        printf("The %dth bit is not set (0).\n", bitPosition);
    }

    /**
     * Explanation of this example:
     * number = 42 -> binary: 00101010
     * bitPosition = 3 -> counting from right (0-indexed)
     * 3rd bit is 1 -> function returns true -> output: "The 3th bit is set"
     */

    return 0;
}

/*
Summary:
- This program demonstrates how to check a specific bit of a number using bitwise operators.
- Only bitwise shift (<<) and AND (&) are used.
- Time complexity is O(1) because operations are constant time.
- Space complexity is O(1) because no extra memory is used.
- Works for any integer and any valid bit position.
*/
