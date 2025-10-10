
/**
 * EditDistance.java
 * -----------------
 * This program implements the Edit Distance (Levenshtein Distance) algorithm
 * using Dynamic Programming.
 *
 * The Edit Distance between two strings is the minimum number of single-character
 * edits (insertions, deletions, or substitutions) required to change one word into another.
 * Approach:
 * We use Dynamic Programming to build a 2D table dp[m+1][n+1] where each cell dp[i][j] represents the edit distance 
 * between word1[0..i-1] and word2[0..j-1].
 * Recurrence Relation:
 * if word1[i-1] == word2[j-1]:
 * dp[i][j] = dp[i-1][j-1]
 * else:
 * dp[i][j] = 1 + min(
 * dp[i-1][j],   // Deletion
 * dp[i][j-1],   // Insertion
 * dp[i-1][j-1]  // Substitution )
 * 
 * 
 * Example:
 * Input: word1 = "kitten", word2 = "sitting"
 * Output: 3
 * Explanation:
 *   kitten → sitten (substitution)
 *   sitten → sittin (substitution)
 *   sittin → sitting (insertion)
 *
 * Time Complexity:  O(m * n)
 * Space Complexity: O(m * n)
 * where m = length of word1, n = length of word2
 */

public class EditDistance {

    /**
     * Function to compute the edit distance using Dynamic Programming.
     *
     * @param word1 The first string.
     * @param word2 The second string.
     * @return The minimum edit distance between word1 and word2.
     */
    public static int calEditDistance(String word1, String word2) {
        int m = word1.length();
        int n = word2.length();

        // dp[i][j] will hold the edit distance between word1[0..i-1] and word2[0..j-1]
        int[][] dp = new int[m + 1][n + 1];

        // Initialize base cases
        for (int i = 0; i <= m; i++) {
            dp[i][0] = i; // i deletions to make word1[0..i-1] -> ""
        }
        for (int j = 0; j <= n; j++) {
            dp[0][j] = j; // j insertions to make "" -> word2[0..j-1]
        }

        // Fill dp table
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (word1.charAt(i - 1) == word2.charAt(j - 1)) {
                    dp[i][j] = dp[i - 1][j - 1]; // no change needed
                } else {
                    dp[i][j] = 1 + Math.min(
                        dp[i - 1][j - 1], // substitution
                        Math.min(
                            dp[i - 1][j],   // deletion
                            dp[i][j - 1]    // insertion
                        )
                    );
                }
            }
        }

        return dp[m][n];
    }

    /**
     * Main method for demonstration.
     */
    public static void main(String[] args) {
        String word1 = "kitten";
        String word2 = "sitting";

        int distance = calEditDistance(word1, word2);
        System.out.println("Edit Distance between \"" + word1 + "\" and \"" + word2 + "\" is: " + distance);
    }
}



/**
 * EditDistanceOptimized.java
 * --------------------------
 * Buri buri~! This version of Edit Distance uses less memory 🧠✨
 * Normally, we make a big fat 2D table for DP... but here we use only two arrays.
 * Why? Because Shin-chan only wants chocolates, not memory leaks 🍫😆
 *
 * Time Complexity:  O(m * n)
 * -------------------------------
 * Space Complexity: O(min(m, n))
 * -------------------------------
 */

public class EditDistanceOptimized {

    /**
     * Function to compute the edit distance in a memory-efficient way!
     */
    public static int calEditDistance(String word1, String word2) {
        int m = word1.length();
        int n = word2.length();

        // If one word is smaller, let’s make it word2 (less space = more candy 🍭)
        if (n > m) {
            return calEditDistance(word2, word1);
        }

        // We'll only keep two rows: previous and current
        int[] prev = new int[n + 1];
        int[] curr = new int[n + 1];

        // 🍪 Base case: transforming "" into word2 — need j insertions
        for (int j = 0; j <= n; j++) {
            prev[j] = j;
        }

        // Let's go Shin-chan! Iterating through each character!
        for (int i = 1; i <= m; i++) {
            curr[0] = i; // turning word1[0..i-1] → "" = i deletions

            for (int j = 1; j <= n; j++) {
                // If letters match, no new candy (no extra operation)
                if (word1.charAt(i - 1) == word2.charAt(j - 1)) {
                    curr[j] = prev[j - 1];
                } else {
                    // Else, pick the minimum of three operations:
                    // 🍌 Delete one (prev[j])
                    // 🍓 Insert one (curr[j-1])
                    // 🍇 Replace one (prev[j-1])
                    curr[j] = 1 + Math.min(prev[j - 1], Math.min(prev[j], curr[j - 1]));
                }
            }

            // Swap rows, like swapping Shin-chan’s candy with Himawari’s 👶🍬
            int[] temp = prev;
            prev = curr;
            curr = temp;
        }

        // The answer hides in prev[n] after all swapping magic! ✨
        return prev[n];
    }

    /**
     * Main method for demonstration 
     */
    public static void main(String[] args) {
        String word1 = "buriburi";
        String word2 = "shinchan";

        int distance = calEditDistance(word1, word2);

        System.out.println("🐷💥 Buri buri! Edit Distance between \"" + word1 + "\" and \"" + word2 + "\" is: " + distance);
        System.out.println("🧮 Shin-chan says: it took only O(min(m, n)) space, teehee~!");
    }
}

