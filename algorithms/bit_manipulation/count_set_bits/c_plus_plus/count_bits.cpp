#include <iostream>
using namespace std;

/*
 * Function: countSetBits
 * ----------------------
 * Counts the number of set bits (1s) in the binary representation of an integer.
 * 
 * Algorithm: Brian Kernighan's Algorithm
 *
 * How it works:
 *   - Every time we perform "n & (n - 1)", it removes the lowest set bit from n.
 *   - We repeat this until n becomes 0.
 *   - The number of iterations = number of set bits in n.
 *
 * Complexity Analysis:
 *   1. Time Complexity:
 *      - Let k = number of set bits in n.
 *      - Each iteration removes one set bit.
 *      - So the loop runs exactly k times.
 *      - O(k) is much faster than checking every bit (which is O(log n)).
 *
 *   2. Space Complexity:
 *      - Only uses a constant amount of extra memory (the 'count' variable).
 *      - No recursion or dynamic memory.
 *      - Therefore, Space Complexity = O(1)
 */
int countSetBits(int n) {
    int count = 0;  // Counter for number of set bits

    while (n) {
        n &= (n - 1);  // Remove the lowest set bit
        count++;        // Increment the counter
    }

    return count;  // Total number of set bits
}

/*
 * Main function:
 * - Demonstrates usage of countSetBits function
 * - Reads an integer from the user
 * - Prints the number of set bits in that integer
 */
int main() {
    int num;

    cout << "Enter an integer: ";
    cin >> num;

    // Call the function and display result
    cout << "Number of set bits in " << num << " = " << countSetBits(num) << endl;

    /*
     Example:
     --------
     Input: 13
     Binary representation: 1101
     Set bits: 3
     Output: Number of set bits in 13 = 3
    */

    return 0;
}
