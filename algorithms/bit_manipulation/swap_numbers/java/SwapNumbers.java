package algorithms.bit_manipulation.swap_numbers.java;

/**
 * SwapNumbers demonstrates swapping two integers without using a temporary variable
 * by leveraging the bitwise XOR operation.
 *
 * Time Complexity: O(1) – constant number of operations.
 * Space Complexity: O(1) – no extra space used.
 */
public class SwapNumbers {

    /**
     * Swaps two integer values using the bitwise XOR operator.
     * 
     * XOR Swap Logic:
     * - XOR properties: 
     *   1. x ^ x = 0
     *   2. x ^ 0 = x
     *   3. (x ^ y) ^ y = x (reversible)
     * 
     * Steps:
     * Suppose a = 5, b = 10
     * 1. a = a ^ b → a holds XOR of a and b
     * 2. b = a ^ b → b now holds original a
     * 3. a = a ^ b → a now holds original b
     *
     * @param a first integer
     * @param b second integer
     */
    public static void swapNumbers(int a, int b) {
        System.out.println("--- Before Swap ---");
        System.out.println("a = " + a);
        System.out.println("b = " + b);

        // Step 1: a becomes a XOR b
        a = a ^ b;

        // Step 2: b becomes original a
        b = a ^ b;

        // Step 3: a becomes original b
        a = a ^ b;

        System.out.println("--- After Swap ---");
        System.out.println("a = " + a);
        System.out.println("b = " + b);
    }

    public static void main(String[] args) {
        // Example: swapping two integers
        int a = 10;
        int b = 20;

        swapNumbers(a, b);
    }
}