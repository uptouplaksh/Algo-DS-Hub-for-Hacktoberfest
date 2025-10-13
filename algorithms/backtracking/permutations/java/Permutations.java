import java.util.*;
import java.util.Arrays;

/**
 * Permutations.java
 *
 * Generates all permutations of a given array of distinct integers using
 * a backtracking (recursive) approach.
 *
 * Time Complexity: O(n * n!)
 * - There are n! permutations and copying/printing each permutation takes O(n).
 *
 * Space Complexity: O(n)
 * - Recursion depth is n and the current permutation list is size up to n.
 *
 * Notes:
 * - No package declaration so the file can be placed directly at the repository
 * path:
 * algorithms/backtracking/permutations/java/Permutations.java
 * - Uses a boolean[] 'used' array to track which elements are already included.
 */
public class Permutations {

    /**
     * Backtracking helper to build permutations.
     *
     * @param nums    input array of distinct integers
     * @param used    boolean array marking used indices
     * @param current current permutation being built
     * @param result  list collecting all permutations
     */
    public static void backtrack(int[] nums, boolean[] used, List<Integer> current, List<List<Integer>> result) {
        // If current permutation has length n, add a copy to result
        if (current.size() == nums.length) {
            result.add(new ArrayList<>(current));
            return;
        }

        // Try every unused number at the current position
        for (int i = 0; i < nums.length; i++) {
            if (!used[i]) {
                // Choose
                used[i] = true;
                current.add(nums[i]);

                // Explore
                backtrack(nums, used, current, result);

                // Un-choose (backtrack)
                current.remove(current.size() - 1);
                used[i] = false;
            }
        }
    }

    /**
     * Public API to generate permutations.
     *
     * @param nums input array
     * @return list of permutations (each permutation is a List<Integer>)
     */
    public static List<List<Integer>> generatePermutations(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        if (nums == null)
            return result;
        backtrack(nums, new boolean[nums.length], new ArrayList<>(), result);
        return result;
    }

    /**
     * Runnable example: prints all permutations for the sample array.
     *
     * @param args not used
     */
    public static void main(String[] args) {
        int[] nums = { 1, 2, 3 };
        List<List<Integer>> permutations = generatePermutations(nums);

        System.out.println("All permutations of " + Arrays.toString(nums) + ":");
        int idx = 1;
        for (List<Integer> p : permutations) {
            System.out.println(idx++ + ": " + p);
        }
    }
}
