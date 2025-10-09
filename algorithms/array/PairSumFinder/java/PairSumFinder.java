/**
 * PairSumFinder.java
 * 
 * Find all unique pairs in an array that sum to a given target.
 * 
 * Time Complexity: O(n)
 * Space Complexity: O(n)
 */

import java.util.*;

public class PairSumFinder {

    public static void findPairs(int[] nums, int target) {
        Set<Integer> seen = new HashSet<>();
        Set<String> output = new HashSet<>();

        for (int num : nums) {
            int complement = target - num;
            if (seen.contains(complement)) {
                // Sort pair to avoid duplicates like (3,7) and (7,3)
                int a = Math.min(num, complement);
                int b = Math.max(num, complement);
                output.add("(" + a + ", " + b + ")");
            }
            seen.add(num);
        }

        if (output.isEmpty()) {
            System.out.println("No pairs found for target " + target);
        } else {
            System.out.println("Pairs that sum to " + target + ":");
            for (String pair : output) {
                System.out.println(pair);
            }
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter array size: ");
        int n = sc.nextInt();
        int[] nums = new int[n];

        System.out.println("Enter array elements:");
        for (int i = 0; i < n; i++) {
            nums[i] = sc.nextInt();
        }

        System.out.print("Enter target sum: ");
        int target = sc.nextInt();

        findPairs(nums, target);
        sc.close();
    }
}
