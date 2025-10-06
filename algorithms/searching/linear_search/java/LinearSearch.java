/*
 * LinearSearch.java
 * Implementation of Linear Search in Java
 * 
 * Description:
 * Linear Search sequentially checks each element in an array to find a target value.
 * Returns the index of the target if found, otherwise returns -1.
 * 
 * Time Complexity: O(n) - worst case, every element is checked once
 * Space Complexity: O(1) - no additional memory used
 */

public class LinearSearch {

    /**
     * Performs linear search on the given array.
     *
     * @param arr    The array to search through
     * @param target The value to search for
     * @return Index of target if found; -1 otherwise
     */
    public static int linearSearch(int[] arr, int target) {
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] == target) {
                return i; // Target found, return its index
            }
        }
        return -1; // Target not found
    }

    /**
     * Example usage of the Linear Search function
     */
    public static void main(String[] args) {
        int[] numbers = {5, 10, 15, 20, 25};
        int target = 15;

        int index = linearSearch(numbers, target);

        if (index != -1) {
            System.out.println("Target " + target + " found at index: " + index);
        } else {
            System.out.println("Target " + target + " not found in the array.");
        }
    }
}
