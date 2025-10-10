/*
 * Integer to Roman Numeral Converter
 * 
 * Greedy Algorithm: Makes the locally optimal choice at each step
 * (always use the largest possible Roman numeral that fits)
 * Time Complexity: O(1) - fixed 13 iterations max
 * Space Complexity: O(1) - constant space
 */
public class IntegerToRoman {

    /**
     * Converts an integer to its Roman numeral representation
     *
     */
    public static String intToRoman(int num) {
        // Map integer values to Roman numerals in descending order
        // Includes subtractive cases (IV, IX, XL, XC, CD, CM)
        int[] values = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
        String[] numerals = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};

        // StringBuilder: efficient string building (avoids creating new String objects)
        StringBuilder result = new StringBuilder();

        // For loop: iterate through each Roman numeral from largest to smallest
        for (int i = 0; i < values.length; i++) {
            // While loop: use current numeral as many times as possible (greedy choice)
            while (num >= values[i]) {
                result.append(numerals[i]); // Add Roman numeral to result
                num -= values[i];           // Subtract its value from remaining number
            }
        }

        return result.toString();
    }

    /**
     * Test cases demonstrating the algorithm
     */
    public static void main(String[] args) {
        System.out.println(intToRoman(3));    // Expected: III
        System.out.println(intToRoman(4));    // Expected: IV (subtractive case)
        System.out.println(intToRoman(58));   // Expected: LVIII
        System.out.println(intToRoman(89));   // Expected: LXXXIX
        System.out.println(intToRoman(1994)); // Expected: MCMXCIV
    }

}

/*
 * Algorithm Walkthrough (Example: num = 58)
 * 
 * Initial: num = 58, result = ""
 * 
 * Step 1: Check 1000 (M) → 58 < 1000, skip
 * Step 2: Check 900 (CM) → 58 < 900, skip
 * Step 3: Check 500 (D) → 58 < 500, skip
 * Step 4: Check 400 (CD) → 58 < 400, skip
 * Step 5: Check 100 (C) → 58 < 100, skip
 * Step 6: Check 90 (XC) → 58 < 90, skip
 * Step 7: Check 50 (L) → 58 >= 50, append "L", num = 8
 * Step 8: Check 40 (XL) → 8 < 40, skip
 * Step 9: Check 10 (X) → 8 < 10, skip
 * Step 10: Check 9 (IX) → 8 < 9, skip
 * Step 11: Check 5 (V) → 8 >= 5, append "V", num = 3
 * Step 12: Check 4 (IV) → 3 < 4, skip
 * Step 13: Check 1 (I) → 3 >= 1, append "I" three times, num = 0
 * 
 * Result: "LVIII" (50 + 5 + 3 = 58)
 */
