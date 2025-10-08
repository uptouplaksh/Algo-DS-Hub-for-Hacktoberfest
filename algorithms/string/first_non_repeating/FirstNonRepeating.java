package string.first_non_repeating;


public class FirstNonRepeating {

    // Method to find first non-repeating character in a string
    static char nonRepeatingChar(String s) {
        if (s.length() == 0) return '$'; // Handle empty string

        int[] freq = new int[256]; // Support all ASCII characters

        // Count frequency of each character
        for (int i = 0; i < s.length(); i++) {
            freq[s.charAt(i)]++;
        }

        // Find the first character with frequency 1
        for (int i = 0; i < s.length(); i++) {
            if (freq[s.charAt(i)] == 1) return s.charAt(i);
        }

        return '$'; // If no non-repeating character
    }

    // Example usage
    public static void main(String[] args) {
        String str = "ruturaj";
        char result = nonRepeatingChar(str);
        System.out.println("First non-repeating character: " + result);
    }

    // Time Complexity: O(n)
    // Space Complexity: O(1) (fixed-size freq array of 256)
    //  Author: Ruturaj Pawar (@Ruturaj-007)
}
