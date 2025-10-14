/*
 * File: check_bit.java
 * Description: Program to check if the i-th bit of a number is set
 * using bitwise operators.
 */

import java.util.Scanner;

public class check_bit {
    
    /**
     * Checks if the i-th bit of number n is set.
     * Creates a mask (1 << i) and performs AND operation with n.
     * 
     * @param n The number to check
     * @param i The bit position (0-indexed from right)
     * @return 1 if bit is set, 0 otherwise
     */
    public static int checkIthBit(int n, int i) {
        int mask = 1 << i;  // Create mask with i-th bit set
        return (n & mask) != 0 ? 1 : 0;  // AND operation: non-zero means bit is set
    }
    
    /**
     * Prints binary representation of a number.
     * 
     * @param n The number to print
     * @param bits Number of bits to display
     */
    public static void printBinary(int n, int bits) {
        System.out.print("Binary: ");
        for (int i = bits - 1; i >= 0; i--) {
            System.out.print((n >> i) & 1);  // Extract each bit
            if (i % 4 == 0 && i > 0) System.out.print(" ");
        }
        System.out.println();
    }
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n, i;
        
        System.out.println("=== Check i-th Bit Program ===\n");
        
        // Example: Check bit 2 of 13 (binary: 1101)
        n = 13;
        i = 2;
        System.out.println("Example:");
        System.out.println("Number: " + n);
        printBinary(n, 8);
        System.out.println("Checking bit " + i + ": " + 
                         (checkIthBit(n, i) == 1 ? "SET (1)" : "NOT SET (0)") + "\n");
        
        // Interactive test
        System.out.println("=== Interactive Test ===");
        System.out.print("Enter a number: ");
        n = scanner.nextInt();
        System.out.print("Enter bit position to check (0-indexed): ");
        i = scanner.nextInt();
        
        System.out.println("\nNumber: " + n);
        printBinary(n, 16);
        System.out.println("Bit " + i + " is: " + 
                         (checkIthBit(n, i) == 1 ? "SET (1)" : "NOT SET (0)"));
        
        scanner.close();
    }
}