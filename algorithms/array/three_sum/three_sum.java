import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class three_sum {

    /**
     * Finds all unique triplets in the array that sum to zero.
     *
     * This method uses sorting + two-pointer technique for optimal performance.
     * Duplicates are handled using a HashSet to ensure uniqueness.
     *
     * Time Complexity: O(n^2)
     * Space Complexity: O(n) (for storing unique triplets)
     */
    public List<List<Integer>> threeSum(int[] nums) {
        // If the array has fewer than 3 elements, no triplet is possible
        if (nums == null || nums.length < 3) return new ArrayList<>();

        // Sort the array to use two-pointer approach
        Arrays.sort(nums);

        // HashSet ensures uniqueness of triplets
        Set<List<Integer>> uniqueTriplets = new HashSet<>();

        // Iterate through the array
        for (int i = 0; i < nums.length - 2; i++) {
            int left = i + 1;
            int right = nums.length - 1;

            // Two-pointer search for pairs that sum with nums[i] to zero
            while (left < right) {
                int sum = nums[i] + nums[left] + nums[right];

                if (sum == 0) {
                    // Found a valid triplet
                    uniqueTriplets.add(Arrays.asList(nums[i], nums[left], nums[right]));
                    left++;
                    right--;
                } else if (sum < 0) {
                    // Sum too small, move left pointer to increase sum
                    left++;
                } else {
                    // Sum too large, move right pointer to decrease sum
                    right--;
                }
            }
        }

        // Convert HashSet to List before returning
        return new ArrayList<>(uniqueTriplets);
    }

    /**
     * Runnable example to test the threeSum method.
     */
    public static void main(String[] args) {
        int[] arr = {-1, 0, 1, 2, -1, -4};
        
        // Call threeSum method
        List<List<Integer>> result = new three_sum().threeSum(arr);
        
        // Print input and output
        System.out.println("Input: " + Arrays.toString(arr));
        System.out.println("Output (unique triplets): " + result);
    }
}
