/**
 * ==========================
 * Time Complexity: O(n * n!)
 *   - There are n! permutations of n elements
 *   - Each permutation takes O(n) time to build (copying the array)
 *
 * Space Complexity: O(n)
 *   - The recursion stack and the path/used tracking uses up to O(n) space
 * ==========================
 */
/**
 * Generate all permutations of a given array of distinct integers
 * using backtracking (recursive) approach.
 *
 * @param {number[]} nums - Array of distinct integers
 * @return {number[][]} - All possible permutations
 */
function permute(nums) {
  const results = [];

  /**
   * Backtracking helper function
   * @param {number[]} path - Current permutation being built
   * @param {Set<number>} used - Tracks which numbers have been used in the current path
   */
  function backtrack(path, used) {
    // Base case: if the current path's length equals the input array length,
    // we have a complete permutation
    if (path.length === nums.length) {
      results.push([...path]); // Make a deep copy of path
      return;
    }

    // Explore all unused elements
    for (let i = 0; i < nums.length; i++) {
      if (used.has(i)) continue; // Skip already used elements

      path.push(nums[i]);       // Choose the element
      used.add(i);              // Mark it as used

      backtrack(path, used);    // Recurse

      path.pop();               // Undo the choice (backtrack)
      used.delete(i);           // Unmark the element
    }
  }

  backtrack([], new Set());

  return results;
}

/**
 * Example usage
 */
function runExample() {
  const input = [1, 2, 3];
  const permutations = permute(input);

  console.log(`All permutations of [${input}]:`);
  permutations.forEach((perm, index) => {
    console.log(`${index + 1}: [${perm}]`);
  });
}

runExample();

