/*
 * Swaps two integer variables without using a temporary variable, using the bitwise XOR algorithm.
 *
 * Time Complexity: O(1) - The number of operations is constant.
 * Space Complexity: O(1) - No extra space is used.
 */
public class SwapNumbers {
    /**
     * The main method demonstrates the swapping of two integer variables
     * using the bitwise XOR swap algorithm.
     * @param args Command line arguments (not used in this example).
     */
    public static void main(String[] args) {
        // Initialize two integer variables.
        int a = 10;
        int b = 20;
        System.out.println("--- Before Swap ---");
        System.out.println("a = " + a);
        System.out.println("b = " + b);
        System.out.println();

        // The XOR swap algorithm consists of three steps:
        // Step 1: a now becomes a XOR b.
        // The bits in 'a' now hold the result of XORing the original 'a' and 'b'.
        a = a ^ b;

        // Step 2: b now becomes (a XOR b) XOR b = a.
        // XORing the result from Step 1 with the original 'b' effectively
        // cancels out 'b', leaving the original value of 'a' in 'b'.
        b = a ^ b;

        // Step 3: a now becomes (a XOR b) XOR a = b.
        // XORing the result from Step 1 with the new value of 'b' (which is the
        // original 'a') cancels out 'a', leaving the original value of 'b' in 'a'.
        a = a ^ b;

        System.out.println("--- After Swap ---");
        System.out.println("a = " + a);
        System.out.println("b = " + b);
    }
}