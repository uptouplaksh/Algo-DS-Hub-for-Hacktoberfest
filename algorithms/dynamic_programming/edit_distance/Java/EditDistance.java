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