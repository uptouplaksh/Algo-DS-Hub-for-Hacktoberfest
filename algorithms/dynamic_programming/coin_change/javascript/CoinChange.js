/**
 * Coin Change Problem - Dynamic Programming Implementation (JavaScript)
 *
 * Description:
 * This module provides a function to compute the minimum number of coins
 * required to make a given amount using the provided coin denominations.
 * If it is not possible to form the amount, it returns -1.
 *
 * Approach:
 * - We use a bottom-up dynamic programming approach.
 * - dp[i] represents the minimum number of coins required to form amount i.
 * - Initialize dp[0] = 0 (0 coins needed for amount 0).
 * - For each amount i, check every coin and update dp[i] = min(dp[i], dp[i - coin] + 1)
 *   if (i - coin >= 0).
 *
 * Time Complexity: O(amount * n)
 *   where n = number of coin denominations
 * Space Complexity: O(amount)
 *   for the 1D dp array
 */

function coinChange(coins, amount) {
  // Initialize DP array with Infinity (impossible states)
  const dp = new Array(amount + 1).fill(Infinity);
  dp[0] = 0; // Base case: 0 coins needed to make amount 0

  // Build up the solution for all amounts up to target
  for (let i = 1; i <= amount; i++) {
    for (const coin of coins) {
      if (i - coin >= 0) {
        dp[i] = Math.min(dp[i], dp[i - coin] + 1);
      }
    }
  }

  // If dp[amount] is still Infinity, it means amount cannot be formed
  return dp[amount] === Infinity ? -1 : dp[amount];
}

// -------------------------------------------------------------
// Example usage (runnable block)
// -------------------------------------------------------------
if (require.main === module) {
  const coins = [1, 2, 5];
  const amount = 11;

  const result = coinChange(coins, amount);

  console.log("Coin denominations:", coins);
  console.log("Target amount:", amount);
  console.log("Minimum coins required:", result);
}

/*
Expected Output:
Coin denominations: [ 1, 2, 5 ]
Target amount: 11
Minimum coins required: 3
Explanation: 11 can be made with 5 + 5 + 1 = 3 coins
*/
